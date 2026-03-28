from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def listar_vagas(request: Request):
    return templates.TemplateResponse(request, "vagas/lista.html", {"vagas": []})


@router.get("/criar", response_class=HTMLResponse)
async def form_criar_vaga(request: Request):
    return templates.TemplateResponse(request, "vagas/criar.html")


@router.get("/{vaga_id}", response_class=HTMLResponse)
async def detalhes_vaga(request: Request, vaga_id: int):
    return templates.TemplateResponse(request, "vagas/detalhes.html", {"vaga": None})
