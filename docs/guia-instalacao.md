# Guia de Instalação — ConectaTalentos

## Pré-requisitos

| Requisito | Versão mínima | Verificação |
|-----------|--------------|-------------|
| Python | 3.11+ | `python --version` |
| pip | 23+ | `pip --version` |
| Git | qualquer | `git --version` |
| Espaço em disco | ~2 GB | (modelos spaCy + dependências) |

> **Nota:** O banco de dados é SQLite — nenhum servidor de banco de dados é necessário.

---

## 1. Clonar o repositório

```bash
git clone https://github.com/IA-para-DEVs-SD/Grupo-4-Conecta-Talentos.git
cd Grupo-4-Conecta-Talentos
```

---

## 2. Criar e ativar ambiente virtual

```bash
# Criar
python -m venv .venv

# Ativar (Linux/macOS)
source .venv/bin/activate

# Ativar (Windows)
.venv\Scripts\activate
```

---

## 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### Instalar modelo spaCy (necessário para anonimização com Presidio)

```bash
python -m spacy download pt_core_news_lg
```

> Se o modelo não estiver disponível, o sistema usa fallback via regex para anonimização. O processamento continua normalmente.

---

## 4. Configurar variáveis de ambiente

Copie o arquivo de exemplo e preencha os valores:

```bash
cp .env.example .env
```

Edite o `.env`:

```env
# Aplicação
APP_NAME=ConectaTalentos
DEBUG=True
SECRET_KEY=troque-por-uma-chave-segura

# Banco de Dados (SQLite — caminho relativo ao projeto)
DATABASE_URL=sqlite:///./data/database.db

# OpenAI (obrigatório para análise de currículos)
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4o-mini
OPENAI_MAX_TOKENS=2000

# Alternativa gratuita: Groq
# GROQ_API_KEY=gsk_...
# GROQ_MODEL=llama-3.3-70b-versatile

# Upload de arquivos
UPLOAD_DIR=./data/uploads
MAX_FILE_SIZE_MB=10
MAX_PDF_PAGES=10

# Anonimização
PRESIDIO_LANGUAGE=pt
```

### Variáveis obrigatórias

| Variável | Descrição |
|----------|-----------|
| `OPENAI_API_KEY` | Chave da API OpenAI (ou `GROQ_API_KEY` como alternativa) |
| `DATABASE_URL` | Caminho do banco SQLite |

### Variáveis opcionais (com padrões)

| Variável | Padrão | Descrição |
|----------|--------|-----------|
| `APP_NAME` | `ConectaTalentos` | Nome da aplicação |
| `DEBUG` | `False` | Modo debug (ativa seed de dados) |
| `OPENAI_MODEL` | `gpt-4o-mini` | Modelo OpenAI |
| `OPENAI_MAX_TOKENS` | `2000` | Máximo de tokens na resposta |
| `UPLOAD_DIR` | `./data/uploads` | Diretório de PDFs enviados |
| `MAX_FILE_SIZE_MB` | `10` | Tamanho máximo de PDF em MB |
| `MAX_PDF_PAGES` | `10` | Máximo de páginas por PDF |
| `PRESIDIO_LANGUAGE` | `pt` | Idioma para anonimização |

---

## 5. Criar diretórios necessários

```bash
mkdir -p data/uploads
```

---

## 6. Inicializar o banco de dados

O banco é criado automaticamente na primeira execução. Para inicializar manualmente via Alembic:

```bash
alembic upgrade head
```

---

## 7. Executar a aplicação

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Acesse:
- **Interface web:** http://localhost:8000
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc
- **Health check:** http://localhost:8000/health

---

## 8. Executar testes

```bash
# Todos os testes
pytest

# Com cobertura
pytest --cov=app --cov-report=html

# Arquivo específico
pytest tests/test_vaga_service.py -v

# Sem testes de integração (mais rápido)
pytest tests/ -v --ignore=backend/tests/integration
```

---

## Instalação para produção

### Variáveis de ambiente recomendadas

```env
DEBUG=False
SECRET_KEY=<chave-aleatória-longa-e-segura>
DATABASE_URL=sqlite:///./data/database.db
OPENAI_API_KEY=<sua-chave>
```

### Executar com múltiplos workers

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

> **Atenção:** SQLite não suporta múltiplos writers simultâneos. Para produção com alta carga, considere migrar para PostgreSQL ajustando `DATABASE_URL`.

---

## Troubleshooting

### `ModuleNotFoundError: No module named 'app'`

Execute sempre a partir da raiz do projeto com o ambiente virtual ativado:

```bash
source .venv/bin/activate
uvicorn app.main:app --reload
```

### `OSError: [E050] Can't find model 'pt_core_news_lg'`

O modelo spaCy não está instalado. Execute:

```bash
python -m spacy download pt_core_news_lg
```

O sistema funciona sem ele usando fallback regex, mas a anonimização será menos precisa.

### `openai.AuthenticationError: Incorrect API key`

Verifique se `OPENAI_API_KEY` está corretamente definida no `.env` e se o arquivo `.env` está na raiz do projeto.

### `sqlite3.OperationalError: unable to open database file`

O diretório `data/` não existe. Crie-o:

```bash
mkdir -p data/uploads
```

### Erro ao fazer upload de PDF: `422 Unprocessable Entity`

Causas comuns:
- PDF corrompido ou protegido por senha
- PDF baseado em imagem (sem texto extraível — use OCR antes)
- Arquivo excede `MAX_FILE_SIZE_MB` ou `MAX_PDF_PAGES`

### `429 Too Many Requests` ao gerar ranking

Limite de requisições da API OpenAI atingido. Aguarde alguns minutos ou use a alternativa Groq configurando `GROQ_API_KEY`.

### Pre-commit hooks falhando

```bash
# Instalar hooks
pre-commit install

# Executar manualmente
pre-commit run --all-files
```
