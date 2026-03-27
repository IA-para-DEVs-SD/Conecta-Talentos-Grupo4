# Guia Completo de Recriação do Projeto ConectaTalentos

Este documento contém todas as informações necessárias para recriar fielmente o projeto ConectaTalentos do zero. Siga as instruções na ordem apresentada.

---

## 1. Informações do Repositório

### Repositório GitHub
- **URL Original**: `https://github.com/IA-para-DEVs-SD/Conecta-Talentos-Grupo4.git`
- **URL Atual**: `https://github.com/IA-para-DEVs-SD/Grupo-4-Conecta-Talentos.git`
- **Nome**: Grupo-4-Conecta-Talentos
- **Descrição**: Sistema inteligente de ranqueamento de currículos com IA

### Branches
- `main` - Branch de produção
- `develop` - Branch de desenvolvimento
- `feature/padronizacao-projeto` - Branch atual com steering documents

### Colaboradores (Grupo 4)
- Gustavo da Rosa Heidemann
- Halan Germano Bacca
- Ismael Lunkes Pereira
- Leandro da Silva Gerolim
- Mariana Cristina da Silva Gabriel
- Pedro Santos da Mota

---

## 2. Estrutura de Diretórios

### Criar Estrutura Base

```bash
# Criar diretórios principais
mkdir -p .github
mkdir -p .kiro/specs/conecta-talentos
mkdir -p .kiro/steering
mkdir -p .vscode
mkdir -p backend/docs
mkdir -p backend/src/services
mkdir -p backend/tests
mkdir -p scripts

# Criar arquivos .gitkeep para manter diretórios vazios
touch .github/.gitkeep
touch backend/tests/.gitkeep
touch scripts/.gitkeep
```

---

## 3. Arquivos de Configuração

### 3.1 `.gitignore`

<details>
<summary>Clique para ver conteúdo completo</summary>

```gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
PIP_DELETE_THIS_DIRECTORY.txt

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# pipenv
Pipfile.lock

# poetry
poetry.lock

# pdm
.pdm.toml

# PEP 582
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
.idea/
*.iml
*.iws
.idea_modules/

# VS Code
.vscode/
*.code-workspace

# macOS
.DS_Store
.AppleDouble
.LSOverride

# Windows
Thumbs.db
Thumbs.db:encryptable
ehthumbs.db
ehthumbs_vista.db
*.stackdump
[Dd]esktop.ini
$RECYCLE.BIN/
*.cab
*.msi
*.msix
*.msm
*.msp
*.lnk

# Linux
*~
.fuse_hidden*
.directory
.Trash-*
.nfs*

# Projeto específico
data/database.db
data/uploads/
*.pdf
!exemplo.pdf

# Logs
*.log
logs/

# Temporary files
*.tmp
*.temp
*.swp
*.swo
*~

# IDE
.vscode/
.idea/
*.sublime-project
*.sublime-workspace

# Kiro (manter apenas specs e steering)
.kiro/.venv/
.kiro/cache/
```
</details>

### 3.2 `.vscode/settings.json`

```json
{
    "kiroAgent.configureMCP": "Disabled"
}
```

### 3.3 `backend/.env.example`

```env
# Variáveis de ambiente do backend
# Copie este arquivo para .env e preencha os valores

# API Keys
# OPENAI_API_KEY=sua-chave-aqui

# Configurações da aplicação
# APP_ENV=development
# APP_PORT=8000
```

### 3.4 `backend/requirements-basico.txt`

```txt
# Dependências básicas para a classe ExtratorPDF
# ConectaTalentos - IA para Devs

# Processamento de PDF
pymupdf==1.23.21
```

---

## 4. Documentação GitHub

### 4.1 `.github/CONTRIBUTING.md`

Este arquivo contém o guia completo de contribuição com:
- Como configurar o ambiente
- Como criar features
- Padrão de commits semânticos
- Fluxo Git (Gitflow)
- Checklist de PR
- Como executar testes
- Padrões de documentação
- Estilo de código Python
- Como reportar bugs
- Como fazer code review

**Nota**: Arquivo muito extenso. Consulte o arquivo original no repositório ou use o conteúdo fornecido anteriormente.

### 4.2 `.github/PADROES.md`

Este arquivo define todos os padrões do projeto:
- Nomenclatura de repositórios
- Padrão Gitflow detalhado
- Commit semântico com exemplos
- Nomenclatura de boards/projetos
- Estrutura obrigatória do README
- Estrutura de pastas
- Checklist de code review
- Padrões de teste
- Documentação de código (docstrings)
- Convenções Python (nomenclatura, imports)
- Segurança e boas práticas

**Nota**: Arquivo muito extenso. Consulte o arquivo original no repositório.

