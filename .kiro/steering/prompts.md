# Histórico de Prompts - ConectaTalentos

Este documento registra os principais prompts utilizados durante o desenvolvimento do projeto ConectaTalentos, servindo como referência para interações futuras com assistentes de IA.

## Configuração Inicial do Projeto

### 1. Análise e Criação de Steering Rules

**Prompt:**
```
Analyze this repository and create basic steering rules that would help guide an AI assistant.

Steering documents are markdown files that are always in '.kiro/steering'.

Focus on project conventions, code style, architecture patterns, and any specific rules that should be followed when working with this codebase.

For the initial setup, please only create the following files:
  - product.md: Short summary of the product
  - tech.md: Build system used, tech stack, libraries, frameworks etc. If there are any common commands for building, testing, compiling etc make sure to include a section for that
  - structure.md: Project organization and folder structure
  
You do not need to create any folders. They have been created for you.

The goal is to be succinct, but capture information that will be useful for an LLM application operating in this project.
```

**Resultado:**
- Criação de `product.md` com visão geral do produto
- Criação de `tech.md` com stack tecnológico e comandos comuns
- Criação de `structure.md` com organização e padrões do projeto

**Data:** 2026-03-27

---

### 2. Commit, Push e Pull Request

**Prompt:**
```
de o commit de tudo, inclusive do steering de o push e crie o pr na develop
```

**Resultado:**
- Commit com mensagem seguindo conventional commits
- Push para branch `feature/padronizacao-projeto`
- Criação do PR #56 para branch `develop`

**Data:** 2026-03-27

---

## Gestão de Issues e Organização do Projeto

### 3. Consolidação de Issues do Repositório

**Prompt:**
```
utilizando o gh cli, valida os nossos issues do repositorio atual, e altere eles também no dashboard do projeto, eu quero agrupalos em tarefas maiores e reduzir a quantidade de tarefas, agrupe em tarefas similares
```

**Resultado:**
- Análise de 34 issues abertos (Epics 1-11)
- Consolidação em 10 issues maiores e mais gerenciáveis:
  - #57 - CRUD de Vagas (API + Frontend) — agrupou #17-#21
  - #58 - Upload e Armazenamento de Currículos — agrupou #22-#25
  - #59 - Pipeline de Processamento de PDF — agrupou #26
  - #60 - Anonimização de Dados (Presidio + Integração) — agrupou #27-#29
  - #61 - Análise por IA e Ranking de Candidatos — agrupou #30-#37
  - #62 - Infraestrutura Web (FastAPI + Navegação + UI) — agrupou #38-#41
  - #63 - Banco de Dados (Setup + Schema + Repositórios + Cascata) — agrupou #42-#45
  - #64 - Logging e Tratamento de Erros — agrupou #46-#50
  - #65 - Testes e Qualidade (Setup + Cobertura + E2E) — agrupou #51-#53
  - #66 - Documentação (APIs + Guia de Instalação) — agrupou #54-#55
- Issues antigos fechados com referência ao novo issue consolidado
- Issue #7 (revisão do repositório) mantido aberto por ser independente

**Data:** 2026-03-27

---

### 4. Rebase da Branch Develop

**Prompt:**
```
faça um rebase na develop para ela ficar identica a branch main
```

**Resultado:**
- Fetch das branches remotas
- Checkout para `develop`
- Reset hard para `origin/main` (commit `d23a277`)
- Push forçado para atualizar `origin/develop`
- Branch `develop` ficou idêntica à `main`

**Data:** 2026-03-27

---

### 5. Recuperação do Diagrama UML

**Prompt:**
```
no Commit a45c121 foi adicionado um diagrama: 📊 Diagrama UML — Fluxos do Sistema. por favor recupere esse diagrama e adicione ele em um arquivo chamado diagramaUml.md, e faça a referencia dele no readme
```

**Resultado:**
- Recuperação do conteúdo do diagrama UML do commit `a45c121` via `git show`
- Criação do arquivo `diagramaUml.md` com todos os diagramas Mermaid (Pipeline Principal, Req 1-10)
- Adição da referência no `README.md` na seção de documentações

