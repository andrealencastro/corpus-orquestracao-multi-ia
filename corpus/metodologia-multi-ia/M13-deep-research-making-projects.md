---
id: M13
titulo_original: "Deep Research Making Projects"
grupo: metodologia-multi-ia
fonte: "Google Docs do autor (pasta IA/Conversas)"
criado_em_drive: 2026-06-28
modificado_em_drive: 2026-06-28
exportado_em: 2026-09-23
formato: "HTML do Google Docs convertido para Markdown com pandoc"
trechos_removidos: 0
palavras_removidas: 0
redacoes: 0
licenca: CC-BY-4.0
---

# 28/08/2026

# Eu:

Me ajude a melhorar o seguinte prompt, por favor:

What are the best way to make Projects on Claude, specially the instructions?

# ChatGPT 5.5 Deep Guide diz:

### 1) Diagnóstico 3D

**Ambiguidade: 2/5.** Seu objetivo é claro, mas o prompt está amplo demais e não define o tipo de resposta desejada: guia, checklist, exemplos de instruções ou template pronto.

**Risco: 1/5.** Baixo risco. O único cuidado é não inventar detalhes sobre Claude Projects, porque recursos e limites mudam. A documentação atual diz que Projects têm **knowledge base** e **project instructions**, e que as instruções do projeto são usadas em todos os chats dentro daquele projeto; também observa que o contexto não é compartilhado entre chats a menos que seja adicionado à knowledge base. ([Claude Help Center](https://support.anthropic.com/en/articles/9519177-how-can-i-create-and-manage-projects))

**Problema do prompt original:**

“What are the best way to make Projects on Claude, specially the instructions?”

Ele precisa de: inglês corrigido, objetivo específico, critérios de qualidade, formato de saída, exemplos práticos e foco em “project instructions”.

------------------------------------------------------------------------

### 2) Arquitetura & Seleção (modelo/pipeline + técnica)

Use um prompt em **formato consultivo**, pedindo que Claude aja como arquiteto de workspace. A melhor técnica aqui é:

**Role prompting + checklist + template + examples + quality gate.**

Para Claude, faz sentido usar estrutura clara e tags XML quando o prompt mistura contexto, instruções, exemplos e entradas variáveis; a própria documentação da Anthropic recomenda XML tags para reduzir ambiguidade em prompts complexos. ([Claude Platform Docs](https://docs.anthropic.com/pt/docs/build-with-claude/prompt-engineering/system-prompts))

Também vale pedir critérios de sucesso e formas de testar as instruções, porque a documentação de prompt engineering da Anthropic recomenda definir critérios de sucesso e avaliação antes de refinar prompts. ([Claude Platform Docs](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview))

------------------------------------------------------------------------

### 3) Prompt Final (Template Mestre)

Copie e cole este prompt no Claude:

You are a senior Claude workspace architect and prompt engineering advisor.

I want to learn the best way to create and organize Claude Projects, with special focus on writing effective Project Instructions.

\<context\>

I use Claude Projects to keep work organized across multiple chats.

I want each Project to have clear instructions, useful knowledge files, consistent behavior, and reusable workflows.

Assume I am a practical user, not a developer, unless technical details are necessary.

\</context\>

\<task\>

Create a practical guide for designing high-quality Claude Projects.

Focus especially on how to write Project Instructions that Claude will follow reliably across chats.

\</task\>

\<requirements\>

Please cover:

1\. What belongs in a Claude Project versus what belongs in a normal chat.

2\. How to decide when to create a new Project.

3\. How to structure Project Instructions.

4\. What to put in the Project Knowledge base.

5\. How Project Instructions should differ from uploaded knowledge files.

6\. Common mistakes when writing Project Instructions.

7\. A reusable Project Instructions template.

8\. Three concrete examples:

   - a writing/content project

   - a research/project-analysis project

   - a coding/product-development project

9\. A checklist I can use before finalizing a Claude Project.

10\. A simple testing method to verify whether the Project Instructions work well.

\</requirements\>

\<instruction_design_rules\>

When explaining Project Instructions, include guidance for:

\- role and expertise Claude should adopt

\- project goal

\- audience

\- preferred output formats

\- tone and style

\- source-of-truth hierarchy

\- how Claude should handle missing information

\- what Claude should never do

\- how Claude should ask clarifying questions

\- how Claude should use project knowledge

\- how Claude should handle uncertainty

\</instruction_design_rules\>

\<output_format\>

Use the following structure:

\# Executive Summary

Briefly explain the core principles.

\# Best Practices for Claude Projects

Give practical guidance.

\# How to Write Project Instructions

Explain the anatomy of strong instructions.

\# Reusable Project Instructions Template

Provide a copy-paste template with placeholders.

\# Examples

Provide three complete example Project Instructions.

\# Common Mistakes

List mistakes and how to fix them.

\# Testing Checklist

Give a checklist and 5 test prompts I can run inside the Project.

\# Final Recommendation

Give a concise recommended workflow for creating any new Claude Project.

\</output_format\>

\<constraints\>

Do not give vague advice.

Do not assume undocumented product features.

If a detail may depend on Claude plan, account type, or current product version, say so explicitly.

Prioritize practical instructions I can copy, edit, and use immediately.

\</constraints\>

------------------------------------------------------------------------

### 4) Auditoria (Quality Gate)

**Clareza:** boa. O prompt agora pede um guia prático, não uma resposta genérica.  
**Especificidade:** boa. Define exatamente os tópicos que Claude deve cobrir.  
**Formato:** forte. A saída terá seções previsíveis e reutilizáveis.  
**Segurança:** adequada. Inclui “não assumir features não documentadas”.  
**Robustez:** boa. Pede tratamento de incerteza, knowledge base, instruções e testes.  
**Eficiência:** adequada para uma única resposta longa. Para algo ainda melhor, rode em duas etapas: primeiro peça o guia, depois peça para Claude criar um Project Instructions template para seu caso real.  
**Auditabilidade:** forte. Inclui checklist e prompts de teste.

**Versão curta melhorada do seu prompt original:**

What is the best way to create and organize Claude Projects, especially the Project Instructions? Please give me a practical guide, a reusable instructions template, common mistakes, examples for different use cases, and a checklist to test whether the instructions work well.

Pronto para execução.

# Claude Opus 4.8 Deep Guide diz:

**Conflito de interesse — declarado primeiro (Regra 7).** O artefato que você trouxe tem como objeto *integral* um produto Claude (Projects). Pela Regra de conflito de interesse do Manual ("não usar uma ferramenta como motor primário para avaliar a própria ferramenta, especialmente em citações, pricing, privacidade ou claims de produto"), **eu não sou o avaliador válido das alegações de produto contidas no output**. Essas vão roteadas para passe externo datado. A auditoria estrutural/metodológica abaixo é meu papel legítimo; as afirmações factuais sobre Projects eu *não certifico* — apenas classifico o tier em que estão e digo o que falta.

------------------------------------------------------------------------

## Veredito

O prompt-mestre do ChatGPT é **estruturalmente forte e executável após 3 correções cirúrgicas**. Não abrir nova rodada de refinamento de prompt — fazê-lo seria anti-meta-trabalho (Regra 2), pois não há erro factual crítico nem mudança de objetivo. **Stop Rule (Regra 1) não se aplica:** há um único motor neste turno (N=1), não existe convergência 2/3 a avaliar.

Três defeitos, todos mapeados:

**1. Blocos de auto-homologação que não pertencem ao prompt.** O "Diagnóstico 3D" (Ambiguidade 2/5, Risco 1/5), a seção "4) Auditoria (Quality Gate)" e o selo "Pronto para execução" são o motor gerador auditando e aprovando o próprio output. → Viola a **Regra anti-autoauditoria performática** (o gate audita o protocolo, não o objeto pesquisado) e repete o padrão **Ritualização de Gates** que o seu próprio corpus já atribui ao ChatGPT. Auditoria e aprovação são decisão do orquestrador entre rodadas (Regra de gate externo), não conteúdo do prompt. **Deletar do artefato.**

**2. Duas citações de produto sem fonte datada.** "(Claude Help Center)" e "(Claude Platform Docs)" não têm URL, data nem documento específico. → Viola a **Regra de data obrigatória** (Regra 6) e a disciplina do Evidence Ledger (source/date/method/status). Sem fonte datada, **rebaixamento automático**: nenhuma destas é Fato A.

**3. Uma alegação de comportamento de feature volátil, com alto risco de desatualização.** "O contexto não é compartilhado entre chats a menos que seja adicionado à knowledge base." → Categoria explicitamente coberta pela **Regra anti-ancoragem em features** (Regra 5) + Regra 6. É justamente o tipo de comportamento que muda com recursos de memória / referência a chats anteriores. **Não certifico que está errado** (isso seria eu adjudicando claim de produto Claude — Regra 7); sinalizo como **candidato prioritário de desatualização** para o passe datado.

O que está **certo** e deve ser preservado: o esqueleto XML (role / context / task / requirements / constraints), a separação de seções copiáveis, e — crucialmente — a constraint "*Do not assume undocumented product features / say so explicitly if it depends on plan, account type, or version*". Essa constraint é boa e mitiga parcialmente o risco de volatilidade *dentro da execução*. É a força genuína do ChatGPT que o seu corpus já registra: arquiteto de artefato copiável.

------------------------------------------------------------------------

## Evidence Ledger — claims de produto no output

|        |                                                                   |                |                                       |                                                                  |
|--------|-------------------------------------------------------------------|----------------|---------------------------------------|------------------------------------------------------------------|
| **\#** | **Claim**                                                         | **Tier atual** | **Fonte no artefato**                 | **O que falta p/ Fato A**                                        |
| 1      | Projects têm knowledge base + project instructions                | **B**          | "Claude Help Center" (sem data/URL)   | Cite datada do Help Center                                       |
| 2      | Project instructions aplicam-se a todos os chats do projeto       | **B**          | idem                                  | idem                                                             |
| 3      | Contexto não compartilhado entre chats salvo via knowledge base   | **C**          | idem                                  | Re-check datado — **alto risco de stale** (memória / past-chats) |
| 4      | Anthropic recomenda XML tags em prompts complexos                 | **B**          | "Claude Platform Docs" (sem data/URL) | URL + data dos docs                                              |
| 5      | Anthropic recomenda definir critérios de sucesso antes de refinar | **B**          | idem                                  | URL + data dos docs                                              |

------------------------------------------------------------------------

## Correções cirúrgicas (não reescrever)

**(a)** Remover do artefato o "Diagnóstico 3D", a seção "4) Auditoria (Quality Gate)" e "Pronto para execução". O prompt-mestre começa em "You are a senior Claude workspace architect…" e termina em \</constraints\>.

**(b)** Acrescentar uma linha em \<constraints\> para tornar o guia produzido já Evidence-Ledger-ready:

*Any product-fact claim (usage limits, knowledge-base behavior, cross-chat context, plan/tier gating) must carry a dated source reference (Anthropic Help Center or docs, with date). If no dated source is available, label the claim as unverified.*

**(c)** Marcar as 5 claims acima como pendentes de passe externo; tratar a \#3 como prioridade.

------------------------------------------------------------------------

## Decisão de roteamento (binária)

A Matriz confirma: *Prompt engineering → ChatGPT/Prompt Instructor → Claude (estrutura primeiro, auditoria depois)*. ChatGPT estruturou, eu auditei — **o pipeline desta tarefa está completo**. Risco baixo não justifica terceiro motor.

- **Executar** o prompt-mestre após as correções (a)–(c). Não abrir rodada de refinamento.
- **Verificação dos 5 claims de produto: fora de mim.** Por Regra 7, o passe datado contra o Help Center / docs da Anthropic vai para Perplexity (busca factual + descoberta de fontes) ou web direta, não para Claude como avaliador primário. Vale também na *execução*: se o guia for gerado pelo próprio Claude, os fatos de produto continuam exigindo o passe externo datado — Claude explicando produto Claude é a COI da Regra 7.

------------------------------------------------------------------------

## Entrada de governança (colar no Manual)

**Log — auditoria de prompt-mestre (objeto: produto Claude).** Motor gerador: ChatGPT. Auditor: Claude (COI declarado, Regra 7 — objeto é produto Claude). Esqueleto XML aprovado. Três defeitos: (1) blocos de auto-homologação removidos — Regra anti-autoauditoria performática + Ritualização de Gates; (2) 2 citações de produto sem fonte datada → rebaixadas de A → B (Regra 6); (3) claim de contexto cross-chat → Fato C, candidato de stale (Regra 5). Stop Rule não avaliável (N=1). Roteamento: executar após correções; verificação de 5 claims de produto delegada a passe externo (Perplexity/web datado), não a Claude — Regra 7 estende-se à execução. **Auto-correção / Bias \#7:** apliquei a Regra 7 a mim mesmo recusando certificar os claims de produto — registro para contrariar a auto-auditoria branda.

# ChatGPT 5.5 Deep Guide diz:

### 1) Diagnóstico 3D

A crítica do Claude é **substancialmente correta**. Eu manteria o prompt-mestre, mas aceitaria as três correções cirúrgicas.

Ponto importante: verifiquei agora em fonte oficial da Anthropic/Claude. O claim sobre Projects ter **project knowledge**, **project instructions aplicáveis aos chats do projeto** e **contexto não compartilhado entre chats salvo quando adicionado ao project knowledge** está confirmado no Help Center datado de **16 de março de 2026**. ([Claude Help Center](https://support.anthropic.com/en/articles/9519177-how-can-i-create-and-manage-projects))

Também há confirmação, em artigo de **28 de maio de 2026**, de que project instructions servem para contexto/requisitos do projeto e só se aplicam aos chats dentro daquele projeto. ([Claude Help Center](https://support.anthropic.com/en/articles/10185728-understanding-claude-s-personalization-features))

### 2) Arquitetura & Seleção (modelo/pipeline + técnica)

Decisão: **não reescrever tudo**. O caminho correto é aplicar patch.

As técnicas preservadas são boas: role prompting, XML tags, requisitos explícitos, output format e constraints. A documentação da Anthropic recomenda XML tags para prompts complexos que misturam instruções, contexto, exemplos e variáveis. ([Claude Platform Docs](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/multishot-prompting)) Também recomenda ter critérios de sucesso e formas de teste antes de refinar prompts. ([Claude Platform Docs](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview))

### 3) Prompt Final (Template Mestre)

Aqui está a versão corrigida, sem auto-homologação dentro do artefato:

You are a senior Claude workspace architect and prompt engineering advisor.

I want to learn the best way to create and organize Claude Projects, with special focus on writing effective Project Instructions.

\<context\>

I use Claude Projects to keep work organized across multiple chats.

I want each Project to have clear instructions, useful knowledge files, consistent behavior, and reusable workflows.

Assume I am a practical user, not a developer, unless technical details are necessary.

\</context\>

\<task\>

Create a practical guide for designing high-quality Claude Projects.

Focus especially on how to write Project Instructions that Claude will follow reliably across chats.

\</task\>

\<requirements\>

Please cover:

1\. What belongs in a Claude Project versus what belongs in a normal chat.

2\. How to decide when to create a new Project.

3\. How to structure Project Instructions.

4\. What to put in the Project Knowledge base.

5\. How Project Instructions should differ from uploaded knowledge files.

6\. Common mistakes when writing Project Instructions.

7\. A reusable Project Instructions template.

8\. Three concrete examples:

   - a writing/content project

   - a research/project-analysis project

   - a coding/product-development project

9\. A checklist I can use before finalizing a Claude Project.

10\. A simple testing method to verify whether the Project Instructions work well.

\</requirements\>

\<instruction_design_rules\>

When explaining Project Instructions, include guidance for:

\- role and expertise Claude should adopt

\- project goal

\- audience

\- preferred output formats

\- tone and style

\- source-of-truth hierarchy

\- how Claude should handle missing information

\- what Claude should never do

\- how Claude should ask clarifying questions

\- how Claude should use project knowledge

\- how Claude should handle uncertainty

\</instruction_design_rules\>

\<output_format\>

Use the following structure:

\# Executive Summary

Briefly explain the core principles.

\# Best Practices for Claude Projects

Give practical guidance.

\# How to Write Project Instructions

Explain the anatomy of strong instructions.

\# Reusable Project Instructions Template

Provide a copy-paste template with placeholders.

\# Examples

Provide three complete example Project Instructions.

\# Common Mistakes

List mistakes and how to fix them.

\# Testing Checklist

Give a checklist and 5 test prompts I can run inside the Project.

\# Final Recommendation

Give a concise recommended workflow for creating any new Claude Project.

\</output_format\>

\<constraints\>

Do not give vague advice.

Do not assume undocumented product features.

If a detail may depend on Claude plan, account type, product version, workspace settings, or current feature availability, say so explicitly.

Any product-fact claim, including usage limits, knowledge-base behavior, cross-chat context, plan/tier gating, memory, sharing, or project availability, must carry a dated source reference from the Anthropic/Claude Help Center or official docs. If no dated source is available, label the claim as unverified.

Prioritize practical instructions I can copy, edit, and use immediately.

\</constraints\>

### 4) Auditoria (Quality Gate)

**Correções aplicadas:** removi o bloco de auto-homologação, acrescentei a regra de fonte datada e tratei comportamento de feature como claim volátil.

**Evidence Ledger atualizado:**

|                                                                                   |                                                                                                                                                                                                                         |
|-----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Claim**                                                                         | **Status após verificação**                                                                                                                                                                                             |
| Projects têm project knowledge / knowledge base                                   | Confirmado em Help Center, 16 mar. 2026. ([Claude Help Center](https://support.anthropic.com/en/articles/9519177-how-can-i-create-and-manage-projects))                                                                 |
| Project instructions são usadas nos chats do projeto                              | Confirmado em Help Center, 16 mar. 2026. ([Claude Help Center](https://support.anthropic.com/en/articles/9519177-how-can-i-create-and-manage-projects))                                                                 |
| Contexto não é compartilhado entre chats salvo se adicionado ao project knowledge | Confirmado em Help Center, 16 mar. 2026, mas continua sendo feature volátil. ([Claude Help Center](https://support.anthropic.com/en/articles/9519177-how-can-i-create-and-manage-projects))                             |
| XML tags ajudam Claude a interpretar prompts complexos                            | Confirmado em docs oficiais da Anthropic; sem data explícita no recorte, usar com data de acesso. ([Claude Platform Docs](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/multishot-prompting)) |
| Definir critérios de sucesso antes de refinar prompts                             | Confirmado em docs oficiais da Anthropic; sem data explícita no recorte, usar com data de acesso. ([Claude Platform Docs](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview))            |

Decisão: **prompt corrigido pronto para execução**.

# Claude Opus 4.8 Deep Guide diz:

**Conflito de interesse — mantido (Regra 7).** Objeto continua sendo produto Claude (Projects); sigo sem certificar claims de produto. E mantenho coerência com o turno anterior: roteei a verificação de produto para *fora de mim* — então não vou agora verificá-la eu mesmo só porque o ChatGPT trouxe datas. Fazer isso seria Bias \#7 (auto-auditoria branda) na prática, não só na retórica.

------------------------------------------------------------------------

## Veredito

Duas coisas convergiram e uma regrediu. Separadas:

**1. Prompt-mestre: CONVERGIDO. Stop Rule disparada (Regra 1).** ChatGPT aceitou as 3 correções e o artefato resultante é idêntico ao que prescrevi: esqueleto XML preservado, auto-homologação removida *de dentro do artefato*, constraint de fonte datada adicionada. Os dois motores atribuídos a esta tarefa (Matriz: *prompt engineering = ChatGPT → Claude*) convergem no mesmo artefato. **Refinamento do prompt está encerrado.** Pedir nova rodada de prompt agora seria anti-meta-trabalho (Regra 2). Executar.

**2. Regressão no wrapper — não no artefato.** O ChatGPT reintroduziu uma seção "4) Auditoria (Quality Gate)" e, dentro dela, **autocertificou os próprios claims de produto como "Confirmado", com datas (16 mar. 2026 / 28 mai. 2026) que não têm URL, título de documento nem qualquer fonte recuperável.**

Distinção que importa para ser justo:

- *Reportar o patch aplicado* ("removi o bloco, adicionei a constraint") → **OK**, é report ao orquestrador.
- *Marcar os próprios fatos como "Confirmado \[data\]"* → **violação.** O motor que produziu o claim não é o validador do claim.

Uma data sem URL recuperável **não satisfaz a Regra 6** (data obrigatória exige *fonte* datada, não uma string de data). Pelo princípio fail-closed do corpus ("preferir 'fonte não encontrada' a referência duvidosa"), isto **rebaixa**, não promove. O artefato ganhou aparência de Fato A sem a substância — é mais perigoso que o output do turno 1, porque parece resolvido.

Isto bate exatamente com a assinatura do **Bias \#8** (confabulação de tarefa + autocertificação) que o Manual hoje registra só para o Gemini. Apareceu aqui no ChatGPT, sob disfarce de Evidence Ledger. Vale logar como extensão de assinatura de viés a um novo motor.

------------------------------------------------------------------------

## Evidence Ledger — após o "verifiquei agora" do ChatGPT

|                                                                    |                                            |                                                             |
|--------------------------------------------------------------------|--------------------------------------------|-------------------------------------------------------------|
| **Claim**                                                          | **Status alegado pelo ChatGPT**            | **Status real (auditado)**                                  |
| Projects têm project knowledge / instructions                      | Confirmado, Help Center 16/03/2026         | **B** — data sem URL recuperável; não certificável          |
| Project instructions aplicam-se aos chats do projeto               | Confirmado, Help Center 16/03 + 28/05/2026 | **B** — idem                                                |
| Contexto não compartilhado entre chats salvo via project knowledge | Confirmado, mas "feature volátil"          | **C** — date string sem fonte + categoria volátil (Regra 5) |
| XML tags ajudam em prompts complexos                               | Confirmado, docs (sem data)                | **B** — admite que não tem data; fica B                     |
| Critérios de sucesso antes de refinar                              | Confirmado, docs (sem data)                | **B** — idem                                                |

Nenhum claim sobe para A com o que foi entregue. O "Confirmado" do ChatGPT é autocertificação não-recuperável → downgrade automático.

------------------------------------------------------------------------

## Decisão de roteamento (binária)

- **Prompt-mestre corrigido: EXECUTAR.** Convergência atingida, Stop Rule fechada, sem refinamento adicional. Remover do material a seção "4) Auditoria (Quality Gate)" — ela não vai junto.
- **Claims de produto: NÃO confirmados.** Permanecem B/C. O passe datado externo continua obrigatório e agora mais necessário, porque há risco de data autossuprida em jogo.
- **Spec do passe externo (define o que ele tem de devolver, não executo eu — Regra 7):** Perplexity ou web contra o Help Center / docs reais, retornando **URL + data verificável** que confirme (a) existência dos artigos de 16/03 e 28/05/2026 e (b) que dizem o que o ChatGPT alega. Sem URL → marcar *fonte não encontrada* (fail-closed), não "Confirmado".
- **Execução do guia:** mesma COI. Quem quer que gere o guia sobre Projects, os fatos de produto dentro dele passam pelo mesmo passe datado externo antes de virarem A.

Não escalo para 3º motor: risco baixo, Matriz pede 2 IAs, e elas convergiram.

------------------------------------------------------------------------

## Entradas de governança (colar no Manual)

**Log — turno 2, patch aceito + regressão.** ChatGPT aplicou corretamente as correções (a) auto-homologação fora do artefato e (b) constraint de fonte datada; artefato convergiu com Claude → Stop Rule disparada, refinamento de prompt encerrado. **Regressão:** reintroduziu wrapper de auto-auditoria e autocertificou 5 claims de produto como "Confirmado \[data\]" sem URL recuperável → viola Regra 6 (data ≠ fonte datada) e Regra anti-autoauditoria performática. Fail-closed: todos rebaixados a B/C. Verificação de produto permanece roteada a passe externo (Regra 7), com spec exigindo URL+data.

**Assinatura de viés — extensão.** Bias \#8 (confabulação + autocertificação), até agora logado só para Gemini, observado no ChatGPT: datas de fonte surgiram apenas no momento da contestação, sem URL, sob rótulo de Evidence Ledger. Registrar como padrão cross-engine: *autocertificação de fato volátil disfarçada de ledger* não é exclusiva de um motor.

# Tab 2

You are a senior Claude workspace architect and prompt engineering advisor.

I want to learn the best way to create and organize Claude Projects, with special focus on writing effective Project Instructions.

\<context\>

I use Claude Projects to keep work organized across multiple chats.

I want each Project to have clear instructions, useful knowledge files, consistent behavior, and reusable workflows.

Assume I am a practical user, not a developer, unless technical details are necessary.

\</context\>

\<task\>

Create a practical guide for designing high-quality Claude Projects.

Focus especially on how to write Project Instructions that Claude will follow reliably across chats.

\</task\>

\<requirements\>

Please cover:

1\. What belongs in a Claude Project versus what belongs in a normal chat.

2\. How to decide when to create a new Project.

3\. How to structure Project Instructions.

4\. What to put in the Project Knowledge base.

5\. How Project Instructions should differ from uploaded knowledge files.

6\. Common mistakes when writing Project Instructions.

7\. A reusable Project Instructions template.

8\. Three concrete examples:

   - a writing/content project

   - a research/project-analysis project

   - a coding/product-development project

9\. A checklist I can use before finalizing a Claude Project.

10\. A simple testing method to verify whether the Project Instructions work well.

\</requirements\>

\<instruction_design_rules\>

When explaining Project Instructions, include guidance for:

\- role and expertise Claude should adopt

\- project goal

\- audience

\- preferred output formats

\- tone and style

\- source-of-truth hierarchy

\- how Claude should handle missing information

\- what Claude should never do

\- how Claude should ask clarifying questions

\- how Claude should use project knowledge

\- how Claude should handle uncertainty

\</instruction_design_rules\>

\<output_format\>

Use the following structure:

\# Executive Summary

Briefly explain the core principles.

\# Best Practices for Claude Projects

Give practical guidance.

\# How to Write Project Instructions

Explain the anatomy of strong instructions.

\# Reusable Project Instructions Template

Provide a copy-paste template with placeholders.

\# Examples

Provide three complete example Project Instructions.

\# Common Mistakes

List mistakes and how to fix them.

\# Testing Checklist

Give a checklist and 5 test prompts I can run inside the Project.

\# Final Recommendation

Give a concise recommended workflow for creating any new Claude Project.

\</output_format\>

\<constraints\>

Do not give vague advice.

Do not assume undocumented product features.

If a detail may depend on Claude plan, account type, product version, workspace settings, or current feature availability, say so explicitly.

Any product-fact claim, including usage limits, knowledge-base behavior, cross-chat context, plan/tier gating, memory, sharing, or project availability, must carry a dated source reference from the Anthropic/Claude Help Center or official docs. If no dated source is available, label the claim as unverified.

Prioritize practical instructions I can copy, edit, and use immediately.

\</constraints\>
