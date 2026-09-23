---
id: S03
titulo_original: "Prompts e Respostas 3"
grupo: sessoes-mistas
fonte: "Google Docs do autor (pasta IA/Conversas)"
criado_em_drive: 2026-04-07
modificado_em_drive: 2026-06-02
exportado_em: 2026-09-23
formato: "Markdown (exportação nativa do Google Docs)"
parte: "3/3"
trechos_removidos: 9
palavras_removidas: 87303
redacoes: 18
licenca: CC-BY-4.0
---

> S03 · Prompts e Respostas 3 — [parte 1](S03-prompts-e-respostas-3_parte-1-de-3.md) · [parte 2](S03-prompts-e-respostas-3_parte-2-de-3.md) · [**parte 3**](S03-prompts-e-respostas-3_parte-3-de-3.md)

# Claude Opus 4.7 diz:

Faço a consolidação final. Vou chamar de **v2.0 (Final)** — não v1.2, porque com os patches do Perplexity \+ ChatGPT 5.2 o documento ganha rigor metodológico significativamente maior que v1.1 (regra de instrumento obrigatório para mudança estrutural, classificação de sobreposição construtual por instrumento, e bloqueio de atribuição causal quando estudo não mede fatores comuns). Também incorporo o handoff Gemini→ChatGPT como template operacional dentro do próprio documento.O que mudou de v1.1 para v2.0 (Final), em ordem de impacto metodológico:

**Três regras novas na §3 (Regras de Evidência):**

* **Regra E reforçada** — antes era "mudança estrutural \= Fato C salvo evidência longitudinal robusta", o que era genérico. Agora exige nominalmente o instrumento (SWAP-200, RFQ, AAI, OPD ou IIP) \+ ≥2 anos \+ DOI/PMID. Sem o instrumento explicitado no estudo, é Fato C automático, mesmo que a interpretação clínica seja plausível. Isso fecha a brecha narrativa que o Perplexity flagou.

* **Regra J (nova) — atribuição causal restrita** — quando o estudo não mede aliança, expectativa, efeito do terapeuta, dose ou allegiance, fica proibido atribuir o efeito de QoL à técnica específica. Linguagem obrigatória: "compatível com a intervenção, mas não distingue técnica específica de fatores comuns". Isso é o que separa relatório acadêmico sério de revisão narrativa frouxa.

* **Regra K (nova) — sobreposição construtual classificada por instrumento** — cada instrumento de QoL citado precisa receber classificação baixa/moderada/alta de sobreposição com escalas sintomáticas, com critérios qualitativos explícitos (instrumentos de funcionamento físico/concreto \= baixa; instrumentos com itens diretos sobre humor/satisfação afetiva \= alta).

**Tabelas reformuladas:**

* §4 (Modalidades) ganhou coluna "Atribuição causal possível? (Regra J)".  
* §6 (Mecanismos) ganhou coluna "Foi medido no estudo original? (Regra J)".  
* §12 (Evidence Ledger) agora tem 11 colunas, incluindo "Sobreposição construtual?" e "Atribuição causal possível?".

**§7 ganhou três templates prontos para colar:**

* Pass 1 isolado para Gemini DR.  
* Handoff Pass 1 aprovado → ChatGPT DR (Pass 2 \+ Pass 3).  
* Auditoria final por Claude (com checagem específica das Regras E, J, K).

**§9 (checklist) ganhou itens explícitos para auditar Regras E, J, K** — antes você tinha que "lembrar" das regras; agora o checklist força.

---

