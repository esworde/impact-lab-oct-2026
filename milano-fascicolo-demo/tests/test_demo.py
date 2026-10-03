"""Synthetic data only. Run: MOCK_MODE=true python -m unittest discover -s tests -v"""
import asyncio
import unittest
from unittest.mock import patch

import app as server
from fascicolo import FascicoloClient, is_portal_url, normalize_card, normalize_payment


class NormalizationTests(unittest.TestCase):
    def test_unknown_and_ambiguous_fields_are_not_guessed(self):
        payment = normalize_payment(["Scadenza", "Importo", "Importo"],
                                    ["01/01/2026", "€ 10", "€ 20"])
        self.assertIsNone(payment.date)
        self.assertIsNone(payment.amount)
        self.assertIn("€ 10", payment.raw_text)

    def test_column_order_and_missing_fields(self):
        payment = normalize_payment(["Stato", "Causale", "Importo"], ["Pagato", "TARI", "€ 125,00"])
        self.assertEqual(payment.description, "TARI")
        self.assertEqual(payment.amount, "€ 125,00")
        self.assertIsNone(payment.date)

    def test_misaligned_row_remains_raw(self):
        payment = normalize_payment(["Data", "Importo"], ["Totale"])
        self.assertIsNone(payment.date)
        self.assertEqual(payment.raw_text, "Totale")

    def test_card_uses_labels_only(self):
        payment = normalize_card("Causale: Servizio comunale\nImporto: € 40,00\n03/05/2026")
        self.assertEqual(payment.amount, "€ 40,00")
        self.assertIsNone(payment.date)

    def test_verified_portal_card_format(self):
        payment = normalize_card("Tributi\nTARI sintetica\npagato\nImporto: 10,00 €\nData pagamento: 01/01/2026")
        self.assertEqual(payment.description, "TARI sintetica")
        self.assertEqual(payment.status, "pagato")
        self.assertEqual(payment.date, "01/01/2026")
        self.assertEqual(payment.amount, "10,00 €")

    def test_strict_portal_origin(self):
        self.assertTrue(is_portal_url("https://fascicolo.comune.milano.it/"))
        self.assertFalse(is_portal_url("https://fascicolo.comune.milano.it.evil.test/"))
        self.assertFalse(is_portal_url("http://fascicolo.comune.milano.it/"))


class LifecycleTests(unittest.IsolatedAsyncioTestCase):
    async def test_mock_never_starts_playwright_and_clears_data(self):
        session = server.DemoSession()
        with patch.object(server, "MOCK_MODE", True), patch("fascicolo.async_playwright") as browser:
            await session.run()
            self.assertEqual(session.state, "done")
            self.assertEqual(len(session.payments), 2)
            self.assertEqual(session.payments[0]["description"], "TARI")
            browser.assert_not_called()
            await session.close()
            self.assertEqual(session.payments, [])
            self.assertIsNone(session.client)

    async def test_disconnect_cancels_in_progress_work(self):
        session = server.DemoSession()
        session.client = FascicoloClient(mock=True)
        session.task = asyncio.create_task(asyncio.sleep(60))
        task = session.task
        await session.close()
        self.assertTrue(task.cancelled())
        self.assertEqual(session.state, "disconnected")

    async def test_unexpected_error_is_redacted(self):
        session = server.DemoSession()
        with patch.object(server.fascicolo.FascicoloClient, "start", side_effect=RuntimeError("PRIVATE_SENTINEL")):
            await session.run()
        self.assertEqual(session.state, "error")
        self.assertNotIn("PRIVATE_SENTINEL", str(session.snapshot()))
        await session.close()

    async def test_reload_keeps_browser_context_and_cancels_old_wait(self):
        session = server.DemoSession()
        session.client = server.fascicolo.FascicoloClient(mock=True)
        context = object()
        session.client.context = context
        old_client = session.client
        old_class = type(old_client)
        session.task = asyncio.create_task(asyncio.sleep(60))
        old_task = session.task
        await session.reload_adapter()
        self.assertIs(session.client, old_client)
        self.assertIs(session.client.context, context)
        self.assertIsNot(type(session.client), old_class)
        self.assertTrue(old_task.cancelled())
        session.client.context = None
        await session.close()


if __name__ == "__main__":
    unittest.main()
