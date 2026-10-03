import asyncio
import importlib
import os
from contextlib import asynccontextmanager, suppress
from dataclasses import asdict
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.trustedhost import TrustedHostMiddleware

import fascicolo

BASE = Path(__file__).resolve().parent
MOCK_MODE = os.getenv("MOCK_MODE", "false").lower() == "true"


class DemoSession:
    def __init__(self):
        self.client = None
        self.task = None
        self.lock = asyncio.Lock()
        self.reset()

    def reset(self):
        self.state = "disconnected"
        self.message = "Non collegato"
        self.payments = []

    def snapshot(self):
        return {"state": self.state, "message": self.message, "mock": MOCK_MODE,
                "payments": self.payments, "can_resume": self.client is not None and self.state in {"error", "waiting_login", "done"}}

    async def run(self, resume=False):
        try:
            if not resume:
                self.client = fascicolo.FascicoloClient(mock=MOCK_MODE)
                await self.client.start()
            self.state = "waiting_login"
            self.message = ("Modalità mock: simulazione dell’accesso." if MOCK_MODE else
                            "Completa l’autenticazione nella finestra del browser che si è aperta.")
            await self.client.wait_for_login()
            self.state, self.message = "authenticated", "Accesso completato"
            await self.client.navigate_to_payments()
            self.state, self.message = "fetching", "Recupero pagamenti..."
            self.payments = [asdict(payment) for payment in await self.client.get_payments()]
            self.state = "done"
            self.message = ("Dati di esempio recuperati." if MOCK_MODE else
                            "Pagamenti recuperati dalla vista corrente. Eventuali altre pagine o filtri non sono inclusi.")
        except fascicolo.DemoError as error:
            self.state, self.message = "error", str(error)
            self.payments = []
        except Exception:
            # Playwright exceptions may contain page details/URLs: never log them.
            self.state, self.message = "error", "Operazione non riuscita. Controlla la finestra del browser e i selettori in fascicolo.py, poi premi Riprendi oppure Scollega."
            self.payments = []

    async def stop_work(self):
        if self.task and not self.task.done():
            self.task.cancel()
            with suppress(asyncio.CancelledError):
                await self.task
        self.task = None

    async def reload_adapter(self):
        # Reload trusted local Python code without exporting/recreating the context.
        await self.stop_work()
        importlib.invalidate_caches()
        importlib.reload(fascicolo)
        self.client.__class__ = fascicolo.FascicoloClient

    async def close(self):
        await self.stop_work()
        if self.client:
            await self.client.close()
        self.client = self.task = None
        self.reset()


session = DemoSession()


@asynccontextmanager
async def lifespan(app):
    yield
    await session.close()


app = FastAPI(title="Milano Fascicolo Demo", lifespan=lifespan,
              docs_url=None, redoc_url=None, openapi_url=None)
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["127.0.0.1", "localhost", "[::1]"])


@app.middleware("http")
async def local_only(request: Request, call_next):
    origin = request.headers.get("origin")
    same_origin = not origin or origin == f"{request.url.scheme}://{request.headers.get('host')}"
    if (request.client and request.client.host not in {"127.0.0.1", "::1", "testclient"}
        or not same_origin or request.headers.get("sec-fetch-site") == "cross-site"):
        return JSONResponse({"detail": "Accesso consentito solo dalla demo locale."}, status_code=403)
    if request.method == "POST" and request.headers.get("x-demo-request") != "1":
        return JSONResponse({"detail": "Richiesta non valida."}, status_code=403)
    response = await call_next(request)
    response.headers["Cache-Control"] = "no-store"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Referrer-Policy"] = "no-referrer"
    response.headers["Content-Security-Policy"] = "default-src 'self'; script-src 'self'; style-src 'self'; connect-src 'self'; frame-ancestors 'none'; base-uri 'none'; form-action 'none'"
    return response


app.mount("/static", StaticFiles(directory=BASE / "static"), name="static")


@app.get("/")
async def index():
    return FileResponse(BASE / "templates" / "index.html")


@app.get("/api/status")
async def status():
    return session.snapshot()


@app.post("/api/connect", status_code=202)
async def connect():
    async with session.lock:
        if session.client or session.task and not session.task.done():
            raise HTTPException(409, "Sessione già aperta. Usa Riprendi o Scollega.")
        session.reset()
        session.state, session.message = "starting", "Avvio della sessione..."
        session.task = asyncio.create_task(session.run())
        return session.snapshot()


@app.post("/api/resume", status_code=202)
async def resume():
    async with session.lock:
        if not session.client or session.state not in {"error", "waiting_login", "done"}:
            raise HTTPException(409, "Nessuna sessione da riprendere.")
        try:
            await session.reload_adapter()
        except Exception:
            session.state, session.message = "error", "Correzione locale non caricabile. La sessione del browser è mantenuta aperta."
            return session.snapshot()
        session.state, session.message = "waiting_login", "Ripresa della sessione..."
        session.task = asyncio.create_task(session.run(resume=True))
        return session.snapshot()


@app.post("/api/inspect")
async def inspect_visible_ui():
    async with session.lock:
        if not session.client:
            raise HTTPException(409, "Nessuna sessione aperta.")
        try:
            return await session.client.describe_ui()
        except Exception:
            raise HTTPException(409, "Pagina in navigazione o browser chiuso. Riprova.") from None


@app.post("/api/disconnect")
async def disconnect():
    async with session.lock:
        await session.close()
        return session.snapshot()