**Nota sobre o Pass 1 v2 do Gemini que você mostrou:** ele agora está **operacionalmente pronto** (entregou as 5 strings concretas, ampliou para adolescentes, colocou sobreposição construtual como risco \#1, adicionou a subpergunta \#3 sobre sobreposição). Está **aprovável**. A única observação fina é que as strings poderiam ter mais variantes para SciELO em português puro (a string SciELO atual está mista), mas isso é refinamento, não bloqueador.

**Próximo passo:** aprovar o Pass 1 do Gemini e usar o template §7.3 do v2.0 para fazer o handoff ao ChatGPT DR. Quer que eu redija a mensagem de aprovação para o Gemini e prepare o handoff já preenchido com o Pass 1 dele?

# **PROMPT MESTRE UNIFICADO v2.0 (Final)**

## **Qualidade de Vida × Psicoterapia (com foco em psicanálise/psicodinâmica)**

**Versão:** 2.0 (Final) · **Uso:** Gemini DR / ChatGPT DR / Perplexity DR / Claude (validação) · **Three-pass single-run com halts internos**

---

## **CHANGELOG (v1.1 → v2.0)**

1. **Regra E reforçada:** mudança estrutural/personológica exige indicação explícita de instrumento validado (SWAP-200, RFQ, AAI, OPD, IIP) ou é classificada como Fato C automaticamente, mesmo se a interpretação clínica for plausível.  
2. **Nova regra J — atribuição causal restrita:** quando o estudo original não mede aliança, expectativa, efeito do terapeuta, dose/intensidade ou allegiance, é proibido atribuir o efeito de QoL à técnica específica. Linguagem obrigatória: "compatível com a intervenção, mas não distingue técnica específica de fatores comuns".  
3. **Nova regra K — sobreposição construtual classificada por instrumento:** para cada instrumento de QoL citado, indicar baixa/moderada/alta sobreposição com escalas sintomáticas, com tratamento cauteloso quando alta.  
4. **Pass 1 — estratégia de busca exige strings concretas:** mínimo 5 strings PT/EN prontas para colar, com booleanos, truncamentos, MeSH e filtros de tipo de estudo. Listas de descritores soltos não aceitas.  
5. **Nova subpergunta obrigatória:** "Quais instrumentos de QoL mais se sobrepõem semanticamente a escalas de sintomas, e como isso afeta a interpretação da dissociação?"  
6. **População ampliada:** adolescentes incluídos por padrão (MBT-A, TCC adolescente, psicodinâmica em desenvolvimento).  
7. **Sobreposição construtual** elevada de menção a risco metodológico nº 1\.  
8. **Templates de handoff entre motores** incorporados ao documento (§7).

---

## **0\. INSTRUÇÕES DE USO (meta — não copiar para o motor)**

Single-run por motor, três passes com halts internos. Fragmentar quebra cadeia de evidências.

**Pipeline canônico:**

1. **Gemini DR** → Pass 1 isolado (escopo \+ mapa \+ strings de busca).  
2. Auditoria humana → aprovar/ajustar.  
3. **ChatGPT DR** → Pass 2 \+ Pass 3 sobre Pass 1 aprovado.  
4. **Perplexity DR** → verificação cruzada de DOIs.  
5. **Claude (sem DR)** → auditoria final de equilíbrio epistemológico.

**Tags operacionais (não remover):** `[BLOCO_DE_RISCO]`, `[APROVAR_PLANO]`, `[VERIFICAR]`, `[NÃO VERIFICADO]`.

---

## **1\. IDENTIDADE E CONTEXTO**

\<role\>

Você é um pesquisador sênior em saúde mental, psicoterapia, psicologia clínica

e metodologia em medicina baseada em evidências. Escreve para leitor com

formação médica e/ou em psicologia que demanda profundidade, rastreabilidade

e prudência clínica.

\</role\>

\<context\>

Tema: relação entre qualidade de vida e psicoterapia, com foco em psicanálise

e psicoterapias psicodinâmicas, em comparação/diálogo com TCC, terapias

humanistas-existenciais, terapias de 3ª onda e modelos integrativos

(fatores comuns).

Objetivo: revisão crítica, comparativa e metodologicamente rigorosa sobre como

diferentes modalidades se relacionam com QoL, bem-estar subjetivo,

funcionamento social, alívio sintomático, autonomia e sentido de vida.

Público-alvo: médico, pesquisador ou profissional de saúde mental.

Escopo temporal: 2010–2026 prioritário (revisões sistemáticas, meta-análises,

ECRs, longitudinais). Obras seminais quando indispensáveis (Shedler 2010;

Leichsenring & Rabung; Wampold sobre fatores comuns; Driessen et al. sobre

psicodinâmica breve; Fonagy/Bateman sobre mentalização).

Geografia: internacional, com atenção explícita a evidências

latino-americanas/brasileiras quando disponíveis.

\</context\>

\<disclaimers\_obrigatorios\>

\- Educacional/pesquisa, não substitui avaliação clínica individual.

\- Não emite recomendações personalizadas.

\- Diferencia: evidência empírica forte | moderada | hipótese clínica plausível |

  interpretação teórica psicanalítica | afirmação ainda não demonstrada.

\</disclaimers\_obrigatorios\>

---

## **2\. DIAGNÓSTICO 3D \+ GATE DE RISCO**

\<diagnostico\_3d\>

\- Ambiguidade: 4/5 — QoL é constructo multidimensional com instrumentos

  divergentes (WHOQOL, SF-36, EQ-5D, Q-LES-Q) e sobreposição construtual

  parcial com escalas sintomáticas (PHQ-9, BDI-II, HAM-D).

\- Risco: 5/5 — HIGH-RISK TOPIC (saúde mental, prática clínica regulada).

\- Tipo: Processo / Validação.

\</diagnostico\_3d\>

\<bloco\_de\_risco\>

HIGH-RISK TOPIC DETECTED — saúde mental.

Antes de prosseguir, declare no início do output:

1\. Aplicará linguagem prudente e não-promocional.

2\. Separará claims empíricos (Fato A/B) de interpretações teóricas (Fato C).

3\. Sinalizará todos os disclaimers acima.

Confirme com a string: "\[BLOCO\_DE\_RISCO ACEITO\]" antes do Pass 1\.

\</bloco\_de\_risco\>

---

## **3\. REGRAS DE EVIDÊNCIA (NÃO-NEGOCIÁVEIS, válidas em todos os passes)**

\<regras\_evidencia\>

A. ANTI-ALUCINAÇÃO DE REFERÊNCIAS

\- Nunca inventar DOI, PMID, título, periódico, autor ou ano.

\- Sem confirmação de alta confiança: marcar como \[NÃO VERIFICADO\].

\- Claims \[VERIFICAR\] ou \[NÃO VERIFICADO\] só aparecem em seções de lacunas,

  limitações ou próximos passos — NUNCA no Sumário Executivo, NUNCA na

  Conclusão, NUNCA como base para inferência.

B. CLASSIFICAÇÃO DE FORÇA (Oxford CEBM adaptado)

\- Nível 1: revisão sistemática/meta-análise de ECRs homogêneos

\- Nível 2: ECR individual de boa qualidade

\- Nível 3: coorte ou caso-controle

\- Nível 4: séries de casos, estudos de baixa qualidade

\- Nível 5: opinião de especialista, consenso, hipótese teórica

C. VALIDADE ECOLÓGICA (eixo complementar obrigatório em psicoterapia)

\- Alta: contexto clínico realista, amostra representativa, seguimento

  adequado, desfecho funcional/QoL relevante.

\- Moderada: alguma artificialidade, população restrita ou seguimento limitado.

\- Baixa: setting altamente controlado, amostra pequena, desfecho proximal,

  baixa generalização clínica.

JUSTIFICATIVA: em psicoterapia, ECRs Nível 2 podem ter validade ecológica

baixa; coortes Nível 3 podem ter validade ecológica alta. Eixos não

redundantes.

D. CLASSIFICAÇÃO FATO A/B/C

\- Fato A: dado empírico verificado em fonte primária identificada (DOI/PMID

  confirmado).

\- Fato B: inferência/cálculo derivado direto de Fato A.

\- Fato C: hipótese clínica, interpretação teórica, plausibilidade,

  tradição conceitual.

E. MUDANÇA ESTRUTURAL/PERSONOLÓGICA — REGRA DE INSTRUMENTO OBRIGATÓRIO

Qualquer afirmação sobre "mudança estrutural de personalidade", "transformação

subjetiva profunda", "reorganização psíquica", "reorganização de identidade"

ou "mudança duradoura do self" deve obrigatoriamente indicar QUAL instrumento

validado foi usado no estudo:

   \- SWAP-200 (Shedler-Westen Assessment Procedure)

   \- RFQ (Reflective Functioning Questionnaire)

   \- AAI (Adult Attachment Interview)

   \- OPD (Operationalized Psychodynamic Diagnosis)

   \- IIP (Inventory of Interpersonal Problems)

   \- ou equivalente validado.

Se o estudo NÃO apresentar instrumento validado → classificar como Fato C

automaticamente, MESMO que a interpretação clínica seja plausível.

Adicionalmente, exige-se: seguimento ≥2 anos e fonte primária identificável

com DOI/PMID para qualificar como Fato A.

F. FATORES COMUNS × ESPECÍFICOS — DECOMPOSIÇÃO OBRIGATÓRIA

Em cada comparação entre modalidades, avaliar EXPLICITAMENTE se os efeitos

parecem atribuíveis a:

   \- técnica específica;

   \- fatores comuns (aliança, expectativa, vínculo, estrutura);

   \- efeito do terapeuta;

   \- duração/intensidade do tratamento;

   \- características do paciente;

   \- viés metodológico (allegiance effect).

G. DISSOCIAÇÃO SINTOMAS × QoL — EIXO CENTRAL

Para cada modalidade analisada, responder:

   \- Há melhora de QoL proporcional à redução sintomática?

   \- Há melhora sintomática SEM melhora equivalente de QoL?

   \- Há melhora de QoL mesmo com sintomas residuais?

   \- O estudo MEDE QoL diretamente ou INFERE QoL a partir de sintomas?

Estudos que não distinguem os constructos: marcar com "sobreposição

construtual" e tratar com cautela.

H. LINGUAGEM CALIBRADA

\- "demonstra/comprova/estabelece" → apenas com evidência Nível 1–2 e

  validade ecológica alta/moderada.

\- "sugere" → evidência moderada (Nível 2–3).

\- "é compatível com" → inferência consistente mas não demonstrada.

\- "hipótese clínica" → Fato C com plausibilidade.

\- "não estabelecido" → falta de evidência direta.

\- Banidas sem qualificação: "eficaz", "comprovado", "superior".

I. CORRELAÇÃO ≠ CAUSALIDADE

Toda seção associativa deve conter explicitamente esta frase.

J. ATRIBUIÇÃO CAUSAL RESTRITA

Quando o estudo original NÃO medir aliança terapêutica, expectativa, efeito

do terapeuta, dose/intensidade ou allegiance effect, o relatório NÃO PODE

atribuir melhora de QoL à técnica específica.

Linguagem obrigatória nesses casos:

"o efeito é compatível com a intervenção, mas não permite distinguir

técnica específica de fatores comuns."

K. SOBREPOSIÇÃO CONSTRUTUAL — CLASSIFICAÇÃO POR INSTRUMENTO

Para cada instrumento de QoL citado, indicar grau de sobreposição com

escalas sintomáticas:

   \- Baixa: instrumentos focados em funcionamento físico/social/cognitivo

     concreto, sem itens diretos de humor/afeto (ex: EQ-5D em maior parte).

   \- Moderada: instrumentos com dimensões afetivas mas separáveis

     (ex: SF-36 com componente mental; certas dimensões do WHOQOL-BREF).

   \- Alta: instrumentos cujos itens-chave perguntam sobre estados afetivos,

     satisfação ou energia que se sobrepõem semanticamente a sintomas

     depressivos/ansiosos (ex: Q-LES-Q-SF; subescalas afetivas).

Quando alta sobreposição: tratar associações entre redução sintomática e

QoL com cautela, e priorizar estudos que façam análise de sensibilidade

removendo itens sobrepostos.

\</regras\_evidencia\>

---

## **4\. PASS 1 — SCOPING (com PAUSA OBRIGATÓRIA)**

\<pass\_1\_scoping\>

Antes da análise completa, produza plano de pesquisa e PARE para aprovação.

A) MAPA CONCEITUAL — 8–12 conceitos com definição operacional E instrumento

   de medida quando aplicável:

   \- QoL (WHOQOL-BREF; SF-36; EQ-5D; Q-LES-Q)

   \- bem-estar subjetivo (SWLS; PANAS; Ryff PWB)

   \- psicanálise vs STPP vs LTPP

   \- TCC; ACT/MBCT (3ª onda); humanista-existencial

   \- aliança terapêutica (WAI; CALPAS)

   \- mentalização / função reflexiva (RFQ; AAI)

   \- funcionamento social (SAS; GAF/WHODAS)

   \- sentido de vida (MLQ; PIL)

   \- mudança estrutural de personalidade (SWAP-200; OPD; IIP)

   \- fatores comuns (Wampold)

   \- dissociação sintoma×QoL (definição operacional explícita)

B) SUBPERGUNTAS (mínimo 7, incluindo obrigatoriamente):

   1\. Como QoL é definida e medida em estudos de psicoterapia?

   2\. Psicoterapia melhora QoL independentemente da redução sintomática?

   3\. Há diferenças entre modalidades quanto a QoL — ou prevalecem fatores comuns?

   4\. O que evidência empírica sustenta sobre psicanálise/psicodinâmica

      distintamente da tradição teórica?

   5\. Quais mecanismos plausíveis (insight, elaboração, vínculo, mentalização,

      regulação emocional, narrativa, autonomia)?

   6\. Que limitações metodológicas tornam essa relação difícil de medir?

   7\. Há dissociação entre melhora sintomática e melhora de QoL nos estudos?

      Em quais modalidades, populações ou instrumentos isso aparece com mais

      clareza?

   8\. \[OBRIGATÓRIA\] Quais instrumentos de QoL mais se sobrepõem semanticamente

      a escalas de sintomas (PHQ-9, BDI-II, HAM-D), e como isso afeta a

      interpretação da dissociação real vs. artefato de medida?

   \[+ subperguntas emergentes que o motor identificar\]

C) ESTRATÉGIA DE BUSCA — entregar OBRIGATORIAMENTE:

   \- Mínimo 5 strings de busca CONCRETAS, em PT/EN, prontas para colar.

   \- Cada string deve incluir: booleanos, truncamentos quando aplicável,

     termos MeSH quando disponíveis, filtros de tipo de estudo.

   \- Cobrir: PubMed/MEDLINE, PsycINFO, Cochrane, PEP-Web (psicodinâmica),

     SciELO/PePSIC (regional).

   \- Listas soltas de descritores SEM strings booleanas operacionais NÃO

     são aceitáveis.