**Data:** 2026-03-27

---

### 6. Criação de Feature Branch e Commit

**Prompt:**
```
crie uma feature seguindo o padrão e faça um commit das alterações
```

**Resultado:**
- Criação da branch `feature/diagrama-uml` a partir de `develop`
- Commit: `docs: adiciona diagrama UML dos fluxos do sistema e referência no README`
- Push para `origin/feature/diagrama-uml`

**Data:** 2026-03-27

---

### 7. Registro de Prompts da Conversa

**Prompt:**
```
agora adicione todos os prompts dessa conversa no Prompt.md e faça o commit
```

**Resultado:**
- Adição de todos os prompts da conversa (itens 3-7) no arquivo `.kiro/steering/prompts.md`
- Commit na branch `feature/diagrama-uml`

**Data:** 2026-03-27

---

## Padrões de Interação Identificados

### Comandos Git
- Preferência por comandos em português
- Uso de conventional commits para mensagens
- PRs com descrição detalhada incluindo checklist

### Documentação
- Documentos em markdown
- Estrutura clara com seções bem definidas
- Foco em informações práticas e acionáveis
- Exemplos de código quando relevante

### Estilo de Comunicação
- Respostas diretas e objetivas
- Confirmação de ações realizadas
- Links para recursos criados (PRs, issues, etc.)

### Git e Versionamento
- **NÃO fazer commit/push automaticamente** após alterações
- Apenas fazer commit e push quando explicitamente solicitado pelo usuário
- Aguardar confirmação antes de versionar mudanças

### Implementação Incremental
- **Implementar item por item** em tarefas complexas
- Após cada item implementado, **perguntar ao usuário se deseja fazer commit**
- Aguardar confirmação do usuário antes de prosseguir para o próximo item
- Manter commits pequenos e focados em uma única funcionalidade
- Cada commit deve ter uma mensagem clara seguindo conventional commits

---

## Notas para Futuras Interações

1. **Idioma**: O usuário alterna entre português e inglês. Seguir o idioma do prompt.

2. **Contexto do Projeto**: ConectaTalentos é um sistema de ranqueamento de currículos com IA, focado em:
   - Conformidade com LGPD
   - Otimização de tokens para LLM
   - Arquitetura em camadas (controllers → services → repositories → processors)

3. **Ferramentas Preferidas**:
   - Git CLI para versionamento
   - GitHub CLI (`gh`) para PRs
   - Python 3.11+ com FastAPI
   - PyMuPDF para processamento de PDFs
   - Microsoft Presidio para anonimização

4. **Estrutura de Branches**:
   - `develop`: branch principal de desenvolvimento
   - `feature/*`: branches de funcionalidades
   - PRs sempre direcionados para `develop`

---

## Prompts Úteis para Referência Futura

### Análise de Código
```
Analise o código em [arquivo] e sugira melhorias seguindo os padrões do projeto
```

### Criação de Testes
```
Crie testes unitários para [componente] usando pytest e hypothesis
```

### Documentação
```
Documente a funcionalidade [nome] seguindo o padrão estabelecido em backend/docs/
```

### Refatoração
```
Refatore [componente] para seguir a arquitetura em camadas definida em structure.md
```

### Implementação de Features
```
Implemente [funcionalidade] seguindo os requisitos em .kiro/specs/conecta-talentos/requirements.md
```

---

## Implementação do Pipeline de Processamento de Currículos

### 8. Integração do ExtratorPDF no Pipeline

**Prompt:**
```
Integrar o ExtratorPDF já implementado no pipeline de processamento automático de currículos.
Critérios de aceite:
- Extração executada automaticamente após upload
- Texto extraído armazenado no banco
- Erros tratados adequadamente
- Testes de integração criados
```

**Resultado:**
- Criação de `app/processors/extrator_pdf.py` — wrapper do ExtratorPDF no layer de processors, expondo `extrair_texto_pdf()`
- Atualização de `app/services/curriculo_service.py`:
  - Adicionado método `_extrair_e_persistir()` chamado automaticamente após salvar o arquivo
  - Extração executada em `upload()` e `upload_multiplos()`
  - Erros de extração (`PDFError`) tratados com graceful degradation: status `"erro_extracao"` sem interromper o fluxo
