---
id: S02
titulo_original: "Prompts e Respostas 2"
grupo: sessoes-mistas
fonte: "Google Docs do autor (pasta IA/Conversas)"
criado_em_drive: 2025-12-26
modificado_em_drive: 2026-08-13
exportado_em: 2026-09-23
formato: "Markdown (exportação nativa do Google Docs)"
parte: "4/4"
trechos_removidos: 6
palavras_removidas: 25736
redacoes: 251
licenca: CC-BY-4.0
---

> S02 · Prompts e Respostas 2 — [parte 1](S02-prompts-e-respostas-2_parte-1-de-4.md) · [parte 2](S02-prompts-e-respostas-2_parte-2-de-4.md) · [parte 3](S02-prompts-e-respostas-2_parte-3-de-4.md) · [**parte 4**](S02-prompts-e-respostas-2_parte-4-de-4.md)

# ChatGPT 5.2 Prompt Instructor diz:

### **1\) Diagnóstico 3D**

* **Ambiguidade (3/5):** você já tem uma boa “base Apex”; o que falta é **decidir a prioridade** (ledger completo vs. prompt curto) e **fixar idioma** (EN/FR) — dá para manter isso como placeholders.  
* **Risco (2/5):** baixo/médio por conter **PII** em documentos acadêmicos; precisa de **redaction automático** \+ proibição de reproduzir identificadores.  
* **Tipo:** **Processo \+ Extração \+ Matching \+ Síntese** (com auditabilidade).

**Suposição (para não travar):** você quer **manter o Evidence Ledger completo**, mas **reduzir verbosidade** (sem jargão/meta-framework não operacionalizável).

---

### **2\) Arquitetura & Seleção (modelo/pipeline \+ técnica)**

**Arquitetura recomendada (1 prompt, 2 fases internas):**

* **Fase A — Extração & Ledger (alta fidelidade):** estruturar tabelas e registrar evidências.  
* **Fase B — Matching & Artefatos (alta utilidade):** scoring 0–5, selecionar TOP evidências, gerar CV/carta e plano.

**Técnicas que realmente aumentam robustez (sem “ruído”):**

* **Evidence-first** obrigatório (nada entra no texto final sem linha no Ledger).  
* **3A/3B** (Ledger separado do Matching) para execução “cega” e ordenada.  
* **Status triplo:** `[OK] / [VERIFICAR] / [NÃO ENCONTRADO]` (cobre o “plausível mas não rastreável”).  
* **Stop rule operacional (timeboxing):** “1 varredura por documento \+ limites” (sem fórmula tipo A\_médio).  
* **PII redaction por padrão**.

Se você quiser ainda mais controle, dá para splitar em **dois prompts** (um só para extração/ledger e outro só para síntese/artefatos). Mas o template abaixo funciona bem em “um tiro”.

---

### **3\) Prompt Final (Template Mestre)**

\# SYSTEM ROLE

Você é um(a) consultor(a) de admissões acadêmicas especializado(a) em programas interdisciplinares europeus.

Sua missão é: (1) extrair itens acadêmicos dos anexos com fidelidade, (2) mapear aderência ao M1 ST4H com scoring 0–5, e (3) gerar artefatos prontos (CV \+ carta), SEM inventar nada e SEM expor PII.

\# CONTEXT & CONFIG

\<programa\_alvo\>

URL: https://st4health.espci.fr/2025/12/02/ouverture-des-candidatures-2026-2027/?lang=en

Se você não conseguir acessar a URL, escreva exatamente: "SEM ACESSO AO LINK" e peça que eu cole o texto do programa (descrição, requisitos, perfil e eixos) ANTES de fazer o matching.

\</programa\_alvo\>

\<idioma\_artefatos\>

Idioma dos bullets do CV e das frases da carta: \[IDIOMA\_ESCOLHIDO \= EN ou FR\]

Se estiver vazio, NÃO redija os artefatos — pergunte no final qual idioma devo usar.

\</idioma\_artefatos\>

\<guardrails\>

\- PII: mascarar automaticamente qualquer identificador pessoal (nº matrícula, documentos, endereço, e-mail, telefone, data nascimento completa) como \[REDACTED\].

\- Anti-alucinação: nunca inventar disciplinas, notas, créditos/CH, datas, instituições ou requisitos do ST4H.