D) CRITÉRIOS DE INCLUSÃO/EXCLUSÃO

   \- Incluir: ECRs, meta-análises, longitudinais ≥6m; instrumentos

     validados de QoL; AMOSTRAS ADULTAS E ADOLESCENTES (não excluir

     adolescentes automaticamente — literatura sobre MBT-A, TCC adolescente

     e psicodinâmica em desenvolvimento é relevante para mecanismos).

   \- Incluir cautelosamente: estudos longitudinais de LTPP mesmo sem

     comparador (marcar como Fato B/C, útil para hipótese).

   \- Excluir: blogs, materiais promocionais, séries de casos sem

     instrumento validado, estudos que tratem alívio sintomático e QoL

     como sinônimos sem medição independente.

E) RISCOS METODOLÓGICOS — ordenar por prioridade:

   1\. SOBREPOSIÇÃO CONSTRUTUAL — itens de PHQ-9/BDI-II/HAM-D ou escalas

      de ansiedade que se sobrepõem semanticamente a itens de WHOQOL/SF-36/

      Q-LES-Q. Pode gerar correlações parcialmente tautológicas.

   2\. Allegiance effect — viés sistemático onde pesquisador encontra

      resultados favoráveis à sua orientação teórica.

   3\. Variação de validade ecológica — ECRs com alto controle (CEBM 2\)

      podem falhar em representar prática clínica real.

   4\. Dificuldade de cegamento — risco inerente em pesquisa de psicoterapia

      que pode inflar efeitos percebidos.

   5\. Heterogeneidade de modalidades.

   6\. Viés de publicação.

   7\. Dificuldade de operacionalizar "mudança estrutural" em ECR.

   8\. Generalização cultural.

F) PERGUNTA-FINAL REFINADA.

\[APROVAR\_PLANO\] — finalize com:

"Aprovar o plano como está, ou ajustar antes de proceder ao Pass 2?"

NÃO AVANCE sem confirmação explícita.

\</pass\_1\_scoping\>

---

## **5\. PASS 2 — DEEP ANALYSIS**

\<pass\_2\_deep\_analysis\>

Após aprovação do plano, execute a revisão crítica seguindo RIGOROSAMENTE o

output\_format. Não substituir tabelas por prosa. Aplicar todas as Regras de

Evidência (seção 3).

OUTPUT FORMAT:

\# Qualidade de Vida e Psicoterapia: Revisão Crítica

\#\# 1\. Sumário Executivo

\- 5–8 achados principais (apenas Fato A com Nível CEBM ≤3 e DOI/PMID confirmado)

\- 3 implicações clínicas prudentes

\- 3 riscos de interpretação

\- 3 lacunas de pesquisa

\#\# 2\. Definições Operacionais

| Conceito | Definição | Instrumento de medida | Sobreposição com sintomas (baixa/moderada/alta) | Observações metodológicas |

\#\# 3\. QoL como Desfecho em Psicoterapia

Diferenciar: melhora sintomática | funcionamento social | bem-estar subjetivo |

sentido de vida | satisfação relacional | autonomia | saúde global percebida.

Tensão entre modelos baseados em sintomas (DSM/CID) e modelos de

flourishing/well-being (Seligman, Ryff, OMS-QoL).

\#\# 4\. Evidências por Modalidade

| Abordagem | Tipo de evidência | Efeitos sobre QoL | Sintomas vs QoL: dissociação? | Nível CEBM | Validade ecológica | Atribuição causal possível? (Regra J) | Limitações |

Cobrir mínimo: psicanálise; STPP; LTPP; TCC; ACT/MBCT; humanista-existencial;

integrativas/fatores comuns.

\#\# 5\. Foco Especial — Psicanálise e Psicoterapias Psicodinâmicas

\- Contribuição teórica (Fato C explícito).

\- Evidência empírica disponível (Fato A com nível CEBM e validade ecológica).

\- Curto, médio, longo prazo (separar sleeper effect se aplicável).

\- Efeitos sobre personalidade — APLICAR REGRA E:

  qualquer claim sobre mudança estrutural deve indicar instrumento validado

  utilizado no estudo (SWAP-200, RFQ, AAI, OPD, IIP) \+ seguimento ≥2 anos \+

  DOI/PMID. Sem isso → Fato C automaticamente.

\- Distinguir: psicanálise clássica | STPP | LTPP.

\- Discutir explicitamente: Shedler 2010; Leichsenring & Rabung; Driessen et al.;

  Fonagy/Bateman (mentalização); críticas metodológicas (controvérsias LTPP).

\#\# 6\. Mecanismos de Mudança

| Mecanismo | Como afetaria QoL | Evidência disponível | Técnica específica ou fator comum? | Foi medido no estudo original? (Regra J) | Nível CEBM | Validade ecológica | Fato A/B/C |

Cobrir: redução sintomática; aliança; insight; elaboração; mentalização;

regulação emocional; mudança narrativa/identitária; autonomia; sentido.

\#\# 7\. Comparação Crítica de Modelos

\- Modelos baseados em sintomas

\- Modelos baseados em funcionamento

\- Modelos baseados em bem-estar

\- Modelos baseados em transformação subjetiva

Tensionar EXPLICITAMENTE fatores comuns (Wampold) × especificidade de técnicas.

Não aceitar "modalidade A \> modalidade B" sem decomposição (Regra F).

\#\# 8\. Limitações da Literatura

Sobreposição construtual; allegiance effect; heterogeneidade; cegamento;

viés de publicação; duração; efeito do terapeuta; adesão/abandono;

instrumentos divergentes; cultura; operacionalização de "mudança estrutural"

em ECR.

\#\# 9\. Conclusão Balanceada

Resposta direta a "Qual é a relação entre QoL e psicoterapia?" — linguagem

prudente, não-promocional, cientificamente qualificada. Indicar consenso,

controvérsia, vácuo de evidência.

\#\# 10\. Referências (APA 7, com DOI/PMID quando disponíveis)

Não inventar referências. Sem DOI/PMID confirmado: marcar \[NÃO VERIFICADO\]

ou omitir.

\#\# 11\. Tabela de Qualidade das Fontes

| Fonte | Tipo | População | Método | Credibilidade | Validade ecológica | Limitações | Relevância |

\#\# 12\. Evidence Ledger

| \# | Claim | Fonte | DOI/PMID confirmado? (S/N) | Tipo de evidência | Nível CEBM | Validade ecológica | Sobreposição construtual? | Atribuição causal possível? | Fato A/B/C | Confiança | Status: OK / VERIFICAR / NÃO VERIFICADO / INCERTO |

\</pass\_2\_deep\_analysis\>

---

## **6\. PASS 3 — VALIDATION (auditoria cética interna)**

\<pass\_3\_validation\>

Após o Pass 2, atue como REVISOR METODOLÓGICO CÉTICO — especialista em EBM,

vieses em psicoterapia e leitura crítica de literatura psicanalítica.

Audite o relatório que você acabou de produzir. Encontre tudo o que está fraco.

PASSOS:

1\. Liste todos os claims verificáveis do Pass 2\.

2\. Para cada claim:

   \- DOI/PMID presente e confirmável?

   \- Força da evidência (CEBM \+ validade ecológica)?

   \- Risco de viés (incluindo allegiance)?

   \- Linguagem forte demais? ("eficaz", "comprovado", "estabelece")

   \- Precisa reescrita prudente?

   \- Atribuição causal foi feita sem dados de fatores comuns? (violação Regra J)

   \- Mudança estrutural foi afirmada sem instrumento validado? (violação Regra E)

3\. Identifique:

   \- generalizações indevidas

   \- correlação × causalidade confundidas

   \- omissão de limitações

   \- Fato C apresentado como consenso empírico

   \- claims sem DOI/PMID que vazaram para Sumário Executivo ou Conclusão

   \- claims sobre "mudança estrutural" sem instrumento validado nem

     seguimento longitudinal

   \- comparações de modalidades sem decomposição fatores comuns × específicos

   \- estudos com sobreposição construtual sintoma×QoL não sinalizados

   \- instrumentos de QoL não classificados quanto à sobreposição

4\. Reescreva conclusões frágeis em versão cientificamente segura.

5\. Lista final: aprovados | exigem verificação | devem ser removidos |

   lacunas importantes.

OUTPUT — AUDITORIA METODOLÓGICA:

\#\#\# A. Claims-to-Sources Table

| \# | Claim | Fonte | DOI/PMID | Evidência | Confiança | Problema | Ação |

\#\#\# B. Red Flags

Conceituais, clínicas e metodológicas (lista numerada).

\#\#\# C. Correções de Linguagem

| Original | Problema | Versão corrigida |

\#\#\# D. Conclusão Revisada

Reescrever a conclusão final em tom equilibrado e calibrado.

\#\#\# E. Nota de Confiabilidade (1–5) em cada eixo:

\- Completude

\- Rastreabilidade (DOI/PMID disponíveis vs ausentes)

\- Equilíbrio clínico (evidência vs teoria)

\- Força das evidências

\- Validade ecológica média

\- Tratamento da dissociação sintomas×QoL

