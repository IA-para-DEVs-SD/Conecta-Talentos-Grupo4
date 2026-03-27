# 📊 Diagrama UML — Fluxos do Sistema

O diagrama abaixo unifica todos os requisitos e user stories do sistema ConectaTalentos, mostrando como os fluxos se conectam desde o cadastro de vagas até a visualização do ranking final.

---

## 🔄 Pipeline Principal

Visão geral do fluxo completo do sistema, do cadastro à decisão do RH:

```mermaid
flowchart LR
    A(("🧑‍💼\nRH"))
    B["📋 Cadastro\nde Vaga"]
    C["📄 Upload\nde CVs"]
    D["🔍 Extração\nde Texto"]
    E["🔒 Anonimização\nLGPD"]
    F["⚡ Otimização\nde Tokens"]
    G["🤖 Análise\nLLM"]
    H[("🗄️\nBanco")]
    I["🏆 Ranking\nFinal"]

    A --> B --> C --> D --> E --> F --> G --> H --> I --> A

    style A fill:#4A90D9,stroke:#2C5F8A,color:#fff,stroke-width:2px
    style B fill:#6C5CE7,stroke:#4A3DB0,color:#fff,stroke-width:2px
    style C fill:#6C5CE7,stroke:#4A3DB0,color:#fff,stroke-width:2px
    style D fill:#00B894,stroke:#008E6E,color:#fff,stroke-width:2px
    style E fill:#E17055,stroke:#B5453A,color:#fff,stroke-width:2px
    style F fill:#FDCB6E,stroke:#D4A84E,color:#333,stroke-width:2px
    style G fill:#E84393,stroke:#B5306F,color:#fff,stroke-width:2px
    style H fill:#636E72,stroke:#4A5357,color:#fff,stroke-width:2px
    style I fill:#00CEC9,stroke:#009E9A,color:#fff,stroke-width:2px
```

---

## 📋 Req 1 — Cadastro de Vagas

```mermaid
flowchart TD
    A(("🧑‍💼 RH")) --> B["Preenche dados da vaga\n📌 título, descrição\n🛠️ requisitos técnicos\n⏳ experiência mínima\n🎯 competências"]
    B --> C{"✅ Campos obrigatórios\npreenchidos?"}
    C -- "❌ Não" --> D["⚠️ Exibe erro\nde validação"]
    D --> B
    C -- "✅ Sim" --> E[("🗄️ Persiste\nno banco")]
    E --> F["✔️ Vaga cadastrada"]
    F --> G["📝 Listar / Editar\nvagas existentes"]

    style A fill:#4A90D9,stroke:#2C5F8A,color:#fff,stroke-width:2px
    style B fill:#6C5CE7,stroke:#4A3DB0,color:#fff,stroke-width:2px
    style C fill:#FDCB6E,stroke:#D4A84E,color:#333,stroke-width:2px
    style D fill:#E17055,stroke:#B5453A,color:#fff,stroke-width:2px
    style E fill:#636E72,stroke:#4A5357,color:#fff,stroke-width:2px
    style F fill:#00B894,stroke:#008E6E,color:#fff,stroke-width:2px
    style G fill:#00CEC9,stroke:#009E9A,color:#fff,stroke-width:2px
```

---

## 📄 Req 2 — Upload de Currículos

```mermaid
flowchart TD
    A(("🧑‍💼 RH")) --> B["Seleciona vaga\ne faz upload"]
    B --> C{"📎 Formato\né PDF?"}
    C -- "❌ Não" --> D["⚠️ Erro:\nformato inválido"]
    D --> B
    C -- "✅ Sim" --> E[("🗄️ Armazena\nPDF original")]
    E --> F["🔗 Associa CV à vaga"]
    F --> G["✔️ Upload concluído\n📁 Aceita múltiplos PDFs"]

    style A fill:#4A90D9,stroke:#2C5F8A,color:#fff,stroke-width:2px
    style B fill:#6C5CE7,stroke:#4A3DB0,color:#fff,stroke-width:2px
    style C fill:#FDCB6E,stroke:#D4A84E,color:#333,stroke-width:2px
    style D fill:#E17055,stroke:#B5453A,color:#fff,stroke-width:2px
    style E fill:#636E72,stroke:#4A5357,color:#fff,stroke-width:2px
    style F fill:#00B894,stroke:#008E6E,color:#fff,stroke-width:2px
    style G fill:#00CEC9,stroke:#009E9A,color:#fff,stroke-width:2px
```

