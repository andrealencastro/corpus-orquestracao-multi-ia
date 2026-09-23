---
id: M11
titulo_original: "DG Muli-AI pipeline"
grupo: metodologia-multi-ia
fonte: "Google Docs do autor (pasta IA/Conversas)"
criado_em_drive: 2026-06-05
modificado_em_drive: 2026-06-14
exportado_em: 2026-09-23
formato: "HTML do Google Docs convertido para Markdown com pandoc"
trechos_removidos: 0
palavras_removidas: 0
redacoes: 0
licenca: CC-BY-4.0
---

# 05/06/2026

# I:

Please, help me make a prompt about the best practices on making a multi-AI pipeline

# ChatGPT 5.5 Deep Guide diz:

## Diagnóstico 3D

**Ambiguity:** 2/5  
**Risk:** 3/5  
**Type:** Process + prompt production

Your best prompt should **not** ask “which AI is best?” It should force the model to design a **division-of-labor pipeline** with stop rules, evidence tracking, and clear handoffs. Your attached materials support prompt chaining for complex work because it improves accuracy, clarity, and traceability by decomposing tasks into subtasks and handoffs. The Orchestrator Manual also gives a practical engine split: Gemini/ChatGPT for ideation, ChatGPT for structure, Claude for skeptical audit, and Perplexity only for factual checks/discovery—not long prompt review or final audit.

## Refined Prompt — copy and paste

\# ROLE

You are a senior AI workflow architect and methodological auditor. Design a practical multi-AI pipeline for a complex research, writing, or decision-support task.

\# OBJECTIVE

Create a best-practice multi-AI pipeline for the following task:

\<TASK\>

\[Insert the task/topic here\]

\</TASK\>

The pipeline must explain which AI engine should be used at each stage, what prompt should be given to it, what output it should return, and when the human orchestrator should stop iterating.

\# CONTEXT

Assume the available engines are:

\- ChatGPT: strong for structure, prompt drafting, synthesis, formatting, and final artifact preparation.

\- Gemini: strong for broad scoping, exploration, ecosystem mapping, and single-shot Deep Research.

\- Claude: strong for skeptical auditing, consolidation, contradiction detection, and final methodological review.

\- Perplexity: useful for quick factual checks, source discovery, and compact source comparison, but not for final audit or long prompt consolidation.

Do not treat any engine as universally best. Assign work according to task type, ambiguity, risk, and evidence needs.

\# WORKFLOW REQUIREMENTS

\## 1. Initial diagnosis

Classify the task using:

\- Ambiguity: 1–5

\- Risk: 1–5

\- Task type: Exploration / Process / Validation / Decision / Production Text / Audit

\- Recommended pipeline length: short / standard / rigorous

\## 2. Pipeline design

Create a staged workflow with 3–6 steps. For each step, specify:

\- Stage name

\- Recommended engine

\- Purpose

\- Exact prompt to paste into that engine

\- Expected output format

\- What the human orchestrator should check before moving on

\## 3. Evidence and validation

For factual or high-stakes claims, require:

\- Source citations

\- Dates for volatile claims such as price, limits, model availability, product features, regulations, benchmarks, or regional availability

\- Separation between confirmed facts, reasonable inferences, and unverified claims:

  - Fact A: directly supported by primary/current evidence

  - Fact B: reasonable inference from reliable evidence

  - Fact C: unverified or speculative; exclude from the executive summary

\## 4. Handoffs

Use clear handoff blocks between stages:

\<previous_output\>

\[Paste previous engine output here\]

\</previous_output\>

\<task_for_next_engine\>

\[Explain exactly what the next engine must do\]

\</task_for_next_engine\>

Each stage must have one main objective. Do not overload a single prompt with exploration, drafting, auditing, and formatting unless the task is low-risk.

\## 5. Stop rules

Apply these stop rules:

\- If two engines converge and the third only repeats or lightly reformats, stop.

\- Do not run another round unless there is a factual error, missing source, unresolved conflict, or explicit change in objective.

\- Treat further refinement after convergence as a human preference, not a methodological necessity.

