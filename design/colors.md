# Colors

## How the palette works

The global tokens hold eight color ramps, plus white and black at several alpha levels. **A step's number is its HSL lightness**: `blue-40` has a lightness of about 40%, and `blue-97` is almost white. Lower numbers are darker.

| Ramp | Role | Base step |
|---|---|---|
| `blue` | Default theme (primary) | `blue-40` `#0066cc` |
| `seagreen` | Secondary theme; the Modello Comuni primary | `seagreen-24` `#007a52` |
| `slate` | Blue-grey neutral for secondary UI, borders and muted text | `slate-44` `#5c6f82` |
| `gray` | Pure neutral for body text and muted backgrounds | `gray-15` `#262626` |
| `red` | System: danger and errors | `red-50` `#cc334d` |
| `emerald` | System: success | `emerald-25` `#008055` |
| `orange` | System: warning | `orange-40` `#cc7a00` |
| `teal` | Accent | none; the semantic tokens use `teal-32` `#089994` |

Semantic tokens choose a step that passes contrast checks. The base step does not always pass: warning uses `orange-30` (5.4:1 on white) rather than the base `orange-40` (3.3:1).

## Semantic roles

| Role | Token | Hex | Notes |
|---|---|---|---|
| Page background | `color.background.inverse` | `#ffffff` | |
| Body text | `color.text.base` | `#1a1a1a` | 17.4:1 on white |
| Secondary text | `color.text.secondary` | `#2f475e` | Detail content and secondary button text |
| Muted text | `color.text.muted` | `#5c6f82` | Short supporting text only |
| Link | `color.link.base` → `hover` → `active` | `#0066cc` → `#004d99` → `#003366` | Underlined |
| Primary action | `color.background.primary` (`-hover`, `-active`) | `#0066cc` / `#004d99` / `#003366` | White (`inverse`) text on top |
| Secondary action | `color.background.secondary` (`-hover`, `-active`) | `#5c6f82` / `#2f475e` / `#17324d` | White (`inverse`) text on top |
| Accent | `color.background.accent`, `color.text.accent` | `#089994` | Large text and icons only (3.5:1) |
| Section tint | `background.primary-lighter`, `muted`, `subtle` | `#f2f7fc`, `#f5f5f5`, `#d4d4d4` | |
| Emphasis section | `color.background.emphasis` | `#17324d` | White (`inverse`) text on top |
| Divider | `color.border.subtle` | `#c5c7c9` | Decorative only (1.7:1) |
| Input or control border | `color.border.secondary` | `#5c6f82` | 5.2:1, meets the 3:1 rule for UI |
| Success | `background.success`, `-light`, `text.success` | `#008055`, `#c8f6e7` | |
| Warning | `background.warning`, `-light`, `text.warning` | `#995c00`, `#f6e4c8` | |
| Danger | `background.danger`, `-light`, `text.danger` | `#cc334d`, `#fbeff1` | |
| Disabled | `background.disabled`, `border.disabled`, `link.disabled` | `#d9dadb`, `#d9dadb`, `#929da9` | |
| Focus ring | `color.outline.focus` | `#1a1a1a` | |

### Pairing rules

These come from the token descriptions:

- On solid `primary`, `secondary`, `emphasis`, `success`, `warning` and `danger` backgrounds, make text, links, icons and borders `inverse` (white).
- On `*-light` backgrounds, use any text color **except** `inverse`.
- Always underline `link.secondary`.
- `accent` text is meant for interactive elements on contrasting backgrounds, but it reaches only 3.5:1 on white and 3.75:1 on `emphasis`. Use it for large text (24px and up, or 18.66px and up in bold) and for icons.

## Contrast

Contrast ratios were computed with the WCAG 2.x relative-luminance formula. AA requires 4.5:1 for text, and 3:1 for large text and UI parts. AAA requires 7:1.

