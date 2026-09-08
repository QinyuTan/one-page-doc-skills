# one-pager

> Compress anything — a book, a 60-page report, meeting notes, a proposal — into **exactly one A4 page** that argues like an Amazon memo and looks like it came from a magazine's art desk.

An agent skill that produces one-page narrative documents: full-sentence argumentation (no bullet-stacked decks), evidence anchored and traceable, editorial print typography — deliberately **not** a PPT tool.

## Why

Every common format fails the same way. Slides scatter one idea across twelve bullets. Documents sprawl past anyone's attention. AI summaries are walls of text with no hierarchy. A one-pager forces the highest form of clarity: the discipline of fitting everything that matters into one page — the constraint is the product.

This skill is two decision layers, each with one authoritative reference:

| Layer | Reference | Governs |
|---|---|---|
| Narrative | `one-pager/references/narrative-methodology.md` | What to say, how to say it, what to cut — Amazon narrative culture (6-pager, PR/FAQ, Working Backwards) × MBB distillation (pyramid, 80/20, Action Title) |
| Visual | `one-pager/references/style-system.md` | How it looks — L1 气质 × L2 骨架 × L3 皮肤 routing, T1–T7 presets, R1–R10 veto rules |
| Mechanics | `one-pager/references/typography.md` | Invariant A4 rules every template shares |

## What it does

**Pipeline**: `ARGUE → COMPOSE → EXPORT`

1. **ARGUE** — route the narrative protocol: 0→1 (build an argument from an idea) or 100→1 (distill existing material). Then the scenario fork, decided by one question — *what does the reader do next?*

   | Reader's next action | Scenario | House pattern |
   |---|---|---|
   | Retell it | 学习复述 — books, courses, long articles | Book Memo (Adler × Sivers × Feynman) |
   | Decide | 决策行动 — proposals, approvals, meeting notes | Proposal 五段式 (real AWS GCR proposal distilled) |
   | Be convinced | 信服洞察 — research reports, data analyses | Insight Page (Zelazny × FT data journalism) |

   Full sentences for arguments, numbers over adjectives, every claim passing the "So What?" test, and a 9-gate QC check (elevator test → horizontal logic → weasel scan → … → data traceability) before any visual work begins.

2. **COMPOSE** — route the visual style (7 气质 presets × skeleton × skin), declare the template, fill an A4 page. Every number in the body carries a `(D#)` anchor resolving into an appendix traceability table; discipline lives on page one, evidence lives in the appendix.

3. **EXPORT** — one self-contained HTML file (no external fonts/URLs, images base64-embedded) plus PDF/PNG via the bundled `export.py` (headless Chromium/Edge, with a scrollHeight overflow assertion — the one-page constraint is verified, never hoped for).

## Examples

| Scenario | Fork | Preview |
|---|---|---|
| 《Working Backwards》 book notes → book-club one-pager | 学习复述 | [HTML](examples/book-memo-working-backwards.html) · [PNG](examples/book-memo-working-backwards.png) |
| Q3 acquisition experiments → management decision memo | 决策行动 | [HTML](examples/proposal-q3-budget-zh.html) · [PNG](examples/proposal-q3-budget-zh.png) |
| 40-page pricing research → exec brief (English) | 决策行动 | [HTML](examples/proposal-pricing-en.html) · [PNG](examples/proposal-pricing-en.png) |
| Competitive research report → 3-minute insight page | 信服洞察 | [HTML](examples/insight-competitive-research.html) · [PNG](examples/insight-competitive-research.png) |

## Install

**Any agent with skills support** (Claude Code, Codex, Cursor, Windsurf, …):

```bash
npx skills add <your-github-username>/one-pager
```

**Manual**: copy the `one-pager/` directory into your agent's skills folder (e.g. `.claude/skills/` or `~/.agents/skills/`).

**Python (optional, for export)**: `pip install playwright && playwright install chromium` — otherwise `export.py` falls back to headless Edge/Chrome automatically.

## Use

Just describe the job in your own words:

- "帮我把这本《原则》的笔记读薄成一页纸" (把书读薄)
- "把 Q3 实验结果写成一页纸给管理层，结论是……"
- "这份 60 页调研报告没人看完，压成一页让人 3 分钟抓住结论"
- "Write a one-pager for our seed round"

The skill routes the protocol, fork, and visual style from your phrasing — and tells you what it chose (declared template + skin) before writing any HTML.

## Repository layout

```
one-pager/                the skill itself
├── SKILL.md              pipeline orchestration (PREFLIGHT → ARGUE → COMPOSE → EXPORT)
├── references/
│   ├── narrative-methodology.md   narrative decision layer (Amazon × MBB)
│   ├── style-system.md            visual decision layer (L1×L2×L3, T1-T7, R1-R10)
│   ├── typography.md              A4 mechanics + T1 implementation + .page DOM contract
│   ├── humanize.md                text polish (humanize checklist + first-read rule)
│   ├── batch-mode.md              book-scale tiering N0/N1/N2 (6-pager principles)
│   └── input-protocol.md          Phase 0 preflight + verification toolbox
├── assets/template.html           T1 skeleton (.page / .narrative / .appendix tiers)
├── scripts/
│   ├── export.py                  PDF/PNG export + overflow check
│   ├── extract.py                 PDF text extraction (page-anchored)
│   └── check.py                   bundled verification toolbox
└── evals/
    ├── evals.json                 4 scenarios × structural+humanize+first-read assertions
    ├── README.md                  reproduction protocol
    └── files/                      input fixtures (3 files)
examples/                 4 real outputs (HTML + PNG previews), regenerated to pass
                          the skill's own current assertions
```

## Evaluated

Four scenarios × (with-skill vs baseline) subagent runs: fork routing 4/4, house-pattern structure assertions all passing, body weasel-word-free, one-page constraint held through 2–3 rounds of word-cutting without ever shrinking type. A separate 20-query trigger-routing test (10 should-trigger incl. deck-as-input probes, 10 near-miss negatives) passed 20/20 in subagent simulation; re-verified after the description trim with the fragile subset. The eval protocol ships with input fixtures — see `one-pager/evals/`; the `examples/` directory doubles as reference output for each eval and passes the current assertion set (`scripts/check.py` reports `ALL RUN CHECKS PASS` on all four).

## License

MIT
