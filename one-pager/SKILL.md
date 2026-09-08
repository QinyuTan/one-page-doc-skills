---
name: one-pager
description: Compress any input — a book, article, course notes, slides/deck, market research, proposal, or quarterly report — into a single-page narrative document (one-pager) combining Amazon memo-style argumentation with editorial print typography. Use whenever the user wants to distill lengthy material into one page ("把书读薄", "summarize this book/article/deck into one page"), write a one-page proposal, memo, pitch, executive brief or summary, or insight page, or needs a compact, shareable, visually polished single-page document for learning, presenting, reporting, or convincing. Also use when the user complains that slides are too scattered, documents are too long or too dense, reading takes too much effort, or asks for a "single page", "一页纸", "one-pager", or a dense-but-readable digest. Do NOT use to create or edit multi-slide decks — it is deliberately NOT a PPT tool; it produces exactly one content page (plus an optional data appendix).
---

# One-Pager

Think in narrative, not slides. This skill compresses any input into **exactly one A4 page** — a document that argues like an Amazon memo and looks like it came from a good magazine's art desk.

It exists because every common format fails the same way: PPTs scatter one idea across twelve bullets, docs sprawl past anyone's attention, and AI summaries are walls of text with no visual hierarchy. A one-pager forces the highest form of clarity: the discipline of fitting everything that matters into one page.

Two decision layers, each with exactly one authoritative reference — this SKILL.md only orchestrates the pipeline:

- **What to say** — `references/narrative-methodology.md` (Amazon narrative culture × MBB distillation; solely governs content, structure, and cutting)
- **How it looks** — `references/style-system.md` (L1 气质 × L2 骨架 × L3 皮肤, T1–T7 presets, R1–R10 veto rules)

Plus the invariant A4 mechanics every template shares (`references/typography.md`). A one-pager that argues well but looks default, or looks great but argues nothing, has failed — the page must deliver narrative logic, key content, and visual craft at once.

> 术语注：narrative-methodology.md 的 **L1/L2/L3** 指叙事三层（论证/段落/句子）；style-system.md 的 **L1/L2/L3** 指视觉三层（气质/骨架/皮肤）——读哪份文件就以哪份为准。style-system 的 **T1–T7** 指视觉预捆模板；batch-mode.md 的 **N0/N1/N2** 指批量产出三级（一页纸/六页稿/附页）。三套编号互不相干。

## The pipeline

Phase 0 preflight, then three phases, strictly ordered. QC gate failure sends you back to Phase 1, never forward to nicer typography.

### Phase 0 — PREFLIGHT: classify and prepare the input

Read `references/input-protocol.md`. Classify the input by shape (plain text / PDF / URL / idea-only / multi-file), run the matching preflight (PDFs get text-extracted first — the skill does not parse them natively; the extraction step is documented, not improvised), and for book-scale sources run the navigation-first 80/20 scan (TOC → introduction → book-structure → all chapter summaries → afterword, then selective deep reads, with per-chapter depth recorded for the 论据地图). The preflight decides which Phase 1 protocol is even available.

### Phase 1 — ARGUE: run the narrative protocol

1. Read `references/narrative-methodology.md` first. It solely decides what to say, how to say it, and what to cut. Select the protocol:
   - **0→1 生成** — no source material; build the argument from an idea (定读者与动作 → Working Backwards PR → 反方 FAQ 轰炸 → SCQ+A 金字塔 → 五维度填空 → 句法过稿).
   - **100→1 浓缩** — compress existing material (book, long doc, notes, report) via the five-step distillation (80/20 扫描 → 单句主张 → 归纳分组 → 结论做标题 → 证据降级). 浓缩 ≠ 摘要：归纳向上，不是删减向下。
   - **批量输入 batch** — single source ≥ 50k characters, or multiple files combining to ≥ 50k: produce the tiered output (N0 one-pager + N1 six-page narrative + N2 appendix) per `references/batch-mode.md`, which borrows Amazon 6-pager principles (body ≤ 6 pages, appendix unlimited, silent-read survival). Multiple files under 50k combined stay on the normal 100→1 protocol. Declare `MODE: batch` in your output.