| Pair | Foreground | Background | Ratio | WCAG 2.x |
|---|---|---|---|---|
| text.base on white | `#1a1a1a` | `#ffffff` | 17.40:1 | AAA |
| text.secondary on white | `#2f475e` | `#ffffff` | 9.62:1 | AAA |
| text.muted / disabled on white | `#5c6f82` | `#ffffff` | 5.18:1 | AA |
| text.primary (link) on white | `#0066cc` | `#ffffff` | 5.57:1 | AA |
| link.hover on white | `#004d99` | `#ffffff` | 8.33:1 | AAA |
| link.disabled on white | `#929da9` | `#ffffff` | 2.76:1 | — |
| text.accent on white | `#089994` | `#ffffff` | 3.50:1 | AA large / UI |
| text.success on white | `#008055` | `#ffffff` | 4.98:1 | AA |
| text.warning on white | `#995c00` | `#ffffff` | 5.40:1 | AA |
| text.danger on white | `#cc334d` | `#ffffff` | 5.06:1 | AA |
| inverse on background.primary | `#ffffff` | `#0066cc` | 5.57:1 | AA |
| inverse on background.secondary | `#ffffff` | `#5c6f82` | 5.18:1 | AA |
| inverse on background.emphasis | `#ffffff` | `#17324d` | 13.13:1 | AAA |
| inverse on background.success | `#ffffff` | `#008055` | 4.98:1 | AA |
| inverse on background.warning | `#ffffff` | `#995c00` | 5.40:1 | AA |
| inverse on background.danger | `#ffffff` | `#cc334d` | 5.06:1 | AA |
| inverse on background.accent | `#ffffff` | `#089994` | 3.50:1 | AA large / UI |
| text.base on background.primary-lighter | `#1a1a1a` | `#f2f7fc` | 16.15:1 | AAA |
| text.base on background.muted | `#1a1a1a` | `#f5f5f5` | 15.96:1 | AAA |
| text.primary on background.primary-lighter | `#0066cc` | `#f2f7fc` | 5.17:1 | AA |
| text.base on danger-light | `#1a1a1a` | `#fbeff1` | 15.51:1 | AAA |
| text.base on success-light | `#1a1a1a` | `#c8f6e7` | 14.75:1 | AAA |
| text.base on warning-light | `#1a1a1a` | `#f6e4c8` | 13.96:1 | AAA |
| border.subtle on white (non-text) | `#c5c7c9` | `#ffffff` | 1.70:1 | — |
| border.secondary (input border) on white | `#5c6f82` | `#ffffff` | 5.18:1 | AA |
| text.accent on background.emphasis | `#089994` | `#17324d` | 3.75:1 | AA large / UI |
| Comuni: primary #007a52 on white | `#007a52` | `#ffffff` | 5.38:1 | AA |
| Comuni: white on primary #007a52 | `#ffffff` | `#007a52` | 5.38:1 | AA |
| Comuni: white on header slim #00402b | `#ffffff` | `#00402b` | 11.88:1 | AAA |
| Comuni: white on footer #202a2e | `#ffffff` | `#202a2e` | 14.66:1 | AAA |
| Comuni: #d4d4d4 footer links on #202a2e | `#d4d4d4` | `#202a2e` | 9.89:1 | AAA |
| Comuni: body #191919 on white | `#191919` | `#ffffff` | 17.58:1 | AAA |
| Comuni: text #455a64 (link list) on white | `#455a64` | `#ffffff` | 7.24:1 | AAA |
| Comuni: body on card grey #ebeef0 | `#191919` | `#ebeef0` | 15.09:1 | AAA |
| Comuni: error #d9364f on white | `#d9364f` | `#ffffff` | 4.57:1 | AA |
| Comuni: alert #a66300 on white | `#a66300` | `#ffffff` | 4.77:1 | AA |
| Comuni: notice #d97e00 on white | `#d97e00` | `#ffffff` | 3.03:1 | AA large / UI |
| Comuni: secondary #009966 on white | `#009966` | `#ffffff` | 3.65:1 | AA large / UI |
| Comuni: grey dark #5a768a on white | `#5a768a` | `#ffffff` | 4.78:1 | AA |
| Comuni: grey border #7d8c9c on white (non-text) | `#7d8c9c` | `#ffffff` | 3.44:1 | AA large / UI |

## Global ramps

Each ramp lists the contrast against white and against `#1a1a1a` (body text). A step rated AA against white can carry normal-size text on a white page.

### blue

