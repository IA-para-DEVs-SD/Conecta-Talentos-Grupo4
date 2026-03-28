from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.config import get_settings
from app.database import init_db
from app.controllers import vaga_controller, curriculo_controller, ranking_controller

settings = get_settings()

app = FastAPI(title=settings.app_name, debug=settings.debug)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.on_event("startup")
def startup_event() -> None:
    init_db()


app.include_router(vaga_controller.router, prefix="/vagas", tags=["vagas"])
app.include_router(curriculo_controller.router, prefix="/curriculos", tags=["curriculos"])
app.include_router(ranking_controller.router, prefix="/ranking", tags=["ranking"])


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html")


@app.get("/health")
async def health():
    return {"status": "ok", "app": settings.app_name}
