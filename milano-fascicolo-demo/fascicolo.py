"""Read only the visible UI, in a temporary, headed browser context."""
import asyncio
from contextlib import suppress
from dataclasses import dataclass
from urllib.parse import urljoin, urlsplit

from playwright.async_api import Error as PlaywrightError, async_playwright


# PORTAL ADAPTER — all site-specific choices live here.
# Entry URL verified from the official public service page on 2026-10-03.
# Pagamenti link, heading and .items-body/.item-card were verified after manual
# login on 2026-10-03. Alternative selectors remain candidates. No API endpoints.
FASCICOLO_URL = "https://fascicolo.comune.milano.it/"
PORTAL_HOSTS = {"fascicolo.comune.milano.it"}
LOGIN_MARKERS = (("link", "Esci"), ("button", "Esci"),
                 ("link", "Logout"), ("button", "Logout"),
                 ("heading", "Il mio fascicolo"),
                 ("link", "Pagamenti"))  # Verified in the authenticated UI, 2026-10-03.
PAYMENT_NAMES = ("Pagamenti", "I miei pagamenti", "Archivio pagamenti",
                 "Archivio pagamenti e rimborsi")
NAVIGATION_ROLES = ("link", "button", "tab")
EMPTY_MESSAGES = ("Nessun pagamento", "Nessun pagamento presente",
                  "Nessun pagamento trovato", "Non sono presenti pagamenti")
CONTENT_SELECTOR = "main, [role='main']"
TABLE_SELECTOR = "table, [role='table'], [role='grid']"
ROW_SELECTOR = "tr, [role='row']"
HEADER_SELECTOR = "th, [role='columnheader']"
CELL_SELECTOR = "td, th, [role='cell'], [role='gridcell'], [role='rowheader']"
DATA_CELL_SELECTOR = "td, [role='cell'], [role='gridcell']"
# Optional: set these ONLY to verified selectors for the payments region/cards.
PAYMENTS_REGION_SELECTOR: str | None = ".items-page .items-body"  # Verified on Pagamenti.
PAYMENT_CARD_SELECTOR: str | None = ".item-card"  # Verified: visible payment cards.
CARD_DESCRIPTION_SELECTOR = ".item-title"
CARD_STATUS_SELECTOR = ".item-stato .chip-text"
FIELD_LABELS = {
    "date": ("data", "data pagamento", "data del pagamento", "data versamento"),
    "description": ("descrizione", "causale", "tributo", "servizio", "oggetto"),
    "amount": ("importo", "importo pagato", "importo versato", "totale", "importo (€)"),
    "status": ("stato", "stato pagamento", "esito"),
}
LOGIN_TIMEOUT_SECONDS = 600
CONTENT_TIMEOUT_SECONDS = 30

# Only rendered text nodes; never form values, HTML, storage or network bodies.
VISIBLE_TEXT = """element => {
  const parts = [];
  function visit(node) {
    if (node.nodeType === Node.TEXT_NODE) { parts.push(node.textContent); return; }
    if (node.nodeType !== Node.ELEMENT_NODE) return;
    if (node.matches('input, textarea, select, script, style, noscript, button')) return;
    const style = getComputedStyle(node);
    if (node.hidden || style.display === 'none' || style.visibility === 'hidden'
        || style.visibility === 'collapse' || Number(style.opacity) === 0) return;
    for (const child of node.childNodes) visit(child);
    if (style.display !== 'inline') parts.push('\\n');
  }
  visit(element);
  return parts.join('').trim();
}"""


@dataclass
class Payment:
    date: str | None = None
    description: str | None = None
    amount: str | None = None
    status: str | None = None
    raw_text: str | None = None


class DemoError(Exception):
    """Contains ONLY a safe, fixed user-facing message."""


def field_for(label: str) -> str | None:
    label = " ".join(label.casefold().strip(" :").split())
    return next((field for field, labels in FIELD_LABELS.items() if label in labels), None)