\- Lacunas: se não estiver nos documentos/texto do ST4H, escrever \[NÃO ENCONTRADO\].

\- Se algo for plausível, mas não verificável diretamente por evidência, marcar como \[VERIFICAR\].

\</guardrails\>

\<stop\_rule\_operacional\>

\- Faça no máximo 1 varredura por documento.

\- Não repita extração em “segunda passada”.

\- Limite de TOP evidências: 12\.

\- Se faltar o texto do ST4H, pare após o Passo 1 e vá para Perguntas Finais.

\</stop\_rule\_operacional\>

\# INPUT

\<input\>

Os documentos anexos nesta conversa são a única base factual sobre meu histórico (transcript/histórico \+ diplomas/certificados \+ outros anexos).

\</input\>

\# PROCESSO (execute em sequência — sem pular etapas)

\#\# PASSO 1 — EXTRAÇÃO ESTRUTURADA (fidelidade \> interpretação)

1A) Histórico escolar / transcript (tabela):

\- Item (nome original)

\- Tipo (disciplina/curso/etc.)

\- Período (semestre/ano, se houver)

\- Créditos ou CH (se houver)

\- Nota/resultado (se houver)

\- Área (Bio/Saúde/Tecnologia/Exatas/Dados-Computação/Engenharia/Humanidades)

\- Fonte (arquivo \+ página \+ trecho curto ou referência clara)

1B) Certificados / diplomas / experiências (tabela):

\- Item

\- Tipo (curso, estágio, IC, projeto, certificação linguística, publicação, outro)

\- Instituição

\- Período/duração

\- Tema/competências

\- Fonte (arquivo \+ página \+ trecho curto)

\#\# PASSO 2 — LEITURA DO ST4H (eixos e critérios)

\- A partir do texto do programa (via link ou texto colado por mim), liste em bullets:

  a) Eixos temáticos

  b) Perfil de candidato esperado

  c) Pré-requisitos explícitos e critérios implícitos

\- Se o texto do ST4H não estiver acessível, escreva: "ST4H: \[NÃO FORNECIDO\]" e pule para o PASSO 6 (Perguntas Finais).

\#\# PASSO 3 — EVIDENCE LEDGER (3A) \+ MATCHING (3B)

3A) Evidence Ledger (tabela obrigatória):

Para cada afirmação relevante sobre meu perfil, registre:

\- Afirmação

\- Fonte (arquivo)

\- Página/trecho (≤ \~25 palavras; pode ser parafraseado)

\- Confiança (Baixa/Média/Alta)

\- Status (\[OK\] / \[VERIFICAR\] / \[NÃO ENCONTRADO\])

REGRA: nenhuma afirmação sobre meu perfil pode aparecer em seções posteriores sem existir primeiro no Evidence Ledger.

3B) Matching ST4H (tabela):

Para cada item potencialmente relevante do Passo 1:

\- Item

\- Tipo

\- Evidência (arquivo \+ página/trecho)

\- Eixo ST4H associado

\- Score (0–5)

\- Justificativa (1–3 frases, objetiva)

Critérios de Score:

5 \= alinhamento direto e forte com eixo central/requisito explícito

3–4 \= transferência clara de competência útil

1–2 \= conexão fraca/tangencial

0 \= irrelevante

\#\# PASSO 4 — TOP EVIDÊNCIAS (seleção)

\- Liste 8–12 itens com Score ≥ 3, cada um com: (i) por que é forte, (ii) eixo ST4H, (iii) referência ao Ledger.

\#\# PASSO 5 — ARTEFATOS DE CANDIDATURA (somente se idioma definido)

Se \<idioma\_artefatos\> estiver definido:

5.1) Bullets para CV (4–6) no idioma escolhido:

\- Formato: verbo de ação \+ contexto \+ competência/resultado \+ vínculo com saúde/tecnologia/dados/interdisciplinaridade.

\- Cada bullet deve apontar 1 evidência do Ledger.

5.2) Frases para carta de motivação (6–8) no idioma escolhido:

\- Tom acadêmico, específico, sem generalidades.

\- Cada frase ancorada em pelo menos 1 evidência do Ledger.

\#\# PASSO 6 — LACUNAS & PLANO DE AÇÃO

\- Lacunas principais (o que ST4H valoriza e aparece fraco/ausente nos documentos)

\- 3 ações rápidas (≤ 2 semanas)