\- Tratamento de fatores comuns×específicos

\- Aplicação da Regra E (mudança estrutural)

\- Aplicação da Regra J (atribuição causal restrita)

\- Aplicação da Regra K (classificação de sobreposição)

\- Clareza

\- Utilidade para pesquisa

\#\#\# F. Recomendação Final

\- Pronto para uso acadêmico? Sim / Não / Com revisão

\- 3 ações de revisão prioritárias antes de citar este material.

\</pass\_3\_validation\>

---

## **7\. AJUSTE POR MOTOR \+ TEMPLATES DE HANDOFF**

### **7.1 Calibração por motor**

| Motor | O que enfatizar |
| ----- | ----- |
| **Gemini DR** | Mapa conceitual amplo, conexões interdisciplinares (filosofia da mente, neurociência da aliança). Reforçar separação teoria psicanalítica × evidência empírica. Cobrar Pass 1 estrito com strings de busca PT/EN concretas. |
| **ChatGPT DR** | Estruturação rígida do output, Evidence Ledger completo com colunas "DOI/PMID confirmado?" e "Atribuição causal possível?". Motor mais consistente para Pass 3\. |
| **Perplexity DR** | Verificação cruzada de DOIs e referências. Não usar como motor primário — usar para auditar referências dos outros dois. |
| **Claude (sem DR)** | Após runs DR, alimentar com outputs agregados e pedir auditoria de equilíbrio clínico, flagging de claims promocionais, calibração de linguagem, checagem das Regras E, J e K. |

### **7.2 Template — Pass 1 isolado para Gemini DR**

\<instruction\>

Execute APENAS o PASS 1 — SCOPING do Prompt Mestre Unificado v2.0 sobre:

"Qual é a relação entre qualidade de vida e psicoterapia, com foco em

psicanálise e psicoterapias psicodinâmicas, em diálogo com TCC, terapias

humanistas-existenciais, terceira onda e fatores comuns?"

Não avance para análise completa.

Aplique:

\- \[BLOCO\_DE\_RISCO ACEITO\]

\- Mapa conceitual com instrumentos

\- Mínimo 7 subperguntas (incluindo obrigatoriamente a \#8 sobre sobreposição

  construtual)

\- Mínimo 5 strings de busca CONCRETAS PT/EN prontas para colar

  (PubMed/PsycINFO/Cochrane/PEP-Web/SciELO), com booleanos, truncamentos,

  MeSH e filtros de tipo de estudo

\- Critérios de inclusão/exclusão (incluir adolescentes)

\- Riscos metodológicos ordenados — sobreposição construtual em \#1

\- Pergunta final refinada

Finalize obrigatoriamente com:

\[APROVAR\_PLANO\]

"Aprovar o plano como está, ou ajustar antes de proceder ao Pass 2?"

Não produza o relatório final ainda.

\</instruction\>

### **7.3 Template — Handoff Pass 1 aprovado → ChatGPT DR (Pass 2 \+ Pass 3\)**

\<instruction\>

Você receberá abaixo o Pass 1 APROVADO, produzido pelo Gemini Deep Research,

para a pesquisa:

"Qual é a relação entre qualidade de vida e psicoterapia, com foco em

psicanálise e psicoterapias psicodinâmicas, em diálogo com TCC, terapias

humanistas-existenciais, terceira onda e fatores comuns?"

Sua tarefa é executar APENAS:

\- Pass 2 — Deep Analysis

\- Pass 3 — Validation

Use rigorosamente o Prompt Mestre Unificado v2.0 (regras A–K da seção 3).

Não refaça o escopo, salvo se encontrar erro metodológico grave. Nesse caso,

sinalize antes de prosseguir.

Regras obrigatórias:

\- Nunca inventar DOI/PMID. Sem confirmação: \[NÃO VERIFICADO\].

\- Claims \[NÃO VERIFICADO\] não entram no Sumário Executivo nem na Conclusão.

\- Separar Fato A, Fato B e Fato C.

\- Aplicar CEBM \+ validade ecológica em todas as tabelas.

\- Avaliar dissociação sintomas × QoL por modalidade.

\- Decompor fatores comuns × técnica específica em cada comparação.

\- Mudança estrutural/personológica \= Fato C salvo instrumento validado

  (SWAP/RFQ/AAI/OPD/IIP) \+ seguimento ≥2 anos \+ DOI/PMID.

\- Quando estudo não medir aliança/expectativa/efeito do terapeuta/dose:

  proibido atribuir efeito à técnica específica (Regra J).

\- Classificar sobreposição construtual de cada instrumento de QoL

  (baixa/moderada/alta) (Regra K).

\- Produzir Evidence Ledger completo e Claims-to-Sources Table.

\- Finalizar com auditoria cética interna (Pass 3).

\<pass\_1\_aprovado\>

\[COLE AQUI O PASS 1 APROVADO PELO ORQUESTRADOR HUMANO\]

\</pass\_1\_aprovado\>

\</instruction\>

### **7.4 Template — Auditoria final por Claude**

Você é revisor metodológico independente. Recebe abaixo o output completo

(Pass 2 \+ Pass 3\) de uma pesquisa estruturada sob o Prompt Mestre Unificado

v2.0 sobre qualidade de vida e psicoterapia.

Sua tarefa: identificar especificamente:

1\. Claims de Fato C apresentados como Fato A.

2\. Violações da Regra E — mudança estrutural sem instrumento validado.

3\. Violações da Regra J — atribuição causal sem dados de fatores comuns.

4\. Violações da Regra K — instrumentos de QoL não classificados.

5\. Linguagem que decaiu de "sugere" para "demonstra/comprova".

6\. Problemas de validade ecológica não sinalizados.

7\. DOIs/PMIDs ausentes ou suspeitos no Evidence Ledger.

8\. Equilíbrio epistemológico — psicanálise tratada como consenso empírico

   ou como sem qualquer evidência (ambos viés).

Output:

\- Lista numerada de violações encontradas, por gravidade.

\- Reescrita das 5 frases mais problemáticas.

\- Recomendação: pronto para citar / requer revisão / inutilizável.

\<output\_completo\>

\[COLE AQUI O OUTPUT COMPLETO DO CHATGPT DR — Pass 2 \+ Pass 3\]

\</output\_completo\>

---

## **8\. VERSÃO CURTA — single-shot drop-in**

Quando não houver tempo para o pipeline completo:

Você é pesquisador sênior em saúde mental e psicoterapia. Produza Deep

Research sobre: "Qual é a relação entre qualidade de vida e psicoterapia,

com foco em psicanálise e psicodinâmicas, em diálogo com TCC, humanistas,

3ª onda e fatores comuns?"

ANTES da análise: produza plano com mapa conceitual, mínimo 7 subperguntas

(incluindo sobreposição construtual sintoma×QoL), mínimo 5 strings de busca

PT/EN concretas, critérios de inclusão/exclusão (incluir adolescentes),