def normalize_payment(headers: list[str], cells: list[str]) -> Payment:
    """Unknown/ambiguous columns remain None; preserve only visible row text."""
    values = {}
    for field in FIELD_LABELS:
        matches = [i for i, label in enumerate(headers) if field_for(label) == field]
        if len(matches) == 1 and len(headers) == len(cells):
            values[field] = cells[matches[0]].strip() or None
    return Payment(**values, raw_text=" | ".join(cells).strip() or None)


def normalize_card(text: str) -> Payment:
    """Only explicit 'label: value' lines, never infer dates/amounts by position."""
    pairs = [line.split(":", 1) for line in text.splitlines() if ":" in line]
    payment = normalize_payment([p[0] for p in pairs], [p[1] for p in pairs])
    payment.raw_text = text or None
    # Verified card order: category, title, status, then explicitly labelled fields.
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if payment.date and payment.amount and len(lines) >= 5:
        if lines[2].casefold() in {"pagato", "da pagare", "scaduto", "in corso", "annullato"}:
            payment.description = payment.description or lines[1]
            payment.status = payment.status or lines[2]
    return payment


def is_portal_url(url: str) -> bool:
    parsed = urlsplit(url)
    return parsed.scheme == "https" and parsed.hostname in PORTAL_HOSTS