| Step | Hex | CSS variable | vs white | vs `#1a1a1a` |
|---|---|---|---|---|
| 20 | `#003366` | `--it-color-blue-20` | 12.61:1 AAA | 1.38:1 — |
| 25 | `#004080` | `--it-color-blue-25` | 10.27:1 AAA | 1.69:1 — |
| 30 | `#004d99` | `--it-color-blue-30` | 8.33:1 AAA | 2.09:1 — |
| 40 **base** | `#0066cc` | `--it-color-blue-40` | 5.57:1 AA | 3.13:1 AA large / UI |
| 48 | `#207ad5` | `--it-color-blue-48` | 4.37:1 AA large / UI | 3.98:1 AA large / UI |
| 57 | `#4392e0` | `--it-color-blue-57` | 3.27:1 AA large / UI | 5.33:1 AA |
| 67 | `#6aaaeb` | `--it-color-blue-67` | 2.45:1 — | 7.10:1 AAA |
| 77 | `#94c4f5` | `--it-color-blue-77` | 1.83:1 — | 9.51:1 AAA |
| 87 | `#bfdfff` | `--it-color-blue-87` | 1.38:1 — | 12.61:1 AAA |
| 97 | `#f2f7fc` | `--it-color-blue-97` | 1.08:1 — | 16.15:1 AAA |

### seagreen

| Step | Hex | CSS variable | vs white | vs `#1a1a1a` |
|---|---|---|---|---|
| 10 | `#003121` | `--it-color-seagreen-10` | 14.37:1 AAA | 1.21:1 — |
| 14 | `#004931` | `--it-color-seagreen-14` | 10.51:1 AAA | 1.66:1 — |
| 19 | `#006242` | `--it-color-seagreen-19` | 7.43:1 AAA | 2.34:1 — |
| 24 **base** | `#007a52` | `--it-color-seagreen-24` | 5.38:1 AA | 3.24:1 AA large / UI |
| 39 | `#329574` | `--it-color-seagreen-39` | 3.69:1 AA large / UI | 4.71:1 AA |
| 54 | `#64af96` | `--it-color-seagreen-54` | 2.59:1 — | 6.72:1 AA |
| 69 | `#96cab9` | `--it-color-seagreen-69` | 1.83:1 — | 9.49:1 AAA |
| 76 | `#afd7ca` | `--it-color-seagreen-76` | 1.57:1 — | 11.10:1 AAA |
| 84 | `#c8e4db` | `--it-color-seagreen-84` | 1.35:1 — | 12.91:1 AAA |
| 92 | `#e1f2ec` | `--it-color-seagreen-92` | 1.16:1 — | 15.01:1 AAA |

### slate

| Step | Hex | CSS variable | vs white | vs `#1a1a1a` |
|---|---|---|---|---|
| 20 | `#17324d` | `--it-color-slate-20` | 13.13:1 AAA | 1.33:1 — |
| 28 | `#2f475e` | `--it-color-slate-28` | 9.62:1 AAA | 1.81:1 — |
| 36 | `#455b71` | `--it-color-slate-36` | 7.03:1 AAA | 2.48:1 — |
| 44 **base** | `#5c6f82` | `--it-color-slate-44` | 5.18:1 AA | 3.36:1 AA large / UI |
| 52 | `#768594` | `--it-color-slate-52` | 3.78:1 AA large / UI | 4.60:1 AA |
| 62 | `#929da9` | `--it-color-slate-62` | 2.76:1 — | 6.31:1 AA |
| 68 | `#a3adb7` | `--it-color-slate-68` | 2.28:1 — | 7.64:1 AAA |
| 78 | `#c5c7c9` | `--it-color-slate-78` | 1.70:1 — | 10.27:1 AAA |
| 85 | `#d9dadb` | `--it-color-slate-85` | 1.40:1 — | 12.43:1 AAA |
| 93 | `#ebeced` | `--it-color-slate-93` | 1.18:1 — | 14.71:1 AAA |

### gray

