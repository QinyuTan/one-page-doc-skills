# Evals — reproduction protocol

Four scenarios cover the three scenario forks plus a pain-point trigger case (no "one-pager" keyword in the prompt — the complaint alone must trigger the skill).

| Eval | Protocol | Fork / house pattern | Input fixture | Reference output |
|---|---|---|---|---|
| 1 | 100→1 | 学习复述 · Book Memo | `files/notes.md` | `../../examples/book-memo-working-backwards.html` |
| 2 | 100→1 (data in prompt) | 决策行动 · Proposal 五段式 | — | `../../examples/proposal-q3-budget-zh.html` |
| 3 | 100→1 | 决策行动 · Proposal 五段式 (English) | `files/market_research.md` | `../../examples/proposal-pricing-en.html` |
| 4 | 100→1, pain-point trigger | 信服洞察 · Insight Page | `files/competitive-research.md` | `../../examples/insight-competitive-research.html` |

## How to reproduce

For each eval, run the prompt twice in fresh sessions (subagents preferred, so the with-skill run has no leakage from the baseline):

1. **Baseline**: the prompt + fixture, no skill.
2. **With-skill**: read `../SKILL.md` and follow it (it routes you into `../references/` as instructed), same prompt + fixture.

Then grade the with-skill output against the `assertions` in `evals.json`:

- **Structural assertions are programmatically checkable** — fork-specific sections present, cross-fork elements absent (e.g. Book Memo pages must not carry `The End` or `Owner:` labels), `(D#)` anchors resolving bidirectionally into the appendix traceability table, weasel-word scan on the body, PDF page census (1 content page + appendix pages).
- **Visual quality is human judgment** — render the HTML and review against the declared template and R1–R10 rules (per the style system's own "Show Don't Tell" principle, eyes beat prose).

## Notes

- Fixture data is synthetic but internally consistent; eval 3's assertions reference figures that appear verbatim in `files/market_research.md` (122% NRR, +$1.9M ARR, 41% lost-deal reason).
- The reference outputs in `examples/` were produced by the iteration-1 with-skill runs and subsequently hardened to pass the current assertion set (dash budgets, acronym glossing, confidence statement); treat them as calibration anchors, not golden files — wording may differ across models while still passing every structural assertion. Verify any candidate with `python ../scripts/check.py <file.html>`.
- Iteration-1 headline results (single model): fork routing 4/4, house-pattern structure assertions all passing, body weasel-free, one-page constraint held without shrinking type, trigger routing 20/20 on a separate query set.
