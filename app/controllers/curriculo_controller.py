from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/upload/{vaga_id}", response_class=HTMLResponse)
async def form_upload(request: Request, vaga_id: int):
    return templates.TemplateResponse(request, "curriculos/upload.html", {"vaga_id": vaga_id})