| Step | Hex | CSS variable | vs white | vs `#1a1a1a` |
|---|---|---|---|---|
| 10 | `#1a1a1a` | `--it-color-gray-10` | 17.40:1 AAA | 1.00:1 — |
| 15 **base** | `#262626` | `--it-color-gray-15` | 15.13:1 AAA | 1.15:1 — |
| 25 | `#404040` | `--it-color-gray-25` | 10.37:1 AAA | 1.68:1 — |
| 32 | `#525252` | `--it-color-gray-32` | 7.81:1 AAA | 2.23:1 — |
| 45 | `#737373` | `--it-color-gray-45` | 4.74:1 AA | 3.67:1 AA large / UI |
| 64 | `#a3a3a3` | `--it-color-gray-64` | 2.52:1 — | 6.90:1 AA |
| 83 | `#d4d4d4` | `--it-color-gray-83` | 1.48:1 — | 11.74:1 AAA |
| 90 | `#e5e5e5` | `--it-color-gray-90` | 1.26:1 — | 13.82:1 AAA |
| 96 | `#f5f5f5` | `--it-color-gray-96` | 1.09:1 — | 15.96:1 AAA |
| 98 | `#fafafa` | `--it-color-gray-98` | 1.04:1 — | 16.67:1 AAA |

### red

| Step | Hex | CSS variable | vs white | vs `#1a1a1a` |
|---|---|---|---|---|
| 25 | `#661a26` | `--it-color-red-25` | 12.06:1 AAA | 1.44:1 — |
| 30 | `#7a1f2e` | `--it-color-red-30` | 10.18:1 AAA | 1.71:1 — |
| 37 | `#992639` | `--it-color-red-37` | 7.80:1 AAA | 2.23:1 — |
| 44 | `#b32d43` | `--it-color-red-44` | 6.23:1 AA | 2.80:1 — |
| 50 **base** | `#cc334d` | `--it-color-red-50` | 5.06:1 AA | 3.44:1 AA large / UI |
| 60 | `#d65c70` | `--it-color-red-60` | 3.73:1 AA large / UI | 4.66:1 AA |
| 70 | `#e08593` | `--it-color-red-70` | 2.64:1 — | 6.59:1 AA |
| 80 | `#ebadb8` | `--it-color-red-80` | 1.87:1 — | 9.28:1 AAA |
| 90 | `#f5d6db` | `--it-color-red-90` | 1.35:1 — | 12.87:1 AAA |
| 96 | `#fbeff1` | `--it-color-red-96` | 1.12:1 — | 15.51:1 AAA |

### emerald

| Step | Hex | CSS variable | vs white | vs `#1a1a1a` |
|---|---|---|---|---|
| 15 | `#004d33` | `--it-color-emerald-15` | 9.96:1 AAA | 1.75:1 — |
| 20 | `#006644` | `--it-color-emerald-20` | 7.04:1 AAA | 2.47:1 — |
| 25 **base** | `#008055` | `--it-color-emerald-25` | 4.98:1 AA | 3.50:1 AA large / UI |
| 35 | `#00b377` | `--it-color-emerald-35` | 2.72:1 — | 6.39:1 AA |
| 40 | `#00cc88` | `--it-color-emerald-40` | 2.10:1 — | 8.28:1 AAA |
| 48 | `#22d499` | `--it-color-emerald-48` | 1.92:1 — | 9.07:1 AAA |
| 57 | `#43e0ac` | `--it-color-emerald-57` | 1.68:1 — | 10.36:1 AAA |
| 67 | `#6ee7bf` | `--it-color-emerald-67` | 1.52:1 — | 11.47:1 AAA |
| 77 | `#99eed2` | `--it-color-emerald-77` | 1.35:1 — | 12.86:1 AAA |
| 87 | `#c8f6e7` | `--it-color-emerald-87` | 1.18:1 — | 14.75:1 AAA |

### orange

