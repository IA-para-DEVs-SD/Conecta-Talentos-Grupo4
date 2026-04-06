from urllib.parse import quote

from fastapi import APIRouter, Depends, File, Request, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.curriculo_service import (
    CurriculoNaoEncontradoError,
    CurriculoService,
    VagaNaoEncontradaError,
)
from app.services.vaga_service import VagaNotFoundError, VagaService

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.post(
    "/api/{vaga_id}",
    status_code=201,
    summary="Upload de currículos",
    responses={
        201: {"description": "Currículos enviados com sucesso"},
        400: {"description": "Nenhum currículo válido enviado"},
        404: {"description": "Vaga não encontrada"},
        413: {"description": "Arquivo muito grande"},
        415: {"description": "Formato de arquivo inválido (apenas PDF)"},
    },
)
async def api_upload_curriculos(
    vaga_id: int,
    arquivos: list[UploadFile] = File(..., description="Arquivos PDF dos currículos"),
    db: Session = Depends(get_db),
):
    """Faz upload de um ou mais currículos em PDF para uma vaga.

    O texto é extraído e anonimizado automaticamente após o upload.

    **Statuses possíveis do currículo:**
    - `pendente` — aguardando processamento
    - `extraido` — texto extraído com sucesso
    - `anonimizado` — texto extraído e anonimizado (LGPD)
    - `erro_extracao` — falha na extração do PDF

    **Exemplo de response:**
    ```json
    {
      "enviados": 2,
      "erros": [],
      "curriculos": [
        {"id": 1, "nome_arquivo": "joao_silva.pdf", "status": "anonimizado"},
        {"id": 2, "nome_arquivo": "maria_souza.pdf", "status": "anonimizado"}
      ]
    }
    ```
    """
    from fastapi import HTTPException

    service = CurriculoService(db)

    itens = []
    for arq in arquivos:
        conteudo = await arq.read()
        itens.append((arq.filename or "sem_nome.pdf", conteudo))

    try:
        sucessos, erros = service.upload_multiplos(vaga_id, itens)
    except VagaNaoEncontradaError as e:
        raise HTTPException(
            status_code=404, detail=f"Vaga #{vaga_id} não encontrada."
        ) from e

    return JSONResponse(
        status_code=201 if sucessos else 400,
        content={
            "enviados": len(sucessos),
            "erros": erros,
            "curriculos": [
                {
                    "id": c.id,
                    "nome_arquivo": c.nome_arquivo,
                    "status": c.status,
                }
                for c in sucessos
            ],
        },
    )


@router.get(
    "/api/{vaga_id}",
    summary="Listar currículos da vaga",
    responses={
        200: {"description": "Lista de currículos da vaga"},
    },
)
def api_listar_curriculos(vaga_id: int, db: Session = Depends(get_db)):
    """Retorna todos os currículos enviados para uma vaga."""
    service = CurriculoService(db)
    curriculos = service.listar_por_vaga(vaga_id)
    return {
        "vaga_id": vaga_id,
        "total": len(curriculos),
        "curriculos": [
            {
                "id": c.id,
                "nome_arquivo": c.nome_arquivo,
                "status": c.status,
                "enviado_em": c.enviado_em.isoformat() if c.enviado_em else None,
            }
            for c in curriculos
        ],
    }


@router.delete(
    "/api/{curriculo_id}",
    status_code=204,
    summary="Excluir currículo",
    responses={
        204: {"description": "Currículo excluído com sucesso"},
        404: {"description": "Currículo não encontrado"},
    },
)
def api_deletar_curriculo(curriculo_id: int, db: Session = Depends(get_db)):
    """Exclui um currículo e sua análise associada (cascade)."""
    from fastapi import HTTPException

    service = CurriculoService(db)
    try:
        service.deletar(curriculo_id)
    except CurriculoNaoEncontradoError as e:
        raise HTTPException(
            status_code=404, detail=f"Currículo #{curriculo_id} não encontrado."
        ) from e


@router.get("/upload/{vaga_id}", response_class=HTMLResponse)
def form_upload(request: Request, vaga_id: int, db: Session = Depends(get_db)):
    vaga_service = VagaService(db)
    try:
        vaga = vaga_service.obter(vaga_id)
    except VagaNotFoundError:
        return RedirectResponse(
            url=f"/vagas?msg={quote('Vaga não encontrada.')}&msg_level=danger",
            status_code=303,
        )
    curriculo_service = CurriculoService(db)
    curriculos = curriculo_service.listar_por_vaga(vaga_id)
    return templates.TemplateResponse(
        request,
        "curriculos/upload.html",
        {
            "vaga": vaga,
            "vaga_id": vaga_id,
            "curriculos": curriculos,
            "erro": None,
        },
    )


@router.post("/upload/{vaga_id}", response_class=HTMLResponse)
async def upload_curriculos(
    request: Request,
    vaga_id: int,
    arquivos: list[UploadFile] = File(...),
    db: Session = Depends(get_db),
):
    service = CurriculoService(db)

    itens = []
    for arq in arquivos:
        conteudo = await arq.read()
        itens.append((arq.filename or "sem_nome.pdf", conteudo))

    try:
        sucessos, erros = service.upload_multiplos(vaga_id, itens)
    except VagaNaoEncontradaError:
        return RedirectResponse(
            url=f"/vagas?msg={quote('Vaga não encontrada.')}&msg_level=danger",
            status_code=303,
        )

    if erros and not sucessos:
        msg = quote("; ".join(erros))
        return RedirectResponse(
            url=f"/curriculos/upload/{vaga_id}?msg={msg}&msg_level=danger",
            status_code=303,
        )

    partes = []
    if sucessos:
        n = len(sucessos)
        partes.append(f"{n} currículo(s) enviado(s) com sucesso")
    if erros:
        partes.append(f"{len(erros)} erro(s): {'; '.join(erros)}")

    level = "success" if not erros else "warning"
    msg = quote(". ".join(partes) + ".")
    return RedirectResponse(
        url=f"/curriculos/upload/{vaga_id}?msg={msg}&msg_level={level}",
        status_code=303,
    )


@router.post("/{curriculo_id}/excluir")
def excluir_curriculo(
    curriculo_id: int,
    db: Session = Depends(get_db),
):
    service = CurriculoService(db)
    try:
        curriculo = service.obter(curriculo_id)
        vaga_id = curriculo.vaga_id
    except CurriculoNaoEncontradoError:
        return RedirectResponse(
            url=f"/vagas?msg={quote('Currículo não encontrado.')}&msg_level=danger",
            status_code=303,
        )
    service.deletar(curriculo_id)
    return RedirectResponse(
        url=f"/curriculos/upload/{vaga_id}?msg={quote('Currículo excluído com sucesso!')}&msg_level=success",
        status_code=303,
    )
