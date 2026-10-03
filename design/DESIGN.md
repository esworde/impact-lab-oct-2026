# Design system: .italia and Modello Comuni

This is the visual language of Italian public-sector websites, extracted for Impact Lab projects. Use it when your prototype should look and behave like a digital service from the City of Milan, or any other Comune.

| File | Contents |
|---|---|
| [DESIGN.md](DESIGN.md) | This page: sources, quick start, rules and layout grid |
| [tokens.md](tokens.md) | All 299 design tokens, each with its CSS variable and resolved value |
| [colors.md](colors.md) | Palettes, semantic color roles, the Modello Comuni palette and contrast ratios |
| [typography.md](typography.md) | Fonts, type scale, heading and body styles, and the Comuni text utilities |
| [components.md](components.md) | The UI Kit component inventory, Bootstrap Italia classes and the Comuni page templates |

## Sources

These files were extracted on 3 October 2026 from:

| Repository | Version | What it provides | License |
|---|---|---|---|
| [italia/design-tokens-italia](https://github.com/italia/design-tokens-italia) | v1.3.3 (`b59fe73`) | Design tokens as JSON (global, semantic and specific), compiled to CSS and SCSS variables | BSD-3-Clause |
| [italia/design-ui-kit](https://github.com/italia/design-ui-kit) | v3.8.0 (`7bb653c`) | UI Kit Italia, the Figma source of truth: foundation pages, styles and about 45 component pages | CC BY 4.0 |
| [italia/design-comuni-pagine-statiche](https://github.com/italia/design-comuni-pagine-statiche) | v2.4.0 (`0fa4176`) | HTML templates for the *Modello Comuni*, the national model for municipal websites and online services | BSD-3-Clause |

The Comuni templates are built on [Bootstrap Italia](https://italia.github.io/bootstrap-italia/) **2.9.2**, which is based on Bootstrap 5.2.3. Values labeled "Bootstrap Italia" come from that package's SCSS, because that SCSS is what the templates actually render.

### How the pieces fit

```
UI Kit Italia (Figma) ──Tokens Studio export──▶ design-tokens-italia ──▶ --it-* CSS vars / $it-* SCSS vars
        │
        └── component designs ──▶ Bootstrap Italia (CSS + JS on Bootstrap 5) ──▶ Modello Comuni templates
```

Bootstrap Italia 2.9.2 does **not** import the token package; that import is commented out in its `_variables.scss`. It hardcodes the same values instead and adds comments naming the matching tokens, for example `$gray-100: hsl(0, 0%, 96%); // color-gray-96`. The two therefore agree on values, but Bootstrap Italia gives you no `--it-*` variables.

## Quick start

### A. Full component library (what the Comuni templates use)

```html
<!doctype html>
<html lang="it">
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-italia@2.9.2/dist/css/bootstrap-italia.min.css">
</head>
<body>
  <!-- markup from https://italia.github.io/bootstrap-italia/docs/ -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap-italia@2.9.2/dist/js/bootstrap-italia.bundle.min.js"></script>
  <script>bootstrap.loadFonts('https://cdn.jsdelivr.net/npm/bootstrap-italia@2.9.2/dist/fonts')</script>
</body>
</html>
```

- The bundle does not load fonts on its own. `loadFonts()` injects the `@font-face` rules for Titillium Web, Lora and Roboto Mono.
- Icons come from an SVG sprite: `<svg class="icon icon-primary"><use href="/assets/sprites.svg#it-search"></use></svg>`. **Self-host** `dist/svg/sprites.svg`, because `<use>` cannot load a sprite from another origin. See [components.md](components.md#icons).
- Bootstrap Italia 2.18.3 is the latest release. The Comuni templates are validated against 2.9.2, so pin whichever version you test with.

### B. Tokens only (custom UI on the same foundations)

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/design-tokens-italia@1.3.3/dist/css/variables.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Titillium+Web:ital,wght@0,300;0,400;0,600;0,700;1,400&family=Lora:ital,wght@0,400;0,700;1,400&family=Roboto+Mono:wght@400;600;700&display=swap">
```

```css
body {
  font-family: var(--it-font-sans), Geneva, Tahoma, sans-serif;
  color: var(--it-color-text-base);
  line-height: 1.5;
}
a { color: var(--it-color-link-base); text-decoration: underline; }
a:hover { color: var(--it-color-link-hover); }
.button-primary {
  background: var(--it-color-background-primary);
  color: var(--it-color-text-inverse);
  font-weight: var(--it-font-weight-semibold);
  padding: var(--it-spacing-xs) var(--it-spacing-m); /* 12px 24px, same as Bootstrap Italia .btn */
  border: 0;
  border-radius: var(--it-radius-smooth);
}
.button-primary:hover { background: var(--it-color-background-primary-hover); }
.button-primary:active { background: var(--it-color-background-primary-active); }
:focus-visible { outline: 3px solid var(--it-color-outline-focus); outline-offset: 3px; }
```

## Rules

1. **Use semantic tokens in components.** Write `color.background.primary` and `color.text.secondary`, not `color.blue.40`. Global ramps only define the palette. This is what lets a Comune change its primary color without breaking anything.
2. **Meet WCAG 2.1 AA contrast at minimum.** Text needs 4.5:1 (3:1 when large); icons and input borders need 3:1. Every `text.*` token passes on white except `accent` (3.5:1), which is for large text and icons only. See the [contrast table](colors.md#contrast).
3. **Never signal feedback by color alone.** Success, warning and danger states always pair the color with an icon and a text label (WCAG 1.4.1).
4. **Keep focus visible on every background.** Bootstrap Italia draws a 2px ring in `#995c00` (`orange-30`). The Modello Comuni draws a 3px black ring plus a 3px white outline with a 3px offset. The token is `color.outline.focus` (`#1a1a1a`).
5. **Make links look like links.** Links are underlined by default. `link.secondary` must always be underlined. Hover and active states darken the color: `#0066cc` → `#004d99` → `#003366`.
6. **Space on a 4px baseline.** Every spacing token is a multiple of `spacing.1x` (4px). Bootstrap Italia components use an 8px rhythm (`$v-gap`).
7. **Use Titillium Web for UI and headings** and Roboto Mono for code and figures. Lora is optional, for long-form reading.
8. **Write Italian-first, structured pages.** Set `<html lang="it">` and use one `<h1>` per page. Make the skip links ("Vai ai contenuti", "Vai al footer") the first focusable elements, and add breadcrumbs to every inner page.
9. **Design mobile-first.** Each heading and body style has a mobile size and a larger size from 576px up.

## Layout grid

Bootstrap Italia 2.9.2:

| Breakpoint | Min width | `.container` max width | `.row.variable-gutters` gutter |
|---|---|---|---|
| `xs` | 0 | 100% | 12px |
| `sm` | 576px | 540px | 12px |
| `md` | 768px | 720px | 20px |
| `lg` | 992px | 960px | 24px |
| `xl` | 1200px | **1176px** | 24px |
| `xxl` | 1400px | 1320px | 28px |

- The grid has 12 columns with a default gutter of 24px. Per-breakpoint gutters apply only when you add `.variable-gutters`.
- Text switches to desktop sizes at **576px** (`sm`). The main navigation collapses below **992px** (`lg`).
- Hover-only styles start at **1025px** (`$grid-breakpoints-hover`).
- Aspect ratios: `1x1`, `3x2`, `4x3`, `16x9`, `21x9`.
- Border radius is 4px by default (`radius.smooth`), 2px for small elements, 8px for large ones and 40px for pills (`radius.rounded`). Chips are fully rounded, and card tags use a 50px radius.
- Z-index layers above Bootstrap's: zoom `1080`, growl `1090`, cookie bar `1100`.

## Modello Comuni at a glance

- **Primary color:** HSB 160/100/48, which is `#007a52` (the same as `color.seagreen.24`). Each Comune can set its own through `$primary-h`, `$primary-s` and `$primary-b`; Milan's is `#a60d27`. See [colors.md](colors.md#modello-comuni) and [Comune di Milano](colors.md#comune-di-milano).
- **Chrome:** the slim header is `#00402b`, the center header and navbar use the primary color, the footer is `#202a2e`, body text is `#191919` and grey cards are `#ebeef0`.
- **Main menu (fixed by the model):** Amministrazione · Novità · Servizi · Vivere il Comune.
- **Every page ends the same way:** a page rating ("Quanto sono chiare le informazioni su questa pagina?"), then the "Contatta il comune" box, then the footer.
- **Service flows** follow the steps *scheda servizio → accesso → dati → riepilogo → conferma*, with a stepper, a section index and a bottom bar with the actions Indietro / Salva richiesta / Avanti. See [components.md](components.md#page-templates).