riscos metodológicos (sobreposição construtual em \#1). PARE para aprovação.

DEPOIS: relatório em Markdown com:

1\. Sumário executivo (apenas Fato A com DOI/PMID confirmado)

2\. Definições operacionais com instrumentos e sobreposição construtual

3\. Evidências gerais sobre psicoterapia × QoL

4\. Tabela por modalidade: Tipo de evidência | Efeitos | Dissociação? | CEBM |

   Validade ecológica | Atribuição causal possível? | Limitações

5\. Mecanismos de mudança (técnica específica vs fator comum, foi medido?)

6\. Limitações metodológicas

7\. Evidence Ledger (Claim | Fonte | DOI/PMID? | CEBM | Val. ecológica |

   Sobreposição? | Atrib. causal? | Fato A/B/C | Status)

8\. Claims-to-Sources Table

9\. Referências APA 7

REGRAS NÃO-NEGOCIÁVEIS:

\- Nunca inventar DOI/PMID. Sem confirmação: \[NÃO VERIFICADO\]. Claims

  \[NÃO VERIFICADO\] não entram em Sumário/Conclusão.

\- Mudança estrutural \= Fato C salvo instrumento validado (SWAP/RFQ/AAI/OPD/

  IIP) \+ ≥2 anos \+ DOI/PMID.

\- Quando estudo não mede aliança/expectativa/efeito terapeuta/dose: proibido

  atribuir efeito à técnica específica. Usar "compatível com a intervenção,

  mas não distingue técnica específica de fatores comuns".

\- Para cada instrumento de QoL: classificar sobreposição com sintomas

  (baixa/moderada/alta).

\- Linguagem: sugere / compatível / hipótese / não estabelecido. Banir

  "eficaz/comprovado/superior" sem qualificação.

\- "Correlação não implica causalidade" em toda seção associativa.

\- Conclusão prudente, não-promocional.

---

## **9\. CHECKLIST DE QUALIDADE (auto-auditoria do orquestrador)**

Antes de aceitar output de qualquer motor:

* \[ \] `[BLOCO_DE_RISCO ACEITO]` aparece no início?  
* \[ \] Pass 1 parou em `[APROVAR_PLANO]`?  
* \[ \] Pass 1 entregou strings de busca PT/EN concretas (não descritores soltos)?  
* \[ \] Pass 1 inclui subpergunta sobre sobreposição construtual?  
* \[ \] Pass 1 inclui adolescentes no critério de inclusão?  
* \[ \] Sumário Executivo contém apenas Fato A com Nível CEBM ≤3 e DOI/PMID confirmado?  
* \[ \] Cada claim do Evidence Ledger tem coluna "DOI/PMID confirmado?" preenchida?  
* \[ \] Nenhum DOI/PMID foi inventado? (verificação via Perplexity/PubMed)  
* \[ \] Tabelas incluem coluna "Validade ecológica"?  
* \[ \] Tabela de modalidades inclui "Sintomas vs QoL: dissociação?" e "Atribuição causal possível?"  
* \[ \] Tabela de mecanismos inclui "Técnica específica ou fator comum?" e "Foi medido no estudo?"  
* \[ \] **Regra E**: Claims sobre mudança estrutural indicam instrumento validado (SWAP/RFQ/AAI/OPD/IIP) \+ ≥2 anos \+ DOI/PMID? Sem isso \= Fato C?  
* \[ \] **Regra J**: Quando estudo não mede fatores comuns, atribuição é restrita à linguagem "compatível com, mas não distingue"?  
* \[ \] **Regra K**: Cada instrumento de QoL tem classificação de sobreposição (baixa/moderada/alta)?  
* \[ \] Comparações entre modalidades decompõem fatores comuns × específicos × efeito do terapeuta × allegiance?  
* \[ \] Estudos com sobreposição construtual sintoma×QoL foram sinalizados?  
* \[ \] Linguagem calibrada (sugere / compatível / hipótese / não estabelecido)?  
* \[ \] "Correlação não implica causalidade" em todas seções associativas?  
* \[ \] Pass 3 produziu Claims-to-Sources, Red Flags, Conclusão Revisada?  
* \[ \] Nota de Confiabilidade ≥3,5/5 em todas as dimensões?

Item falho → devolver ao motor com pedido específico de correção.

---

**Fim do Prompt Mestre Unificado v2.0 (Final).**

# Tab 14

# **PROMPT MESTRE UNIFICADO v2.0 (Final)**

## **Qualidade de Vida × Psicoterapia (com foco em psicanálise/psicodinâmica)**

**Versão:** 2.0 (Final) · **Uso:** Gemini DR / ChatGPT DR / Perplexity DR / Claude (validação) · **Three-pass single-run com halts internos**

---

## **CHANGELOG (v1.1 → v2.0)**

1. **Regra E reforçada:** mudança estrutural/personológica exige indicação explícita de instrumento validado (SWAP-200, RFQ, AAI, OPD, IIP) ou é classificada como Fato C automaticamente, mesmo se a interpretação clínica for plausível.  
2. **Nova regra J — atribuição causal restrita:** quando o estudo original não mede aliança, expectativa, efeito do terapeuta, dose/intensidade ou allegiance, é proibido atribuir o efeito de QoL à técnica específica. Linguagem obrigatória: "compatível com a intervenção, mas não distingue técnica específica de fatores comuns".  
3. **Nova regra K — sobreposição construtual classificada por instrumento:** para cada instrumento de QoL citado, indicar baixa/moderada/alta sobreposição com escalas sintomáticas, com tratamento cauteloso quando alta.  
4. **Pass 1 — estratégia de busca exige strings concretas:** mínimo 5 strings PT/EN prontas para colar, com booleanos, truncamentos, MeSH e filtros de tipo de estudo. Listas de descritores soltos não aceitas.  
5. **Nova subpergunta obrigatória:** "Quais instrumentos de QoL mais se sobrepõem semanticamente a escalas de sintomas, e como isso afeta a interpretação da dissociação?"  
6. **População ampliada:** adolescentes incluídos por padrão (MBT-A, TCC adolescente, psicodinâmica em desenvolvimento).  
7. **Sobreposição construtual** elevada de menção a risco metodológico nº 1\.  
8. **Templates de handoff entre motores** incorporados ao documento (§7).

---

## **0\. INSTRUÇÕES DE USO (meta — não copiar para o motor)**

Single-run por motor, três passes com halts internos. Fragmentar quebra cadeia de evidências.

**Pipeline canônico:**

1. **Gemini DR** → Pass 1 isolado (escopo \+ mapa \+ strings de busca).  
2. Auditoria humana → aprovar/ajustar.  
3. **ChatGPT DR** → Pass 2 \+ Pass 3 sobre Pass 1 aprovado.  
4. **Perplexity DR** → verificação cruzada de DOIs.  
5. **Claude (sem DR)** → auditoria final de equilíbrio epistemológico.

**Tags operacionais (não remover):** \[BLOCO\_DE\_RISCO\], \[APROVAR\_PLANO\], \[VERIFICAR\], \[NÃO VERIFICADO\].

---

## **1\. IDENTIDADE E CONTEXTO**

\<role\>

Você é um pesquisador sênior em saúde mental, psicoterapia, psicologia clínica e metodologia em medicina baseada em evidências. Escreve para leitor com formação médica que demanda profundidade, rastreabilidade e prudência clínica.

\</role\>

\<context\>

Tema: relação entre qualidade de vida e psicoterapia, com foco em psicanálise e psicoterapias psicodinâmicas, em comparação/diálogo com TCC, terapias humanistas-existenciais, terapias de 3ª onda e modelos integrativos

(fatores comuns).

Objetivo: revisão crítica, comparativa e metodologicamente rigorosa sobre como diferentes modalidades se relacionam com QoL, bem-estar subjetivo, funcionamento social, alívio sintomático, autonomia e sentido de vida.

Público-alvo: médico, pesquisador ou profissional de saúde mental.

Escopo temporal: 2010–2026 prioritário (revisões sistemáticas, meta-análises, ECRs, longitudinais). Obras seminais quando indispensáveis (Shedler 2010; Leichsenring & Rabung; Wampold sobre fatores comuns; Driessen et al. sobre psicodinâmica breve; Fonagy/Bateman sobre mentalização).

Geografia: internacional, com atenção explícita a evidências latino-americanas/brasileiras quando disponíveis.

\</context\>

\<disclaimers\_obrigatorios\>

\- Educacional/pesquisa, não substitui avaliação clínica individual.

\- Não emite recomendações personalizadas.

\- Diferencia: evidência empírica forte | moderada | hipótese clínica plausível |interpretação teórica psicanalítica | afirmação ainda não demonstrada.

\</disclaimers\_obrigatorios\>

---

## **2\. DIAGNÓSTICO 3D \+ GATE DE RISCO**

\<diagnostico\_3d\>

\- Ambiguidade: 4/5 — QoL é constructo multidimensional com instrumentos divergentes (WHOQOL, SF-36, EQ-5D, Q-LES-Q) e sobreposição construtual parcial com escalas sintomáticas (PHQ-9, BDI-II, HAM-D).

\- Risco: 5/5 — HIGH-RISK TOPIC (saúde mental, prática clínica regulada).

\- Tipo: Processo / Validação.

\</diagnostico\_3d\>

\<bloco\_de\_risco\>

HIGH-RISK TOPIC DETECTED — saúde mental.

Antes de prosseguir, declare no início do output:

1\. Aplicará linguagem prudente e não-promocional.

2\. Separará claims empíricos (Fato A/B) de interpretações teóricas (Fato C).

3\. Sinalizará todos os disclaimers acima.

Confirme com a string: "\[BLOCO\_DE\_RISCO ACEITO\]" antes do Pass 1\.

\</bloco\_de\_risco\>

---

## **3\. REGRAS DE EVIDÊNCIA (NÃO-NEGOCIÁVEIS, válidas em todos os passes)**

\<regras\_evidencia\>

A. ANTI-ALUCINAÇÃO DE REFERÊNCIAS

\- Nunca inventar DOI, PMID, título, periódico, autor ou ano.

\- Sem confirmação de alta confiança: marcar como \[NÃO VERIFICADO\].

\- Claims \[VERIFICAR\] ou \[NÃO VERIFICADO\] só aparecem em seções de lacunas, limitações ou próximos passos — NUNCA no Sumário Executivo, NUNCA na

Conclusão, NUNCA como base para inferência.

B. CLASSIFICAÇÃO DE FORÇA (Oxford CEBM adaptado)

\- Nível 1: revisão sistemática/meta-análise de ECRs homogêneos

\- Nível 2: ECR individual de boa qualidade

\- Nível 3: coorte ou caso-controle

\- Nível 4: séries de casos, estudos de baixa qualidade

\- Nível 5: opinião de especialista, consenso, hipótese teórica

C. VALIDADE ECOLÓGICA (eixo complementar obrigatório em psicoterapia)

\- Alta: contexto clínico realista, amostra representativa, seguimento adequado, desfecho funcional/QoL relevante.

\- Moderada: alguma artificialidade, população restrita ou seguimento limitado.

\- Baixa: setting altamente controlado, amostra pequena, desfecho proximal, baixa generalização clínica.

JUSTIFICATIVA: em psicoterapia, ECRs Nível 2 podem ter validade ecológica baixa; coortes Nível 3 podem ter validade ecológica alta. Eixos não redundantes.

D. CLASSIFICAÇÃO FATO A/B/C

\- Fato A: dado empírico verificado em fonte primária identificada (DOI/PMID confirmado).

\- Fato B: inferência/cálculo derivado direto de Fato A.

\- Fato C: hipótese clínica, interpretação teórica, plausibilidade, tradição conceitual.

E. MUDANÇA ESTRUTURAL/PERSONOLÓGICA — REGRA DE INSTRUMENTO OBRIGATÓRIO

Qualquer afirmação sobre "mudança estrutural de personalidade", "transformação subjetiva profunda", "reorganização psíquica", "reorganização de identidade" ou "mudança duradoura do self" deve obrigatoriamente indicar QUAL instrumento validado foi usado no estudo:

   \- SWAP-200 (Shedler-Westen Assessment Procedure)

   \- RFQ (Reflective Functioning Questionnaire)

   \- AAI (Adult Attachment Interview)

   \- OPD (Operationalized Psychodynamic Diagnosis)

   \- IIP (Inventory of Interpersonal Problems)

   \- ou equivalente validado.

Se o estudo NÃO apresentar instrumento validado → classificar como Fato C automaticamente, MESMO que a interpretação clínica seja plausível.

Adicionalmente, exige-se: seguimento ≥2 anos e fonte primária identificável com DOI/PMID para qualificar como Fato A.

F. FATORES COMUNS × ESPECÍFICOS — DECOMPOSIÇÃO OBRIGATÓRIA

Em cada comparação entre modalidades, avaliar EXPLICITAMENTE se os efeitos parecem atribuíveis a:

   \- técnica específica;

   \- fatores comuns (aliança, expectativa, vínculo, estrutura);

   \- efeito do terapeuta;

   \- duração/intensidade do tratamento;

   \- características do paciente;

   \- viés metodológico (allegiance effect).

G. DISSOCIAÇÃO SINTOMAS × QoL — EIXO CENTRAL

Para cada modalidade analisada, responder:

   \- Há melhora de QoL proporcional à redução sintomática?

   \- Há melhora sintomática SEM melhora equivalente de QoL?

   \- Há melhora de QoL mesmo com sintomas residuais?

   \- O estudo MEDE QoL diretamente ou INFERE QoL a partir de sintomas?

Estudos que não distinguem os constructos: marcar com "sobreposição construtual" e tratar com cautela.

H. LINGUAGEM CALIBRADA

\- "demonstra/comprova/estabelece" → apenas com evidência Nível 1–2 e validade ecológica alta/moderada.

\- "sugere" → evidência moderada (Nível 2–3).

\- "é compatível com" → inferência consistente mas não demonstrada.

\- "hipótese clínica" → Fato C com plausibilidade.

\- "não estabelecido" → falta de evidência direta.

\- Banidas sem qualificação: "eficaz", "comprovado", "superior".

I. CORRELAÇÃO ≠ CAUSALIDADE

Toda seção associativa deve conter explicitamente esta frase.

J. ATRIBUIÇÃO CAUSAL RESTRITA

Quando o estudo original NÃO medir aliança terapêutica, expectativa, efeito do terapeuta, dose/intensidade ou allegiance effect, o relatório NÃO PODE atribuir melhora de QoL à técnica específica.

Linguagem obrigatória nesses casos:

"o efeito é compatível com a intervenção, mas não permite distinguir técnica específica de fatores comuns."

K. SOBREPOSIÇÃO CONSTRUTUAL — CLASSIFICAÇÃO POR INSTRUMENTO

Para cada instrumento de QoL citado, indicar grau de sobreposição com escalas sintomáticas:

   \- Baixa: instrumentos focados em funcionamento físico/social/cognitivo concreto, sem itens diretos de humor/afeto (ex: EQ-5D em maior parte).

   \- Moderada: instrumentos com dimensões afetivas mas separáveis (ex: SF-36 com componente mental; certas dimensões do WHOQOL-BREF).

   \- Alta: instrumentos cujos itens-chave perguntam sobre estados afetivos, satisfação ou energia que se sobrepõem semanticamente a sintomas depressivos/ansiosos (ex: Q-LES-Q-SF; subescalas afetivas).

Quando alta sobreposição: tratar associações entre redução sintomática e QoL com cautela, e priorizar estudos que façam análise de sensibilidade removendo itens sobrepostos.

\</regras\_evidencia\>

---

## **4\. PASS 1 — SCOPING (com PAUSA OBRIGATÓRIA)**

\<pass\_1\_scoping\>

Antes da análise completa, produza plano de pesquisa e PARE para aprovação.

A) MAPA CONCEITUAL — 8–12 conceitos com definição operacional E instrumento de medida quando aplicável:

   \- QoL (WHOQOL-BREF; SF-36; EQ-5D; Q-LES-Q)

   \- bem-estar subjetivo (SWLS; PANAS; Ryff PWB)

   \- psicanálise vs STPP vs LTPP

   \- TCC; ACT/MBCT (3ª onda); humanista-existencial

   \- aliança terapêutica (WAI; CALPAS)

   \- mentalização / função reflexiva (RFQ; AAI)

   \- funcionamento social (SAS; GAF/WHODAS)

   \- sentido de vida (MLQ; PIL)

   \- mudança estrutural de personalidade (SWAP-200; OPD; IIP)

   \- fatores comuns (Wampold)

   \- dissociação sintoma×QoL (definição operacional explícita)