| Step | Hex | CSS variable | vs white | vs `#1a1a1a` |
|---|---|---|---|---|
| 20 | `#663d00` | `--it-color-orange-20` | 9.41:1 AAA | 1.85:1 — |
| 25 | `#804d00` | `--it-color-orange-25` | 7.05:1 AAA | 2.47:1 — |
| 30 | `#995c00` | `--it-color-orange-30` | 5.40:1 AA | 3.22:1 AA large / UI |
| 35 | `#b36b00` | `--it-color-orange-35` | 4.18:1 AA large / UI | 4.16:1 AA large / UI |
| 40 **base** | `#cc7a00` | `--it-color-orange-40` | 3.31:1 AA large / UI | 5.26:1 AA |
| 48 | `#d48d22` | `--it-color-orange-48` | 2.75:1 — | 6.33:1 AA |
| 57 | `#e0a243` | `--it-color-orange-57` | 2.23:1 — | 7.81:1 AAA |
| 67 | `#e7b66e` | `--it-color-orange-67` | 1.86:1 — | 9.38:1 AAA |
| 77 | `#eecd9a` | `--it-color-orange-77` | 1.52:1 — | 11.47:1 AAA |
| 87 | `#f6e4c8` | `--it-color-orange-87` | 1.25:1 — | 13.96:1 AAA |

### teal

| Step | Hex | CSS variable | vs white | vs `#1a1a1a` |
|---|---|---|---|---|
| 20 | `#05615e` | `--it-color-teal-20` | 7.30:1 AAA | 2.39:1 — |
| 26 | `#077f7b` | `--it-color-teal-26` | 4.85:1 AA | 3.59:1 AA large / UI |
| 32 | `#089994` | `--it-color-teal-32` | 3.50:1 AA large / UI | 4.97:1 AA |
| 36 | `#09afa9` | `--it-color-teal-36` | 2.72:1 — | 6.40:1 AA |
| 42 | `#0bcbc5` | `--it-color-teal-42` | 2.03:1 — | 8.59:1 AAA |
| 50 | `#2bd6d0` | `--it-color-teal-50` | 1.81:1 — | 9.64:1 AAA |
| 60 | `#52e0db` | `--it-color-teal-60` | 1.61:1 — | 10.81:1 AAA |
| 70 | `#79ece8` | `--it-color-teal-70` | 1.40:1 — | 12.41:1 AAA |
| 80 | `#a3f5f2` | `--it-color-teal-80` | 1.24:1 — | 14.01:1 AAA |
| 90 | `#ccfffd` | `--it-color-teal-90` | 1.09:1 — | 15.99:1 AAA |

`color.white` is `#ffffff`. The black alpha levels (`color.black.05` to `.100`) are used for shadows, where `color.shadow.whisper`, `soft` and `dark` are the 5%, 10% and 15% levels, and for overlays. Modals use a 0.8 opacity backdrop.

## Bootstrap Italia's HSB color system

Bootstrap Italia generates the whole primary palette from three numbers, `$primary-h`, `$primary-s` and `$primary-b`: hue, saturation and brightness in HSB (also called HSV). Change the three numbers and every primary shade follows. This is how each Comune sets its own color.

```scss
// Bootstrap Italia default: #0066cc (blue-40)
$primary-h: 210; $primary-s: 100; $primary-b: 80;

// Modello Comuni default: #007a52 (seagreen-24), set in bootstrap-italia-comuni.scss
$primary-h: 160; $primary-s: 100; $primary-b: 48;
```

The generated scales are `a` (tints and shades), `b` (tones) and `c` (saturation steps):

