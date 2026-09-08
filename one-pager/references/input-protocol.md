# Input Protocol & Verification Toolbox — Phase 0 与验证工具

Two things this skill learned from real book-scale runs, written down so every future run starts from them instead of reinventing them:

1. **Phase 0 — input preflight**: what to do with each input type before Phase 1 can start.
2. **The verification toolbox**: the programmatic assertions every deliverable passes before handoff (the run-log-worthy checks, not vibes).

## Phase 0 — Input preflight

Classify the input **before** routing Phase 1, because the protocol choice (0→1 vs 100→1 vs batch) depends on what actually arrives:

| Input shape | Preflight | Then |
|---|---|---|
| Plain text / Markdown | None — read directly | 100→1 (or batch if ≥ 50k chars, `references/batch-mode.md`) |
| **PDF** | Extract text first with `scripts/extract.py <input.pdf> [out.txt]` (ships with the skill; inserts `===== PAGE N =====` anchors). This skill does not parse PDFs natively — extraction is the bundled, documented step | Route on the extracted text; the extraction output doubles as the traceability table's 可复核路径 source |
| URL / web page | Fetch and convert to text | Route on the fetched text; record source URL in the traceability table |
| No file, idea only | None | 0→1 生成 protocol |
| Multiple files | Read each; note per-file role (which is the source, which is context) | Batch mode if combined ≥ 50k chars, else 100→1 |

PDF gotchas seen in practice: 307 pages extracted to ~500k characters works fine, but page-marker anchors (`===== PAGE N =====`) are worth inserting during extraction — they become the traceability table's 可复核路径 column for free.

## The 80/20 scan for book-scale sources

When the source is a whole book (or equivalently large), do **not** read linearly. Scan the navigation structure first — it carries a disproportionate share of the argument:

1. **Table of contents** — the author's own structure claim.
2. **Introduction / preface** — the thesis, the author's credibility basis, and often the one-sentence formula the whole book hangs on.
3. **How-to-read / book-structure section** — the author's own summary of what each chapter does; this is the author doing 80/20 for you.
4. **Chapter summaries (本章小结)** — the highest-density distillation in most technical books; read **all** of them before deciding anything else.
5. **Epilogue / afterword** — where authors park their honest open problems and the claims they most want remembered.
6. **Then** selectively deep-read only the chapters the one-pager's claim will lean on hardest.

Record the reading depth per chapter in the appendix 论据地图 (精读 / 小结级 / 目录级) — the reader has the right to know which paragraphs are first-hand and which are second-hand. Depth honesty is a feature, not a confession.

## The verification toolbox

Every deliverable passes these **programmatic** checks before handoff. They are cheap, objective, and catch what eyeballs miss. Run them in a real browser (or headless) against the final HTML, plus a PDF page census:

```js
// 1. R1 one-page: the N0 .page box must not overflow
const page = document.querySelector('.page');
page.scrollHeight <= page.clientHeight + 1;              // +1 = rendering tolerance

// 2. Q4 weasel scan on the body (extend the list per narrative-methodology L3)
!/显著|大幅|几乎|一定程度上|best-in-class|遥遥领先/.test(document.querySelector('.body').textContent);

// 3. Q9 anchor bidirectionality: every D# in body+N1 resolves to a traceability row, and vice versa
const dInBody = (bodyText.match(/D\d/g) || []).length;
const dRows = [...document.querySelectorAll('.appendix table tbody tr')]
  .filter(tr => /^D\d+$/.test(tr.cells[0]?.textContent?.trim())).length;

// 4. Humanize spot-checks: dashes ≤ 2 per N0 page (N1 budget = pages × 2),
//    label-colon LEADS ≤ 1 per section outside mandated house-pattern structures,
//    no 3 consecutive equal-length sentences

// 5. First-read spot-check: grep the body for bare acronyms/first-use jargon
//    (each acronym's first occurrence must carry a gloss)
```

```python
# 6. PDF census with pypdf: page count matches the declared tiering
#    N0 = 1 page; batch adds N1 ≤ 6; appendix follows; all pages A4 (595×842pt)
from pypdf import PdfReader
r = PdfReader(out)
assert len(r.pages) == expected_total
assert all(abs(float(p.mediabox.width) - 595) < 2 for p in r.pages)
```

All of the above ship as **`scripts/check.py`** — run `uv run --with pypdf python scripts/check.py <file.html>` after export. It runs the DOM assertions via Playwright (chromium/msedge/chrome channel, whichever launches) and the PDF census together, and prints NOT RUN for anything it cannot execute (this file's own discipline).

Fallbacks, in order: Playwright chromium (scripted `export.py --check`) → headless Edge/Chrome CLI for the PDF + manual browser DevTools for the assertions → worst case, pypdf page census only and say so in the run log. A check that cannot run must be reported as not run, never silently skipped.

What the toolbox deliberately does **not** check: visual quality (R2–R7, human judgment — that's the style system's Show-Don't-Tell territory) and whether the claim is right (that's the user's review).

## Where this sits in the pipeline

```
Phase 0 preflight → Phase 1 ARGUE (+QC gate + text polish) → Phase 2 COMPOSE → Phase 3 EXPORT + toolbox
```

The toolbox runs at Phase 3 on the *final* HTML/PDF pair. Any assertion failure loops back per its own rule (R1 → overflow protocol; Q4/Q9 → Phase 1; tier mismatch → batch-mode budget).