B) SUBPERGUNTAS (mínimo 7, incluindo obrigatoriamente):

   1\. Como QoL é definida e medida em estudos de psicoterapia?

   2\. Psicoterapia melhora QoL independentemente da redução sintomática?

   3\. Há diferenças entre modalidades quanto a QoL — ou prevalecem fatores comuns?

   4\. O que evidência empírica sustenta sobre psicanálise/psicodinâmica distintamente da tradição teórica?

   5\. Quais mecanismos plausíveis (insight, elaboração, vínculo, mentalização, regulação emocional, narrativa, autonomia)?

   6\. Que limitações metodológicas tornam essa relação difícil de medir?

   7\. Há dissociação entre melhora sintomática e melhora de QoL nos estudos?

      Em quais modalidades, populações ou instrumentos isso aparece com mais clareza?

   8\. \[OBRIGATÓRIA\] Quais instrumentos de QoL mais se sobrepõem semanticamente a escalas de sintomas (PHQ-9, BDI-II, HAM-D), e como isso afeta a interpretação da dissociação real vs. artefato de medida? \[+ subperguntas emergentes que o motor identificar\]

C) ESTRATÉGIA DE BUSCA — entregar OBRIGATORIAMENTE:

   \- Mínimo 5 strings de busca CONCRETAS, em PT/EN, prontas para colar.

   \- Cada string deve incluir: booleanos, truncamentos quando aplicável, termos MeSH quando disponíveis, filtros de tipo de estudo.

   \- Cobrir: PubMed/MEDLINE, PsycINFO, Cochrane, PEP-Web (psicodinâmica), SciELO/PePSIC (regional).

   \- Listas soltas de descritores SEM strings booleanas operacionais NÃO são aceitáveis.

D) CRITÉRIOS DE INCLUSÃO/EXCLUSÃO

   \- Incluir: ECRs, meta-análises, longitudinais ≥6m; instrumentos validados de QoL; AMOSTRAS ADULTAS E ADOLESCENTES (não excluir adolescentes automaticamente — literatura sobre MBT-A, TCC adolescente e psicodinâmica em desenvolvimento é relevante para mecanismos).

   \- Incluir cautelosamente: estudos longitudinais de LTPP mesmo sem comparador (marcar como Fato B/C, útil para hipótese).

   \- Excluir: blogs, materiais promocionais, séries de casos sem instrumento validado, estudos que tratem alívio sintomático e QoL como sinônimos sem medição independente.

E) RISCOS METODOLÓGICOS — ordenar por prioridade:

   1\. SOBREPOSIÇÃO CONSTRUTUAL — itens de PHQ-9/BDI-II/HAM-D ou escalas de ansiedade que se sobrepõem semanticamente a itens de WHOQOL/SF-36/ Q-LES-Q. Pode gerar correlações parcialmente tautológicas.

   2\. Allegiance effect — viés sistemático onde pesquisador encontra resultados favoráveis à sua orientação teórica.

   3\. Variação de validade ecológica — ECRs com alto controle (CEBM 2\) podem falhar em representar prática clínica real.

   4\. Dificuldade de cegamento — risco inerente em pesquisa de psicoterapia que pode inflar efeitos percebidos.

   5\. Heterogeneidade de modalidades.

   6\. Viés de publicação.

   7\. Dificuldade de operacionalizar "mudança estrutural" em ECR.

   8\. Generalização cultural.

F) PERGUNTA-FINAL REFINADA.

\[APROVAR\_PLANO\] — finalize com:

"Aprovar o plano como está, ou ajustar antes de proceder ao Pass 2?"

NÃO AVANCE sem confirmação explícita.

\</pass\_1\_scoping\>

---

## **5\. PASS 2 — DEEP ANALYSIS**

\<pass\_2\_deep\_analysis\>

Após aprovação do plano, execute a revisão crítica seguindo RIGOROSAMENTE o output\_format. Não substituir tabelas por prosa. Aplicar todas as Regras de

Evidência (seção 3).

OUTPUT FORMAT:

\# Qualidade de Vida e Psicoterapia: Revisão Crítica

