#!/usr/bin/env python3
"""Extract text from a PDF for one-pager distillation (Phase 0 preflight, references/input-protocol.md).

Usage:
  uv run --with pypdf python extract.py <input.pdf> [output.txt]

Output defaults to <input>.txt next to the PDF. Page anchors
(`===== PAGE N =====`) are inserted so the appendix traceability table's
可复核路径 column can cite pages directly.
"""
import sys
from pathlib import Path

from pypdf import PdfReader


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    src = Path(sys.argv[1]).resolve()
    if not src.exists():
        sys.exit(f"not found: {src}")
    out = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else src.with_suffix(".txt")

    reader = PdfReader(str(src))
    parts = []
    for i, page in enumerate(reader.pages):
        try:
            text = page.extract_text() or ""
        except Exception as e:  # page-level failure shouldn't kill the run
            text = f"[page {i + 1} extract failed: {e}]"
        parts.append(f"\n===== PAGE {i + 1} =====\n{text}")

    full = "".join(parts)
    out.write_text(full, encoding="utf-8")
    print(f"pages: {len(reader.pages)}")
    print(f"chars: {len(full)}")
    print(f"saved: {out}")


if __name__ == "__main__":
    main()
