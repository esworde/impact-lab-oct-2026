# Components and page patterns

Components exist in three layers. Pick the lowest layer that gives you what you need:

1. **UI Kit Italia (Figma).** The designs, with every variant and state.
2. **Bootstrap Italia.** The HTML, CSS and JS implementation. Copy its markup from the [Bootstrap Italia docs](https://italia.github.io/bootstrap-italia/docs/).
3. **Modello Comuni templates.** `cmp-*` partials and full pages that combine Bootstrap Italia components into municipal pages and service flows.

## UI Kit Italia v3.8.0 inventory

**Foundation pages:** Colors, Typography, Design Tokens, Icons, Grid, Spacing, Borders & radius, Shadows, Sizing and Media Ratio.

The kit draws most components twice, once for mobile and once for desktop. Pages marked "TO BE" in the file (Input, Select, Toggle) are drafts of the next version.

| Component | Variants in the kit | Bootstrap Italia classes |
|---|---|---|
| Button | Primary, Secondary, Success, Danger and White · Filled or Outline · Large, Small, Mini · text, text with left or right icon, icon only · Default, Hover, Focus, Pressed, Disabled | `.btn` `.btn-primary` `.btn-outline-primary` `.btn-lg` `.btn-sm` `.btn-xs` `.btn-icon` |
| Link | Text link states | `a` (underlined) |
| Alert | Primary, Success, Warning, Error, Info | `.alert` `.alert-success` `.alert-warning` `.alert-danger` `.alert-info` |
| Notifications | Standard, Info, Success, Warning, Error | `.notification` (JS `Notification`) |
| Callout | Default, Note, Important, Success, Warning, Error · Standard or Highlight | `.callout` plus `.success`, `.warning`, `.danger`, `.important` or `.note`; `.callout-highlight`, `.callout-more` |
| Progress indicator | Bar (determinate or indeterminate; default, success, warning, error), donut, spinner, in-button | `.progress` `.progress-bar` `.progress-donut-wrapper` `.progress-spinner` `.btn-progress` |
| Accordion | Basic, nested, left icon, active background | `.accordion` `.accordion-item` |
| Blockquote | Simple, card | `.blockquote` `.blockquote-simple` `.blockquote-card` |
| Dropdown | Opened from a link or from any button style | `.dropdown` `.dropdown-menu` `.btn-dropdown` |
| Pagination | Icons, double arrows, page changer, "more" links | `nav.pagination-wrapper` `.pagination` |
| Breadcrumb | Default, with icons | `nav.breadcrumb-container` `.breadcrumb` |
| Checkbox, Radio | Control only, with label, inline group, stacked (control on the left or right) | `.form-check` |
| Toggle | Single or group, label on the left or right | `.toggles` with `.lever` |
| Input | Text field (standard, success, warning, error; with icon or button), password with strength meter, search, number, textarea, date picker, time picker | `.form-group` + `.form-control`, `.input-number`, `.password-meter`, `.it-datepicker-wrapper`, `.it-timepicker-wrapper` |
| Select | Single select | `.select-wrapper` |
| Upload | File list, image list, avatar, gallery, drag and drop | `.upload` `.upload-dragdrop` `.upload-avatar` |
| Images and image grids | Thumbnail, caption, overlay, grid, masonry | `.figure` `.img-responsive-wrapper` `.it-grid-list-wrapper` |
| List | Text, links, avatars, thumbnails, icons, actions, metadata, multiline | `.it-list-wrapper` `.link-list-wrapper` |
| Avatar | Photo, icon or text · status and presence · stacked or grouped | `.avatar` `.avatar-group` |
| Chips | Standard, Primary, Success, Warning, Error · text, dismiss, icon, avatar | `.chip` |
| Badge | Context, interactive, display text | `.badge` |
| Popover, Tooltip | Standard, icon with link, info | `data-bs-toggle="popover"`, `data-bs-toggle="tooltip"` |
| Tabs | Horizontal (top or bottom) or vertical (left or right) · label, icon, background | `.nav-tabs` |
| Modal | Standard, with icon, dismissable, links list, radio list, long content | `.modal` |
| Steppers | Top bar; bottom bar with navigation, or navigation plus save | `.steppers` `.steppers-header` `.steppers-nav` |
| BottomNav | Mobile bottom navigation | `.bottom-nav` |
| Card | Editorial (news, event, media) · Info and service (service, person, document, place, related content) · Presentation (banner) | `.card-wrapper` `.card` `.card-teaser` `.card-bg` `.card-img` `.card-big` |
| Sidebar | Left or right · label, icon with label, nested | `.sidebar-wrapper` |
| Tables | Standard, with borders, alternate rows, nested · large or small | `.table` |
| Megamenu | Standard, section link at top or bottom, CTA at bottom or right, showcase | `.nav-item.megamenu` |
| Header | Slim, central, nav, full | `.it-header-wrapper` containing `.it-header-slim-wrapper`, `.it-header-center-wrapper` and `.it-header-navbar-wrapper` |
| Hero | Desktop and mobile layouts | `.it-hero-wrapper` |
| Timeline | Full timeline | `.it-timeline-wrapper` |
| Footer | Compact, expanded, alternate | `.it-footer` containing `.it-footer-main` and `.it-footer-small-prints` |
| Carousel | Editorial cards, image cards, fullscreen image | `.it-carousel-wrapper` (built on Splide) |
| Cookiebar | Single banner | `.cookiebar` |
| Dimmer | Text, icon with text, title with one or more actions | `.dimmable` `.dimmer` |
| Navscroll | Fixed left or right, with progress bar, inline menu | `.navbar.it-navscroll-wrapper` |
| Skiplinks | Skip-to-content links | `.skiplinks` |
| Video player | Player, consent overlay | `.vjs-theme-bootstrap-italia`, `.acceptoverlay` |
| Back, Forward, Back to top | Navigation helpers | `.forward`, `.back-to-top` |
| Rating | Outline or filled stars | `.rating` |

## Key measurements (Bootstrap Italia 2.9.2)

| Component | Spec |
|---|---|
| Button | Padding 12px 24px, 16px semibold, radius 4px, no border. `.btn-xs`: 12px 16px padding, 14px text. `.btn-lg`: 16px 24px padding, 18px text. No uppercase. |
| Text input | Height 40px. No box border: only a 1px bottom border in `#5c6f82` (`slate-44`, 5.2:1). Radius 0. The label sits in the field and shrinks to 14px above it when the field has focus or a value. `.form-group` has a 48px bottom margin. |
| Card | Padding 24px. Title 18/24px bold in `#2f475e`, body 16px (18px on desktop) with 24px line height. Shadow `0 2px 20px rgba(0,0,0,.1)`, border `#c5c7c9`. Category label 14px with 0.9px tracking. |
| Header | Slim bar 48px high. Center band up to 120px high (80px on mobile), with an 82px logo (48px on mobile) and the Comune name at 28px semibold (20px on mobile). Search button is a 48px circle. |
| Hero | 620px high on desktop, 380px on mobile; the small hero is 400, 300 or 230px. The Comuni template overrides the title to 40→48px bold and the text to 20→24px in `#2f475e`. |
| Modal | Max width 32rem (512px), padding 24px, backdrop opacity 0.8. |
| Dropdown | Item padding 12px 24px, menu radius 4px, shadow `0 3px 15px rgba(0,0,0,.1)`. |
| Pagination | Items 40px on mobile and 48px from tablet up, radius 4px, 16px bold. |
| Chip | 24px high with a 12px radius (`.chip-lg`: 32px high, 16px radius). 1px border in `#c5c7c9`, 14px label (16px when large), background `color.background.muted`. |
| Card tag | `.card-tag`: 14px bold text in the primary color, 1px primary border, 50px radius. |
| Timeline | 4px line with a gradient from primary to `#003366`, 24px pins. |
| Alert | Padding 16px. |

## Icons

- The **sprite** is `bootstrap-italia/dist/svg/sprites.svg`, with 170 icons whose ids start with `it-`.
  - Navigation: `it-arrow-*`, `it-chevron-*`, `it-burger`, `it-close`, `it-expand`, `it-collapse`, `it-external-link`
  - Status: `it-check-circle`, `it-warning-circle`, `it-error`, `it-info-circle`, `it-help-circle`
  - Files: `it-file-pdf`, `it-file-csv`, `it-file-json`, `it-file-ods`, `it-file-odt` and other `it-file-*` icons
  - Places and time: `it-calendar`, `it-clock`, `it-map-marker`
  - People and access: `it-user`, `it-lock`, `it-search`
  - Brands: `it-pa`, `it-designers-italia`, `it-team-digitale`, and social logos in plain and `-square` versions
- **Markup:**

  ```html
  <svg class="icon icon-sm icon-primary" aria-hidden="true"><use href="/assets/sprites.svg#it-calendar"></use></svg>
  ```

- **Sizes:** `.icon-xs` 16px, `.icon-sm` 24px, `.icon` 32px (default), `.icon-lg` 48px, `.icon-xl` 64px. Add `.icon-padded` to put padding inside the icon box. The sizes match the `icon.size.*` tokens.
- **Colors:** `.icon-{theme}`, for example `.icon-primary`, `.icon-secondary`, `.icon-success`, `.icon-warning`, `.icon-danger` or `.icon-white`.
- **Self-host the sprite**, because `<use href>` cannot load cross-origin files. Decorative icons need `aria-hidden="true"`. An icon-only control needs a text label, for example `<span class="visually-hidden">Cerca</span>`.

## Modello Comuni components

These partials live in `src/components/cmp-*`. Each is a Handlebars partial, usually with its own SCSS.

### Page structure

| Partial | What it renders |
|---|---|
| `cmp-base` | The HTML shell: `<html lang="it">`, the skip links "Vai ai contenuti" and "Vai al footer", the header, the content block and the footer |
| `cmp-header` | **Slim header:** region name, ITA/ENG language switch, and either "Accedi all'area personale" or the user menu (I miei servizi, Le mie pratiche, Notifiche, Impostazioni, Esci). **Center header:** logo, Comune name, tagline, social links, search. **Navbar:** the main menu plus topic shortcuts and "Tutti gli argomenti" |
| `cmp-footer` | Logo and EU logo, link columns, contacts, and the legal links (notes, privacy, accessibility) |
| `cmp-breadcrumbs` | Breadcrumb trail |
| `cmp-heading`, `cmp-heading-detail` | Title block: H1, subtitle, status or tags, actions (share, "Vedi azioni" dropdown) and a primary CTA |
| `cmp-hero`, `cmp-hero-img` | Hero with title and text; small image hero |
| `cmp-navscroll` | "Indice della pagina", a sticky table of contents with a reading-progress bar |
| `cmp-nav-tab` | Tabs, used in the personal area: Scrivania, Messaggi, Attività, Servizi |
| `cmp-info-progress` | Stepper header for multi-step flows, marking steps as active or confirmed |
| `cmp-nav-steps` | Bottom action bar: Indietro, Salva richiesta, Avanti or Invia |
| `cmp-rating` | Feedback block that asks "Quanto sono chiare le informazioni su questa pagina?" (or, after a service, "Quanto è stato facile usare questo servizio?"). The user picks 1–5 stars, then preset reasons ("Le indicazioni erano chiare" or "A volte le indicazioni non erano chiare"…), then an optional comment |
| `cmp-contacts`, `cmp-contacts-card` | The "Contatta il comune" box: Leggi le domande frequenti, Richiedi assistenza, Chiama il numero verde, Prenota appuntamento. Under "Problemi in città": Segnala disservizio |

### Content

| Partial | What it renders |
|---|---|
| `cmp-card` (`-simple`, `-content-box`), `cmp-card-img`, `cmp-card-teaser`, `cmp-list-card-img` | Card variants and card grids, including document cards |
| `cmp-card-latest-messages` | Message and notification cards with date, title and text, used in the personal area |
| `cmp-icon-card` | Bordered card with an icon; its notice variant has a left border in `#d97e00` |
| `cmp-info-summary` | Summary block of label/value rows with a "Modifica" action, used on recap steps |
| `cmp-info-button-card` | Selectable data card (radio button or edit action), used to pick a saved address, bank account or similar in forms |
| `cmp-tot` | Rows for amounts and totals in payment flows |
| `cmp-timeline` | Deadlines timeline ("Tempi e scadenze") |
| `cmp-accordion` | FAQ and data sections (personal details, ISEE, bank, vehicle, property, disservice) |
| `cmp-callout`, `cmp-alert-box`, `cmp-disclaimer` | Callout; "ATTENZIONE" warning box; success banner ("Richiesta salvata con successo") |
| `cmp-carousel` | Splide carousel, for example the events calendar on the homepage |
| `cmp-icon-link`, `cmp-icon-list`, `cmp-ul-list` | A link with an icon; a titled list of icon links; a plain list |
| `cmp-tag` | Topic tags (chips) |
| `cmp-category-list`, `cmp-filter` | Category checklist filter; results header with an "Ordina" sort dropdown |
| `cmp-map` | Map box with a pin |
| `cmp-text-button`, `cmp-button` | Title, text and button block; button helpers |

### Forms

| Partial | What it renders |
|---|---|
| `cmp-input`, `cmp-text-area`, `cmp-select`, `cmp-dropdown`, `cmp-checkbox`, `cmp-toggle` | Bootstrap Italia form controls with Comuni spacing |
| `cmp-input-calendar` | Date input |
| `cmp-input-search`, `cmp-input-search-button`, `cmp-input-autocomplete` | Search field, search with a button, autocomplete |
| `cmp-upload` | Document upload list ("Carica documento", PDF, JPG or PNG) |
| `cmp-card-radio`, `cmp-card-radio-list`, `cmp-info-radio`, `cmp-info-checkbox` | Radio and checkbox options inside cards, with a title and description (for example a privacy consent) |
| `cmp-modal` | Modal contents: address, bank account, ISEE, vehicle, documents, contacts, terms, save, message, header search and category filter |

## Page templates

The templates are in `src/pages/`, and the [live demo](https://italia.github.io/design-comuni-pagine-statiche/) renders them.

### Site pages (`sito/`)

| Template | Page |
|---|---|
| `homepage` | Featured news, administration cards, events calendar carousel, featured topics, thematic sites, useful-links search, rating, contacts |
| `amministrazione` | Administration landing page |
| `novita`, `novita-dettaglio` | News list and news article |
| `eventi`, `evento-dettaglio` | Events list and event |
| `servizi`, `servizi-categoria`, `servizio-dettaglio` | Service index, category and service page |
| `argomenti`, `argomento` | Topics and topic |
| `documenti-dati` | Documents and data |
| `lista-categorie`, `lista-risorse`, `lista-risorse-categorie` | Generic category and resource lists |
| `domande-frequenti`, `mappa-sito`, `risultati-ricerca` | FAQ, site map, search results |
| `template-area-personale`, `-dettaglio-pratica` | Personal area (Scrivania, Messaggi, Attività, Servizi) and case detail |
| `appuntamento-01`…`06` | Book an appointment: Luogo → Data e orario → Dettagli appuntamento → Richiedente (anonymous or signed in) → Riepilogo → confirmation |
| `segnalazione-01`…`04`, `segnalazioni-elenco`, `segnalazione-dettaglio`, `segnalazione-area-personale` | Report a problem: Autorizzazioni e condizioni → Dati di segnalazione → Riepilogo → confirmation; plus the list, detail and personal-area views |
| `assistenza-01`, `02` | Request assistance: details → confirmation |

### Online service flows (`servizi/`)

Every flow starts from a *scheda servizio* (the service page). Sign-in uses SPID or CIE (`accesso-servizio`) before the steps below, and each flow ends with a confirmation and a personal-area view.

| Flow | Stepper steps |
|---|---|
| `graduatoria` (enrolment in a ranked list) | Informativa sulla privacy → Dati Generali → Preferenze di servizio → Riepilogo |
| `permessi` (permits) | Informativa sulla privacy → Dati Generali → Preferenze di servizio → Riepilogo; includes a payment step |
| `servizi-pagamento` (paid services) | Informativa sulla privacy → Dati Generali → Preferenze di servizio → Riepilogo; includes a payment step |
| `pagamenti-multa` (paying a fine) | Informativa sulla privacy → Dati generali → Dati specifici del servizio → Riepilogo |
| `pagamenti-imu` (IMU property tax) | Informativa sulla privacy → Dati generali → Riepilogo → Preferenze → Anteprima F24 |
| `vantaggi` (economic benefits) | Informativa sulla privacy → Dati Generali → Riepilogo |

### Page anatomy

**A content page** (for example `servizio-dettaglio`) is built from these parts, top to bottom:

```
skip links
header: slim / center / navbar
breadcrumbs
heading: H1 + status + description + primary CTA ("Accedi al servizio")
┌ navscroll "Indice della pagina" ┐┌ sections (each an H2):                        ┐
│ (sticky, left column on desktop)││ A chi è rivolto · Descrizione · Come fare      │
│                                 ││ Cosa serve · Cosa si ottiene · Tempi e scadenze│
│                                 ││ Quanto costa · Accedi al servizio              │
│                                 ││ Ulteriori informazioni · Condizioni di servizio│
│                                 ││ Contatti · Argomenti (tags)                    │
└─────────────────────────────────┘└────────────────────────────────────────────────┘
rating: "Quanto sono chiare le informazioni su questa pagina?"
contacts: "Contatta il comune"
footer
```

**A service-flow step** is built from these parts:

```
breadcrumbs → heading (service name) → stepper header (cmp-info-progress)
navscroll for the step's sections | form cards (cmp-info-button-card, cmp-accordion, inputs)
bottom bar (cmp-nav-steps): Indietro · Salva richiesta · Avanti
contacts → footer
```

## `data-element` hooks

The templates tag key elements with `data-element` attributes. The automated conformity checks for the Modello Comuni look for them, so keep the values exactly as they are if you reuse the markup:

| Area | Values |
|---|---|
| Header and navigation | `main-navigation`, `management` (Amministrazione), `news` (Novità), `all-services` (Servizi), `live` (Vivere il Comune), `all-topics`, `personal-area-login`, `breadcrumb`, `page-index` |
| Category links | `management-category-link`, `news-category-link`, `service-category-link`, `topic-element` |
| Service page | `page-name`, `service-title`, `service-description`, `service-status`, `service-addressed`, `service-how-to`, `service-needed`, `service-achieved`, `service-calendar-text`, `service-calendar-list`, `service-file`, `service-area`, `service-topic`, `service-link`, `service-online-access`, `service-booking-access`, `service-generic-access`, `metatag` (JSON-LD) |
| Feedback | `feedback`, `feedback-title`, `feedback-rating-question`, `feedback-rate-1` to `feedback-rate-5`, `feedback-rating-positive`, `feedback-rating-negative`, `feedback-rating-answer`, `feedback-input-text` |
| Contacts and footer | `contacts`, `faq`, `appointment-booking`, `report-inefficiency`, `legal-notes`, `privacy-policy-link`, `accessibility-link` |
| Lists | `load-other-cards`, `live-button-events`, `live-button-locations` |
