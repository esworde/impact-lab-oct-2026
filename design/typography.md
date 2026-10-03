# Typography

## Font families

| Token | Family | Fallback (Bootstrap Italia) | Use |
|---|---|---|---|
| `font.sans` | Titillium Web | `Geneva, Tahoma, sans-serif` | The default for everything: UI, headings and body |
| `font.serif` | Lora | `Georgia, serif` | Optional long-form reading text (`.font-serif`, or `.lora` in the Comuni templates) |
| `font.mono` | Roboto Mono | `monospace` | Code (`code-font`) and data or figures (`data-font`) |

- **Licenses:** Titillium Web and Lora are under the SIL Open Font License, Roboto Mono under Apache 2.0.
- **Loading:** Bootstrap Italia ships all three fonts in `dist/fonts` and loads them with `bootstrap.loadFonts(path)`. Google Fonts also works; the link is in [DESIGN.md](DESIGN.md#b-tokens-only-custom-ui-on-the-same-foundations).
- **Weights in use:** 300 light, 400 regular, 600 semibold and 700 bold, plus italics. These are the weights Bootstrap Italia loads. A 200 weight (`font-weight.extra-light`) exists as a token but is not loaded.

## Scale

The 11 steps of the scale, in px: 12 · 14 · 16 · 18 · 20 · 24 · 28 · 32 · 40 · 48 · 56. The tokens are `font-size.1` to `font-size.11` (see [tokens.md](tokens.md#font-size)).

## Text styles

Each style has two sizes: one below 576px (mobile) and one from 576px up (desktop). Sizes come from the tokens (`*-font-size` for mobile, `*-font-size-l` for desktop). Line heights are the ones Bootstrap Italia 2.9.2 renders.

| Style | Element or class | Mobile size / line height | Desktop size / line height | Weight | Tokens |
|---|---|---|---|---|---|
| Display | `.display-1` | 48px | 56px / 1.25 | 700 | none |
| Heading 1 | `h1`, `.h1` | 40 / 48px | 48 / 56px | 700 | `heading-1-font-size`, `-l`; letter-spacing −1px |
| Heading 2 | `h2`, `.h2` | 32 / 40px | 40 / 48px | 700 | `heading-2-font-size`, `-l` |
| Heading 3 | `h3`, `.h3` | 28 / 32px | 32 / 40px | 700 | `heading-3-font-size`, `-l` |
| Heading 4 | `h4`, `.h4` | 24 / 32px | 28 / 32px | 600 | `heading-4-font-size`, `-l` |
| Heading 5 | `h5`, `.h5` | 20 / 24px | 24 / 32px | 600 | `heading-5-font-size`, `-l` |
| Heading 6 | `h6`, `.h6` | 16 / 24px | 18 / 24px | 600 | `heading-6-font-size`, `-l` |
| Lead | `.lead` | 20 / 32px | 24 / 32px | 400 | `lead-font-size`, `-l` |
| Body | `p`, `ul`, `ol`, `dl` | 16 / 24px | 18 / 28px | 400 | `body-font-size`, `-l` |
| Small | `small`, `.small` | 14px | 14px | 400 | `caption-font-size`, `label-font-size-s` |
| Caption | `caption`, `figcaption` | 14 / 16px | 14 / 16px | 400 | `caption-font-size` |
| Extra small | `.x-small` | 12px | 12px | inherited | `label-font-size-xs` |
| Blockquote | `blockquote`, `.blockquote` | 18 / 24px | 18 / 24px | 400 | none; 4px left border in `$analogue-2` `#0bd9d2` |
| Button | `.btn` (`.btn-xs`, `.btn-sm`, `.btn-lg`) | 16px (14 / 16 / 18) | same | 600 | none |

- **Heading weights:** H1 to H3 use `heading-font-weight` (700); H4 to H6 use `heading-font-weight-weak` (600).
- **Line heights:** the tokens set the intent (headings 120%, body 150%, lead and caption 130%, labels 110%). Bootstrap Italia uses fixed rem values close to these; for example H1 is 48/40 = 1.2 and body is 24/16 = 1.5.
- **Tracking:** body text uses 0 (`font-tracking.normal`). Large headings tighten it: `short` (−1px) on H1, and `narrow` (−1.3px) or `tight` (−2px) on display sizes in Figma.
- **Text color:** body text is `color.text.base` (`#1a1a1a`), or `#191919` in the Comuni templates. Card titles use `color.text.secondary` (`#2f475e`).

## Specific typography tokens

The full list of role tokens (`heading-*`, `body-*`, `lead-*`, `caption-*`, `label-*`, `code-font`, `data-font`) is in [tokens.md](tokens.md#typography-roles).

## Modello Comuni text utilities

The templates add their own classes in `src/stylesheets/headings/`. The `font($mobile, $desktop)` mixin switches size at 576px. Sizes are in px.

| Class | Mobile → desktop | Weight | Line height |
|---|---|---|---|
| `.title-xxxlarge` | 40 → 48 | 700 | 1.25 |
| `.title-xxlarge` | 32 → 40 | 700 | 1.25 |
| `.title-xxlarge-regular` | 32 → 40 | 400 | 1.25 |
| `.title-xlarge` | 28 → 32 | 700 | 1.25 |
| `.title-large` | 24 | 700 | 1.25 |
| `.title-large-semi-bold` | 24 → 28 | 600 | 1.25 |
| `.title-medium-2`, `-semi-bold`, `-bold` | 20 → 24 | 400, 600, 700 | 1.25 |
| `.title-medium` | 18 | 400 | 1.5 |
| `.title-medium-semi-bold`, `-bold` | 18 | 600, 700 | 1.25 |
| `.title-small` | 16 | 700 | 1.5 |
| `.title-small-semi-bold` | 16 | 600 | 1.5 |
| `.title-xsmall`, `-semi-bold`, `-bold` | 14 | 400, 600, 700 | 1.5 |
| `.subtitle-large` | 28 → 32 | 700 | 1.25 |
| `.subtitle-medium` | 24 → 28 | 600 | 1.25 |
| `.subtitle-small`, `_semi-bold` | 16 | 400, 600 | 1.5 |
| `.text-paragraph` | 16 | 400 | 1.5 |
| `.text-paragraph-medium` | 20 → 24 | 600 | 24px |
| `.text-paragraph-small` | 14 → 16 | 400 | 1.3, then 1.5 from 768px |
| `.text-info` | 12 | 400 | 1.5 |
| `.text-tab` | 14 → 18 | 400 | 2, then 1.5 from 768px |
| `.text-button`, `-semi`, `-normal` | 18 | 700, 600, 400 | 1.5 |
| `.text-button-sm-bold` | 16 | 700 | 1.5 |
| `.text-button-xs-bold` | 12 | 700 | 1.5 |
| `.text-button-card` | 14 | 700 | 1.5 |
| `.date-regular` | 16 | 400 | 1.5 |
| `.date-xsmall` | 14 → 16 | 400 | 1.3 |
| `.lora`, `.titillium` | Switch the font family | | |

## In the Figma UI Kit

- The **Typography** page is the reference and matches the text styles table above. For example, it labels Heading 1 as "48px bold" from 576px up and "40px bold" below. It also shows specimens for lead text (20 and 24px), body text (16 and 18px), Lora body text, captions, lists, description lists and text decorations (underline, highlight, italic, bold, strikethrough).
- The page labels mobile Heading 5 as 24px; the tokens and Bootstrap Italia use 20px.
- The file also contains about 330 text styles. Many are legacy and don't match the v3 tokens, for example `Desktop/H1` at 56/64 and `Mobile/H1` at 40/48 with −0.5px tracking. Prefer the tokens.
- Number styles use Roboto Mono, for example `Desktop/Numbers Regular` at 18/27. Use `data-font` for tables and figures.
