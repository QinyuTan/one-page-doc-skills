#!/usr/bin/env python3
"""one-pager export: HTML -> PDF (default) / PNG (--png) / one-page overflow check (--check).

Strategy:
  1. Playwright (pip) when available -- best fidelity + real overflow measurement.
  2. Edge/Chrome headless CLI fallback (prints PDF/PNG; overflow check unavailable,
     in which case count PDF pages or open the file and look).

Usage:
  python export.py page.html               -> page.pdf next to it
  python export.py page.html --png         -> page.pdf + page.png
  python export.py page.html --check       -> overflow report (Playwright only), no files
  python export.py page.html --pdf out.pdf --png out.png --check
"""
import argparse
import shutil
import subprocess
import sys
from pathlib import Path

A4_W, A4_H = 794, 1123  # px at 96dpi

BROWSERS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/usr/bin/google-chrome",
    "/usr/bin/chromium",
    "/usr/bin/chromium-browser",
]


def find_browser():
    for cand in BROWSERS:
        if Path(cand).exists():
            return cand
    for name in ("msedge", "google-chrome", "chromium", "chromium-browser"):
        found = shutil.which(name)
        if found:
            return found
    return None


def run_cli(browser, html, pdf_out, png_out):
    url = html.resolve().as_uri()
    if pdf_out:
        subprocess.run(
            [browser, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
             f"--print-to-pdf={pdf_out}", url],
            check=True, capture_output=True, timeout=180,
        )
    if png_out:
        subprocess.run(
            [browser, "--headless=new", "--disable-gpu",
             f"--window-size={A4_W},{A4_H}", f"--screenshot={png_out}", url],
            check=True, capture_output=True, timeout=180,
        )


def run_playwright(html, pdf_out, png_out, check):
    from playwright.sync_api import sync_playwright

    result = {}
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": A4_W, "height": A4_H})
        page.goto(html.resolve().as_uri())
        page.wait_for_timeout(400)  # let fonts/images settle

        if check:
            # .page is a fixed-height A4 box; overflowing content raises scrollHeight.
            result = page.evaluate(
                """() => {
                    const el = document.querySelector('.page');
                    if (!el) return { error: 'no .page element found' };
                    return {
                        content_px: el.scrollHeight,
                        limit_px: el.clientHeight,
                        overflows: el.scrollHeight > el.clientHeight + 1,  // +1px: sub-pixel rendering tolerance
                    };
                }"""
            )

        if pdf_out:
            page.pdf(
                path=str(pdf_out), width="210mm", height="297mm",
                print_background=True,
                margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
            )
        if png_out:
            page.screenshot(path=str(png_out), full_page=True)
        browser.close()
    return result


def main():
    ap = argparse.ArgumentParser(description="Export a one-pager HTML to PDF/PNG")
    ap.add_argument("html", type=Path, help="the one-pager HTML file")
    ap.add_argument("--pdf", type=Path, default=None, help="output PDF path (default: <html>.pdf)")
    ap.add_argument("--png", type=Path, default=None, help="also render a PNG at this path")
    ap.add_argument("--check", action="store_true", help="report whether body overflows one A4 page")
    args = ap.parse_args()

    html = args.html.resolve()
    if not html.exists():
        sys.exit(f"not found: {html}")
    pdf_out = (args.pdf or html.with_suffix(".pdf")).resolve()
    png_out = (args.png.resolve() if args.png else None)

    try:
        result = run_playwright(html, pdf_out, png_out, args.check)
        engine = "playwright"
    except (ImportError, Exception) as launch_failure:
        # ImportError: playwright not installed. Any other Exception here is almost
        # always `playwright install chromium` missing (the package exists, the browser
        # binary doesn't) — p.chromium.launch() raises playwright's own Error, which the
        # old ImportError-only catch missed, killing the documented Edge/Chrome fallback.
        browser = find_browser()
        if browser is None:
            sys.exit(f"no renderer: install playwright (`pip install playwright && playwright install chromium`) "
                     f"or provide Edge/Chrome. Playwright attempt failed: {launch_failure}")
        run_cli(browser, html, pdf_out, png_out)
        result, engine = None, f"cli ({browser})"

    if args.check:
        if result is None:
            print(f"[check] engine={engine}: overflow check needs playwright; "
                  f"open the PDF and verify the body is exactly page 1")
        elif result.get("error"):
            print(f"[check] {result['error']}")
            sys.exit(1)
        else:
            verdict = "FAIL — content exceeds one A4 page, apply the overflow protocol" \
                if result["overflows"] else "OK — body fits one A4 page"
            print(f"[check] {verdict} (content {result['content_px']}px vs limit {result['limit_px']}px)")
            if result["overflows"]:
                sys.exit(2)

    if pdf_out and pdf_out.exists():
        print(f"[pdf ] {pdf_out} ({pdf_out.stat().st_size:,} bytes)")
    if png_out and png_out.exists():
        print(f"[png ] {png_out} ({png_out.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