---

## 5. Especificações Kiro

### 5.1 `.kiro/specs/conecta-talentos/.config.kiro`

```json
{"specId": "a1d4b68d-bd71-49f5-b779-d5dd81d29f01", "workflowType": "requirements-first", "specType": "feature"}
```

### 5.2 `.kiro/specs/conecta-talentos/requirements.md`

Documento completo de requisitos com 10 requisitos principais:
1. Cadastro de Vagas
2. Upload e Armazenamento de Currículos
3. Extração de Texto de Currículos
4. Anonimização de Dados Sensíveis
5. Análise e Ranqueamento por LLM
6. Otimização de Tokens do Prompt
7. Visualização de Resultados
8. Interface Web
9. Persistência de Dados
10. Tratamento de Erros

Cada requisito inclui:
- User Story
- Acceptance Criteria detalhados
- Glossário de termos

**Nota**: Arquivo muito extenso (~400 linhas). Consulte o arquivo original.

### 5.3 `.kiro/specs/conecta-talentos/design.md`

Arquivo vazio (a ser preenchido).

### 5.4 `.kiro/specs/conecta-talentos/tasks.md`

Arquivo de tracking de tarefas (conteúdo específico do Kiro).

---

## 6. Steering Documents

### 6.1 `.kiro/steering/product.md`

```markdown
# Product Overview - ConectaTalentos

ConectaTalentos is an AI-powered resume ranking system designed for HR professionals. The system processes PDF resumes, extracts and anonymizes candidate information (LGPD compliant), and uses LLM-based analysis to rank candidates against job requirements.

## Core Functionality

- Job posting management with detailed requirements
- PDF resume upload and text extraction
- Automatic data anonymization (names, CPF, addresses, emails, phone numbers)
- AI-powered candidate analysis and scoring (0-100 scale)
- Ranked candidate lists with justifications, strengths, and gaps
- Web-based interface for HR professionals

## Key Differentiators

- LGPD compliance through Microsoft Presidio anonymization
- Token-optimized prompts for cost-effective LLM usage
- Structured analysis with actionable insights (strengths and gaps)
- End-to-end pipeline from PDF upload to ranked results
```

### 6.2 `.kiro/steering/tech.md`

Documento completo com:
- Stack tecnológico (Backend, PDF/AI, Frontend, Testing, Dev Tools)
- Comandos comuns (setup, desenvolvimento, testes, database, qualidade)
- Configuração de variáveis de ambiente
- Estratégia Git e convenções de commit

**Nota**: Consulte o arquivo atualizado no repositório.

### 6.3 `.kiro/steering/structure.md`

Documento completo com:
- Organização de diretórios atual
- Arquitetura planejada (app/)
- Status de implementação (implementado vs pendente)
- Padrões arquiteturais (camadas, fluxo de dados, tratamento de erros)
- Convenções de nomenclatura
- Organização de imports

**Nota**: Consulte o arquivo atualizado no repositório.

### 6.4 `.kiro/steering/prompts.md`

Histórico de prompts utilizados no projeto com:
- Prompts de configuração inicial
- Padrões de interação identificados
- Notas para futuras interações
- Prompts úteis para referência

---

## 7. Código-Fonte Backend

### 7.1 `backend/src/services/extrator_pdf.py`

Classe completa `ExtratorPDF` com:
- Extração de texto de PDFs usando PyMuPDF
- Validação de arquivos
- Tratamento de erros (PDFError, PDFCorromidoError, PDFMuitoGrandeError)
- Dataclass `TextoExtraido`
- Limite configurável de páginas
- Preservação de estrutura do documento
- Type hints completos
- Docstrings detalhadas

**Tamanho**: ~200 linhas
**Nota**: Arquivo crítico. Consulte o código original completo.

### 7.2 `backend/src/services/exemplo_uso_extrator.py`

Script de demonstração com 4 exemplos:
1. Extração básica
2. Validação de PDF
3. Tratamento de erros
4. Uso em pipeline

**Tamanho**: ~150 linhas

### 7.3 `backend/src/services/pdf_to_text.py`

Função legada de extração de PDF (compatibilidade).

---

## 8. Documentação Backend

### 8.1 `backend/docs/classe-extrator-pdf.md`

Documentação técnica completa da classe ExtratorPDF:
- Visão geral e localização
- Diagrama de classes
- Descrição de todos os componentes
- Fluxo de processamento (com diagrama Mermaid)
- Integração no pipeline
- Requisitos atendidos
- Exemplos de testes
- Dependências
- Uso no projeto
- Melhorias futuras
- Referências

**Tamanho**: ~500 linhas

### 8.2 `backend/docs/como-usar-extrator.md`

