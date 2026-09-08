# Text Polish Pass — Humanize + First-Read

Runs in Phase 1, **after the QC gate and before the handoff to Phase 2**, in two movements: the humanize checklist (how the text sounds — no AI tells) and the first-read rule (who can understand it — a first-time reader, unaided). The QC gate polishes what the text *says*; this pass polishes *sound* and *access*. A page that argues well but reads machine-generated, or reads clean but gates readers behind jargon, fails the reader all the same.

Distilled from the humanizer-zh skill (Wikipedia "Signs of AI writing", WikiProject AI Cleanup), adapted to the one-pager's constraints, plus the first-read accessibility rule.

## Why one-pagers need this most

Distillation concentrates AI tells. Compressing a book into 700 characters tempts the writer into the statistical average of "impressive-sounding" phrasing: three-item lists, label-colon structures, quotable lines. A one-pager is read closely — every sentence gets attention, so every tell gets seen.

## The checklist (apply to the body; appendix is exempt — see Boundaries)

1. **Three-item lists → two or four.** "思考、行动与观察" / "innovation, inspiration, and insight" is the single most common AI tell. If the content genuinely has three parts, keep three; if the third was padding, cut it. Exception: a fork's house pattern may legitimately enumerate (e.g. three fork types) — enumeration that maps to real structure is not rhythm-padding.
2. **Label-colon structures: ≤ 1 per section — outside mandated house-pattern leads.** "短期最锋利的杠杆在模型之外：……" repeated down a page is an outline masquerading as prose. One may stand as a topic sentence; a column of them means the prose never started. **Exception (reconciled with narrative-methodology):** the Proposal 五段式's mandated structural leads — `(a) 因子：`、`[N] 名称：`、`阶段N：`— and equivalent enumerated conventions from any house pattern are structural enumeration, not prose crutches; they are exempt. What this rule catches is *prose* paragraphs opening with label-colon scaffolding when no pattern mandates it.
3. **Dash budget: ≤ 2 per page.** Dashes imitate "punchy" copywriting. Replace with commas, periods, or nothing. The lead's accent bar already provides the visual punch.
4. **No quotable-sounding lines in the body.** If a sentence sounds like it wants to be screenshot ("可以让 Agent 干活，不能让它替你理解"), rewrite it plainer or delete it. Punchlines in Book Memo's 惊讶点 are instructions ("do X because Y"), not aphorisms — check each one.
5. **Rhythm: no three consecutive sentences of equal length.** Vary long and short. A page of uniform 30-character sentences reads as generated even when every fact is right.
6. **Kill filler and system-verb avoidance.** "值得注意的是" → delete; "作为……的证明/体现" → rewrite as 是/有; "为了实现这一目标" → "为此"; "在……的情况下" → "如果".
7. **Promotional register is already banned by the style system's anti-slop list** — this pass catches its textual equivalents: 首屈一指、令人瞩目、深刻揭示、无与伦比. Numbers replace superlatives (already enforced by Q5; this is the second sweep).
8. **Vague attribution out.** "专家认为/研究表明" without a source is a Q9 violation AND an AI tell; one fix serves both gates — name the source or cut the claim.
9. **Negative parallelism: ≤ 1 per page.** "这不仅仅是 X，而是 Y" and "不是 A，而是 B" constructions. Once can land; a stack of them is a pattern.
10. **Ending: state the next fact, not the significance.** No "这标志着一个新时代" closers. The What of it / So What section already carries the implications — let it do that job in concrete terms.

## The First-Read Rule — 首读者可懂

Every sentence must survive a **first-time reader**: someone intelligent, new to this material, reading linearly, with no glossary in hand. The one-pager is often the reader's only entry to the topic — the book-club colleague who never read the book, the executive who never saw the raw research. If a sentence requires having read the source, it has not earned its place on the page.

1. **Jargon earns its place or leaves.** A term appearing for the first time gets a one-line plain-language gloss right there (parenthetical or apposition), or is replaced by the plain language and demoted to the appendix glossary. 「消融实验（逐个拆掉组件看哪个坏）」 stays; a bare 「消融实验」 fails.
2. **Acronyms expand on first use.** NRR → NRR（净收入留存）； LLM → LLM（大模型）. Terms the appendix glossary already defines still get their inline gloss — the reader should never need to leave the page mid-sentence.
3. **No back-references.** 「如上所述」「上述方案」「这个问题」 force re-reading; a one-pager is a single linear pass. Name the thing again instead of pointing at it.
4. **Unpack nested clauses.** If a sentence needs a second pass to parse, split it. (L3 caps length; this catches grammatical nesting — a different failure.)
5. **The test:** hand the body to a smart colleague who has never seen the source. One pass, 60 seconds, they can restate the claim and the ask. Wherever they stall on a term, that term is the bug. This is the Feynman variant of Q1, extended from the 学习复述 fork to every fork and every tier (N0 body and N1 narrative alike).

**Calibration:** the bar is the *target reader's* reasonable knowledge (L2's Who dimension), not the lowest common denominator — an exec page may use business vocabulary freely; a book-club page may not assume the book's own jargon. What is never acceptable, in any fork: terms the page itself imported from the source without translation.

## Boundaries (where humanizer advice does NOT apply)

- **One-page discipline outranks "allow some mess."** The humanizer's general advice to permit digressions and half-formed thoughts is for long-form prose. A one-pager is an argument instrument; every sentence is load-bearing (Q3). Cut, don't wander.
- **The appendix is exempt.** 金句 sections quote the source's own words (with page anchors) — quoting is not generating. Appendix tables and evidence dumps don't need rhythm.
- **Don't touch structure.** This pass rewrites sentences, never claims, section order, or fork patterns. If a sentence can't be humanized without changing what it asserts, leave it and note it for the user.
- **The reader's language register wins.** A decision memo for executives may legitimately be more formal than a book-club page. Match the page's established tone (L2 Who dimension), don't flatten everything to casual.
- **First-read is calibrated, not absolute** (see Calibration above): meet the target reader where they are — but the source's own jargon always gets translated, in every fork.

## Where it sits in the pipeline

```
L1 → L2 → L3 → QC gate (Q1–Q9) → HUMANIZE pass → handoff contract → Phase 2
```

After humanizing, re-run Q8 only if line counts changed materially (the pass usually shortens text, which helps the one-page budget).

## Scoring (self-check before handoff)

Rate the polished body 1–10 on: 直接性 (no throat-clearing), 节奏 (sentence-length variation), 信任读者 (no over-explaining), 真实性 (sounds like a person), 精炼度 (nothing left to cut). Below 35/50 → redo the pass. Record the score in the run log.