---

## 🔍 Req 3 — Extração de Texto

```mermaid
flowchart TD
    A["📄 PDF armazenado"] --> B["🔍 Extrator_PDF\nprocessa documento"]
    B --> C{"✅ PDF válido?\n📏 Máx 10 páginas"}
    C -- "❌ Não" --> D["⚠️ Erro específico\n📝 Registra em log"]
    C -- "✅ Sim" --> E["📃 Texto Estruturado\n📂 Preserva seções\ne parágrafos"]

    style A fill:#636E72,stroke:#4A5357,color:#fff,stroke-width:2px
    style B fill:#00B894,stroke:#008E6E,color:#fff,stroke-width:2px
    style C fill:#FDCB6E,stroke:#D4A84E,color:#333,stroke-width:2px
    style D fill:#E17055,stroke:#B5453A,color:#fff,stroke-width:2px
    style E fill:#00CEC9,stroke:#009E9A,color:#fff,stroke-width:2px
```

---

## 🔒 Req 4 — Anonimização LGPD

```mermaid
flowchart TD
    A["📃 Texto extraído"] --> B["🔒 Anônimizador\nMicrosoft Presidio"]
    B --> C["🔄 Substitui dados sensíveis\n👤 Nome → NOME\n🆔 CPF → CPF\n🏠 Endereço → ENDEREÇO\n📞 Telefone → TELEFONE\n📧 Email → EMAIL"]
    C --> D{"✅ Anonimização\nOK?"}
    D -- "❌ Falha" --> E["⚠️ Registra erro\n▶️ Continua sem anonimização"]
    D -- "✅ Sim" --> F["🛡️ Texto anonimizado\n💼 Info profissional preservada"]
    E --> F

    style A fill:#636E72,stroke:#4A5357,color:#fff,stroke-width:2px
    style B fill:#E17055,stroke:#B5453A,color:#fff,stroke-width:2px
    style C fill:#E17055,stroke:#B5453A,color:#fff,stroke-width:2px
    style D fill:#FDCB6E,stroke:#D4A84E,color:#333,stroke-width:2px
    style E fill:#D63031,stroke:#A52525,color:#fff,stroke-width:2px
    style F fill:#00B894,stroke:#008E6E,color:#fff,stroke-width:2px
```

---

## ⚡ Req 5 e 6 — Otimização de Tokens + Análise LLM

```mermaid
flowchart TD
    A["🛡️ Texto anonimizado"] --> B["🧹 Remove texto\nredundante"]
    B --> C{"📏 Texto >\n2000 tokens?"}
    C -- "✅ Sim" --> D["✂️ Resume seções\nmenos relevantes"]
    C -- "❌ Não" --> E["📦 Monta Prompt Otimizado\n🔧 JSON / lista estruturada"]
    D --> E
    E --> F["🤖 Analisador LLM\ncompara perfil vs vaga"]
    F --> G{"🌐 LLM\ndisponível?"}
    G -- "❌ Não" --> H["⚠️ Erro — permite\nreprocessamento"]
    G -- "✅ Sim" --> I["💯 Score 0-100"]
    I --> J["📝 Justificativa textual"]
    J --> K["💪 Pontos fortes"]
    K --> L["🔍 Gaps / lacunas"]
    L --> M["🏆 Ranking ordenado\npor Score decrescente"]

    style A fill:#00B894,stroke:#008E6E,color:#fff,stroke-width:2px
    style B fill:#FDCB6E,stroke:#D4A84E,color:#333,stroke-width:2px
    style C fill:#FDCB6E,stroke:#D4A84E,color:#333,stroke-width:2px
    style D fill:#FDCB6E,stroke:#D4A84E,color:#333,stroke-width:2px
    style E fill:#FDCB6E,stroke:#D4A84E,color:#333,stroke-width:2px
    style F fill:#E84393,stroke:#B5306F,color:#fff,stroke-width:2px
    style G fill:#FDCB6E,stroke:#D4A84E,color:#333,stroke-width:2px
    style H fill:#E17055,stroke:#B5453A,color:#fff,stroke-width:2px
    style I fill:#E84393,stroke:#B5306F,color:#fff,stroke-width:2px
    style J fill:#E84393,stroke:#B5306F,color:#fff,stroke-width:2px
    style K fill:#00B894,stroke:#008E6E,color:#fff,stroke-width:2px
    style L fill:#D63031,stroke:#A52525,color:#fff,stroke-width:2px
    style M fill:#00CEC9,stroke:#009E9A,color:#fff,stroke-width:2px
```