Guia prático de uso:
- Instalação rápida
- 4 exemplos práticos de uso
- Testando com arquivo de exemplo
- Características da classe
- Erros comuns e soluções
- Integração com o projeto
- Próximos passos

**Tamanho**: ~200 linhas

### 8.3 `backend/docs/base-implementacao.md`

Guia completo de implementação do sistema:
- Stack tecnológica recomendada
- Estrutura completa do projeto (app/)
- Instalação e setup detalhado
- Implementação por componentes (11 componentes)
- Código de exemplo para cada componente
- Templates HTML
- Configurações

**Tamanho**: 1059 linhas (arquivo muito extenso)
**Nota**: Documento crítico para implementação futura.

---

## 9. Scripts Utilitários

### 9.1 `scripts/create-github-issues.sh`

Script Bash para criar issues no GitHub automaticamente.

### 9.2 `scripts/create-github-issues.ps1`

Script PowerShell para criar issues no GitHub (Windows).

### 9.3 `scripts/github-tasks.md`

Definições de tarefas para criação de issues.

### 9.4 `scripts/README.md`

Documentação dos scripts disponíveis.

---

## 10. README Principal

### `README.md`

Estrutura obrigatória:
1. **Nome do Projeto**: Grupo 4 - ConectaTalentos
2. **Descrição**: Sistema inteligente de ranqueamento de currículos com IA
3. **Sumário de Documentações**: Links para todos os documentos
4. **Tecnologias Utilizadas**: Tabela com tecnologias e versões
5. **Instruções de Instalação**: Pré-requisitos e passo a passo
6. **Instruções de Uso**: Comandos para testar o sistema
7. **Integrantes**: Lista completa do Grupo 4

**Nota**: Consulte o README original para conteúdo completo.

---

## 11. Passo a Passo de Recriação

### Etapa 1: Inicializar Repositório

```bash
# Criar diretório do projeto
mkdir Grupo-4-Conecta-Talentos
cd Grupo-4-Conecta-Talentos

# Inicializar Git
git init
git branch -M main

# Criar branch develop
git checkout -b develop
```

### Etapa 2: Criar Estrutura de Diretórios

```bash
# Executar comandos da seção 2
mkdir -p .github .kiro/specs/conecta-talentos .kiro/steering .vscode
mkdir -p backend/docs backend/src/services backend/tests scripts
touch .github/.gitkeep backend/tests/.gitkeep scripts/.gitkeep
```

### Etapa 3: Criar Arquivos de Configuração

```bash
# Criar .gitignore (copiar conteúdo da seção 3.1)
# Criar .vscode/settings.json (seção 3.2)
# Criar backend/.env.example (seção 3.3)
# Criar backend/requirements-basico.txt (seção 3.4)
```

### Etapa 4: Adicionar Documentação GitHub

```bash
# Criar .github/CONTRIBUTING.md (seção 4.1)
# Criar .github/PADROES.md (seção 4.2)
```

### Etapa 5: Adicionar Especificações Kiro

```bash
# Criar .kiro/specs/conecta-talentos/.config.kiro (seção 5.1)
# Criar .kiro/specs/conecta-talentos/requirements.md (seção 5.2)
# Criar .kiro/specs/conecta-talentos/design.md (vazio)
# Criar .kiro/specs/conecta-talentos/tasks.md (vazio ou com conteúdo)
```

### Etapa 6: Adicionar Steering Documents

```bash
# Criar .kiro/steering/product.md (seção 6.1)
# Criar .kiro/steering/tech.md (seção 6.2)
# Criar .kiro/steering/structure.md (seção 6.3)
# Criar .kiro/steering/prompts.md (seção 6.4)
```

### Etapa 7: Adicionar Código Backend

```bash
# Criar backend/src/services/extrator_pdf.py (seção 7.1)
# Criar backend/src/services/exemplo_uso_extrator.py (seção 7.2)
# Criar backend/src/services/pdf_to_text.py (seção 7.3)
```

### Etapa 8: Adicionar Documentação Backend

```bash
# Criar backend/docs/classe-extrator-pdf.md (seção 8.1)
# Criar backend/docs/como-usar-extrator.md (seção 8.2)
# Criar backend/docs/base-implementacao.md (seção 8.3)
```

### Etapa 9: Adicionar Scripts

```bash
# Criar scripts/create-github-issues.sh (seção 9.1)
# Criar scripts/create-github-issues.ps1 (seção 9.2)
# Criar scripts/github-tasks.md (seção 9.3)
# Criar scripts/README.md (seção 9.4)
```

### Etapa 10: Criar README Principal

```bash
# Criar README.md (seção 10)
```

### Etapa 11: Primeiro Commit

