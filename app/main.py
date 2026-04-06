from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.config import get_settings
from app.controllers import curriculo_controller, ranking_controller, vaga_controller
from app.database import init_db
from app.logging_config import get_logger, setup_logging
from app.middleware import ErrorHandlerMiddleware

settings = get_settings()
logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Configura logging
    setup_logging()
    logger.info(f"Iniciando {settings.app_name}")
    
    # Inicializa banco de dados
    init_db()
    logger.info("Banco de dados inicializado")
    
    # Popula dados de exemplo em DEV se banco estiver vazio
    if settings.debug:
        from app.database import SessionLocal
        from app.seed_data import seed_vagas_if_empty
        
        db = SessionLocal()
        try:
            seed_vagas_if_empty(db)
        finally:
            db.close()
    
    yield
    
    logger.info(f"Encerrando {settings.app_name}")


app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    description="""
## ConectaTalentos API

Sistema inteligente de ranqueamento de currículos com IA para profissionais de RH.

### Funcionalidades

- **Vagas** — Cadastro e gerenciamento de vagas com requisitos técnicos
- **Currículos** — Upload de PDFs com extração automática de texto e anonimização LGPD
- **Ranking** — Análise e ranqueamento de candidatos via LLM (score 0–100)

### Fluxo de uso

1. Crie uma vaga em `POST /vagas/api`
2. Faça upload de currículos em `POST /curriculos/api/{vaga_id}`
3. Gere o ranking em `POST /ranking/{vaga_id}/gerar`
4. Consulte os resultados em `GET /ranking/{vaga_id}`

### Autenticação

Atualmente sem autenticação. Configure `SECRET_KEY` no `.env` para uso em produção.

### Códigos de erro comuns

| Código | Significado |
|--------|-------------|
| 400 | Dados inválidos ou arquivo corrompido |
| 404 | Recurso não encontrado |
| 413 | Arquivo muito grande (padrão: 10 MB) |
| 415 | Formato de arquivo não suportado |
| 422 | Erro de validação ou PDF ilegível |
| 429 | Limite de requisições à API de IA excedido |
| 500 | Erro interno do servidor |
| 502 | Erro ao comunicar com serviço de IA |
| 504 | Timeout na análise de IA |
""",
    version="1.0.0",
    contact={
        "name": "Grupo 4 — ConectaTalentos",
        "url": "https://github.com/IA-para-DEVs-SD/Grupo-4-Conecta-Talentos",
    },
    license_info={
        "name": "MIT",
    },
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_tags=[
        {
            "name": "vagas",
            "description": "Gerenciamento de vagas de emprego. Inclui criação, listagem, atualização e exclusão.",
        },
        {
            "name": "curriculos",
            "description": "Upload e gerenciamento de currículos em PDF. O texto é extraído e anonimizado automaticamente.",
        },
        {
            "name": "ranking",
            "description": "Geração e consulta de ranking de candidatos via análise por LLM.",
        },
        {
            "name": "infra",
            "description": "Endpoints de infraestrutura e monitoramento.",
        },
    ],
    lifespan=lifespan,
)

# Middleware de tratamento de erros (deve ser o primeiro)
app.add_middleware(ErrorHandlerMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"] if settings.debug else [],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


app.include_router(vaga_controller.router, prefix="/vagas", tags=["vagas"])
app.include_router(
    curriculo_controller.router, prefix="/curriculos", tags=["curriculos"]
)
app.include_router(ranking_controller.router, prefix="/ranking", tags=["ranking"])


@app.get("/", include_in_schema=False)
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html")


@app.get("/health", tags=["infra"])
async def health():
    return {"status": "ok", "app": settings.app_name}
