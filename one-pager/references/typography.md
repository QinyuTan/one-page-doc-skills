# A4 Mechanics & the T1 Reference Implementation

Two documents govern how the page looks; they do different jobs:

- `references/style-system.md` — the **visual decision layer**: which look (L1 气质 → L2 骨架 → L3 皮肤, or a T1–T7 preset), routed from user phrasing and content shape. Its R1–R10 rules and anti-slop blacklist are law and veto anything here on conflict.
- this file — the **invariant A4 mechanics** every template shares (canvas, self-containment, type floors, print, overflow), plus the px-level spec of T1 as implemented in `assets/template.html`.

Read style-system.md first; read this when composing.

## Canvas & grid (all templates)

- A4 portrait: 794 × 1123 px (= 210 × 297 mm at 96dpi). Fixed size; everything must fit inside.
- Page padding: 52px top/bottom, 56px left/right.
- Body reads in one measure, max-width ~46em. Metrics/callouts may use a 3-column grid; figures full width.
- Chinese display lines ≤ 12 chars (R9); rewrite the headline before shrinking it.

## Self-containment law

One portable file: no external URLs, no webfonts, images base64-embedded only. The page must open and print identically anywhere, offline.

**Declared deviation from T1's display font**: the reference implementation uses the system sans stack (`Helvetica Neue → Microsoft YaHei UI / Noto Sans SC`) instead of Space Grotesk/Archivo-class display faces, because a shareable one-pager's portability outranks font distinctiveness. The anti-slop rule against system-font displays is knowingly traded away here — compensate with the weight ladder (200 display vs 400 body) and the 4:1 size contrast, which carry the Swiss look regardless of typeface. If the user's page is online-only and accepts a network fetch, upgrade to Space Grotesk/Archivo + Noto Sans SC via webfont and declare the deviation.

## Type floors (R3, translated to px)

| Role | Spec |
|---|---|
| Display (title) | 54px, weight 200 — keeps display:body ≥ 4:1 |
| Deck (subtitle) | 14px, weight 400, grey-3 |
| Lead / BLUF | 15.5px, weight 400, 3px accent left bar |
| Body | 13.5px (= 10.1pt, within the 9.5–10.5pt band), line-height 1.78 |
| Metric value | 38px, weight 200 (supporting element; only the title is display-class in T1) |
| Mono meta (kicker, labels, table heads) | 10.7px = 8pt, uppercase, letter-spacing 0.14em, weight 500 |
| Caption / footnote | 10px = 7.5pt — the absolute floor |
| Appendix body | 11.5px, relaxed zone |

Never go below a floor; cut words instead. R1 bans shrinking type to force-fit — the floors exist to make that ban easy to obey.

## T1 reference implementation (`assets/template.html`)

The template encodes these decisions so you fill slots instead of styling:

- **Color**: paper `#fafaf8`, grey-1 `#f0f0ee`, grey-2 `#d4d4d2`, grey-3 `#737373`, ink `#0a0a0a` — fixed, never pure black/white. One accent per page from the four T1 options (IKB `#002FA7` default, orange `#FF6B35`, lemon yellow `#FFD500` / green `#C5E803` as non-text only). R2: accent ≤10% of area.
- **Weight ladder**: bigger = lighter — 200 for display and metric values, 400 body, 500–600 small mono labels.
- **Structure**: 2px ink rule under the header (the only one); 1px grey-2 hairlines elsewhere; 7px accent squares before section labels. Tables: horizontal hairlines only, no vertical borders, no fills. Figures: full-width base64, hairline above/below, mono caption.
- **Appendix**: own A4 page (`break-before: page`), "APPENDIX" kicker, free format at appendix scale. Discipline lives on page one; evidence lives here.

Other T-templates are built to their own spec (style-system §4) on top of these same mechanics — same canvas, same floors, same self-containment, same print rules.

## The `.page` DOM contract (all templates)

`scripts/export.py --check` asserts overflow against `.page` — a fixed-height A4 box (`width: 794px; height: 1123px; overflow: hidden`). **Every template, including T2–T7 built from scratch, must keep a `.page` element with exactly that geometry as the assertion anchor** — restyle its interior freely, never the fixed-height box itself. A page without `.page` silently breaks one-page verification; that is the one DOM rule this skill cannot verify for you if you drop it.

## Print & export

- `@page { size: A4; margin: 0 }`, print background colors on.
- The PDF must be exactly 1 content page + optional appendix pages. Verify with `scripts/export.py --check` (scrollHeight assertion per R1) or by counting PDF pages.
- One decoration pair per page maximum (R6): in T1 that is hairlines + accent squares.

## Overflow protocol (R1 — in order, never shrink type)

1. Cut words per the narrative budget (merge claims; move detail to the appendix, keep the number).
2. Move more detail to the appendix — anything a diligent reviewer, not the page's reader, needs.
3. Simplify the skeleton: drop the deck line, reduce metrics 3→2 columns, or downgrade the skeleton (e.g. S2→S1) per style-system §2.
4. Renegotiate with the user — the input wants a two-pager; say so instead of silently overflowing.

Never: shrink type below the scale (R1), strip the numbers behind claims, or drop the ask / transfer advice.