```bash
# Adicionar todos os arquivos
git add .

# Commit inicial
git commit -m "chore: inicializa projeto ConectaTalentos

- Adiciona estrutura de diretórios
- Adiciona configurações do projeto
- Adiciona documentação GitHub
- Adiciona especificações Kiro
- Adiciona steering documents
- Adiciona código backend (ExtratorPDF)
- Adiciona documentação técnica
- Adiciona scripts utilitários
- Adiciona README principal"

# Push para repositório remoto
git remote add origin https://github.com/IA-para-DEVs-SD/Grupo-4-Conecta-Talentos.git
git push -u origin develop
```

### Etapa 12: Criar Branch de Feature

```bash
# Criar branch de padronização
git checkout -b feature/padronizacao-projeto

# Fazer ajustes necessários
# Commit e push
git add .
git commit -m "docs: adiciona documentos de steering para guiar assistente IA"
git push -u origin feature/padronizacao-projeto
```

### Etapa 13: Criar Pull Request

```bash
# Usar GitHub CLI
gh pr create --base develop --head feature/padronizacao-projeto \
  --title "docs: adiciona documentos de steering para guiar assistente IA" \
  --body "Descrição do PR..."
```

---

## 12. Verificação de Integridade

### Checklist de Arquivos Obrigatórios

- [ ] `.gitignore`
- [ ] `.vscode/settings.json`
- [ ] `.github/CONTRIBUTING.md`
- [ ] `.github/PADROES.md`
- [ ] `.kiro/specs/conecta-talentos/.config.kiro`
- [ ] `.kiro/specs/conecta-talentos/requirements.md`
- [ ] `.kiro/specs/conecta-talentos/design.md`
- [ ] `.kiro/specs/conecta-talentos/tasks.md`
- [ ] `.kiro/steering/product.md`
- [ ] `.kiro/steering/tech.md`
- [ ] `.kiro/steering/structure.md`
- [ ] `.kiro/steering/prompts.md`
- [ ] `backend/.env.example`
- [ ] `backend/requirements-basico.txt`
- [ ] `backend/src/services/extrator_pdf.py`
- [ ] `backend/src/services/exemplo_uso_extrator.py`
- [ ] `backend/src/services/pdf_to_text.py`
- [ ] `backend/docs/classe-extrator-pdf.md`
- [ ] `backend/docs/como-usar-extrator.md`
- [ ] `backend/docs/base-implementacao.md`
- [ ] `scripts/create-github-issues.sh`
- [ ] `scripts/create-github-issues.ps1`
- [ ] `scripts/github-tasks.md`
- [ ] `scripts/README.md`
- [ ] `README.md`

### Verificar Funcionalidade

```bash
# Criar ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r backend/requirements-basico.txt

# Testar extração de PDF
python backend/src/services/exemplo_uso_extrator.py
```

---

## 13. Informações Adicionais

### Tecnologias Principais
- Python 3.11+
- PyMuPDF 1.23.21
- FastAPI (planejado)
- Microsoft Presidio (planejado)
- OpenAI API (planejado)

### Padrões de Código
- Commits semânticos (Conventional Commits)
- Gitflow (main, develop, feature/*)
- Python: PEP 8, type hints, docstrings
- Formatação: Black
- Linting: Ruff

### Contatos do Grupo 4
Consulte README.md para lista completa de integrantes.

---

## 14. Notas Importantes

1. **Arquivos Extensos**: Alguns arquivos são muito longos (>500 linhas). Este guia fornece a estrutura e referências. Consulte o repositório original para conteúdo completo.

2. **Arquivos Binários**: O projeto pode conter arquivos PDF de exemplo que não estão incluídos neste guia.

3. **Histórico Git**: Este guia recria a estrutura atual, não o histórico completo de commits.

4. **Dependências Futuras**: O `requirements-basico.txt` contém apenas PyMuPDF. Dependências adicionais serão necessárias para implementação completa.

5. **Ambiente de Desenvolvimento**: Recomenda-se usar Python 3.11+ e um ambiente virtual.

6. **IDE**: O projeto foi desenvolvido com VS Code, mas pode ser usado com qualquer IDE.

---

## 15. Próximos Passos Após Recriação

1. Implementar componente de anonimização (Microsoft Presidio)
2. Implementar integração com OpenAI API
3. Criar estrutura FastAPI (app/)
4. Implementar modelos de banco de dados
5. Criar interface web
6. Adicionar testes automatizados
7. Configurar CI/CD

---

**Documento criado em**: 2026-03-27  
**Versão**: 1.0  
**Autor**: Mariana Cristina da Silva Gabriel (Grupo 4)  
**Propósito**: Transferência completa de conhecimento do projeto
