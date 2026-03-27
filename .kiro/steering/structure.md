# Project Structure - ConectaTalentos

## Directory Organization

```
conecta-talentos/
├── .git/                       # Git repository data
├── .github/                    # GitHub configuration
│   ├── CONTRIBUTING.md         # Contribution guidelines
│   └── PADROES.md             # Project standards and conventions
│
├── .kiro/                      # Kiro configuration and specs
│   ├── specs/                  # Feature specifications
│   │   └── conecta-talentos/   # Main project spec
│   │       ├── .config.kiro    # Spec configuration
│   │       ├── requirements.md # Requirements document
│   │       ├── design.md       # Design document
│   │       └── tasks.md        # Task tracking
│   └── steering/               # AI assistant guidance rules
│       ├── product.md          # Product overview
│       ├── tech.md             # Technology stack
│       ├── structure.md        # Project structure (this file)
│       └── prompts.md          # Prompt history
│
├── .vscode/                    # VS Code configuration
│   └── settings.json           # Editor settings
│
├── backend/                    # Backend application
│   ├── docs/                   # Technical documentation
│   │   ├── base-implementacao.md      # Implementation guide
│   │   ├── classe-extrator-pdf.md     # ExtratorPDF documentation
│   │   └── como-usar-extrator.md      # Usage guide
│   ├── src/                    # Source code
│   │   └── services/           # Business logic and processors
│   │       ├── extrator_pdf.py        # PDF extraction class
│   │       ├── exemplo_uso_extrator.py # Usage examples
│   │       └── pdf_to_text.py         # Legacy function
│   ├── tests/                  # Test files
│   │   └── .gitkeep            # Keep empty directory
│   ├── .env.example            # Environment variables template
│   └── requirements-basico.txt # Python dependencies
│
├── scripts/                    # Utility scripts
│   ├── create-github-issues.sh # Bash script for issues
│   ├── create-github-issues.ps1 # PowerShell script for issues
│   ├── github-tasks.md         # Task definitions
│   └── README.md               # Scripts documentation
│
├── .gitignore                  # Git ignore rules
└── README.md                   # Project documentation
```

## Planned Architecture (from spec)

The full application will follow this structure:

```
app/
├── main.py                     # FastAPI entry point
├── config.py                   # Settings and environment variables
├── database.py                 # SQLAlchemy setup
│
├── controllers/                # HTTP routes (FastAPI routers)
│   ├── vaga_controller.py
│   ├── curriculo_controller.py
│   └── ranking_controller.py
│
├── services/                   # Business logic layer
│   ├── vaga_service.py
│   ├── curriculo_service.py
│   ├── processamento_service.py
│   └── ranking_service.py
│
├── processors/                 # Processing pipeline components
│   ├── extrator_pdf.py         # PDF text extraction
│   ├── anonimizador.py         # LGPD data anonymization
│   ├── otimizador_prompt.py    # Token optimization
│   └── analisador_llm.py       # LLM analysis
│
├── repositories/               # Data access layer
│   ├── vaga_repository.py
│   ├── curriculo_repository.py
│   └── analise_repository.py
│
├── models/                     # Data models
│   ├── domain.py               # Domain dataclasses
│   └── orm.py                  # SQLAlchemy ORM models
│
├── templates/                  # Jinja2 HTML templates
│   ├── base.html
│   ├── vagas/
│   ├── curriculos/
│   └── ranking/
│
└── static/                     # Static assets
    ├── css/
    └── js/
```

## Current Implementation Status

### Implemented
- **PDF Extraction Module** (`backend/src/services/`)
  - `extrator_pdf.py` - Complete PDF text extraction with PyMuPDF
  - `exemplo_uso_extrator.py` - Usage examples and demonstrations
  - `pdf_to_text.py` - Legacy PDF extraction function
  
- **Documentation** (`backend/docs/`)
  - `classe-extrator-pdf.md` - Complete technical documentation
  - `como-usar-extrator.md` - Usage guide with examples
  - `base-implementacao.md` - Implementation guidelines (1059 lines)

- **Project Configuration**
  - `.gitignore` - Comprehensive ignore rules for Python, IDEs, OS files
  - `.env.example` - Environment variables template
  - `requirements-basico.txt` - Basic dependencies (PyMuPDF)
  - `.vscode/settings.json` - VS Code configuration

- **GitHub Configuration** (`.github/`)
  - `CONTRIBUTING.md` - Contribution guidelines with Git workflow
  - `PADROES.md` - Project standards and conventions
  
- **Kiro Configuration** (`.kiro/`)
  - `specs/conecta-talentos/` - Feature specifications
    - `.config.kiro` - Spec configuration (requirements-first workflow)
    - `requirements.md` - Complete requirements document
    - `design.md` - Design document (empty)
    - `tasks.md` - Task tracking
  - `steering/` - AI assistant guidance
    - `product.md` - Product overview
    - `tech.md` - Technology stack and commands
    - `structure.md` - Project structure (this file)
    - `prompts.md` - Prompt history and patterns

- **Scripts** (`scripts/`)
  - `create-github-issues.sh` - Bash script for issue creation
  - `create-github-issues.ps1` - PowerShell script for issue creation
  - `github-tasks.md` - Task definitions for GitHub
  - `README.md` - Scripts documentation

### Pending
- FastAPI application structure (`app/` directory)
- Database models and repositories
- Anonymization with Microsoft Presidio
- LLM integration with OpenAI API
- Web interface (Jinja2 templates + Bootstrap)
- Complete test suite (pytest + hypothesis)
- Frontend static assets (CSS/JS)

## Architectural Patterns

### Layered Architecture
- **Controllers**: Handle HTTP requests/responses
- **Services**: Implement business logic
- **Repositories**: Abstract data access
- **Processors**: Specialized processing components (PDF, anonymization, LLM)

### Data Flow
1. User uploads PDF via controller
2. Service orchestrates processing pipeline
3. Processors handle extraction → anonymization → LLM analysis
4. Repository persists results
5. Controller returns ranked results

### Error Handling
- Custom exception hierarchy (PDFError, LLMError, etc.)
- Non-critical failures (anonymization) allow graceful degradation
- Critical failures (PDF extraction, LLM) propagate with descriptive messages

## File Naming Conventions

- Python modules: `snake_case.py`
- Classes: `PascalCase`
- Functions/variables: `snake_case`
- Constants: `UPPER_SNAKE_CASE`
- Test files: `test_*.py`
- Documentation: `kebab-case.md`

## Import Organization

Follow this order in Python files:
1. Standard library imports
2. Third-party imports
3. Local application imports

Example:
```python
from pathlib import Path
from dataclasses import dataclass

import pymupdf
from fastapi import APIRouter

from app.models.domain import Vaga
from app.services.vaga_service import VagaService
```