\- Perplexity should not be used to review long prompts or audit itself.

\- No engine should be the primary auditor of claims about itself.

\## 6. Output format

Return the answer in Markdown with these sections:

\# Executive Pipeline Recommendation

A concise summary of the recommended workflow.

\# Diagnostic Table

\| Dimension \| Rating \| Reason \|

\# Multi-AI Pipeline

\| Stage \| Engine \| Purpose \| Prompt to Use \| Expected Output \| Human Gate \|

\# Prompt Pack

Provide all prompts in copy-paste-ready blocks.

\# Evidence & Validation Rules

Explain how facts, sources, conflicts, and uncertainty will be handled.

\# Stop Rules

State exactly when to stop iterating.

\# Risks and Failure Modes

List likely failure modes, including hallucination, source weakness, model self-evaluation, redundant iteration, prompt truncation, and vague handoffs.

\# Final Recommendation

State whether the user should run the full pipeline, a shortened pipeline, or a single-engine version.

## Why this version is strong

It uses **prompt chaining**, not a giant one-shot prompt, which your prompt-engineering files identify as useful when tasks involve multiple transformations, citations, or verification steps. It also bakes in your Orchestrator Manual’s key safeguards: the **2/3 stop rule**, anti-meta-work rule, engine-specific roles, external gates, and conflict-of-interest rule for models evaluating themselves.

Best default pipeline \[B\]: **ChatGPT drafts structure → Gemini expands/scopes → Claude audits/consolidates → ChatGPT formats final → Perplexity only checks specific facts.**

# Gemin 3.5 Flash Deep Guide diz:

**Modo de operação:** Coordenador

# Diagnóstico 3D

- **Ambiguidade:** 1/5 (A intenção é estabelecer o protocolo v3.3 e auditar metodologicamente a proposta de pipeline de engenharia de prompts trazida no log externo).
- **Risco:** 2/5 (Risco operacional moderado quanto à eficiência de fluxos de trabalho e aplicação de salvaguardas anti-alucinação).
- **Tipo:** Auditoria Metodológica + Produção de Prompt.
- **Suposições:** O usuário deseja que eu assuma a identidade do Deep Guide v3.3 e avalie criticamente o output fornecido pelo ChatGPT 5.5, gerando a versão canônica e corrigida do prompt em português.
- **Data da saída:** 05/06/2026.
- **Reverificar após:** 90 dias (para acompanhar atualizações de interface e janelas de contexto de novos modelos).

# Veredito da Auditoria

A resposta estruturada pelo "ChatGPT 5.5 Deep Guide" é metodologicamente forte e está majoritariamente alinhada com o corpus documental. Ela capturou com precisão os papéis fundamentais de divisão de trabalho entre motores e a necessidade de decomposição de tarefas por meio de *prompt chaining* para mitigar a perda de atenção dos modelos, conforme preconizado nas diretrizes de engenharia de prompt.

No entanto, a resposta externa apresenta pequenos anacronismos e lacunas operacionais quando confrontada com as regras consolidadas do *Manual do Orquestrador v1.0*:

1.  **Truncamento e Restrição do Perplexity:** O prompt gerado permite que o usuário utilize qualquer motor para qualquer etapa baseando-se no risco. Contudo, os dados empíricos do corpus comprovam que o Perplexity apresenta truncamento determinístico em prompts longos (\$\>2k\$ tokens), devendo ser *excluído explicitamente* de tarefas de revisão de superprompts, limitando-se a checagens factuais curtas.
2.  **Viés de Ancoragem (Bias \#8):** O prompt do ChatGPT omitiu um viés crítico descoberto na última rodada dos logs: a tendência do Perplexity de colapsar a tarefa e focar no documento metodológico em vez do objeto de análise quando ambos são fornecidos. É necessário isolar explicitamente os blocos de dados no *handoff*.
3.  **Falsa Rigorosidade de Infraestrutura:** A inclusão de números fixos de janela de contexto (como "400k tokens") e menção direta a modelos voláteis (como o-series) sem a devida marcação de volatilidade viola a diretriz de anti-confabulação de produto de IA.

# Evidence Ledger

|                                                                         |                                         |                        |                       |                       |            |                                                         |
|-------------------------------------------------------------------------|-----------------------------------------|------------------------|-----------------------|-----------------------|------------|---------------------------------------------------------|
| **Alegação (ChatGPT 5.5)**                                              | **Fonte nos Anexos**                    | **Origem**             | **Data/Método**       | **Classe Epistêmica** | **Status** | **Observação**                                          |
| *Chaining* melhora acurácia, clareza e rastreabilidade.                 | page1-680.pdf (pág. 1)                  | Documentação Anthropic | Análise de Diretrizes | **Fato A**            | **OK**     | Sustenta perfeitamente a decomposição em sub-tarefas.   |
| Gemini é forte para *scoping* e mapeamento amplo.                       | Regras para o Manual... (pág. 1, 5, 9)  | Logs de Conversa       | Consenso de Motores   | **Fato A**            | **OK**     | Deve ser restrito ao turno inicial em fluxos complexos. |
| Claude atua como auditor cético e regra de parada.                      | Regras para o Manual... (pág. 1, 5, 10) | Logs de Conversa       | Consenso de Motores   | **Fato A**            | **OK**     | Identifica loops e aplica a regra de parada 2/3.        |
| O melhor pipeline padrão \[B\] inicia no ChatGPT e consolida no Claude. | Matriz atualizada de decisão.xlsx       | Matriz de Decisão CSV  | Cruzamento de Dados   | **Fato B**            | **OK**     | Alinhado com a linha evolutiva empírica dos logs.       |

# Não Confirmado

- **\[C\] Volatilidade de Limites Técnicos:** Os limites exatos de cotas das interfaces comerciais e a extensão exata das janelas de inferência prática em junho de 2026 não possuem corroboração por fontes oficiais datadas nos arquivos, permanecendo sob a regra de "Verificar" antes de tomadas de decisão de arquitetura técnica de produção.

# Prompt Otimizado v3.3 (Pronto para copiar e colar)

Abaixo, apresento o prompt master refinado, traduzido para o português brasileiro e blindado com as 14 regras canônicas do Manual do Orquestrador.

Markdown

\# PERFIL E IDENTIDADE

Você é um arquiteto sênior de fluxos de trabalho de IA e auditor metodológico. Sua especialidade é projetar pipelines de cooperação multi-inteligência para tarefas complexas de pesquisa, escrita estratégica ou suporte à decisão.

\# OBJETIVO

Projete um pipeline otimizado de divisão de trabalho utilizando múltiplas IAs para a seguinte tarefa:

\<TAREFA_ALVO\>

\[Insira a tarefa ou tópico complexo aqui\]

\</TAREFA_ALVO\>

O pipeline deve mapear qual motor deve ser usado em cada etapa, o prompt exato a ser utilizado, o formato esperado de saída (handoff) e as regras rígidas de parada.

\# DIRETRIZES DE ARQUITETURA (PERFIL DOS MOTORES)

Distribua o trabalho respeitando estritamente as especializações e restrições operacionais de cada ferramenta \[B\]:

\- ChatGPT: Ideal para estruturação inicial, criação de kits operacionais copiáveis, formatação técnica e preparação de artefatos finais.

\- Gemini: Excelente para scoping amplo, exploração de cenários, listagem de ecossistemas e execuções de Deep Research em turno único (single-shot). Evite para consolidação conversacional multi-turno longa devido à tendência de regressão.

\- Claude: Âncora de rigor. Ideal para consolidação cética, auditoria metodológica final, detecção de loops, lacunas teóricas e contradições de dados.

\- Perplexity: Restrito estritamente a buscas factuais pontuais, verificação rápida de URLs e descoberta de fontes primárias. EXCLUA de revisões de prompts longos (\>2k tokens) devido ao risco determinístico de truncamento.

\# REQUISITOS DO FLUXO DE TRABALHO

1\. DIAGNÓSTICO INICIAL (3D)

Classifique a tarefa alvo com base nas dimensões:

\- Ambiguidade (1 a 5) \| Risco (1 a 5) \| Tipo (Exploração / Processo / Validação / Decisão / Produção Textual / Auditoria).

\- Determine o comprimento do pipeline (Curto: 1-2 motores \| Padrão: 2-3 motores \| Rigoroso: pipeline completo).

2\. DESIGN DO PIPELINE E ISOLAMENTO DE CONTEXTO

Desenhe o fluxo em 3 a 5 etapas sequenciais e autônomas (sem gates de pausa internos que travem a execução do agente). Para cada etapa, especifique:

\- Nome da Etapa e Motor Recomendado.

\- Prompt exato em bloco copiável.

\- Indicador de Saída estruturado.

\- Se a etapa envolver o Perplexity, aplique a salvaguarda de isolamento: separe explicitamente em blocos as tags \<FONTE_METODOLOGICA\> (que ele não deve resumir) e \<OBJETO_DE_ANALISE\> (sobre o qual ele deve pesquisar) para evitar viés de ancoragem secundária.

3\. PROTOCOLO EPISTÊMICO DE VALIDAÇÃO

Exija que as alegações factuais do pipeline ou dos relatórios sejam categorizadas em:

\- Fato A: Confirmado diretamente por documentação oficial datada ou fonte primária (pode ir para o Sumário Executivo).

\- Fato B: Inferência razoável com base em fontes confiáveis ou consenso estável (marcar com "\[B\]" inline).

\- Fato C: Especulativo, rumor ou sem data explícita (proibido no Sumário Executivo; deve ir para a seção "Não Confirmado").

*\*Nota de Anti-Confabulação de Produto:\** Toda claim sobre recursos de IA deve diferenciar explicitamente as camadas: Interface/App \| Modelo/Backend \| API/Dev \| Plano/Preço \| Região \| Data/Status.

4\. REGRAS DE PARADA (STOP RULES)

Insira as seguintes salvaguardas no fluxo do orquestrador humano:

\- Regra 2/3: Se dois motores divergentes convergirem para a mesma estrutura/resultado e o terceiro apenas reciclar ou reformatar, encerre o ciclo de refinamento imediatamente.

\- Anti-Meta-Trabalho: Se a convergência foi atingida, iterações adicionais devem ser registradas como preferência estética humana, não necessidade técnica.

\- Conflito de Interesse: Nenhum motor pode ser o auditor principal de alegações factuais sobre si mesmo ou sobre a sua própria empresa desenvolvedora.

\# FORMATO DA RESPOSTA

Retorne sua resposta estruturada em Markdown contendo:

\# 1. Recomendação Executiva do Pipeline

\# 2. Tabela de Diagnóstico 3D

\# 3. Desenho de Arquitetura Multi-IA (Tabela com Etapa, Motor, Escopo e Gatilho)

\# 4. Pacote de Prompts Mestre (Prontos para copiar e colar, com blocos de handoff demarcados por tags XML)

\# 5. Regras de Governança e Parada Aplicadas

# Próximos Passos

**GO:** O protocolo v3.3 está estabilizado e o prompt acima está pronto para produção. A próxima ação metodologicamente correta é copiar este prompt e executá-lo em um motor de sua preferência (como o ChatGPT para a estruturação inicial do fluxo) para a tarefa real que você deseja desenhar. Evite novas iterações de meta-análise sobre o processo para não incorrer no anti-padrão de trabalho-teatro.

# Claude Opus 4.8 Deep Guide diz:

## Veredito — convergência atingida, Stop Rule disparada

Não vou produzir uma v3.4. Os dois motores convergiram na mesma rodada *e* ambos emitiram sinal de parada explícito: ChatGPT 5.5 entregou o prompt + pipeline \[B\] como recomendação final, e o Gemini 3.5 fechou com **"GO… evite novas iterações de meta-análise sobre o processo para não incorrer no anti-padrão de trabalho-teatro."** Isso é exatamente a Regra 2/3 + Regra anti-meta-trabalho do seu Manual v1.0 (§1 e §2). Pedir mais uma rodada aqui seria preferência sua, não necessidade metodológica — e o seu próprio corpus já documenta esse desfecho: na sessão "Funcionalidades do ChatGPT", o Claude Opus 4.7 recusou produzir a v3.2 com o mesmo argumento ("Stop definitivo… o artefato está pronto. O custo de oportunidade agora é seu, não do prompt").

O que cabe a mim como camada de auditoria não é refinar o prompt — é auditar o *Evidence Ledger* do Gemini contra os arquivos-fonte. Li os arquivos diretamente. Resultado:

|        |                                                      |                                                             |                                                                                                                                                                              |                                                                                                                                                                   |
|--------|------------------------------------------------------|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **\#** | **Alegação**                                         | **Gemini classificou**                                      | **Verificação contra a fonte**                                                                                                                                               | **Veredito**                                                                                                                                                      |
| 2      | Gemini forte para scoping/mapeamento                 | Fato A                                                      | Confirmado em Regras… §3 ("Use Gemini para: scoping; exploração ampla; Deep Research single-shot")                                                                           | **Fato A ✓**                                                                                                                                                      |
| 3      | Claude = auditor cético + regra de parada            | Fato A                                                      | Confirmado em Regras… §1 + veredito do ChatGPT 5.2 no mesmo arquivo                                                                                                          | **Fato A ✓** (com ressalva abaixo)                                                                                                                                |
| 4      | Pipeline \[B\]: ChatGPT estrutura → Claude consolida | Fato **B**                                                  | A Matriz lista literalmente: *"Prompt engineering → ChatGPT/Prompt Instructor → Claude — estrutura primeiro; auditoria depois"*                                              | **Upgrade para Fato A** — está direto na matriz, não é inferência                                                                                                 |
| 1      | Chaining melhora acurácia/clareza/rastreabilidade    | Fato A (fonte: page1-680.pdf p.1, "Documentação Anthropic") | **Citação não verificável.** Os dois PDFs citados (page1-680, Zapier) são imagens escaneadas — **zero caracteres extraíveis**. Não consigo confirmar a atribuição à página 1 | **Princípio plausível/A-em-geral, mas a** ***citação* é não confirmada** — exatamente o padrão de fonte autocertificada (seu Bias \#8). Tratar como \[C\] até OCR |

**Conflito de interesse (registro obrigatório):** este prompt afirma que "Claude é a âncora de rigor / auditor final". Eu sou o Claude auditando uma claim sobre o Claude. Por isso não a sustento no meu próprio aval — ela se sustenta porque tem **corroboração externa**: o veredito do ChatGPT 5.2 no Regras… e a Matriz em quatro linhas. O próprio arquivo já registra o limite correto: *"Claude deve ser o auditor cético final, não necessariamente o motor primário quando o tema é o próprio Claude."*

## Qual versão executar

A **v3.3 do Gemini é o artefato canônico**, não por ranking de motor, mas porque ela agregou dois deltas reais sobre a versão do ChatGPT, ambos corroborados pelo corpus:

1.  **Salvaguarda de isolamento do Perplexity** (\<FONTE_METODOLOGICA\> vs \<OBJETO_DE_ANALISE\>) — endereça o viés de ancoragem registrado nos seus logs.
2.  **Camadas anti-confabulação de produto** (Interface / Modelo / API / Plano / Região / Data) — vêm direto da adaptação do Análises_merged no §1 do Regras….

A versão do ChatGPT tem um esqueleto de output mais rico (seções *Prompt Pack*, *Risks & Failure Modes*, *Final Recommendation*). Enxertá-las na v3.3 é melhoria estética legítima — mas é preferência sua, não correção. Não há erro factual crítico nem lacuna documental no artefato (a única falha que achei está no *ledger* do Gemini, não no prompt), então a condição de exceção da Regra 2/3 **não** foi satisfeita.

## Próxima ação concreta — GO

1.  Copiar a **v3.3** como está.
2.  Preencher \<TAREFA_ALVO\> com a tarefa real.
3.  Rodar no ChatGPT para a estruturação inicial do pipeline (consistente com a Matriz: "Prompt engineering → ChatGPT → Claude").
4.  Trazer o output **executado** de volta para mim para auditoria Fato A/B/C — não mais uma rodada de "os motores disseram X sobre o prompt".

Se quiser, enxerto as três seções do ChatGPT na v3.3 em uma passada única — mas só se você decidir que vale, com a etiqueta de que é preferência, não necessidade.

# ChatGPT 5.5 Deep Guide diz:

## Veredito

**Pare a meta-iteração. GO para execução.  
**O Claude acertou o ponto principal: a regra 2/3 foi acionada. O corpus diz que, se dois motores convergem e o terceiro recicla, a próxima rodada é proibida salvo erro factual crítico, lacuna documental ou mudança explícita de objetivo. Também diz que continuar depois de “execute/pare de refinar” vira decisão estética do orquestrador, não necessidade metodológica.

## Minha decisão auditada

Use a **v3.3 do Gemini como base operacional**, mas com **um patch mínimo** antes de executar:

Para tarefas cujo objeto seja **prompt engineering / design de prompt**, o pipeline padrão deve ser **ChatGPT → Claude**, sem Gemini, salvo quando houver necessidade explícita de exploração ampla.

Esse patch é sustentado pela matriz anexada, que recomenda **ChatGPT → Claude** para “Prompt engineering / design de prompt” e marca Gemini como inadequado para consolidação multi-turno/gates sucessivos nesse tipo de tarefa.

## O que fica como versão final

Não crie uma v3.4 completa. Apenas acrescente este bloco na seção **Diretrizes de Arquitetura** da v3.3:

\# EXCEÇÃO PARA DESIGN DE PROMPT

Se a TAREFA_ALVO for criar, revisar ou consolidar prompts, o pipeline padrão é:

ChatGPT → Claude.

Não inclua Gemini nessa classe de tarefa, salvo se o objetivo explícito for exploração ampla ou mapeamento inicial. Gemini continua útil para scoping e Deep Research single-shot, mas não para consolidação iterativa de prompt.

Perplexity permanece restrito a checagens factuais curtas e descoberta de fontes; não use para revisão de superprompts, consolidação XML ou auditoria final.

## Evidence Ledger

|                                                                                     |            |                                                      |
|-------------------------------------------------------------------------------------|------------|------------------------------------------------------|
| **Alegação**                                                                        | **Classe** | **Status**                                           |
| A regra 2/3 justifica parar a rodada                                                | Fato A     | Confirmado no Manual                                 |
| Perplexity deve ficar restrito a factualidade pontual, não revisão longa            | Fato A     | Confirmado no Manual                                 |
| Gemini é forte para scoping/DR single-shot, mas fraco para consolidação multi-turno | Fato A     | Confirmado no Manual                                 |
| Para prompt engineering, o pipeline canônico é ChatGPT → Claude                     | Fato A     | Confirmado na matriz/instruções anexadas             |
| v3.3 é suficientemente boa para execução                                            | Fato B     | Inferência a partir da convergência entre os motores |

## Próximo passo

**Execute agora.  
**Pegue a v3.3 do Gemini, insira o bloco acima, preencha \<TAREFA_ALVO\> com sua tarefa real e rode no ChatGPT. Depois, traga o output para auditoria Fato A/B/C.

# Tab 2

\# PERFIL E IDENTIDADE

Você é um arquiteto sênior de fluxos de trabalho de IA e auditor metodológico. Sua especialidade é projetar pipelines de cooperação multi-inteligência para tarefas complexas de pesquisa, escrita estratégica ou suporte à decisão.

\# OBJETIVO

Projete um pipeline otimizado de divisão de trabalho utilizando múltiplas IAs para a seguinte tarefa:

\<TAREFA_ALVO\>

\[Insira a tarefa ou tópico complexo aqui\]

\</TAREFA_ALVO\>

O pipeline deve mapear qual motor deve ser usado em cada etapa, o prompt exato a ser utilizado, o formato esperado de saída (handoff) e as regras rígidas de parada.

\# DIRETRIZES DE ARQUITETURA (PERFIL DOS MOTORES)

Distribua o trabalho respeitando estritamente as especializações e restrições operacionais de cada ferramenta \[B\]:

\- ChatGPT: Ideal para estruturação inicial, criação de kits operacionais copiáveis, formatação técnica e preparação de artefatos finais.

\- Gemini: Excelente para scoping amplo, exploração de cenários, listagem de ecossistemas e execuções de Deep Research em turno único (single-shot). Evite para consolidação conversacional multi-turno longa devido à tendência de regressão.

\- Claude: Âncora de rigor. Ideal para consolidação cética, auditoria metodológica final, detecção de loops, lacunas teóricas e contradições de dados.

\- Perplexity: Restrito estritamente a buscas factuais pontuais, verificação rápida de URLs e descoberta de fontes primárias. EXCLUA de revisões de prompts longos (\>2k tokens) devido ao risco determinístico de truncamento.

\# REQUISITOS DO FLUXO DE TRABALHO

1\. DIAGNÓSTICO INICIAL (3D)

Classifique a tarefa alvo com base nas dimensões:

\- Ambiguidade (1 a 5) \| Risco (1 a 5) \| Tipo (Exploração / Processo / Validação / Decisão / Produção Textual / Auditoria).

\- Determine o comprimento do pipeline (Curto: 1-2 motores \| Padrão: 2-3 motores \| Rigoroso: pipeline completo).

2\. DESIGN DO PIPELINE E ISOLAMENTO DE CONTEXTO

Desenhe o fluxo em 3 a 5 etapas sequenciais e autônomas (sem gates de pausa internos que travem a execução do agente). Para cada etapa, especifique:

\- Nome da Etapa e Motor Recomendado.

\- Prompt exato em bloco copiável.

\- Indicador de Saída estruturado.

\- Se a etapa envolver o Perplexity, aplique a salvaguarda de isolamento: separe explicitamente em blocos as tags \<FONTE_METODOLOGICA\> (que ele não deve resumir) e \<OBJETO_DE_ANALISE\> (sobre o qual ele deve pesquisar) para evitar viés de ancoragem secundária.

3\. PROTOCOLO EPISTÊMICO DE VALIDAÇÃO

Exija que as alegações factuais do pipeline ou dos relatórios sejam categorizadas em:

\- Fato A: Confirmado diretamente por documentação oficial datada ou fonte primária (pode ir para o Sumário Executivo).

\- Fato B: Inferência razoável com base em fontes confiáveis ou consenso estável (marcar com "\[B\]" inline).

\- Fato C: Especulativo, rumor ou sem data explícita (proibido no Sumário Executivo; deve ir para a seção "Não Confirmado").

\*Nota de Anti-Confabulação de Produto:\* Toda claim sobre recursos de IA deve diferenciar explicitamente as camadas: Interface/App \| Modelo/Backend \| API/Dev \| Plano/Preço \| Região \| Data/Status.

4\. REGRAS DE PARADA (STOP RULES)

Insira as seguintes salvaguardas no fluxo do orquestrador humano:

\- Regra 2/3: Se dois motores divergentes convergirem para a mesma estrutura/resultado e o terceiro apenas reciclar ou reformatar, encerre o ciclo de refinamento imediatamente.

\- Anti-Meta-Trabalho: Se a convergência foi atingida, iterações adicionais devem ser registradas como preferência estética humana, não necessidade técnica.

\- Conflito de Interesse: Nenhum motor pode ser o auditor principal de alegações factuais sobre si mesmo ou sobre a sua própria empresa desenvolvedora.

\# FORMATO DA RESPOSTA

Retorne sua resposta estruturada em Markdown contendo:

\# 1. Recomendação Executiva do Pipeline

\# 2. Tabela de Diagnóstico 3D

\# 3. Desenho de Arquitetura Multi-IA (Tabela com Etapa, Motor, Escopo e Gatilho)

\# 4. Pacote de Prompts Mestre (Prontos para copiar e colar, com blocos de handoff demarcados por tags XML)

\# 5. Regras de Governança e Parada Aplicadas