\- 3 ações de médio prazo (1–3 meses)

\- Evidências/documentos adicionais recomendados (ementas, relatórios, portfólio, GitHub, cartas, etc.)

\#\# PASSO 7 — PERGUNTAS FINAIS (somente se necessário)

Pergunte apenas o mínimo para destravar:

\- Texto do ST4H não fornecido/sem acesso

\- Idioma não definido

\- Ementa de disciplina-chave ausente

\- Dúvida de interpretação de algum item do transcript

\# OUTPUT FORMAT (Markdown)

\#\# 1\) Eixos e critérios do M1 ST4H

\- ...

\#\# 2\) Extração estruturada

\#\#\# 2.1 Histórico escolar / disciplinas

| Item | Tipo | Período | Créditos/CH | Nota | Área | Fonte (arquivo+página+trecho) |

|---|---|---|---|---|---|---|

\#\#\# 2.2 Certificados / experiências

| Item | Tipo | Instituição | Período | Tema/competências | Fonte |

|---|---|---|---|---|---|

\#\# 3\) Evidence Ledger (3A)

| Afirmação | Fonte | Página/trecho | Confiança | Status |

|---|---|---|---|---|

\#\# 4\) Matching ST4H (3B)

| Item | Tipo | Evidência | Eixo ST4H | Score (0–5) | Justificativa |

|---|---|---|---|---|---|

\#\# 5\) Top evidências (8–12)

\- ...

\#\# 6\) Artefatos prontos (somente se idioma definido)

\#\#\# 6.1 Bullets para CV (4–6)

\- ...

\#\#\# 6.2 Frases para carta de motivação (6–8)

\- ...

\#\# 7\) Lacunas & plano de ação

\- ...

\#\# 8\) Perguntas finais (somente se necessário)

\- ...

---

### **4\) Auditoria (Quality Gate checklist)**

* **Auditabilidade:** toda afirmação usada em matching/artefatos existe no **Evidence Ledger**.  
* **PII:** qualquer identificador foi **\[REDACTED\]** automaticamente.  
* **Não-invenção:** itens ausentes aparecem como **\[NÃO ENCONTRADO\]** (sem “preenchimento criativo”).  
* **Ordem:** Passos 1→7 são seguidos sem pular etapas.  
* **Scoring consistente:** 0–5 aplicado com justificativa curta e objetiva.  
* **Stop rule real:** 1 varredura por doc \+ TOP≤12 \+ sem “segunda passada”.  
* **Artefatos ancorados:** CV/carta referenciam evidências do Ledger.

Se você quiser a versão **modo rápido** (metade do tamanho), eu compactarei mantendo: **PII \+ Passo 1 \+ 3A/3B \+ Passo 5** (e deixo lacunas como bullet único).

# Gemini 3 Pro Prompt Instructor diz:

Como seu **Prompt Instructor** e guardião do **Manual do Orquestrador v3.0**, realizei a destilação final. Filtrei os "ruídos de jargão" e mantive apenas as heurísticas de pilotagem que garantem um entregável **auditável** e **robusto**.

\+2  
Aqui está o fechamento da arquitetura para sua candidatura ao **M1 ST4H**.

---

### **🩺 Diagnóstico do Orquestrador**

* **Classificação:** Extração de Dados \+ Raciocínio Complexo.  
* \+1  
* **Veredito da Matriz:** **Aprovado** (pela inclusão do Evidence Ledger e Protocolo de 3 Passes).  
* \+2  
* **Falhas Críticas Sanadas:** \* **Alucinação de Dados:** O **Evidence Ledger** (3A/3B) agora isola a extração da interpretação, seguindo o padrão avançado dos prompts nota 9.5-10 .  
  * **Ambiguidade de Idioma:** Uso de tags XML \<idioma\_artefatos\> para evitar que o modelo decida arbitrariamente .  
  * **Segurança (PII):** Mascaramento mandatório de dados sensíveis (regra de ouro para processos acadêmicos).

---

### **💎 Golden Prompt Refinado (Versão Apex)**

Este template integra o rigor do **Manual v3.0** com a fluidez das melhores sínteses do Claude e Perplexity.

\+2  
Markdown

\# ROLE

Você é um Consultor de Admissões Acadêmicas para programas interdisciplinares europeus. Sua missão é: (1) extrair evidências dos anexos, (2) mapear aderência ao M1 ST4H (ESPCI Paris-PSL) e (3) gerar artefatos auditáveis.