| Variable | Formula (H, S, B) | Default `210/100/80` | Comuni `160/100/48` |
|---|---|---|---|
| `$primary-a1` | tint/shade: `H, S−75, 99` | `#bdddfc` | `#bdfce7` |
| `$primary-a2` | tint/shade: `H+1, S−60, 96` | `#93c2f5` | `#93f5d6` |
| `$primary-a3` | tint/shade: `H, S−45, 92` | `#6aaaeb` | `#6aebc0` |
| `$primary-a4` | tint/shade: `H, S−30, 88` | `#4392e0` | `#43e0ac` |
| `$primary-a5` | tint/shade: `H, S−15, 84` | `#207bd6` | `#20d69a` |
| `$primary-a6` | tint/shade: `H, S, 80` | `#0066cc` | `#00cc88` |
| `$primary-a7` | tint/shade: `H, S, 70` | `#0059b3` | `#00b377` |
| `$primary-a8` | tint/shade: `H, S, 60` | `#004d99` | `#009966` |
| `$primary-a9` | tint/shade: `H, S, 50` | `#004080` | `#008055` |
| `$primary-a10` | tint/shade: `H, S, 40` | `#003366` | `#006644` |
| `$primary-a11` | tint/shade: `H, S, 30` | `#00264d` | `#004d33` |
| `$primary-a12` | tint/shade: `H, S, 20` | `#001a33` | `#003322` |
| `$primary-b1` | tone: `H, S, B` | `#0066cc` | `#007a52` |
| `$primary-b2` | tone: `H, S−10, B−10` | `#1262b3` | `#0a6144` |
| `$primary-b3` | tone: `H, S−20, B−20` | `#1f5c99` | `#0e4734` |
| `$primary-b4` | tone: `H, S−30, B−30` | `#265380` | `#0e2e23` |
| `$primary-b5` | tone: `H, S−40, B−40` | `#294766` | `#081410` |
| `$primary-b6` | tone: `H, S−50, B−50` | `#26394d` | `#010302` |
| `$primary-b7` | tone: `H, S−60, B−60` | `#1f2933` | `#020302` |
| `$primary-b8` | tone: `H, S−70, B−70` | `#12161a` | `#020302` |
| `$primary-c1` | saturation: `H, S×0.1, B×1.2` | `#dce9f5` | `#84938e` |
| `$primary-c2` | saturation: `H, S×0.2, B×1.2` | `#c4dcf5` | `#769389` |
| `$primary-c3` | saturation: `H, S×0.3, B×1.2` | `#abd0f5` | `#679384` |
| `$primary-c4` | saturation: `H, S×0.4, B×1.2` | `#93c4f5` | `#58937f` |
| `$primary-c5` | saturation: `H, S×0.5, B×1.2` | `#7ab8f5` | `#49937a` |
| `$primary-c6` | saturation: `H, S×0.6, B×1.2` | `#62abf5` | `#3b9376` |
| `$primary-c7` | saturation: `H, S×0.7, B×1.2` | `#499ff5` | `#2c9371` |
| `$primary-c8` | saturation: `H, S×0.8, B×1.2` | `#3193f5` | `#1d936c` |
| `$primary-c9` | saturation: `H, S×0.9, B×1.2` | `#1887f5` | `#0f9367` |
| `$primary-c10` | saturation: `H, S×1, B×1.2` | `#007af5` | `#009362` |
| `$primary-c11` | saturation: `H, S, B×1.1` | `#0070e0` | `#00875a` |
| `$primary-c12` | saturation: `H, S, B` | `#0066cc` | `#007a52` |

With B = 48, the tone scale runs out of brightness after `b5`. Bootstrap Italia clamps B to 1, so `b6` to `b8` are near-black. Don't use them with the Comuni primary.

### Bootstrap theme colors

| Bootstrap name | Bootstrap Italia value | Token |
|---|---|---|
| `primary` | `hsb($primary-h, $primary-s, $primary-b)` | `color.blue.40` by default |
| `secondary`, `info` | `hsl(210 17% 44%)` | `color.slate.44` `#5c6f82` |
| `success` | `hsl(160 100% 25%)` | `color.emerald.25` `#008055` |
| `warning` | `hsl(36 100% 30%)` | `color.orange.30` `#995c00` |
| `danger` | `hsl(350 60% 50%)` | `color.red.50` `#cc334d` |
| `dark` | `hsl(210 54% 20%)` | ≈ `color.slate.20` `#17324d` |
| `light` | `hsb(255, 5, 95)` | none |

The grays `$gray-100` to `$gray-900` correspond to `color.gray.96`, `90`, `83`, `64`, `45`, `32`, `25`, `15` and `10`. Each theme color also produces utility classes: `.bg-*`, `.text-*`, `.btn-*`, `.btn-outline-*`, `.alert-*`, `.icon-*`.

### Accent families

These use fixed HSB values that do not depend on the primary color:

| Variable | HSB | Hex |
|---|---|---|
| `$analogue-1` | `243, 85, 100` | `#3126ff` |
| `$analogue-2` | `178, 95, 85` | `#0bd9d2` |
| `$complementary-1` | `351, 75, 97` | `#f73e5a` |
| `$complementary-2` | `36, 100, 100` | `#ff9900` |
| `$complementary-3` | `159, 100, 81` | `#00cf86` |
| `$neutral-1` | `210, 70, 30` | `#17324d` |
| `$neutral-2` | `210, 5, 95` | `#e6ecf2` |