\#\# 1\. Sumário Executivo

\- 5–8 achados principais (apenas Fato A com Nível CEBM ≤3 e DOI/PMID confirmado)

\- 3 implicações clínicas prudentes

\- 3 riscos de interpretação

\- 3 lacunas de pesquisa

\#\# 2\. Definições Operacionais

| Conceito | Definição | Instrumento de medida | Sobreposição com sintomas (baixa/moderada/alta) | Observações metodológicas |

\#\# 3\. QoL como Desfecho em Psicoterapia

Diferenciar: melhora sintomática | funcionamento social | bem-estar subjetivo | sentido de vida | satisfação relacional | autonomia | saúde global percebida.

Tensão entre modelos baseados em sintomas (DSM/CID) e modelos de flourishing/well-being (Seligman, Ryff, OMS-QoL).

\#\# 4\. Evidências por Modalidade

| Abordagem | Tipo de evidência | Efeitos sobre QoL | Sintomas vs QoL: dissociação? | Nível CEBM | Validade ecológica | Atribuição causal possível? (Regra J) | Limitações |

Cobrir mínimo: psicanálise; STPP; LTPP; TCC; ACT/MBCT; humanista-existencial; integrativas/fatores comuns.

\#\# 5\. Foco Especial — Psicanálise e Psicoterapias Psicodinâmicas

\- Contribuição teórica (Fato C explícito).

\- Evidência empírica disponível (Fato A com nível CEBM e validade ecológica).

\- Curto, médio, longo prazo (separar sleeper effect se aplicável).

\- Efeitos sobre personalidade — APLICAR REGRA E: qualquer claim sobre mudança estrutural deve indicar instrumento validado utilizado no estudo (SWAP-200, RFQ, AAI, OPD, IIP) \+ seguimento ≥2 anos \+ DOI/PMID. Sem isso → Fato C automaticamente.

\- Distinguir: psicanálise clássica | STPP | LTPP.

\- Discutir explicitamente: Shedler 2010; Leichsenring & Rabung; Driessen et al.; Fonagy/Bateman (mentalização); críticas metodológicas (controvérsias LTPP).

\#\# 6\. Mecanismos de Mudança

| Mecanismo | Como afetaria QoL | Evidência disponível | Técnica específica ou fator comum? | Foi medido no estudo original? (Regra J) | Nível CEBM | Validade ecológica | Fato A/B/C |

Cobrir: redução sintomática; aliança; insight; elaboração; mentalização; regulação emocional; mudança narrativa/identitária; autonomia; sentido.

\#\# 7\. Comparação Crítica de Modelos

\- Modelos baseados em sintomas

\- Modelos baseados em funcionamento

\- Modelos baseados em bem-estar

\- Modelos baseados em transformação subjetiva

Tensionar EXPLICITAMENTE fatores comuns (Wampold) × especificidade de técnicas.

Não aceitar "modalidade A \> modalidade B" sem decomposição (Regra F).

\#\# 8\. Limitações da Literatura

Sobreposição construtual; allegiance effect; heterogeneidade; cegamento; viés de publicação; duração; efeito do terapeuta; adesão/abandono; instrumentos divergentes; cultura; operacionalização de "mudança estrutural" em ECR.

\#\# 9\. Conclusão Balanceada

Resposta direta a "Qual é a relação entre QoL e psicoterapia?" — linguagem prudente, não-promocional, cientificamente qualificada. Indicar consenso, controvérsia, vácuo de evidência.

\#\# 10\. Referências (APA 7, com DOI/PMID quando disponíveis)

Não inventar referências. Sem DOI/PMID confirmado: marcar \[NÃO VERIFICADO\] ou omitir.

\#\# 11\. Tabela de Qualidade das Fontes

| Fonte | Tipo | População | Método | Credibilidade | Validade ecológica | Limitações | Relevância |

\#\# 12\. Evidence Ledger

| \# | Claim | Fonte | DOI/PMID confirmado? (S/N) | Tipo de evidência | Nível CEBM | Validade ecológica | Sobreposição construtual? | Atribuição causal possível? | Fato A/B/C | Confiança | Status: OK / VERIFICAR / NÃO VERIFICADO / INCERTO |

\</pass\_2\_deep\_analysis\>

---

## **6\. PASS 3 — VALIDATION (auditoria cética interna)**

\<pass\_3\_validation\>

Após o Pass 2, atue como REVISOR METODOLÓGICO CÉTICO — especialista em EBM, vieses em psicoterapia e leitura crítica de literatura psicanalítica.

Audite o relatório que você acabou de produzir. Encontre tudo o que está fraco.

PASSOS:

1\. Liste todos os claims verificáveis do Pass 2\.

2\. Para cada claim:

   \- DOI/PMID presente e confirmável?

   \- Força da evidência (CEBM \+ validade ecológica)?

   \- Risco de viés (incluindo allegiance)?

   \- Linguagem forte demais? ("eficaz", "comprovado", "estabelece")

   \- Precisa reescrita prudente?

   \- Atribuição causal foi feita sem dados de fatores comuns? (violação Regra J)

   \- Mudança estrutural foi afirmada sem instrumento validado? (violação Regra E)

3\. Identifique:

   \- generalizações indevidas

   \- correlação × causalidade confundidas

   \- omissão de limitações

   \- Fato C apresentado como consenso empírico

   \- claims sem DOI/PMID que vazaram para Sumário Executivo ou Conclusão

   \- claims sobre "mudança estrutural" sem instrumento validado nem seguimento longitudinal

   \- comparações de modalidades sem decomposição fatores comuns × específicos

   \- estudos com sobreposição construtual sintoma×QoL não sinalizados

   \- instrumentos de QoL não classificados quanto à sobreposição

4\. Reescreva conclusões frágeis em versão cientificamente segura.

5\. Lista final: aprovados | exigem verificação | devem ser removidos | lacunas importantes.

OUTPUT — AUDITORIA METODOLÓGICA:

\#\#\# A. Claims-to-Sources Table

| \# | Claim | Fonte | DOI/PMID | Evidência | Confiança | Problema | Ação |

\#\#\# B. Red Flags

Conceituais, clínicas e metodológicas (lista numerada).

\#\#\# C. Correções de Linguagem

| Original | Problema | Versão corrigida |

\#\#\# D. Conclusão Revisada

Reescrever a conclusão final em tom equilibrado e calibrado.

\#\#\# E. Nota de Confiabilidade (1–5) em cada eixo:

\- Completude

\- Rastreabilidade (DOI/PMID disponíveis vs ausentes)

\- Equilíbrio clínico (evidência vs teoria)

\- Força das evidências

\- Validade ecológica média

\- Tratamento da dissociação sintomas×QoL

\- Tratamento de fatores comuns×específicos

\- Aplicação da Regra E (mudança estrutural)

\- Aplicação da Regra J (atribuição causal restrita)

\- Aplicação da Regra K (classificação de sobreposição)

\- Clareza

\- Utilidade para pesquisa

\#\#\# F. Recomendação Final

\- Pronto para uso acadêmico? Sim / Não / Com revisão

\- 3 ações de revisão prioritárias antes de citar este material.

\</pass\_3\_validation\>

---

## **7\. AJUSTE POR MOTOR \+ TEMPLATES DE HANDOFF**

### **7.1 Calibração por motor**

| Motor | O que enfatizar |
| :---- | :---- |
| **Gemini DR** | Mapa conceitual amplo, conexões interdisciplinares (filosofia da mente, neurociência da aliança). Reforçar separação teoria psicanalítica × evidência empírica. Cobrar Pass 1 estrito com strings de busca PT/EN concretas. |
| **ChatGPT DR** | Estruturação rígida do output, Evidence Ledger completo com colunas "DOI/PMID confirmado?" e "Atribuição causal possível?". Motor mais consistente para Pass 3\. |
| **Perplexity DR** | Verificação cruzada de DOIs e referências. Não usar como motor primário — usar para auditar referências dos outros dois. |
| **Claude (sem DR)** | Após runs DR, alimentar com outputs agregados e pedir auditoria de equilíbrio clínico, flagging de claims promocionais, calibração de linguagem, checagem das Regras E, J e K. |

### **7.2 Template — Pass 1 isolado para Gemini DR**

\<instruction\>

Execute APENAS o PASS 1 — SCOPING do Prompt Mestre Unificado v2.0 sobre:

"Qual é a relação entre qualidade de vida e psicoterapia, com foco em psicanálise e psicoterapias psicodinâmicas, em diálogo com TCC, terapias humanistas-existenciais, terceira onda e fatores comuns?"

Não avance para análise completa.

Aplique:

\- \[BLOCO\_DE\_RISCO ACEITO\]

\- Mapa conceitual com instrumentos

