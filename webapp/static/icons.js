// Lucide Static 1.51.0 · ISC / MIT · license: assets/LUCIDE-LICENSE.txt
"use strict";
const ICON_PATHS = Object.freeze({
  route:
    '<circle cx="6" cy="19" r="3" /><path d="M9 19h8.5a3.5 3.5 0 0 0 0-7h-11a3.5 3.5 0 0 1 0-7H15" /><circle cx="18" cy="5" r="3" />',
  "message-circle-question-mark":
    '<path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719" /><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3" /><path d="M12 17h.01" />',
  "arrow-up-right": '<path d="M7 7h10v10" />\n  <path d="M7 17 17 7" />',
  "arrow-right": '<path d="M5 12h14" />\n  <path d="m12 5 7 7-7 7" />',
  "arrow-left": '<path d="m12 19-7-7 7-7" />\n  <path d="M19 12H5" />',
  "arrow-up": '<path d="m5 12 7-7 7 7" />\n  <path d="M12 19V5" />',
  "arrow-down": '<path d="M12 5v14" />\n  <path d="m19 12-7 7-7-7" />',
  "arrow-down-right": '<path d="m7 7 10 10" />\n  <path d="M17 7v10H7" />',
  check: '<path d="M20 6 9 17l-5-5" />',
  circle: '<circle cx="12" cy="12" r="10" />',
  "circle-check":
    '<circle cx="12" cy="12" r="10" />\n  <path d="m16 9-5.5 5.5L8 12" />',
  x: '<path d="M18 6 6 18" />\n  <path d="m6 6 12 12" />',
  plus: '<path d="M5 12h14" />\n  <path d="M12 5v14" />',
  "lock-keyhole":
    '<circle cx="12" cy="16" r="1" />\n  <rect x="3" y="10" width="18" height="12" rx="2" />\n  <path d="M7 10V7a5 5 0 0 1 10 0v3" />',
  "message-circle":
    '<path d="M2.992 16.342a2 2 0 0 1 .094 1.167l-1.065 3.29a1 1 0 0 0 1.236 1.168l3.413-.998a2 2 0 0 1 1.099.092 10 10 0 1 0-4.777-4.719" />',
  "user-round":
    '<circle cx="12" cy="8" r="5" />\n  <path d="M20 21a8 8 0 0 0-16 0" />',
  globe:
    '<circle cx="12" cy="12" r="10" />\n  <path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20" />\n  <path d="M2 12h20" />',
  blocks:
    '<path d="M10 22V7a1 1 0 0 0-1-1H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-5a1 1 0 0 0-1-1H2" />\n  <rect x="14" y="2" width="8" height="8" rx="1" />',
});
function icon(name) {
  const known = Object.hasOwn(ICON_PATHS, name) ? name : "circle";
  return `<svg class="ui-icon" data-lucide="${known}" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">${ICON_PATHS[known]}</svg>`;
}
// Use only on interface labels, never on user stories or assistant responses.
function iconLabel(text) {
  const escaped = String(text ?? "").replace(
    /[&<>"']/g,
    (c) =>
      ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[
        c
      ],
  );
  const symbols = {
    "↗": "arrow-up-right",
    "→": "arrow-right",
    "←": "arrow-left",
    "↑": "arrow-up",
    "↓": "arrow-down",
    "↘": "arrow-down-right",
    "✓": "check",
    "×": "x",
    "✳": "message-circle",
  };
  return escaped.replace(/[↗→←↑↓↘✓×✳]/g, (symbol) => icon(symbols[symbol]));
}
document.querySelectorAll("[data-icon]").forEach((el) => {
  el.innerHTML = icon(el.dataset.icon);
});
