# Design tokens

Source: [italia/design-tokens-italia](https://github.com/italia/design-tokens-italia) v1.3.3, `tokens/*.json`: 299 tokens. The tables below were generated from the JSON and checked against the compiled `dist/css/variables.css`.

## How they are built

- Designers maintain the tokens in the UI Kit Figma file with [Tokens Studio](https://docs.tokens.studio) and export them as JSON (`$value`, `$type`, `$description`).
- [Style Dictionary](https://styledictionary.com/) 5 compiles them to `dist/css/variables.css` and `dist/scss/_variables.scss`.
- **Naming:** the JSON path in kebab-case with an `it-` prefix, so `color.background.primary` becomes `--it-color-background-primary` in CSS and `$it-color-background-primary` in SCSS. The package README still shows names without the prefix, but the compiled files use it.
- **References are preserved** (`outputReferences: true`). Semantic variables point at global ones, for example `--it-color-background-primary: var(--it-color-blue-40)`. Override a global variable and every token that references it changes too.

## Three tiers

| Tier | File | Tokens | Use it for |
|---|---|---|---|
| Global | `tokens/global.json` | 145 | The raw palette and scales. Don't use these directly in components. |
| Semantic | `tokens/semantic.json` | 97 | Design decisions such as "primary background", "subtle border" or "muted text". This is the default choice in UI code. |
| Specific | `tokens/specific.json` | 57 | A single element: icon colors and sizes, heading sizes, body, label and caption roles. |

## Install

```sh
npm install design-tokens-italia   # requires Node >= 22
```

```css
@import url('https://cdn.jsdelivr.net/npm/design-tokens-italia@1.3.3/dist/css/variables.css');

.notice {
  color: var(--it-color-text-base);
  background: var(--it-color-background-primary-lighter);
  border-left: var(--it-border-thick) solid var(--it-color-border-primary);
  padding: var(--it-spacing-s) var(--it-spacing-m);
  border-radius: var(--it-radius-smooth);
  box-shadow: var(--it-elevation-low);
}
```

```scss
@use 'design-tokens-italia/dist/scss/variables' as *;

.notice { color: $it-color-text-base; padding: $it-spacing-s $it-spacing-m; }
```

## Semantic tokens

### Color: background

| Token | CSS variable | Value | Use |
|---|---|---|---|
| `color.background.primary` | `--it-color-background-primary` | `color.blue.40` → `#0066cc` | Primary fill for interactive elements (buttons, links) and brand-identity elements. |
| `color.background.primary-light` | `--it-color-background-primary-light` | `color.blue.87` → `#bfdfff` | Light-contrast alternative to primary for interactive elements. |
| `color.background.primary-lighter` | `--it-color-background-primary-lighter` | `color.blue.97` → `#f2f7fc` | Low-contrast primary tint that marks a page section or part of one. |
| `color.background.primary-hover` | `--it-color-background-primary-hover` | `color.blue.30` → `#004d99` | Hover state of `primary`. |
| `color.background.primary-active` | `--it-color-background-primary-active` | `color.blue.20` → `#003366` | Active/pressed state of `primary`. |
| `color.background.primary-muted` | `--it-color-background-primary-muted` | `color.blue.30` → `#004d99` | Page-section background. |
| `color.background.primary-deep` | `--it-color-background-primary-deep` | `color.blue.20` → `#003366` | Page-section background (darkest). |
| `color.background.secondary` | `--it-color-background-secondary` | `color.slate.44` → `#5c6f82` | Alternative fill for secondary interactive elements or page sections. |
| `color.background.secondary-hover` | `--it-color-background-secondary-hover` | `color.slate.28` → `#2f475e` | Hover state of `secondary`. |
| `color.background.secondary-active` | `--it-color-background-secondary-active` | `color.slate.20` → `#17324d` | Active/pressed state of `secondary`. |
| `color.background.secondary-light` | `--it-color-background-secondary-light` | `color.slate.68` → `#a3adb7` | Light secondary fill. |
| `color.background.secondary-lighter` | `--it-color-background-secondary-lighter` | `color.slate.85` → `#d9dadb` | Very light secondary fill. |
| `color.background.accent` | `--it-color-background-accent` | `color.teal.32` → `#089994` | Accent fill for interactive elements. |
| `color.background.accent-hover` | `--it-color-background-accent-hover` | `color.teal.26` → `#077f7b` | Hover state of `accent`. |
| `color.background.muted` | `--it-color-background-muted` | `color.gray.96` → `#f5f5f5` | Very light background for page sections or text blocks. |
| `color.background.inverse` | `--it-color-background-inverse` | `color.white` → `#ffffff` | Inverse (white) background, used inside primary, secondary or neutral sections. |
| `color.background.disabled` | `--it-color-background-disabled` | `color.slate.85` → `#d9dadb` | Disabled interactive elements. |
| `color.background.subtle` | `--it-color-background-subtle` | `color.gray.83` → `#d4d4d4` | Light background that separates page sections. |
| `color.background.emphasis` | `--it-color-background-emphasis` | `color.slate.20` → `#17324d` | Emphasis background that highlights a specific page section. |
| `color.background.success` | `--it-color-background-success` | `color.emerald.25` → `#008055` | Success fill for interactive elements and components. Text on it must be `inverse`. |
| `color.background.success-light` | `--it-color-background-success-light` | `color.emerald.87` → `#c8f6e7` | Success tint for sections and components with medium or long content. Any text color except `inverse`. |
| `color.background.success-hover` | `--it-color-background-success-hover` | `color.emerald.20` → `#006644` | Hover state of `success`. |
| `color.background.success-active` | `--it-color-background-success-active` | `color.emerald.15` → `#004d33` | Active/pressed state of `success`. |
| `color.background.warning` | `--it-color-background-warning` | `color.orange.30` → `#995c00` | Warning fill for interactive elements and components. Text on it must be `inverse`. |
| `color.background.warning-light` | `--it-color-background-warning-light` | `color.orange.87` → `#f6e4c8` | Warning tint for sections and components with medium or long content. Any text color except `inverse`. |
| `color.background.warning-hover` | `--it-color-background-warning-hover` | `color.orange.25` → `#804d00` | Hover state of `warning`. |
| `color.background.warning-active` | `--it-color-background-warning-active` | `color.orange.20` → `#663d00` | Active/pressed state of `warning`. |
| `color.background.danger` | `--it-color-background-danger` | `color.red.50` → `#cc334d` | Danger/error fill for interactive elements and components. Text on it must be `inverse`. |
| `color.background.danger-light` | `--it-color-background-danger-light` | `color.red.96` → `#fbeff1` | Danger tint for sections and components with medium or long content. Any text color except `inverse`. |
| `color.background.danger-hover` | `--it-color-background-danger-hover` | `color.red.37` → `#992639` | Hover state of `danger`. |
| `color.background.danger-active` | `--it-color-background-danger-active` | `color.red.25` → `#661a26` | Active/pressed state of `danger`. |

### Color: border

| Token | CSS variable | Value | Use |
|---|---|---|---|
| `color.border.primary` | `--it-color-border-primary` | `color.blue.40` → `#0066cc` | Primary border for clickable elements. |
| `color.border.primary-hover` | `--it-color-border-primary-hover` | `color.blue.30` → `#004d99` | Hover state of `primary`. |
| `color.border.primary-active` | `--it-color-border-primary-active` | `color.blue.20` → `#003366` | Active/pressed state of `primary`. |
| `color.border.secondary` | `--it-color-border-secondary` | `color.slate.44` → `#5c6f82` | Secondary border for clickable elements. |
| `color.border.secondary-hover` | `--it-color-border-secondary-hover` | `color.slate.28` → `#2f475e` | Hover state of `secondary`. |
| `color.border.secondary-active` | `--it-color-border-secondary-active` | `color.slate.20` → `#17324d` | Active/pressed state of `secondary`. |
| `color.border.inverse` | `--it-color-border-inverse` | `color.white` → `#ffffff` | Inverse border on primary, secondary or emphasis backgrounds. |
| `color.border.disabled` | `--it-color-border-disabled` | `color.slate.85` → `#d9dadb` | Disabled interactive elements. |
| `color.border.subtle` | `--it-color-border-subtle` | `color.slate.78` → `#c5c7c9` | Divider between page sections, components or single elements. |
| `color.border.success` | `--it-color-border-success` | `color.emerald.25` → `#008055` | Success border for interactive or static elements (alerts, notifications). |
| `color.border.success-hover` | `--it-color-border-success-hover` | `color.emerald.20` → `#006644` | Hover state of `success`. |
| `color.border.success-active` | `--it-color-border-success-active` | `color.emerald.15` → `#004d33` | Active/pressed state of `success`. |
| `color.border.warning` | `--it-color-border-warning` | `color.orange.30` → `#995c00` | Warning border for interactive or static elements. |
| `color.border.warning-hover` | `--it-color-border-warning-hover` | `color.orange.25` → `#804d00` | Hover state of `warning`. |
| `color.border.warning-active` | `--it-color-border-warning-active` | `color.orange.20` → `#663d00` | Active/pressed state of `warning`. |
| `color.border.danger` | `--it-color-border-danger` | `color.red.50` → `#cc334d` | Danger/error border for interactive or static elements. |
| `color.border.danger-hover` | `--it-color-border-danger-hover` | `color.red.37` → `#992639` | Hover state of `danger`. |
| `color.border.danger-active` | `--it-color-border-danger-active` | `color.red.25` → `#661a26` | Active/pressed state of `danger`. |

### Color: text

| Token | CSS variable | Value | Use |
|---|---|---|---|
| `color.text.base` | `--it-color-text-base` | `color.gray.10` → `#1a1a1a` | Default body text. |
| `color.text.primary` | `--it-color-text-primary` | `color.blue.40` → `#0066cc` | Link text. |
| `color.text.secondary` | `--it-color-text-secondary` | `color.slate.28` → `#2f475e` | Alternative body text, detail content, secondary button text. |
| `color.text.muted` | `--it-color-text-muted` | `color.slate.44` → `#5c6f82` | Supporting text for very short content. |
| `color.text.disabled` | `--it-color-text-disabled` | `color.slate.44` → `#5c6f82` | Disabled text. |
| `color.text.success` | `--it-color-text-success` | `color.emerald.25` → `#008055` | Success text; can be interactive (button, link). |
| `color.text.success-hover` | `--it-color-text-success-hover` | `color.emerald.20` → `#006644` | Hover state of `success`. |
| `color.text.success-active` | `--it-color-text-success-active` | `color.emerald.15` → `#004d33` | Active/pressed state of `success`. |
| `color.text.warning` | `--it-color-text-warning` | `color.orange.30` → `#995c00` | Warning text; can be interactive (button, link). |
| `color.text.warning-hover` | `--it-color-text-warning-hover` | `color.orange.25` → `#804d00` | Hover state of `warning`. |
| `color.text.warning-active` | `--it-color-text-warning-active` | `color.orange.20` → `#663d00` | Active/pressed state of `warning`. |
| `color.text.danger` | `--it-color-text-danger` | `color.red.50` → `#cc334d` | Error text; can be interactive (button, link). |
| `color.text.danger-hover` | `--it-color-text-danger-hover` | `color.red.37` → `#992639` | Hover state of `danger`. |
| `color.text.danger-active` | `--it-color-text-danger-active` | `color.red.25` → `#661a26` | Active/pressed state of `danger`. |
| `color.text.inverse` | `--it-color-text-inverse` | `color.white` → `#ffffff` | Text on contrasting backgrounds (primary, secondary, emphasis). |
| `color.text.accent` | `--it-color-text-accent` | `color.teal.32` → `#089994` | Accent text; alternative to primary for interactive elements on contrasting backgrounds. |

### Color: link

| Token | CSS variable | Value | Use |
|---|---|---|---|
| `color.link.base` | `--it-color-link-base` | `color.blue.40` → `#0066cc` | Default link. |
| `color.link.hover` | `--it-color-link-hover` | `color.blue.30` → `#004d99` | Hover state of `base`. |
| `color.link.active` | `--it-color-link-active` | `color.blue.20` → `#003366` | Active/pressed state of `base`. |
| `color.link.secondary` | `--it-color-link-secondary` | `color.slate.28` → `#2f475e` | Secondary link. Always underlined. |
| `color.link.secondary-hover` | `--it-color-link-secondary-hover` | `color.slate.20` → `#17324d` | Hover state of `secondary`. |
| `color.link.secondary-active` | `--it-color-link-secondary-active` | `color.slate.20` → `#17324d` | Active/pressed state of `secondary`. |
| `color.link.inverse` | `--it-color-link-inverse` | `color.white` → `#ffffff` | Link on dark backgrounds. |
| `color.link.disabled` | `--it-color-link-disabled` | `color.slate.62` → `#929da9` | Disabled link. |
| `color.link.accent` | `--it-color-link-accent` | `color.teal.32` → `#089994` | Accent link. |
| `color.link.accent-hover` | `--it-color-link-accent-hover` | `color.teal.26` → `#077f7b` | Hover state of `accent`. |

### Color: focus outline and shadow

| Token | CSS variable | Value | Use |
|---|---|---|---|
| `color.outline.focus` | `--it-color-outline-focus` | `color.gray.10` → `#1a1a1a` | Focus ring. |

| Token | CSS variable | Value | Use |
|---|---|---|---|
| `color.shadow.whisper` | `--it-color-shadow-whisper` | `color.black.05` → `rgba(0,0,0,0.05)` | Barely visible shadow. |
| `color.shadow.soft` | `--it-color-shadow-soft` | `color.black.10` → `rgba(0,0,0,0.10)` | Light shadow. |
| `color.shadow.dark` | `--it-color-shadow-dark` | `color.black.15` → `rgba(0,0,0,0.15)` | Clearly visible shadow. |

### Theme

`theme.italia` describes the default (blue) theme as one set of named shades:

| Token | CSS variable | Value | Use |
|---|---|---|---|
| `theme.italia.base` | `--it-theme-italia-base` | `color.blue.40` → `#0066cc` | Theme base color. |
| `theme.italia.light` | `--it-theme-italia-light` | `color.blue.87` → `#bfdfff` | Light theme tint. |
| `theme.italia.lighter` | `--it-theme-italia-lighter` | `color.blue.97` → `#f2f7fc` | Very light theme tint. |
| `theme.italia.subtle` | `--it-theme-italia-subtle` | `color.blue.30` → `#004d99` | Less saturated theme shade. |
| `theme.italia.muted` | `--it-theme-italia-muted` | `color.blue.25` → `#004080` | Much less saturated theme shade. |
| `theme.italia.deep` | `--it-theme-italia-deep` | `color.blue.20` → `#003366` | Dark theme shade. |

### Spacing

| Token | CSS variable | Value |
|---|---|---|
| `spacing.3xs` | `--it-spacing-3xs` | `spacing.1x` → `4px` |
| `spacing.xxs` | `--it-spacing-xxs` | `spacing.2x` → `8px` |
| `spacing.xs` | `--it-spacing-xs` | `spacing.3x` → `12px` |
| `spacing.s` | `--it-spacing-s` | `spacing.4x` → `16px` |
| `spacing.m` | `--it-spacing-m` | `spacing.6x` → `24px` |
| `spacing.l` | `--it-spacing-l` | `spacing.8x` → `32px` |
| `spacing.xl` | `--it-spacing-xl` | `spacing.10x` → `40px` |
| `spacing.xxl` | `--it-spacing-xxl` | `spacing.12x` → `48px` |
| `spacing.3xl` | `--it-spacing-3xl` | `spacing.24x` → `96px` |

Watch the names: `xs` is **12px** in the current tokens, but the legacy names on the Figma "Design Tokens" page use 8px for `xs`.

| Legacy name (Figma "Design Tokens" page) | px | Current token |
|---|---|---|
| `$spacing-inline-xxs` | 4 | `spacing.3xs` |
| `$spacing-stack-xs`, `$spacing-inline-xs` | 8 | `spacing.xxs` |
| `$spacing-stack-s`, `$spacing-inline-s`, `$spacing-inset-s` | 16 | `spacing.s` |
| `$spacing-stack-m`, `$spacing-inline-m`, `$spacing-inset-m` | 24 | `spacing.m` |
| `$spacing-stack-l`, `$spacing-inline-l`, `$spacing-inset-l` | 32 | `spacing.l` |
| `$spacing-stack-xl`, `$spacing-inset-xl` | 40 | `spacing.xl` |
| `$spacing-stack-xxl` | 48 | `spacing.xxl` |

### Elevation

Values are shown as `x y blur spread color`:

| Token | CSS variable | Value |
|---|---|---|
| `elevation.low` | `--it-elevation-low` | `0 4px 4px 0 rgba(0,0,0,0.05)` |
| `elevation.medium` | `--it-elevation-medium` | `0 8px 16px 0 rgba(0,0,0,0.10)` |
| `elevation.high` | `--it-elevation-high` | `0 16px 48px 0 rgba(0,0,0,0.15)` |

## Specific tokens

### Icons

| Token | CSS variable | Value |
|---|---|---|
| `icon.default` | `--it-icon-default` | `color.text.base` → `#1a1a1a` |
| `icon.primary` | `--it-icon-primary` | `color.background.primary` → `#0066cc` |
| `icon.primary-hover` | `--it-icon-primary-hover` | `color.background.primary-hover` → `#004d99` |
| `icon.primary-active` | `--it-icon-primary-active` | `color.background.primary-active` → `#003366` |
| `icon.secondary` | `--it-icon-secondary` | `color.background.secondary` → `#5c6f82` |
| `icon.secondary-hover` | `--it-icon-secondary-hover` | `color.background.secondary-hover` → `#2f475e` |
| `icon.secondary-active` | `--it-icon-secondary-active` | `color.background.secondary-active` → `#17324d` |
| `icon.success` | `--it-icon-success` | `color.background.success` → `#008055` |
| `icon.success-hover` | `--it-icon-success-hover` | `color.background.success-hover` → `#006644` |
| `icon.success-active` | `--it-icon-success-active` | `color.background.success-active` → `#004d33` |
| `icon.warning` | `--it-icon-warning` | `color.background.warning` → `#995c00` |
| `icon.warning-hover` | `--it-icon-warning-hover` | `color.background.warning-hover` → `#804d00` |
| `icon.warning-active` | `--it-icon-warning-active` | `color.background.warning-active` → `#663d00` |
| `icon.danger` | `--it-icon-danger` | `color.background.danger` → `#cc334d` |
| `icon.danger-hover` | `--it-icon-danger-hover` | `color.background.danger-hover` → `#992639` |
| `icon.danger-active` | `--it-icon-danger-active` | `color.background.danger-active` → `#661a26` |
| `icon.inverse` | `--it-icon-inverse` | `color.background.inverse` → `#ffffff` |
| `icon.disabled` | `--it-icon-disabled` | `color.link.disabled` → `#929da9` |

| Token | CSS variable | Value |
|---|---|---|
| `icon.size.xs` | `--it-icon-size-xs` | `16px` |
| `icon.size.s` | `--it-icon-size-s` | `24px` |
| `icon.size.m` | `--it-icon-size-m` | `32px` |
| `icon.size.l` | `--it-icon-size-l` | `48px` |
| `icon.size.xl` | `--it-icon-size-xl` | `64px` |

Bootstrap Italia icon classes use the same sizes: `.icon-xs` 16, `.icon-sm` 24, `.icon` 32 (default), `.icon-lg` 48 and `.icon-xl` 64.

### Typography roles

Plain sizes apply on mobile; the `-l` sizes apply from 576px up. See [typography.md](typography.md).

| Token | CSS variable | Value |
|---|---|---|
| `code-font` | `--it-code-font` | `font.mono` → `Roboto Mono` |
| `data-font` | `--it-data-font` | `font.mono` → `Roboto Mono` |
| `heading-font-weight` | `--it-heading-font-weight` | `font-weight.bold` → `700` |
| `heading-font-weight-weak` | `--it-heading-font-weight-weak` | `font-weight.semibold` → `600` |
| `heading-leading` | `--it-heading-leading` | `font-leading.2` → `120%` |
| `body-leading` | `--it-body-leading` | `font-leading.5` → `150%` |
| `caption-leading` | `--it-caption-leading` | `font-leading.3` → `130%` |
| `lead-leading` | `--it-lead-leading` | `font-leading.3` → `130%` |
| `heading-1-font-size` | `--it-heading-1-font-size` | `font-size.9` → `40px` |
| `heading-1-font-size-l` | `--it-heading-1-font-size-l` | `font-size.10` → `48px` |
| `heading-2-font-size` | `--it-heading-2-font-size` | `font-size.8` → `32px` |
| `heading-2-font-size-l` | `--it-heading-2-font-size-l` | `font-size.9` → `40px` |
| `heading-3-font-size-l` | `--it-heading-3-font-size-l` | `font-size.8` → `32px` |
| `heading-3-font-size` | `--it-heading-3-font-size` | `font-size.7` → `28px` |
| `heading-4-font-size` | `--it-heading-4-font-size` | `font-size.6` → `24px` |
| `heading-4-font-size-l` | `--it-heading-4-font-size-l` | `font-size.7` → `28px` |
| `heading-5-font-size` | `--it-heading-5-font-size` | `font-size.5` → `20px` |
| `heading-5-font-size-l` | `--it-heading-5-font-size-l` | `font-size.6` → `24px` |
| `heading-6-font-size` | `--it-heading-6-font-size` | `font-size.3` → `16px` |
| `heading-6-font-size-l` | `--it-heading-6-font-size-l` | `font-size.4` → `18px` |
| `body-font-size` | `--it-body-font-size` | `font-size.3` → `16px` |
| `body-font-size-l` | `--it-body-font-size-l` | `font-size.4` → `18px` |
| `caption-font-size` | `--it-caption-font-size` | `font-size.2` → `14px` |
| `lead-font-size` | `--it-lead-font-size` | `font-size.5` → `20px` |
| `lead-font-size-l` | `--it-lead-font-size-l` | `font-size.6` → `24px` |
| `label-font-size-xs` | `--it-label-font-size-xs` | `font-size.1` → `12px` |
| `label-font-size-s` | `--it-label-font-size-s` | `font-size.2` → `14px` |
| `label-font-size` | `--it-label-font-size` | `font-size.3` → `16px` |
| `label-font-size-l` | `--it-label-font-size-l` | `font-size.4` → `18px` |
| `label-leading` | `--it-label-leading` | `font-leading.1` → `110%` |
| `body-font-weight` | `--it-body-font-weight` | `font-weight.regular` → `400` |
| `caption-font-weight-regular` | `--it-caption-font-weight-regular` | `font-weight.regular` → `400` |
| `caption-font-weight-semibold` | `--it-caption-font-weight-semibold` | `font-weight.semibold` → `600` |
| `lead-font-weight` | `--it-lead-font-weight` | `font-weight.regular` → `400` |

## Global tokens

### Color

The eight color ramps (blue, seagreen, slate, gray, red, emerald, orange, teal), with contrast ratios, are listed in [colors.md](colors.md#global-ramps). The remaining global colors are:

| Token | CSS variable | Value |
|---|---|---|
| `color.white` | `--it-color-white` | `#ffffff` |
| `color.black.05` | `--it-color-black-05` | `rgba(0,0,0,0.05)` |
| `color.black.10` | `--it-color-black-10` | `rgba(0,0,0,0.10)` |
| `color.black.15` | `--it-color-black-15` | `rgba(0,0,0,0.15)` |
| `color.black.25` | `--it-color-black-25` | `rgba(0,0,0,0.25)` |
| `color.black.50` | `--it-color-black-50` | `rgba(0,0,0,0.50)` |
| `color.black.85` | `--it-color-black-85` | `rgba(0,0,0,0.85)` |
| `color.black.100` | `--it-color-black-100` | `#000000` |

### Font family

| Token | CSS variable | Value |
|---|---|---|
| `font.sans` | `--it-font-sans` | `Titillium Web` |
| `font.serif` | `--it-font-serif` | `Lora` |
| `font.mono` | `--it-font-mono` | `Roboto Mono` |

### Font size

| Token | CSS variable | Value |
|---|---|---|
| `font-size.1` | `--it-font-size-1` | `12px` |
| `font-size.2` | `--it-font-size-2` | `14px` |
| `font-size.3` | `--it-font-size-3` | `16px` |
| `font-size.4` | `--it-font-size-4` | `18px` |
| `font-size.5` | `--it-font-size-5` | `20px` |
| `font-size.6` | `--it-font-size-6` | `24px` |
| `font-size.7` | `--it-font-size-7` | `28px` |
| `font-size.8` | `--it-font-size-8` | `32px` |
| `font-size.9` | `--it-font-size-9` | `40px` |
| `font-size.10` | `--it-font-size-10` | `48px` |
| `font-size.11` | `--it-font-size-11` | `56px` |

### Line height (leading)

| Token | CSS variable | Value |
|---|---|---|
| `font-leading.1` | `--it-font-leading-1` | `110%` |
| `font-leading.2` | `--it-font-leading-2` | `120%` |
| `font-leading.3` | `--it-font-leading-3` | `130%` |
| `font-leading.4` | `--it-font-leading-4` | `140%` |
| `font-leading.5` | `--it-font-leading-5` | `150%` |

### Letter spacing (tracking)

| Token | CSS variable | Value |
|---|---|---|
| `font-tracking.short` | `--it-font-tracking-short` | `-1px` |
| `font-tracking.narrow` | `--it-font-tracking-narrow` | `-1.3px` |
| `font-tracking.tight` | `--it-font-tracking-tight` | `-2px` |
| `font-tracking.normal` | `--it-font-tracking-normal` | `0px` |

### Font weight

| Token | CSS variable | Value |
|---|---|---|
| `font-weight.extra-light` | `--it-font-weight-extra-light` | `200` |
| `font-weight.light` | `--it-font-weight-light` | `300` |
| `font-weight.regular` | `--it-font-weight-regular` | `400` |
| `font-weight.semibold` | `--it-font-weight-semibold` | `600` |
| `font-weight.bold` | `--it-font-weight-bold` | `700` |

### Spacing

All spacing steps are multiples of the 4px baseline:

| Token | CSS variable | Value |
|---|---|---|
| `spacing.1x` | `--it-spacing-1x` | `4px` |
| `spacing.2x` | `--it-spacing-2x` | `8px` |
| `spacing.3x` | `--it-spacing-3x` | `12px` |
| `spacing.4x` | `--it-spacing-4x` | `16px` |
| `spacing.5x` | `--it-spacing-5x` | `20px` |
| `spacing.6x` | `--it-spacing-6x` | `24px` |
| `spacing.8x` | `--it-spacing-8x` | `32px` |
| `spacing.10x` | `--it-spacing-10x` | `40px` |
| `spacing.12x` | `--it-spacing-12x` | `48px` |
| `spacing.14x` | `--it-spacing-14x` | `56px` |
| `spacing.16x` | `--it-spacing-16x` | `64px` |
| `spacing.24x` | `--it-spacing-24x` | `96px` |

### Sizing

| Token | CSS variable | Value |
|---|---|---|
| `sizing.quarter` | `--it-sizing-quarter` | `25%` |
| `sizing.half` | `--it-sizing-half` | `50%` |
| `sizing.two-thirds` | `--it-sizing-two-thirds` | `75%` |
| `sizing.full` | `--it-sizing-full` | `100%` |

### Border width

| Token | CSS variable | Value |
|---|---|---|
| `border.base` | `--it-border-base` | `1px` |
| `border.double` | `--it-border-double` | `2px` |
| `border.thick` | `--it-border-thick` | `4px` |
| `border.broad` | `--it-border-broad` | `8px` |

### Radius

| Token | CSS variable | Value |
|---|---|---|
| `radius.smooth` | `--it-radius-smooth` | `4px` |
| `radius.circle` | `--it-radius-circle` | `80px` |
| `radius.rounded` | `--it-radius-rounded` | `40px` |

Bootstrap Italia adds two radii with no token: `$border-radius-sm` (2px) and `$border-radius-lg` (8px). It also sets `$tag-radius` to 50px.

### Shadow primitives

| Token | CSS variable | Value |
|---|---|---|
| `shadow.blur.s` | `--it-shadow-blur-s` | `4px` |
| `shadow.blur.m` | `--it-shadow-blur-m` | `16px` |
| `shadow.blur.l` | `--it-shadow-blur-l` | `48px` |
| `shadow.offset.s` | `--it-shadow-offset-s` | `4px` |
| `shadow.offset.m` | `--it-shadow-offset-m` | `8px` |
| `shadow.offset.l` | `--it-shadow-offset-l` | `16px` |

## Quirks

- `--it-elevation-low` is emitted as `0 var(--it-shadow-blur-s) var(--it-shadow-offset-s) 0 …`, with blur and offset in the reverse order from `medium` and `high`. Both values are 4px, so it renders the same. Don't copy the pattern.
- `color.text.muted` and `color.text.disabled` share one value (`slate-44`). A disabled state therefore can't depend on color; also remove the element's interactivity.
- `font-leading.*` values are percentages. In CSS, a percentage `line-height` is computed once and inherited as a fixed length, so prefer unitless values (`1.5`) on containers with mixed font sizes.
- There is no dark theme. Build dark sections from `background.primary`, `primary-deep` or `emphasis`, with `inverse` text, links, icons and borders.
