#!/usr/bin/env python3
"""Verification toolbox for a one-pager HTML deliverable (Phase 3, references/input-protocol.md).

Bundles the programmatic assertions so they run as one command instead of
markdown comments. Requires a browser with remote debugging via Playwright's
msedge/chrome channel, or any system Edge/Chrome; if neither is reachable,
runs the pypdf-only checks and reports the rest as NOT RUN (never silently
skipped — that discipline is the toolbox's own rule).

Tier naming: N0 = the one-pager body (.page), N1 = the batch six-page
narrative (.narrative), N2 = the appendix (.appendix). Visual presets are
T1-T7 (style-system.md) — a different numbering system.

Usage:
  uv run --with pypdf python check.py <one-pager.html> [--pdf <file.pdf>]
Exit codes: 0 all pass · 1 usage/missing · 2 assertion failure · 3 partial (not-run items)
"""
import argparse
import sys
from pathlib import Path


def parse_pdf(pdf: Path):
    from pypdf import PdfReader

    r = PdfReader(str(pdf))
    pages = len(r.pages)
    a4 = all(abs(float(p.mediabox.width) - 595) < 2 for p in r.pages)
    return pages, a4


def browser_assertions(html: Path):
    """Run DOM assertions via Playwright against a real browser; None if unavailable."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return None

    js = """
    () => {
      const page = document.querySelector('.page');
      if (!page) return { error: 'no .page element' };
      const body = document.querySelector('.body') || page;
      const narrative = document.querySelector('.narrative');
      const appendix = document.querySelector('.appendix');
      const paras = [...document.querySelectorAll('.body p, .narrative p')];
      const labelLeads = paras.filter(p => /^[^，。；:]{1,12}[：:]/.test(p.textContent.trim())).length;
      const sections = document.querySelectorAll('.sec-label').length || 1;
      const bodyTxt = body.textContent;
      const nTxt = narrative ? narrative.textContent : '';
      // first-use acronym glossing: acronym not followed by （ or ( within 30 chars
      const bareAcronyms = [...new Set((nTxt + bodyTxt).match(/\\b(LLM|NRR|ARR|MAU|NPS|LTV|CAC|SFT|RL|MCP|RAG|KV)\\b/g) || [])]
        .filter(a => !(bodyTxt + nTxt).match(new RegExp(a + '[^)]{0,28}[（(]')));
      return {
        r1_overflow: page.scrollHeight > page.clientHeight + 1,
        r1_scroll: page.scrollHeight,
        r1_client: page.clientHeight,
        n0_dashes: (bodyTxt.match(/——|—/g) || []).length,
        n1_dashes: (nTxt.match(/——|—/g) || []).length,
        n1_pages: narrative ? Math.ceil(narrative.scrollHeight / 1123) : 0,
        label_colon_leads: labelLeads,
        sections: sections,
        bare_acronyms: bareAcronyms,
        d_in_body: (bodyTxt.match(/D\\d/g) || []).length,
        d_in_n1: (nTxt.match(/D\\d/g) || []).length,
        d_rows: appendix ? [...appendix.querySelectorAll('table tbody tr')]
          .filter(tr => /^D\\d+$/.test((tr.cells[0]?.textContent || '').trim())).length : 0,
        weasel: /显著|大幅|几乎|一定程度上|best-in-class|遥遥领先/.test(bodyTxt),
      };
    }
    """

    with sync_playwright() as p:
        for channel in ("chromium", "msedge", "chrome"):
            try:
                browser = p.chromium.launch(channel=channel) if channel != "chromium" else p.chromium.launch()
                break
            except Exception:
                browser = None
        if browser is None:
            return None
        pg = browser.new_page(viewport={"width": 794, "height": 1123})
        pg.goto(html.resolve().as_uri())
        pg.wait_for_timeout(400)
        result = pg.evaluate(js)
        browser.close()
        return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("html", type=Path)
    ap.add_argument("--pdf", type=Path, default=None)
    args = ap.parse_args()
    html = args.html.resolve()
    if not html.exists():
        sys.exit(f"not found: {html}")
    pdf = (args.pdf or html.with_suffix(".pdf")).resolve()

    checks, failures, notrun = [], [], []

    dom = browser_assertions(html)
    if dom is None:
        notrun += ["R1 overflow", "N0/N1 dash budgets", "label-colon leads",
                   "bare-acronym scan", "Q9 anchor bidirectionality", "Q4 weasel (DOM)"]
    else:
        if dom.get("error"):
            failures.append(dom["error"])
        if dom["r1_overflow"]:
            failures.append(f"R1: N0 overflows (scrollHeight {dom['r1_scroll']} > clientHeight {dom['r1_client']})")
        if dom["n0_dashes"] > 2:
            failures.append(f"humanize: N0 em-dashes {dom['n0_dashes']} > 2")
        n1_budget = max(dom["n1_pages"] * 2, 2)
        if dom["n1_dashes"] > n1_budget:
            failures.append(f"humanize: N1 em-dashes {dom['n1_dashes']} > {n1_budget} (pages {dom['n1_pages']})")
        if dom["n1_pages"] > 6:
            failures.append(f"batch-mode: N1 narrative {dom['n1_pages']} pages > 6 budget")
        if dom["label_colon_leads"] > dom["sections"]:
            failures.append(f"humanize: label-colon leads {dom['label_colon_leads']} > sections {dom['sections']}")
        if dom["bare_acronyms"]:
            failures.append(f"first-read: bare acronyms {dom['bare_acronyms']}")
        if dom["d_in_body"] + dom["d_in_n1"] > 0 and dom["d_rows"] == 0:
            failures.append("Q9: D anchors in body but no traceability rows")
        elif dom["d_rows"] > 0 and dom["d_in_body"] + dom["d_in_n1"] == 0:
            failures.append("Q9: traceability rows exist but no body anchors")
        if dom["weasel"]:
            failures.append("Q4: weasel word in body")
        checks.append(f"DOM: {dom}")

    if pdf.exists():
        try:
            pages, a4 = parse_pdf(pdf)
            if not a4:
                failures.append("PDF: non-A4 page present")
            checks.append(f"PDF: {pages} pages, A4={a4}")
            # N0=1 + N1<=6 is hard; the appendix is unlimited by design, so a high
            # total is only suspicious, not failing — flag for human eyes.
            if pages > 12:
                checks.append(f"NOTE  PDF: {pages} pages total — appendix is unlimited by design; verify this is intended, N1 budget is checked in DOM")
        except Exception as e:
            notrun.append(f"PDF census ({e})")
    else:
        notrun.append("PDF census (no pdf file)")

    print("\n".join(checks) or "no DOM checks ran")
    for f in failures:
        print(f"FAIL  {f}")
    for n in notrun:
        print(f"NOTRUN {n}")
    if failures:
        sys.exit(2)
    if notrun:
        sys.exit(3)
    print("ALL RUN CHECKS PASS")


if __name__ == "__main__":
    main()