- Criação de `tests/test_extracao_pipeline.py` com 5 testes unitários (mock) + 1 teste de integração real com pymupdf

**Data:** 2026-03-30

---

### 9. Implementação do Módulo de Anonimização com Microsoft Presidio

**Prompt:**
```
Implementar o módulo completo de anonimização de dados sensíveis usando Microsoft Presidio,
incluindo configuração, classe Anonimizador e integração no pipeline.
Critérios de aceite:
- Presidio instalado e configurado com reconhecedores em português
- Classe Anonimizador identifica e substitui: nomes, CPF, endereços, telefones, emails
- Preserva informações profissionais
- Anonimização executada após extração de texto no pipeline
- Texto anonimizado armazenado no banco
- Erros tratados adequadamente
- Testes unitários e de integração
```

**Resultado:**
- Criação de `app/processors/anonimizador.py`:
  - Classe `Anonimizador` com duas estratégias: Presidio (spaCy `pt_core_news_lg`) e fallback regex
  - Substitui: `PERSON → [NOME]`, `EMAIL_ADDRESS → [EMAIL]`, `PHONE_NUMBER → [TELEFONE]`, `BR_CPF → [CPF]`, `LOCATION → [ENDERECO]`, `URL → [URL]`
  - Fallback regex cobre CPF, e-mail, telefone e CEP quando Presidio não está disponível
  - `ResultadoAnonimizacao` dataclass com texto substituído, entidades encontradas e contagem
  - `PresidioIndisponivelError` e `AnonimizadorError` para tratamento de erros
- Atualização de `app/services/curriculo_service.py`:
  - Pipeline completo: extração → anonimização em `_extrair_e_persistir()`
  - Falha na anonimização preserva texto extraído com status `"extraido"` (degradação graciosa)
  - Status final de sucesso: `"anonimizado"`
- Atualização de `requirements.txt`: adicionado `presidio-analyzer`, `presidio-anonymizer`, `spacy`
- Atualização de `tests/test_curriculo_service.py`: mocks do pipeline adicionados nos testes existentes
- Criação de `tests/test_anonimizador.py` com 18 testes: regex, Presidio mockado, configuração e integração no pipeline

**Data:** 2026-03-30

---

### 10. Documentação Completa do Projeto (Swagger/OpenAPI + Guia de Instalação)

**Prompt:**
```
Criar documentação completa do projeto: APIs com Swagger/OpenAPI e guia de instalação.
Critérios de aceite:
- Swagger/OpenAPI configurado com todos os endpoints documentados
- Exemplos de request/response e códigos de erro documentados
- Guia de instalação com pré-requisitos, passo a passo, variáveis de ambiente e troubleshooting
```

**Resultado:**
- Atualização de `app/main.py`:
  - Descrição rica com fluxo de uso, tabela de códigos de erro, tags por domínio e metadados de contato/licença
  - `openapi_tags` definidos para `vagas`, `curriculos`, `ranking` e `infra`
- Atualização de `app/controllers/vaga_controller.py`:
  - Endpoints API (`POST`, `PUT`, `GET`, `DELETE`) com `summary`, `responses` e docstrings com exemplos de request/response
- Atualização de `app/controllers/curriculo_controller.py`:
  - Endpoints API documentados com sumários, códigos de resposta e descrição do ciclo de status do currículo (`pendente → extraido → anonimizado`)
- Criação de `docs/guia-instalacao.md`:
  - Pré-requisitos com tabela de versões
  - Passo a passo completo: clone, venv, dependências, modelo spaCy, `.env`, diretórios, banco, execução
  - Tabela de variáveis de ambiente (obrigatórias e opcionais com padrões)
  - Instruções para produção (workers, observações sobre SQLite)
  - Seção de troubleshooting com os erros mais comuns e suas soluções

**Data:** 2026-04-06