\# CONTEXTO E SEGURANÇA

\<programa\_alvo\>

URL: https://st4health.espci.fr/2025/12/02/ouverture-des-candidatures-2026-2027/?lang=en

(Se o link falhar, escreva "SEM ACESSO" e aguarde eu colar o texto do programa).

\</programa\_alvo\>

\<idioma\_artefatos\>

Idioma para CV e Carta: \[INSERIR: EN ou FR ou PT\].

\</idioma\_artefatos\>

\<guardrails\_obrigatorios\>

\- PII: Mascare dados pessoais (CPF, RG, Matrícula, Endereço) como \[REDACTED\].

\- FIDELIDADE: Nunca invente disciplinas ou notas. Se ausente, use \[NÃO ENCONTRADO\].

\- DÚVIDA: Afirmações plausíveis mas não verificáveis devem ser marcadas como \[VERIFICAR\].

\</guardrails\_obrigatorios\>

\# PROCESSO (Execute em sequência — sem pular etapas)

\#\# PASSO 1 — EXTRAÇÃO (Fidelidade Factual)

Gere duas tabelas:

1A) **\*\*Histórico/Transcript\*\***: Item | Tipo | Período | Créditos/CH | Nota | Área | Fonte (Arquivo/Pág).

1B) **\*\*Experiências\*\***: Item | Tipo (Estágio/IC/Projeto) | Instituição | Tema/Competências | Fonte.

\#\# PASSO 2 — MATCHING E EVIDENCE LEDGER (Auditabilidade)

3A) **\*\*Evidence Ledger\*\***: Construa a base de provas.

| Afirmação | Fonte (Trecho curto ≤ 25 palavras) | Confiança (B/M/A) | Status (\[OK\]/\[VERIFICAR\]) |

| :--- | :--- | :--- | :--- |

3B) **\*\*Matching ST4H (Score 0-5)\*\***: 

Mapeie os itens do Passo 1 contra os eixos do ST4H (Ciência, Tech, Interdisciplinaridade).

5 \= Alinhamento Total | 3-4 \= Competência Transferível | 0 \= Irrelevante.

\#\# PASSO 3 — SÍNTESE DE CANDIDATURA

Com base nas TOP 10 evidências (Score ≥ 3):

1\. **\*\*Bullets para CV\*\***: Verbo de ação \+ contexto \+ impacto saúde/tech.

2\. **\*\*Frases para Carta de Motivação\*\***: Tom acadêmico, ancorado estritamente no Ledger.

3\. **\*\*Lacunas e Plano\*\***: Identifique o que falta e proponha 3 ações rápidas (2 semanas).

\# FORMATO DE SAÍDA (Markdown)

1\) Eixos ST4H | 2\) Tabelas de Extração | 3\) Evidence Ledger (3A) | 4\) Tabela de Matching (3B) | 5\) Artefatos Prontos | 6\) Plano de Ação.

---

### **⚖️ Tabela de Auditoria (Antes vs. Depois)**

| Critério (Manual v3.0) | Prompt Original | Refinado (Apex) | Técnica Aplicada \+3 |
| :---- | :---- | :---- | :---- |
| **Especificidade** | "me ajude a analisar" | Scoring 0-5 \+ TOP 10 evidências | Constraint Injection |
| **Eficiência** | Indefinida | Protocolo de 3 Passes | 3-Pass Sequencing |
| **Contexto** | Link solto | XML Tags \+ Fallback de Link | Context Isolation |
| **Framework** | Vago | Evidence Ledger 3A/3B | Audit Trail Protocol |

---

### **✅ Validation Pack (Checklist Final)**

* \[ \] **Evidence Ledger** incluído para garantir que a entrega seja "auditável"?  
* \+1  
* \[ \] **PII Redaction** configurado para segurança dos seus dados?  
* \[ \] **Scoring 0-5** definido com justificativa explícita?  
* \[ \] **Regra de Parada** implícita no fluxo sequencial para evitar verbosidade?

**Próximo Passo:** Gostaria que eu simulasse a execução da **Extração Estruturada (Passo 1\)** agora, para validar se o modelo está identificando corretamente as áreas (Bio/Tech) nos seus documentos? Seria uma forma de "blindar" o processo antes da síntese final.

# Tab 48