---

## 🏆 Req 7 — Visualização de Resultados

```mermaid
flowchart TD
    A(("🧑‍💼 RH")) --> B["📊 Acessa ranking\nda vaga"]
    B --> C["📋 Lista: Score, arquivo\ndo CV, resumo"]
    C --> D["🔎 Expandir justificativa\ncompleta, fortes e gaps"]
    C --> E["🔃 Ordenar por\nScore ou nome"]
    C --> F["🎯 Filtrar por\nScore mínimo"]

    style A fill:#4A90D9,stroke:#2C5F8A,color:#fff,stroke-width:2px
    style B fill:#00CEC9,stroke:#009E9A,color:#fff,stroke-width:2px
    style C fill:#6C5CE7,stroke:#4A3DB0,color:#fff,stroke-width:2px
    style D fill:#E84393,stroke:#B5306F,color:#fff,stroke-width:2px
    style E fill:#FDCB6E,stroke:#D4A84E,color:#333,stroke-width:2px
    style F fill:#00B894,stroke:#008E6E,color:#fff,stroke-width:2px
```

---

## 🌐 Req 8 — Interface Web + 🗄️ Req 9 — Persistência + ⚠️ Req 10 — Erros

```mermaid
flowchart LR
    subgraph WEB["🌐 Interface Web"]
        W1["🖥️ Responsivo desktop"]
        W2["📑 Páginas:\nVagas · Upload · Rankings"]
        W3["⏳ Feedback visual:\nloading · progresso"]
    end

    subgraph DB["🗄️ Persistência"]
        D1["💾 Vagas cadastradas"]
        D2["📄 PDFs armazenados"]
        D3["📊 Scores e rankings"]
        D4["🔄 Recuperação pós-restart"]
        D5["🗑️ Exclusão em cascata"]
    end

    subgraph ERR["⚠️ Tratamento de Erros"]
        E1["📄 Falha no Extrator → msg PDF"]
        E2["🔒 Falha Anônimizador → continua"]
        E3["🤖 Falha LLM → reprocessar"]
        E4["📎 Falha upload → msg erro"]
        E5["📝 Log de todos os erros"]
    end

    WEB --> DB
    WEB --> ERR

    style W1 fill:#4A90D9,stroke:#2C5F8A,color:#fff,stroke-width:2px
    style W2 fill:#4A90D9,stroke:#2C5F8A,color:#fff,stroke-width:2px
    style W3 fill:#4A90D9,stroke:#2C5F8A,color:#fff,stroke-width:2px
    style D1 fill:#636E72,stroke:#4A5357,color:#fff,stroke-width:2px
    style D2 fill:#636E72,stroke:#4A5357,color:#fff,stroke-width:2px
    style D3 fill:#636E72,stroke:#4A5357,color:#fff,stroke-width:2px
    style D4 fill:#636E72,stroke:#4A5357,color:#fff,stroke-width:2px
    style D5 fill:#636E72,stroke:#4A5357,color:#fff,stroke-width:2px
    style E1 fill:#E17055,stroke:#B5453A,color:#fff,stroke-width:2px
    style E2 fill:#E17055,stroke:#B5453A,color:#fff,stroke-width:2px
    style E3 fill:#E17055,stroke:#B5453A,color:#fff,stroke-width:2px
    style E4 fill:#E17055,stroke:#B5453A,color:#fff,stroke-width:2px
    style E5 fill:#E17055,stroke:#B5453A,color:#fff,stroke-width:2px
```
