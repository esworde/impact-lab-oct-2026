"""Optional DOM checks with synthetic content; no login/network to the Comune.
Run: python tests/check_browser.py
"""
import asyncio
import sys
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from fascicolo import FascicoloClient
import fascicolo
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False)
        try:
            context = await browser.new_context()
            page = await context.new_page()
            client = FascicoloClient()
            client.page = page
            generic_region = patch("fascicolo.PAYMENTS_REGION_SELECTOR", None)
            generic_region.start()
            fixture = '''<main><h1>Pagamenti</h1><table><tr>
              <th>Data</th><th>Descrizione</th><th>Importo</th><th>Stato</th></tr>
              <tr><td>15/09/2026</td><td>TARI<span hidden>HIDDEN_SENTINEL</span>
              <input value="SECRET_SENTINEL"><textarea>SECRET_SENTINEL</textarea></td>
              <td>€ 125,00</td><td>Pagato</td></tr>
              <tr hidden><td>HIDDEN_ROW</td><td>NO</td><td>€ 1</td><td>NO</td></tr>
              </table></main>'''
            await page.set_content(fixture)
            payments = await client._extract_visible()
            assert len(payments) == 1
            assert payments[0].description == "TARI"
            assert "SENTINEL" not in str(payments)
            await page.set_content('<main><h1>Pagamenti</h1><p>Caricamento...</p></main>')
            assert await client._extract_visible() is None
            await page.set_content('<main><h1>Pagamenti</h1><p>Nessun pagamento</p></main>')
            assert await client._extract_visible() == []
            await page.set_content(fixture.replace('</main>', fixture + '</main>'))
            assert await client._extract_visible() is None  # Ambiguous regions.
            generic_region.stop()
            await page.set_content('''<div class="items-page"><h1>Pagamenti</h1><div class="items-body">
              <div class="item-card"><div class="item-category">Tributi</div>
              <div class="item-title"><a>TARI sintetica</a></div>
              <div class="item-stato"><span class="chip-text">pagato</span></div>
              <div>Importo: <span>10,00 €</span></div>
              <div>Data pagamento: <b>01/01/2026</b></div>
              <input value="SECRET_SENTINEL"><span hidden>HIDDEN_SENTINEL</span></div></div></div>''')
            payments = await client._extract_visible()
            assert len(payments) == 1
            assert payments[0].description == "TARI sintetica"
            assert payments[0].status == "pagato"
            assert payments[0].amount == "10,00 €"
            assert payments[0].date == "01/01/2026"
            assert "SENTINEL" not in str(payments)
            await context.close()
            print("PASS: verified portal card layout, visible text only, hidden rows/form values excluded, empty/loading/ambiguous views distinguished.")
        finally:
            await browser.close()


asyncio.run(main())