class FascicoloClient:
    def __init__(self, mock: bool = False):
        self.mock = mock
        self.playwright = self.browser = self.context = self.page = None

    async def describe_ui(self):
        """On-demand, memory-only diagnostics. No auth DOM, URLs, form values or payment rows."""
        if self.mock or not self.context:
            return {"pages": []}
        pages = []
        for page in self.context.pages:
            info = {"host": urlsplit(page.url).hostname, "portal": is_portal_url(page.url)}
            if info["portal"]:
                info["frames"] = []
                for frame in page.frames:
                    if not is_portal_url(frame.url):
                        continue
                    signals = await frame.evaluate(r"""selectors => {
                      const visible = e => e.checkVisibility({checkOpacity: true, checkVisibilityCSS: true});
                      const relevant = /fascicolo|pagament|tribut|esci|logout|disconnett|accedi|area personale|benvenut/i;
                      const controls = Array.from(document.querySelectorAll('a,button,[role=button],[role=tab],h1,h2,h3,[role=heading]'))
                        .filter(visible).map(e => ({tag:e.tagName.toLowerCase(), role:e.getAttribute('role'),
                          text:(e.innerText || '').trim().replace(/\s+/g,' ')}))
                        .filter(e => relevant.test(e.text) && e.text.length < 120);
                      const tables = Array.from(document.querySelectorAll('table,[role=table],[role=grid]'))
                        .filter(visible).map(e => ({headers:Array.from(e.querySelectorAll('thead th,[role=columnheader]'))
                          .filter(visible).map(h => h.innerText.trim()), rowCount:e.querySelectorAll('tr,[role=row]').length}));
                      const structure = [];
                      function walk(e, depth) {
                        if (depth > 5 || structure.length >= 100 || !visible(e) || e.matches('script,style,input,textarea,select')) return;
                        structure.push({depth, tag:e.tagName.toLowerCase(), id:e.id, role:e.getAttribute('role'), classes:e.className});
                        for (const child of e.children) walk(child, depth+1);
                      }
                      for (const child of document.body.children) walk(child, 0);
                      const cardStructure = [];
                      const card = selectors.region && selectors.card ? document.querySelector(selectors.region + ' ' + selectors.card) : null;
                      function describe(e, depth) {
                        if (depth > 7 || !visible(e) || e.matches('input,textarea,select,script,style')) return;
                        const t = (e.innerText || '').trim();
                        const label = /^(data( pagamento)?|importo( pagato)?|stato|descrizione|causale|scadenza|pagato|da pagare|dettagli|ricevuta)\s*:?$/i.test(t) ? t : null;
                        cardStructure.push({depth, tag:e.tagName.toLowerCase(), classes:e.className, label,
                          dateLike:/^\d{2}\/\d{2}\/\d{4}$/.test(t), amountLike:/^(€\s*[\d.,]+|[\d.,]+\s*€)$/.test(t)});
                        for (const child of e.children) describe(child, depth+1);
                      }
                      if (card) describe(card,0);
                      return {controls, tables, structure, cardStructure, mainCount:Array.from(document.querySelectorAll('main,[role=main]')).filter(visible).length};
                    }""", {"region": PAYMENTS_REGION_SELECTOR, "card": PAYMENT_CARD_SELECTOR})
                    info["frames"].append(signals)
            pages.append(info)
        return {"pages": pages}

    async def start(self):
        if self.mock:
            return
        try:
            self.playwright = await async_playwright().start()
            self.browser = await self.playwright.chromium.launch(headless=False)
            self.context = await self.browser.new_context(accept_downloads=False)
            self.context.set_default_timeout(2000)
            self.page = await self.context.new_page()
            await self.page.goto(FASCICOLO_URL, wait_until="domcontentloaded", timeout=60000)
        except PlaywrightError:
            await self.close()
            raise DemoError("Impossibile aprire il Fascicolo. Controlla la rete e installa Chromium con playwright install chromium.") from None

    async def _has_login_marker(self, page) -> bool:
        if page.is_closed() or not is_portal_url(page.url):
            return False
        for role, name in LOGIN_MARKERS:
            if await page.get_by_role(role, name=name, exact=True).first.is_visible():
                return True
        return False

    async def wait_for_login(self):
        if self.mock:
            await asyncio.sleep(0.3)
            return
        deadline = asyncio.get_running_loop().time() + LOGIN_TIMEOUT_SECONDS
        while asyncio.get_running_loop().time() < deadline:
            if not self.browser or not self.browser.is_connected() or not self.context.pages:
                raise DemoError("Il browser è stato chiuso. Scollega e avvia una nuova sessione.")
            for page in reversed(self.context.pages):
                try:
                    # On SPID/CIE domains, only the URL is checked. No DOM reads.
                    if await self._has_login_marker(page):
                        self.page = page
                        return
                except PlaywrightError:
                    pass  # Normal during a redirect; do not print URL/exception.
            await asyncio.sleep(1)
        raise DemoError("Attesa di 10 minuti terminata. Il browser resta aperto: completa l’accesso e premi Riprendi. Se sei già nel Fascicolo, verifica LOGIN_MARKERS in fascicolo.py.")

    async def _payment_heading(self) -> bool:
        for name in PAYMENT_NAMES:
            if await self.page.get_by_role("heading", name=name, exact=True).first.is_visible():
                return True
        return False

    async def _require_portal(self):
        if not self.page or self.page.is_closed() or not is_portal_url(self.page.url):
            raise DemoError("Torna al Fascicolo ufficiale nella finestra aperta e premi Riprendi.")

    async def navigate_to_payments(self):
        if self.mock:
            return
        await self._require_portal()
        if await self._payment_heading():
            return
        # Only an unambiguous, visible, explicitly named navigation control.
        for name in PAYMENT_NAMES:
            for role in NAVIGATION_ROLES:
                matches = self.page.get_by_role(role, name=name, exact=True)
                visible = [item for item in await matches.all() if await item.is_visible()]
                if len(visible) != 1:
                    continue
                if role == "link":
                    href = await visible[0].get_attribute("href")
                    if not href or not is_portal_url(urljoin(self.page.url, href)):
                        continue
                await visible[0].click()
                deadline = asyncio.get_running_loop().time() + CONTENT_TIMEOUT_SECONDS
                while asyncio.get_running_loop().time() < deadline:
                    await self._require_portal()
                    if await self._payment_heading():
                        return
                    await asyncio.sleep(0.5)
                raise DemoError("Sezione non riconosciuta. Apri manualmente Pagamenti e premi Riprendi; verifica PAYMENT_NAMES in fascicolo.py.")
        raise DemoError("Voce Pagamenti non individuata con certezza. Aprila manualmente e premi Riprendi; i selettori sono in fascicolo.py.")

    async def _extract_visible(self) -> list[Payment] | None:
        root = self.page.locator(PAYMENTS_REGION_SELECTOR or CONTENT_SELECTOR)
        roots = [item for item in await root.all() if await item.is_visible()]
        if len(roots) != 1:
            return None
        root = roots[0]
        for message in EMPTY_MESSAGES:
            if await root.get_by_text(message, exact=True).first.is_visible():
                return []
        candidates = []
        for table in await root.locator(TABLE_SELECTOR).all():
            if not await table.is_visible():
                continue
            headers = []
            for header in await table.locator(HEADER_SELECTOR).all():
                if await header.is_visible():
                    headers.append(await header.evaluate(VISIBLE_TEXT))
            fields = {field_for(h) for h in headers} - {None}
            # Do not scrape unrelated tables in the same main content.
            if "amount" in fields and len(fields) >= 2:
                candidates.append((table, headers))
        if len(candidates) > 1:
            raise DemoError("Più tabelle compatibili: specifica PAYMENTS_REGION_SELECTOR in fascicolo.py.")
        if candidates:
            table, headers = candidates[0]
            payments = []
            for row in await table.locator(ROW_SELECTOR).all():
                if not await row.is_visible() or await row.locator(DATA_CELL_SELECTOR).count() == 0:
                    continue
                cells = [await cell.evaluate(VISIBLE_TEXT) for cell in await row.locator(CELL_SELECTOR).all()
                         if await cell.is_visible()]
                if any(cells):
                    payments.append(normalize_payment(headers, cells))
            return payments or None  # An unpopulated/loading table is NOT proof of no payments.
        if PAYMENT_CARD_SELECTOR:
            cards = []
            for card in await root.locator(PAYMENT_CARD_SELECTOR).all():
                if not await card.is_visible():
                    continue
                payment = normalize_card(await card.evaluate(VISIBLE_TEXT))
                for field, selector in (("description", CARD_DESCRIPTION_SELECTOR), ("status", CARD_STATUS_SELECTOR)):
                    elements = [element for element in await card.locator(selector).all() if await element.is_visible()]
                    if len(elements) == 1:
                        setattr(payment, field, (await elements[0].evaluate(VISIBLE_TEXT)).strip() or None)
                cards.append(payment)
            return cards or None
        return None

    async def get_payments(self) -> list[Payment]:
        if self.mock:
            await asyncio.sleep(0.3)
            return [Payment("15/09/2026", "TARI", "€ 125,00", "Pagato"),
                    Payment("03/05/2026", "Servizio comunale", "€ 40,00", "Pagato")]
        deadline = asyncio.get_running_loop().time() + CONTENT_TIMEOUT_SECONDS
        previous = None
        stable_since = None
        while asyncio.get_running_loop().time() < deadline:
            await self._require_portal()
            if not await self._payment_heading():
                raise DemoError("La pagina Pagamenti non è più riconoscibile. Aprila e premi Riprendi.")
            result = await self._extract_visible()
            now = asyncio.get_running_loop().time()
            if result is not None and result == previous:
                if stable_since is not None and now - stable_since >= 1:
                    return result
            else:
                stable_since = now
            previous = result
            await asyncio.sleep(0.5)
        raise DemoError("Elenco non riconosciuto: verifica regione, intestazioni o cards in fascicolo.py. Nessun dato viene inventato; non equivale a zero pagamenti.")

    async def close(self):
        # Close the incognito context and Chromium's automatically temporary profile.
        # Never call storage_state(), cookies(), tracing, screenshot or page.content().
        for resource in (self.context, self.browser):
            if resource:
                with suppress(Exception):
                    await resource.close()
        if self.playwright:
            with suppress(Exception):
                await self.playwright.stop()
        self.playwright = self.browser = self.context = self.page = None