2. **Route the scenario fork by one question: what does the reader do next?**
   - **学习复述** (books, long articles, courses) → Book Memo 房屋模式
   - **决策行动** (work docs, meeting notes, proposals, approvals) → Proposal 五段式房屋模式
   - **信服洞察** (research reports, data analyses) → Insight Page 房屋模式

   Off-table material (竞品分析, 复盘, personal summaries) routes by the same question; if no fork fits, challenge whether this should be a one-pager at all before proceeding.
3. Work **L1 → L2 → L3 in order — no skipping** (argument structure → paragraph coverage → sentence discipline; thinking about sentences first is how you end up with no claim). Every number in the body carries a (D#) data anchor with a corresponding row in the appendix traceability table (五列：锚点/数据值/来源/时间版本/可复核路径).
4. **Pass the QC gate (Q1–Q9) before any visual work** — elevator test, horizontal logic, So What, weasel scan, quantification scan, MECE, adversarial FAQ, one-page constraint, data traceability. Any failure loops back into the protocol.
5. **Run the text polish pass.** Read `references/humanize.md` — two movements: the humanize checklist (rewrite the body to remove AI-writing tells: three-item rhythm-padding, label-colon structures, dash overuse, quotable-sounding lines, uniform sentence rhythm) and the first-read rule (every sentence survives a first-time reader: jargon glossed or replaced on first appearance, acronyms expanded, no back-references, parseable in one linear pass — the source's own jargon always gets translated, in every fork). It runs after the QC gate and before the handoff; it rewrites sentences, never claims, structure, or fork patterns. Where humanizer advice conflicts with one-page discipline ("allow digressions"), the one-page constraint wins. Record the self-check score in the run log.
6. Budget heuristic for the body: ≤ 500 English words / ≤ 700 Chinese characters — a pressure tool for distillation; the hard gate is Q8.

Handoff contract to Phase 2 (methodology §7): one-line claim + SCQ opening + 3–7 conclusion-titled information groups + appendix evidence pack (always including the data traceability table). The information-group count is the visual layer's skeleton-selection input (e.g. 3 comparison groups → S5 split, many parallel groups → S1/S6, data-dominant → S7).

### Phase 2 — COMPOSE: route the style, then fill the page

1. **Route the look — and when the user hasn't named a style, help them find it.** Read `references/style-system.md` — the visual decision layer. Route in this order, spending the least interaction the situation needs:
   - **User named a style** ("瑞士风", "像杂志特稿") → map to the nearest template, declare any deviation, don't re-ask.
   - **User's phrasing carries the signal** ("给领导看", "发布会", "有杂志感") → quick-route table §8, proceed.
   - **No signal, but the scenario is clear** → **recommend with a reason**: state the routed template and why it fits this content and reader (e.g. "数据汇报给管理层 → T1 瑞士蓝本：数据密度高、决策场景、打印分发"). The user confirms or overrides — this is guidance, not deciding for them.
   - **Aesthetic intent genuinely unclear** → ask **one** anchoring question in reference objects, not style jargon: 「这份纸更像哪种印刷品——董事会备忘录、杂志特稿、发布会海报，还是开发者文档？」(the T1–T7 presets translated into everyday print objects). One question, then proceed on the answer.
   - **Still torn** → R10: three previews (safe template, bold variant, wildcard) and let their eyes choose — no process metadata on the pages.
   Cap discovery at one round of interaction; a style interrogation is worse than a good default. The user's pick is final — lock it, don't re-confirm.
   **Declare the template number + skin parameters at the top of your output before writing any HTML.**
2. Read `references/typography.md` for the A4 mechanics (canvas, type floors, self-containment, print rules). `assets/template.html` is the T1 reference implementation — fill its slots. Other templates are built to their T-spec in style-system.md §4 on the same mechanics.
3. **Density follows the scenario fork** (style-system §7): 学习复述 → low density (≤3 信息组, display enlarged, ≥40% whitespace); 决策行动/信服洞察 → higher density (≤5 信息组, grid that stands alone without a presenter).
4. Fill the page. Apply R1–R10 as veto rules throughout. If the user's aesthetic intent is unclear, generate three previews per R10 (safe template, bold variant, wildcard) and let their eyes choose — no process metadata ("preview"/"Option A") on the pages themselves.
5. Embed images as base64 so the file is fully self-contained; one file, viewable anywhere, printable as-is.
6. **Verify the page fits** (render, assert scrollHeight per R1). If it overflows: cut words, move detail to the appendix, or simplify the skeleton — never shrink type to force fit (R1).
7. The appendix renders as its own A4 page after the body — labeled, relaxed, free-format, and always carrying the data traceability table. Discipline lives on page one; evidence lives in the appendix. In batch mode, the N1 narrative tier (the template's `.narrative` block) sits between N0 and the appendix — same accent, reusing global body styles, ≤ 6 pages per `references/batch-mode.md`.

### Phase 3 — EXPORT

Run `scripts/export.py <file.html>` to produce PDF (and PNG on request) via headless Chromium/Edge, then `uv run --with pypdf python scripts/check.py <file.html>` for the bundled verification (R1 overflow, Q4 weasel, Q9 anchors, humanize + first-read spot-checks, PDF census; it reports unrunnable checks as NOT RUN instead of skipping them). See `references/input-protocol.md` for what the toolbox deliberately does not check. Deliver the HTML plus exports with toolbox results in the run log.

Python deps (if missing): `pip install playwright && playwright install chromium`, plus `pip install pypdf`. Without Playwright, export.py falls back to system Edge/Chrome automatically.

## Non-negotiables

- **Exactly one content page (N0).** The constraint is the product. In batch mode the six-page narrative is a separate tier with its own ≤ 6-page budget — N0's one-page discipline is untouched.
- **Full-sentence narrative for arguments.** Bullets only for list-natured content (行动项 / Non-Goals / appendix data); enumerated items inside argument prose use 行内编号 [N] to keep the narrative flow and give every point a referenceable anchor.
- **Quantify or cut, with (D#) anchors.** Unsourceable numbers get a source, get cut, or get explicitly marked 估计值/待验证 — never dressed as sourced.
- **Each layer has one arbiter.** Narrative follows narrative-methodology.md; style follows style-system.md (R1–R10 veto). Do not freelance around either.
- **Chinese or English output** matching the user's language; keep proper nouns and established terms in their original language.

## File map

| File | Read when |
|---|---|
| `references/narrative-methodology.md` | Phase 1 — always first; the narrative decision layer |
| `references/humanize.md` | Phase 1 — after the QC gate; text polish (humanize checklist + first-read rule) |
| `references/batch-mode.md` | Phase 1 — book-scale input; the N1 six-page narrative tier (Amazon 6-pager principles) |
| `references/input-protocol.md` | Phase 0 — input preflight (PDF/URL/multi-file) + the 80/20 navigation scan; Phase 3 — the verification toolbox (`scripts/check.py`) |
| `references/style-system.md` | Phase 2 — route the look (L1→L2→L3 / T-presets, R1–R10) |
| `references/typography.md` | Phase 2 — A4 mechanics + T1 implementation |
| `assets/template.html` | Phase 2 — the T1 page skeleton to fill |
| `scripts/export.py` | Phase 3 — PDF/PNG export + overflow check |
| `scripts/extract.py` | Phase 0 — PDF text extraction (page-anchored) |
| `scripts/check.py` | Phase 3 — bundled verification toolbox |

## Examples

**Example 1 — 100→1, 学习复述 fork:**
Input: "帮我把这本《Working Backwards》的笔记读薄成一页，下周读书会分享，重点是团队可以直接借鉴的做法" + notes file
Output: Chinese one-pager via the Book Memo house pattern (一句话定位 → 作者的问题 → 骨架 X 光 → 术语表 → 惊讶点 punchlines → What of it), appendix carries the 论据地图 mapping chapters to conclusions plus remaining notes.

**Example 2 — 100→1, 决策行动 fork:**
Input: "把 Q3 获客实验结果写成一页纸给管理层，数据在附表，结论是裂变 ROI 最高、信息流该砍"
Output: Chinese one-pager via the Proposal 五段式 (Purpose BLUF with decision flag → What we observed (a)–(e) → Proposed solution [1]–[N] with Owner labels → Next Steps with governance cadence → The End), channel data table with (D#) anchors in the appendix traceability table.
