<div align="center">

# one-pager

### Compress anything into one page worth reading.

**An agent skill that produces one-page narrative documents — argument that survives an Amazon memo review, typography that looks like a magazine's art desk did it.**

[![License: MIT](https://img.shields.io/badge/License-MIT-0a0a0a.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/npx%20skills%20add-QinyuTan%2Fone--page--doc--skills-002FA7.svg)](#install)
[![Evals](https://img.shields.io/badge/evals-30%20assertions%20%C3%97%204%20scenarios%20%C3%97%20ALL%20PASS-FF6B35.svg)](#evaluated--audited)
[![Audit](https://img.shields.io/badge/3--round%20adversarial%20audit-7.5%20%E2%86%92%207.4%20%E2%86%92%208.1-brightgreen.svg)](#evaluated--audited)

*A book → 1 page. A 60-page report → 1 page. Your Q3 results → 1 page the CEO actually reads.*

**English · [中文文档](README.zh-CN.md)**

</div>

---

<p align="center">
  <img src="examples/proposal-q3-budget-zh.png" width="31%" alt="Decision memo example">
  <img src="examples/book-memo-working-backwards.png" width="31%" alt="Book memo example">
  <img src="examples/insight-competitive-research.png" width="31%" alt="Insight page example">
</p>
<p align="center"><sub>Three of the four shipped examples — decision memo · book memo · insight page. All pass the skill's own 30-assertion verifier.</sub></p>

---

## Why

Every format fails the same way. Slides scatter one idea across twelve bullets. Documents sprawl past anyone's attention. AI summaries are walls of text with no hierarchy.

A one-pager forces the highest form of clarity — fitting everything that matters into one page. **The constraint is the product.**

The skill is two decision layers, each with exactly one authoritative reference:

| Layer | Governs | Distilled from |
|---|---|---|
| **Narrative** `narrative-methodology.md` | What to say, how to say it, what to cut | Amazon narrative culture (6-pager, PR/FAQ, Working Backwards) × MBB distillation (pyramid, 80/20, Action Title) — with a source genealogy table |
| **Visual** `style-system.md` | How it looks | 48 first-hand style samples → three-level routing, T1–T7 presets, R1–R10 veto rules, an anti-AI-slop blacklist |

Plus invariant A4 mechanics, a dual text-polish pass, and a programmatic verification toolbox. One arbiter per layer, every layer auditable.

## Three forks, one question

Routing asks only: *what does the reader do next?*

| Reader's next action | Scenario | House pattern |
|---|---|---|
| **Retell it** | Books, courses, long articles | Book Memo (Adler × Sivers × Feynman) |
| **Decide** | Proposals, approvals, quarterly reviews | Proposal five-part form (distilled from a real AWS GCR proposal) |
| **Be convinced** | Research reports, data analyses | Insight Page (Zelazny × FT data journalism) |

Book-scale input (≥ 50k characters)? Batch mode tiers it: **N0** one-pager (30 seconds) + **N1** six-page narrative (a 10-minute silent read, built on Amazon 6-pager principles) + **N2** unlimited appendix. Readers dive as deep as they need.

## Seven looks, zero jargon

The visual layer routes like an art director — 7 temperaments × 7 skeletons × 5 skin slots, or a preset straight off the shelf:

| Preset | Name | The page feels like |
|---|---|---|
| **T1** | Swiss Blueprint | A trust's year-end report set by a modernist: Klein-blue accent, hairline rules, type that gets *thinner* as it gets bigger. For data, decisions, anything your leadership prints. |
| **T2** | Magazine Feature | A Sunday long-form supplement: serif display, drop caps, pull quotes, five ink themes. For stories, research, anything human. |
| **T3** | Archive Ledger | An institution's vault: ivory paper, ink, one deep accent, ledger tables with archival numbering. For white papers, investor briefs, anything that should feel *permanent*. |
| **T4** | Poster Manifesto | Half a page for one claim in ultra-bold type; the other half carries the evidence. For launches, manifestos, one message that must land. |
| **T5** | Paper Craft | Handwritten annotations, paper texture, washi tape — three hand-drawn touches maximum. For workshops, interviews, anything warm. |
| **T6** | Era Revival | Win95 chrome, cassette-rainbow, riso print — era symbols that *serve the story*. For nostalgia with intent. |
| **T7** | Terminal Noir | GitHub-dark canvas, terminal green, all mono, scanlines. For developer docs, anything that ships to engineers. |

**You never have to know these names.** The style-discovery protocol spends the least interaction possible:

- Name a style ("Swiss", "like a magazine feature") → mapped directly, deviations declared
- Your phrasing carries the signal ("for the leadership", "launch event") → routed, no questions asked
- Scenario is clear → it **recommends with a reason** ("data memo for leadership → Swiss Blueprint: high density, decision context, print-friendly")
- Genuinely unclear → **one** question, in reference objects rather than jargon: *"Which printed thing is this closest to — a board memo, a magazine feature, a launch poster, or developer docs?"*
- Still torn → three previews (safe / bold / wildcard), you judge with your eyes

Whatever it picks, it **declares template + skin before writing a single line of HTML** — and the R1–R10 hard rules veto anything templated: one accent per page, no gradients, no rounded corners, no decorative color that encodes nothing, display lines capped at 12 Chinese characters.

## The pipeline

```
PREFLIGHT → ARGUE → COMPOSE → EXPORT
(classify      (fork, layers,    (route style,     (self-contained HTML
 the input,     QC gate Q1–Q9,   fill the page,     + PDF/PNG + 6 programmatic
 extract PDFs,  text polish)     verify fit)        assertions)
 scan books)
```

Every number in the body carries a `(D#)` anchor resolving bidirectionally into an appendix traceability table — a reader can crosscheck any figure in under 3 minutes. Text passes a dual polish: no AI tells (dash budgets, no screenshot-quotable lines, rhythm variation) and a **first-read rule** — every sentence survives a first-time reader, jargon glossed on first use.

## Install

```bash
npx skills add QinyuTan/one-page-doc-skills
```

Works with Claude Code, Codex, Cursor, Windsurf, iClaw, Baymax — anything that speaks skills. **Manual**: copy `one-pager/` into your agent's skills folder. **Optional Python** for export: `pip install playwright && playwright install chromium` (falls back to headless Edge/Chrome automatically).

## Use — just talk

- "Distill my notes on *Principles* into one page for Friday's book club"
- "One page on the Q3 experiments for leadership — the call is to cut paid feed and move budget to referral"
- "This 60-page research report is dying in the group chat — compress it to one page people can grasp in 3 minutes"
- "Write a one-pager for our seed round"

Even the complaint alone triggers it: *"too long, no highlights"* is a valid brief. The skill declares its routing before writing any HTML — fork, template, skin — so you can always override.

## Evaluated & audited

- **4 scenarios × (with-skill vs baseline)** subagent runs: fork routing 4/4, structure assertions passing, weasel-word-free, one-page constraint held through 2–3 rounds of word-cutting — **zero type-shrinking, ever** (R1 is a hard rule)
- **20/20 trigger-routing** simulation, including the deck-boundary cases: deck-as-*input* (summarize this board deck) → one-pager; deck-as-*output* (make a 20-slide PPT) → declined, by design
- **3 rounds of independent adversarial audit**: 7.5 → 7.4 → **8.1**. The dip was real — the audit caught examples failing the skill's own newer rules; they were regenerated and now pass. All 4 shipped examples report `ALL RUN CHECKS PASS` via `scripts/check.py`
- The test set ships with fixtures + a reproduction protocol — clone and re-run everything yourself

## Repository

```
one-pager/
├── SKILL.md                       4-phase orchestration (99 lines, no lore)
├── references/
│   ├── narrative-methodology.md   212 lines, sourced: AWS × MBB × Adler × Zelazny
│   ├── style-system.md            185 lines: 3-level routing, T1–T7, R1–R10, anti-slop
│   ├── humanize.md                text polish: de-AI-tell + first-read rule
│   ├── batch-mode.md              book-scale tiering N0/N1/N2 (6-pager)
│   ├── input-protocol.md          preflight + the verification toolbox
│   └── typography.md              A4 mechanics, type floors, .page DOM contract
├── assets/template.html           Swiss skeleton (.page / .narrative / .appendix)
├── scripts/                       export.py · extract.py · check.py
└── evals/                         4 scenarios, 30 assertions, fixtures, protocol
examples/                          4 real outputs — HTML + PNG, all passing
```

## License

MIT — the two methodology references retain their authorship genealogy. Star it, fork it, feed it a book.

<div align="center">

**One page is all it takes.**

<sub>Built with the discipline it sells: this README survives the same rules the skill enforces — one accent, no decoration that encodes nothing, and not a single claim you can't crosscheck.</sub>

</div>