The hues are the same "Secondary Hue 36/159/178/243/351" and "Neutral Hue 210" families found in the UI Kit's Figma color styles. Bootstrap Italia uses `analogue-2` for the blockquote border and its `a1` tint for `<mark>`.

## Modello Comuni

These overrides live in `src/stylesheets/bootstrap-italia-comuni.scss` and `_variables.scss` of the templates:

| Variable | Value | Used for |
|---|---|---|
| `$primary` | HSB 160/100/48 → `#007a52` | Buttons, links, header center, navbar, icons |
| `$header-slim-bg-color` | `#00402b` | Top slim header bar |
| `$header-center-bg-color` | `$primary` | Band with the logo and the Comune name |
| `$section-header-background-color` | `$primary-a10` → `#006644` | Section headers |
| `$section-user-header-background-color` | `#f0f8f5` | Personal-area header |
| `$color-text-primary-hover`, `--bs-link-hover-color` | `hsl(160 100% 15%)` → `#004d33` | Link and button hover |
| `$color-text-primary-active` | `hsl(160 100% 14%)` → `#004730` | Active link |
| `$color-background-primary-lighter` | `hsl(160 40% 92%)` → `#e2f3ed` | Light primary tint |
| `$btn-comuni-primary-hover` | `#fff` | Primary button text stays white on hover |
| `$card-comuni-bg-dark` | `#2c2c2c` | Dark cards |
| `$card-teaser-border` | `rgba(0,122,82,0.1)` | Teaser card border |
| `$footer-comuni-bg-color` | `#202a2e` | Footer (main area and small prints) |
| `$link-list-comuni-color` | `#455a64` | Link lists inside teaser cards |

**Focus style** (overrides Bootstrap Italia's orange ring):

```css
:focus:not(.focus--mouse) {
  border-color: #000 !important;
  box-shadow: 0 0 0 3px #000 !important;
  outline: 3px solid #fff !important;
  outline-offset: 3px;
}
```

### Template color map (`$ca-colors`)

The `$ca-colors` map generates utility classes: `.bg-{group}-{name}` sets the background and `.u-{group}-{name}` sets the text color. Examples are `.bg-grey-card` and `.u-grey-light`.

| Group | Name | Value | Notes |
|---|---|---|---|
| `main` | `black` | `#191919` | Body text |
| `main` | `white` | `#ffffff` | |
| `main` | `error` | `#d9364f` | 4.6:1 |
| `main` | `alert` | `#a66300` | 4.8:1 (`.t-alert`) |
| `main` | `secondary` | `#009966` | 3.7:1, large text only |
| `main` | `notice` | `#d97e00` | 3.0:1, icons and borders only |
| `main` | `success` | `#008758` | |
| `main` | `dark-primary` | `#00402b` | Same as the slim header |
| `grey` | `card` | `#ebeef0` | Grey card background |
| `grey` | `dark` | `#5a768a` | |
| `grey` | `medium` | `#5c6f82` | = `slate-44` |
| `grey` | `lighten` | `#e6e9f2` | |
| `grey` | `light` | `#455a64` | Card titles (`.u-grey-light`) |
| `grey` | `light-grey` | `#e5e5e5` | Card borders and dividers |
| `grey` | `extra-light` | `#bcc0cc` | |
| `grey` | `border` | `#7d8c9c` | |
| `grey` | `primary-grey` | `#007a520d` | Primary at 5% |
| `blue` | `dark` | `#17324d` | = `slate-20` |
| `blue` | `light` | `#0968b4` | |
| `gradient` | `black` | `rgba(25,25,25,0.7)` | |
| `gradient` | `light-black` | `rgba(0,0,0,0.1)` | |

## In the Figma UI Kit

- The "Colors" page documents each color with its design token, accessibility notes and identifying codes.
- The file holds about 1,500 fill styles named `On Light/…` and `On Dark/…`. The families are Primary A/B/C (the HSB scales above), Neutral Hue 210/225/204, Neutral Alpha, Neutral Light, Secondary Hue 36/159/178/243/351 and Gradient. They are the Figma side of the Bootstrap Italia HSB system. The token JSON is newer and smaller; treat it as the source of truth for code.