\- Mínimo 7 subperguntas (incluindo obrigatoriamente a \#8 sobre sobreposição construtual)

\- Mínimo 5 strings de busca CONCRETAS PT/EN prontas para colar (PubMed/PsycINFO/Cochrane/PEP-Web/SciELO), com booleanos, truncamentos, MeSH e filtros de tipo de estudo

\- Critérios de inclusão/exclusão (incluir adolescentes)

\- Riscos metodológicos ordenados — sobreposição construtual em \#1

\- Pergunta final refinada

Finalize obrigatoriamente com:

\[APROVAR\_PLANO\]

"Aprovar o plano como está, ou ajustar antes de proceder ao Pass 2?"

Não produza o relatório final ainda.

\</instruction\>

### **7.3 Template — Handoff Pass 1 aprovado → ChatGPT DR (Pass 2 \+ Pass 3\)**

\<instruction\>

Você receberá abaixo o Pass 1 APROVADO, produzido pelo Gemini Deep Research, para a pesquisa:

"Qual é a relação entre qualidade de vida e psicoterapia, com foco em psicanálise e psicoterapias psicodinâmicas, em diálogo com TCC, terapias humanistas-existenciais, terceira onda e fatores comuns?"

Sua tarefa é executar APENAS:

\- Pass 2 — Deep Analysis

\- Pass 3 — Validation

Use rigorosamente o Prompt Mestre Unificado v2.0 (regras A–K da seção 3).

Não refaça o escopo, salvo se encontrar erro metodológico grave. Nesse caso, sinalize antes de prosseguir.

Regras obrigatórias:

\- Nunca inventar DOI/PMID. Sem confirmação: \[NÃO VERIFICADO\].

\- Claims \[NÃO VERIFICADO\] não entram no Sumário Executivo nem na Conclusão.

\- Separar Fato A, Fato B e Fato C.

\- Aplicar CEBM \+ validade ecológica em todas as tabelas.

\- Avaliar dissociação sintomas × QoL por modalidade.

\- Decompor fatores comuns × técnica específica em cada comparação.

\- Mudança estrutural/personológica \= Fato C salvo instrumento validado

  (SWAP/RFQ/AAI/OPD/IIP) \+ seguimento ≥2 anos \+ DOI/PMID.

\- Quando estudo não medir aliança/expectativa/efeito do terapeuta/dose: proibido atribuir efeito à técnica específica (Regra J).

\- Classificar sobreposição construtual de cada instrumento de QoL

  (baixa/moderada/alta) (Regra K).

\- Produzir Evidence Ledger completo e Claims-to-Sources Table.

\- Finalizar com auditoria cética interna (Pass 3).

\<pass\_1\_aprovado\>

\[COLE AQUI O PASS 1 APROVADO PELO ORQUESTRADOR HUMANO\]

\</pass\_1\_aprovado\>

\</instruction\>

### **7.4 Template — Auditoria final por Claude**

Você é revisor metodológico independente. Recebe abaixo o output completo (Pass 2 \+ Pass 3\) de uma pesquisa estruturada sob o Prompt Mestre Unificado v2.0 sobre qualidade de vida e psicoterapia.

Sua tarefa: identificar especificamente:

1\. Claims de Fato C apresentados como Fato A.

2\. Violações da Regra E — mudança estrutural sem instrumento validado.

3\. Violações da Regra J — atribuição causal sem dados de fatores comuns.

4\. Violações da Regra K — instrumentos de QoL não classificados.

5\. Linguagem que decaiu de "sugere" para "demonstra/comprova".

6\. Problemas de validade ecológica não sinalizados.

7\. DOIs/PMIDs ausentes ou suspeitos no Evidence Ledger.

8\. Equilíbrio epistemológico — psicanálise tratada como consenso empírico

   ou como sem qualquer evidência (ambos viés).

Output:

\- Lista numerada de violações encontradas, por gravidade.

\- Reescrita das 5 frases mais problemáticas.

\- Recomendação: pronto para citar / requer revisão / inutilizável.

\<output\_completo\>

\[COLE AQUI O OUTPUT COMPLETO DO CHATGPT DR — Pass 2 \+ Pass 3\]

\</output\_completo\>

---

## **8\. VERSÃO CURTA — single-shot drop-in**

Quando não houver tempo para o pipeline completo: Você é pesquisador sênior em saúde mental e psicoterapia. Produza Deep Research sobre: "Qual é a relação entre qualidade de vida e psicoterapia, com foco em psicanálise e psicodinâmicas, em diálogo com TCC, humanistas, 3ª onda e fatores comuns?"

ANTES da análise: produza plano com mapa conceitual, mínimo 7 subperguntas (incluindo sobreposição construtual sintoma×QoL), mínimo 5 strings de busca PT/EN concretas, critérios de inclusão/exclusão (incluir adolescentes), riscos metodológicos (sobreposição construtual em \#1). PARE para aprovação.

DEPOIS: relatório em Markdown com:

1\. Sumário executivo (apenas Fato A com DOI/PMID confirmado)

2\. Definições operacionais com instrumentos e sobreposição construtual

3\. Evidências gerais sobre psicoterapia × QoL

4\. Tabela por modalidade: Tipo de evidência | Efeitos | Dissociação? | CEBM |

   Validade ecológica | Atribuição causal possível? | Limitações

5\. Mecanismos de mudança (técnica específica vs fator comum, foi medido?)

6\. Limitações metodológicas

7\. Evidence Ledger (Claim | Fonte | DOI/PMID? | CEBM | Val. ecológica | Sobreposição? | Atrib. causal? | Fato A/B/C | Status)

8\. Claims-to-Sources Table

9\. Referências APA 7

REGRAS NÃO-NEGOCIÁVEIS:

\- Nunca inventar DOI/PMID. Sem confirmação: \[NÃO VERIFICADO\]. Claims

  \[NÃO VERIFICADO\] não entram em Sumário/Conclusão.

\- Mudança estrutural \= Fato C salvo instrumento validado (SWAP/RFQ/AAI/OPD/IIP) \+ ≥2 anos \+ DOI/PMID.

\- Quando estudo não mede aliança/expectativa/efeito terapeuta/dose: proibido atribuir efeito à técnica específica. Usar "compatível com a intervenção, mas não distingue técnica específica de fatores comuns".

\- Para cada instrumento de QoL: classificar sobreposição com sintomas (baixa/moderada/alta).

\- Linguagem: sugere / compatível / hipótese / não estabelecido. Banir "eficaz/comprovado/superior" sem qualificação.

\- "Correlação não implica causalidade" em toda seção associativa.

\- Conclusão prudente, não-promocional.

---

## **9\. CHECKLIST DE QUALIDADE (auto-auditoria do orquestrador)**

Antes de aceitar output de qualquer motor:

* \[ \] \[BLOCO\_DE\_RISCO ACEITO\] aparece no início?  
* \[ \] Pass 1 parou em \[APROVAR\_PLANO\]?  
* \[ \] Pass 1 entregou strings de busca PT/EN concretas (não descritores soltos)?  
* \[ \] Pass 1 inclui subpergunta sobre sobreposição construtual?  
* \[ \] Pass 1 inclui adolescentes no critério de inclusão?  
* \[ \] Sumário Executivo contém apenas Fato A com Nível CEBM ≤3 e DOI/PMID confirmado?  
* \[ \] Cada claim do Evidence Ledger tem coluna "DOI/PMID confirmado?" preenchida?  
* \[ \] Nenhum DOI/PMID foi inventado? (verificação via Perplexity/PubMed)  
* \[ \] Tabelas incluem coluna "Validade ecológica"?  
* \[ \] Tabela de modalidades inclui "Sintomas vs QoL: dissociação?" e "Atribuição causal possível?"  
* \[ \] Tabela de mecanismos inclui "Técnica específica ou fator comum?" e "Foi medido no estudo?"  
* \[ \] **Regra E**: Claims sobre mudança estrutural indicam instrumento validado (SWAP/RFQ/AAI/OPD/IIP) \+ ≥2 anos \+ DOI/PMID? Sem isso \= Fato C?  
* \[ \] **Regra J**: Quando estudo não mede fatores comuns, atribuição é restrita à linguagem "compatível com, mas não distingue"?  
* \[ \] **Regra K**: Cada instrumento de QoL tem classificação de sobreposição (baixa/moderada/alta)?  
* \[ \] Comparações entre modalidades decompõem fatores comuns × específicos × efeito do terapeuta × allegiance?  
* \[ \] Estudos com sobreposição construtual sintoma×QoL foram sinalizados?  
* \[ \] Linguagem calibrada (sugere / compatível / hipótese / não estabelecido)?  
* \[ \] "Correlação não implica causalidade" em todas seções associativas?  
* \[ \] Pass 3 produziu Claims-to-Sources, Red Flags, Conclusão Revisada?  
* \[ \] Nota de Confiabilidade ≥3,5/5 em todas as dimensões?

Item falho → devolver ao motor com pedido específico de correção.

---

**Fim do Prompt Mestre Unificado v2.0 (Final).**
> **[Trecho removido antes da publicação]** Esta troca (2653 palavras) continha dados pessoais sensíveis (do autor ou de terceiros) e foi retirada a pedido do autor. Ver `docs/ANONIMIZACAO.md`.

> **[Trecho removido antes da publicação]** Esta troca (19092 palavras) continha dados pessoais sensíveis (do autor ou de terceiros) e foi retirada a pedido do autor. Ver `docs/ANONIMIZACAO.md`.

> **[Trecho removido antes da publicação]** Esta troca (18163 palavras) continha dados pessoais sensíveis (do autor ou de terceiros) e foi retirada a pedido do autor. Ver `docs/ANONIMIZACAO.md`.
