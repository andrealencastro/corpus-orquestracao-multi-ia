---
id: P04
titulo_original: "DG TCC ST4H"
grupo: pesquisa-academica
fonte: "Google Docs do autor (pasta IA/Conversas)"
criado_em_drive: 2026-04-24
modificado_em_drive: 2026-09-05
exportado_em: 2026-09-23
formato: "Markdown (exportação nativa do Google Docs)"
parte: "3/3"
trechos_removidos: 0
palavras_removidas: 0
redacoes: 11
licenca: CC-BY-4.0
---

> P04 · DG TCC ST4H — [parte 1](P04-dg-tcc-st4h_parte-1-de-3.md) · [parte 2](P04-dg-tcc-st4h_parte-2-de-3.md) · [**parte 3**](P04-dg-tcc-st4h_parte-3-de-3.md)

# ST4H Variação lexical, cognição e saúde mental

Eu:

Me ajude a transformar a pesquisa em anexo em um prompt para eu fazer uma pesquisa profunda sobre o tema dessa pesquisa e conseguir uma bibliografia

# ChatGPT 5.6 Deep Guide diz: [link removido]

### **1\) Diagnóstico 3D**

**Ambiguidade: 2/5.** O anexo já chegou a uma arquitetura bastante definida. A pesquisa profunda não deveria partir genericamente de “variação lexical, cognição e saúde mental”, porque isso abriria literatura demais. O núcleo que emerge do documento é uma pergunta mecanística: **o padrão aparentemente exploratório da busca semântica exige uma política estratégica de exploração ou pode emergir da estrutura da representação semântica e de busca local?**

O documento também separa corretamente os papéis dos três eixos: **computational cognition como pergunta científica principal; linguagem como sistema experimental; digital mental health como justificativa translacional**. Saúde mental fica como extensão exploratória, não como endpoint primário.

**Risco: 3/5.** É pesquisa acadêmica com implicações para saúde mental, mas o objetivo aqui é revisão de literatura e desenho de pesquisa, não decisão clínica.

O prompt abaixo foi desenhado principalmente para responder: **“qual é o estado real da evidência, quais são as teorias concorrentes, como testá-las e qual bibliografia eu preciso dominar?”**

---

### **2\) Arquitetura & Seleção (modelo/pipeline \+ técnica)**

Eu usaria **Deep Research com navegação**, e não uma resposta normal de LLM. A literatura necessária atravessa pelo menos seis corpos que normalmente aparecem separados:

**semantic fluency / semantic foraging → semantic networks / random walk → exploration–exploitation → individual differences & reliability → computational modeling → digital phenotyping / mental health.**

O ponto decisivo é obrigar a pesquisa a testar **duas explicações concorrentes**, em vez de simplesmente procurar artigos que confirmem “lexical exploration”. O próprio anexo identifica a oposição entre a família de **foraging/policy**, associada a Hills, e explicações de **censored random walk / representational structure**, associadas a Abbott/Austerweil.

Também incluí um bloco forte sobre **confiabilidade, model recovery e parameter recovery**, porque o documento identifica o *reliability paradox* como um risco central para qualquer tentativa de correlacionar diferenças individuais entre tarefas.

Minha sugestão é executar o prompt **em inglês**, porque isso melhora a recuperação de termos, autores e papers; porém pedir o **relatório final em português**, mantendo títulos, constructos técnicos e referências no idioma original.

---

### **3\) Prompt Final (Template Mestre)**

Abaixo está a versão que eu usaria.

# **SYSTEM ROLE**

You are a senior interdisciplinary research analyst specializing in cognitive science, computational cognitive neuroscience, psycholinguistics, semantic memory, reinforcement learning, computational psychiatry, and research methodology.

Your task is to conduct a rigorous, source-driven literature review that can support the theoretical framework and bibliography of an M2 research project.

Do not assume that the project's central hypothesis is true. Treat competing theoretical explanations symmetrically and actively search for evidence that could falsify each account.

# **CONTEXT**

The proposed project sits at the intersection of:

* semantic/verbal fluency;  
* semantic memory and lexical-semantic search;  
* exploration–exploitation and decision-making;  
* computational modeling;  
* individual differences;  
* reliability and construct validity;  
* language-derived digital phenotyping;  
* mental health as a secondary/translational application.

The scientific question is primarily one of **computational cognition**.

Language/semantic fluency is the **experimental system**.

Digital mental health is the **translational motivation**, not the primary clinical endpoint.

The central theoretical problem is:

> Does the apparently exploratory structure of semantic search require an individual strategic exploration policy, or can it emerge from the structure of semantic representations and local sampling/search alone?

A related cross-domain question is:

> If an individual-specific strategic exploration component exists in semantic search, does it converge with independently measured exploration in non-linguistic decision-making tasks?

A downstream, exploratory question is:

> What are the implications for interpreting language-derived measures as computational or digital phenotypes in mental-health research?

Do NOT presuppose that “lexical exploration” is already a validated construct.

# **RESEARCH OBJECTIVES**

Conduct a deep literature review that establishes the theoretical, empirical and methodological foundations necessary to evaluate this project.

The review must cover the following research streams.

## **A. Semantic search and semantic fluency**

Map the major theories and empirical findings concerning:

* semantic fluency;  
* category fluency;  
* clustering;  
* switching;  
* inter-response times / IRTs;  
* semantic distance;  
* semantic similarity;  
* lexical frequency effects;  
* semantic memory structure;  
* individual differences in semantic search.

Identify the seminal literature as well as major developments through **September 2026**.

Determine which behavioral signatures have traditionally been interpreted as evidence of strategic search.

## **B. Competing generative accounts of semantic search**

Investigate in depth the theoretical dispute between explanations based on:

### **Account 1 — Strategic / foraging-style exploration**

Including work related to:

* optimal foraging;  
* semantic foraging;  
* patch exploitation;  
* depletion;  
* switching;  
* search policies.

Pay particular attention to the work of Hills, Jones, Todd and related authors.

### **Account 2 — Representational / local-search emergence**

Including:

* semantic networks;  
* random walks;  
* censored random walks;  
* local sampling;  
* network topology;  
* representational structure.

Pay particular attention to Abbott, Austerweil, Griffiths and subsequent work building on or testing these models.

For these two model families:

1. explain their mathematical/computational assumptions;  
2. identify which empirical phenomena each model reproduces;  
3. determine whether the same behavioral signatures can be generated by both;  
4. identify existing direct model-comparison studies;  
5. identify findings that discriminate between them;  
6. identify unresolved controversies;  
7. determine what data would provide the strongest falsification test.

Do not infer a strategic cognitive mechanism merely because a model reproduces clustering or switching.

## **C. Exploration–exploitation outside language**

Review the computational literature on human exploration–exploitation, including:

* directed exploration;  
* random exploration;  
* information seeking;  
* uncertainty;  
* decision noise;  
* reward sensitivity;  
* explore–exploit tasks;  
* multi-armed bandits;  
* Horizon-task paradigms;  
* computational decomposition of exploration.

Pay particular attention to work associated with Wilson, Gershman and related researchers.

Explain which parameters or behavioral measures plausibly represent:

* directed exploration;  
* random exploration;  
* reward sensitivity;  
* uncertainty sensitivity.

Then investigate whether exploration parameters behave as stable **individual-difference measures**.

## **D. Cross-domain exploration**

Search specifically for evidence testing whether exploration is:

* domain-general;  
* domain-specific;  
* trait-like;  
* context-dependent.

Look for studies correlating exploration across:

* reinforcement-learning tasks;  
* bandit tasks;  
* information search;  
* semantic search;  
* memory search;  
* curiosity;  
* creativity/divergent thinking;  
* foraging;  
* other cognitive domains.

A key question is:

> Is there credible evidence for a shared individual-level exploration mechanism across semantic and non-semantic domains?

Report positive, null and contradictory evidence.

Do not interpret absence of correlation without considering measurement reliability.

## **E. Reliability and individual-difference measurement**

Review the literature on the reliability of cognitive-task parameters and individual differences.

Include:

* test–retest reliability;  
* internal reliability;  
* parameter uncertainty;  
* reliability paradox;  
* attenuation of correlations;  
* task impurity;  
* hierarchical estimation / partial pooling;  
* latent-variable approaches where appropriate.

Explicitly investigate work by Hedge et al., Enkavi et al., and later work that evaluates or challenges their conclusions.

Answer:

1. How reliable are behavioral measures of exploration?  
2. How reliable are computational model parameters?  
3. What reliability levels are necessary for credible cross-task correlations?  
4. What methodological solutions are recommended?  
5. Which proposed solutions do NOT actually solve the reliability problem?

Explain the implications for testing convergent and discriminant validity.

## **F. Dependence on semantic representation**

Investigate how measures of semantic search depend on the representation used to define semantic similarity or distance.

Compare at minimum:

* human association networks;  
* semantic networks;  
* LSA or related distributional methods;  
* static embeddings such as word2vec/GloVe;  
* contextual embeddings;  
* other commonly used semantic representations.

Search for evidence that conclusions about:

* clusters;  
* switches;  
* semantic distance;  
* individual rankings;  
* search strategies

change as a function of the chosen semantic representation.

Determine whether a **multiverse/specification-curve analysis across semantic representations** has been used or proposed.

Identify methodological recommendations for representation-robust inference.

## **G. Computational model evaluation**

Review best practices relevant to comparing the competing models.

Include:

* generative modeling;  
* model recovery;  
* parameter recovery;  
* identifiability;  
* posterior predictive checks;  
* simulation-based calibration where relevant;  
* cross-validation;  
* out-of-sample prediction;  
* model complexity;  
* model mimicry;  
* falsification;  
* hierarchical Bayesian modeling.

Explain which methods are essential for determining whether the strategic and representational models are empirically distinguishable.

Search for methodological literature in computational cognitive modeling, including work involving Palminteri, Wyart, Koechlin and other relevant authors where appropriate.

## **H. Timing and process-level data**

Investigate the evidential role of:

* inter-response times;  
* keystroke-level timing;  
* temporal dynamics;  
* pauses before switches;  
* response-order information.

Determine whether timing data discriminate strategic-foraging models from representational/random-walk accounts better than word sequences alone.

## **I. Existing datasets, software and reproducibility resources**

Identify existing open datasets, codebases and tools suitable for testing the project before new data collection.

Investigate, but do not limit the search to:

* semantic-fluency datasets;  
* Hills et al. datasets;  
* Abbott/Austerweil-related implementations;  
* forager / forager-analyses;  
* SNAFU or related semantic-network tools;  
* SWOW;  
* semantic association datasets;  
* Horizon-task implementations or datasets.

For every resource report:

* what it contains;  
* population/sample;  
* variables available;  
* whether individual-level data are available;  
* whether timing/IRT information is available;  
* license/access conditions;  
* code repository or persistent URL;  
* scientific papers describing the dataset/software.

Verify current software capabilities from the official repository/documentation rather than relying on secondary descriptions.

## **J. Mental health and digital phenotyping — secondary layer**

Only after establishing the computational and measurement literature, review how semantic/language measures have been used in:

* digital phenotyping;  
* computational psychiatry;  
* speech/language biomarkers;  
* depression;  
* anhedonia;  
* psychosis/schizophrenia;  
* negative symptoms;  
* cognitive dysfunction.

Distinguish carefully between:

1. predictive associations;  
2. diagnostic classification;  
3. symptom correlations;  
4. longitudinal sensitivity;  
5. mechanistic interpretation.

The key question is NOT:

> “Can language predict mental illness?”

The key question is:

> “Do language-derived computational markers used or proposed in digital mental health have a defensible interpretation in terms of underlying cognitive mechanisms?”

Identify studies that directly address construct/mechanistic validity rather than classification accuracy alone.

Treat mental-health associations as an exploratory or translational layer.

Do not imply that a language measure is a clinical biomarker merely because it correlates with symptoms.

# **SEARCH STRATEGY**

Use multiple complementary searches rather than a single query.

Search major scholarly sources and indexes accessible through the web, including where possible:

* PubMed;  
* PubMed Central;  
* Google Scholar records;  
* Crossref;  
* Semantic Scholar;  
* PsycINFO-related records;  
* Web of Science/Scopus metadata when accessible;  
* arXiv only when peer-reviewed versions are unavailable;  
* journal websites;  
* university repositories;  
* official GitHub repositories for software.

Use citation chaining:

1. identify seminal papers;  
2. inspect papers that cite them;  
3. inspect their reference lists;  
4. search for direct replications, critiques and competing models.

Use combinations of search terms such as:

"semantic fluency" AND exploration  
"semantic foraging"  
"optimal foraging" AND verbal fluency  
"semantic search" AND computational model  
"censored random walk" AND semantic fluency  
"semantic network" AND verbal fluency  
"semantic search" AND random walk  
"semantic search" AND individual differences  
"semantic fluency" AND inter-response time  
"exploration exploitation" AND individual differences  
"directed exploration" AND reliability  
"random exploration" AND reliability  
"Horizon task" AND test-retest  
"computational parameters" AND reliability  
"reliability paradox" cognitive tasks  
"semantic embeddings" AND fluency  
"semantic representation" AND clustering AND fluency  
"digital phenotyping" AND language AND construct validity  
"language biomarkers" AND mechanistic validation  
"speech biomarkers" AND computational psychiatry

Expand and modify these terms as the literature requires.

# **EVIDENCE RULES**

Classify important claims internally as:

**Fact A:** directly supported by a primary source, official repository/documentation, dataset paper, systematic review, or authoritative current source.

**Fact B:** supported by credible secondary literature or reasonable synthesis across sources.

**Fact C:** hypothesis, inference, speculation or unverified claim.

Do not present Fact C as established knowledge.

For disputed findings, show competing evidence.

For null findings, distinguish:

* evidence of absence;  
* absence of evidence;  
* inconclusive results due to low reliability or poor identifiability.

# **SOURCE PRIORITY**

Prioritize:

1. peer-reviewed primary research;  
2. systematic reviews/meta-analyses;  
3. seminal theoretical papers;  
4. methodological papers;  
5. official datasets/software documentation.

Use preprints when they are scientifically important or represent the most recent evidence, but clearly label them as preprints.

Avoid relying on:

* generic blogs;  
* SEO summaries;  
* unsourced websites;  
* AI-generated literature summaries.

# **CITATION VERIFICATION**

This requirement is critical.

For every paper included in the final bibliography, verify whenever possible:

* exact title;  
* authors;  
* year;  
* journal/conference;  
* volume/issue/pages or article number;  
* DOI;  
* PMID when applicable;  
* persistent URL.

Never invent a DOI.

If a DOI cannot be verified, write:

**DOI: Not verified**

Do not silently guess.

If a cited paper appears under multiple versions, identify the peer-reviewed version as primary and mention the preprint only if useful.

# **DELIVERABLE**

Write the final report in **Portuguese**, while preserving article titles, technical constructs and search terminology in the original language.

Structure the report as follows.

## **1\. Executive synthesis**

Maximum 1,500 words.

Explain:

* what the field currently knows;  
* what remains genuinely disputed;  
* whether the central project question is scientifically justified;  
* the strongest evidence for the strategic-search account;  
* the strongest evidence for the representational/local-search account;  
* the most important methodological threats;  
* the major gap the proposed M2 could address.

Do not oversell novelty.

## **2\. Conceptual map**

Create a structured map connecting:

semantic memory  
→ semantic fluency/search  
→ apparent exploration  
→ strategic-policy account vs representational account  
→ cross-domain exploration  
→ individual differences/reliability  
→ mechanistic validity  
→ digital mental-health implications.

## **3\. Historical development of the field**

Give a chronological account of the most important papers and conceptual shifts.

Distinguish:

* seminal/foundational work;  
* major competing theories;  
* modern computational developments;  
* current unresolved questions.

## **4\. Competing-model table**

Create a table with:

| Dimension | Strategic/Foraging account | Representational/Random-walk account |
| ----- | ----- | ----- |
| Core assumption |  |  |
| Main authors/papers |  |  |
| Mechanism |  |  |
| Key free parameters |  |  |
| Predicted behavioral signatures |  |  |
| Role of IRT/timing |  |  |
| Evidence supporting it |  |  |
| Evidence against it |  |  |
| Phenomena reproduced |  |  |
| Unique/falsifiable predictions |  |  |
| Current limitations |  |  |

## **5\. Exploration–exploitation and individual differences**

Explain the directed/random exploration distinction and evaluate evidence for stable individual differences.

Explicitly discuss whether cross-domain correlations are theoretically and psychometrically defensible.

## **6\. Reliability and validity**

Provide a dedicated methodological section covering:

* reliability paradox;  
* test-retest;  
* parameter uncertainty;  
* attenuation;  
* convergent validity;  
* discriminant validity;  
* model dependence.

Explain what the project would have to demonstrate before calling a lexical measure a “computational marker”.

## **7\. Semantic-representation sensitivity**

Compare the main semantic spaces/representations and assess whether model conclusions are representation-dependent.

Propose a reasonable specification-curve or multiverse strategy.

## **8\. Model-comparison methodology**

Explain how a rigorous study could compare the strategic and representational accounts using:

* simulations;  
* model recovery;  
* parameter recovery;  
* posterior predictive checks;  
* behavioral/timing signatures;  
* out-of-sample prediction.

Identify likely identifiability problems.

## **9\. Existing datasets and tools**

Create:

| Resource | Type | Data | Timing available? | Individual-level? | Relevant model | Open access? | Link | Key citation |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |

Highlight resources that could permit preliminary analyses without new data collection.

## **10\. Digital mental-health relevance**

Review the language/digital-phenotyping literature, but explicitly separate:

**prediction/classification** from **mechanistic validation**.

Explain why construct validity matters before interpreting language-derived measures as mental-health markers.

## **11\. Evidence gaps**

Identify 5–10 concrete unresolved questions.

For each, state whether it represents:

* a theoretical gap;  
* methodological gap;  
* measurement gap;  
* replication gap;  
* translational gap.

## **12\. Proposed positioning of the M2 project**

Based only on the evidence found, evaluate this tentative framing:

**Computational Mechanisms of Semantic Exploration: Distinguishing Strategic Search from Representational Structure through Cross-Domain Behavior**

Potential central question:

> Does semantic search require an individual strategic exploration policy, or can its apparent exploratory structure emerge from semantic representation and local search alone?

Potential secondary question:

> If a strategic individual component can be identified reliably, does it show convergent validity with independent measures of directed or random exploration?

Potential translational statement:

> Establishing what language-derived exploration measures actually measure is a prerequisite for interpreting them as computational markers in digital mental-health research.

State which parts are strongly supported, weakly supported, or need reformulation.

## **13\. Priority reading list**

Produce a curated bibliography divided into:

### **Tier 1 — Essential / Must read**

Approximately 15–25 papers indispensable for understanding and designing the project.

### **Tier 2 — Core supporting literature**

Approximately 30–50 papers covering the main theoretical and methodological streams.

### **Tier 3 — Extended / Specialized literature**

Additional papers relevant to specific subproblems.

For every Tier 1 paper include:

* full APA citation;  
* DOI/link;  
* 2–4 sentence summary;  
* why it matters specifically for this project;  
* which project component it informs:  
  * theory;  
  * semantic fluency;  
  * representational account;  
  * strategic exploration;  
  * RL/exploration;  
  * reliability;  
  * modeling;  
  * digital mental health.

## **14\. Bibliography by research stream**

Provide separate bibliographies for:

A. Semantic fluency and semantic search  
B. Semantic foraging  
C. Semantic networks / random walk  
D. Exploration–exploitation  
E. Individual differences and reliability  
F. Computational-model methodology  
G. Semantic representations  
H. Digital phenotyping / computational psychiatry  
I. Mental-health language markers

## **15\. Reference export**

At the end provide:

### **APA bibliography**

and, separately,

### **BibTeX**

for all Tier 1 references.

Only generate BibTeX fields that can be verified from the source.

## **16\. Claims-to-sources audit**

Create a final table:

| Important claim | Evidence | Key sources | Evidence strength | Caveat |
| :---: | :---: | :---: | :---: | :---: |

Include especially the claims on which the proposed project depends.

# **FINAL QUALITY CHECK**

Before finishing, verify that:

* both competing theoretical accounts received serious treatment;  
* null and contradictory evidence was included;  
* no association was transformed into a causal claim;  
* no DOI or reference was fabricated;  
* seminal literature was not omitted merely because it is old;  
* recent literature through September 2026 was actively searched;  
* preprints are clearly labeled;  
* the distinction between prediction and mechanistic explanation is preserved;  
* reliability and identifiability are treated as central, not peripheral;  
* the bibliography is actually useful for writing a research proposal rather than merely long.

If important evidence cannot be verified, explicitly write:

**Não verificado.**

The purpose of this research is not to prove the project correct. It is to determine whether the project is theoretically justified, experimentally discriminating, methodologically feasible, and grounded in the strongest available literature.

---

### **4\) Auditoria (Quality Gate)**

**Clareza:** alta. O prompt tem uma pergunta central, duas teorias concorrentes e define explicitamente o papel secundário da saúde mental.

**Especificidade:** alta. Ele procura desde Hills/Abbott e semantic foraging até directed/random exploration, confiabilidade, representações semânticas, model recovery e digital phenotyping. Isso corresponde à evolução do projeto no anexo, inclusive à preocupação de não transformar “switching” automaticamente em evidência de estratégia.

**Grounding:** forte. Uma decisão importante que mantive é não tratar bandit/explore–exploit como *ground truth*. O projeto deve investigar **validade convergente/discriminante entre métodos**, depois de estabelecer confiabilidade suficiente.

**Robustez:** o prompt exige evidência favorável, contraditória e nula, além de model mimicry, identificabilidade e dependência da representação semântica. Isso reduz bastante o risco de a Deep Research simplesmente produzir uma revisão confirmatória.

**Bibliografia:** este é um dos pontos fortes do prompt. Em vez de pedir apenas “referências”, ele deverá produzir **must-read list \+ bibliografia por subcampo \+ APA \+ BibTeX \+ DOI verificado \+ justificativa de cada paper**. Isso deve lhe dar não só uma lista extensa, mas uma **ordem de leitura**.

**Escopo:** deliberadamente não transformei a revisão em “bibliografia sobre depressão”. O anexo chega justamente à conclusão de que o M2 fica mais defensável quando a validade mecanística vem primeiro e os sintomas/mental health ficam exploratórios.

Eu começaria com **este único Deep Research**, não com vários prompts separados. O resultado dele deve revelar quais dos nove blocos bibliográficos realmente exigem uma segunda rodada específica. **Pronto para execução.**

# Claude Opus 5 Deep Guide diz: [link removido]

## **Veredito**

Prompt apto para execução após duas edições cirúrgicas — mas ele não está no caminho crítico, e executá-lo antes de enviar o e-mail ao PI inverte a prioridade do calendário.

## **Conflito de interesse (declarado antes da auditoria)**

O prompt codifica, como núcleo teórico, argumentos que saíram de mim no painel anexo: Abbott × Hills como tese e não como cuidado metodológico, o eixo de diferenças individuais como teste discriminante paralelo, IRT/keystroke, confundidores verbais, multiverso de representações. Auditar um artefato construído sobre as minhas próprias posições cai na mesma classe da **Regra 7 (anti-autoauditoria)** do Manual v1.0.

Consequência operacional: as duas edições abaixo são estruturais e de disciplina de evidência — não tocam na tese científica. A validação do conteúdo teórico (blocos B, C, D) não deve ser homologada por mim sozinho.

## **Violações e defeitos**

| \# | Achado | Evidência no artefato | Regra |
| ----- | ----- | ----- | ----- |
| 1 | Autocertificação pelo motor gerador | O bloco "4) Auditoria (Quality Gate)" foi escrito pelo mesmo motor que escreveu o bloco 3, e encerra com "Pronto para execução" | Regra 7 (v1.0) |
| 2 | Verificação delegada a um motor que não pode executá-la | `CITATION VERIFICATION` manda "verify… DOI" e "Never invent a DOI". Um agente de Deep Research não resolve DOI; ele reporta o que recuperou. O resultado é Fato A falso por construção | Defeito de desenho; reincide na Regra 7 (o motor certifica a própria citação) |
| 3 | Entregáveis de maior valor no fim da fila | §13 (Tier 1), §14, §15 (BibTeX) e §16 (claims audit) são os últimos itens. Deep Research trunca pelo fim. O que sobra é o texto discursivo; o que se perde é a bibliografia — que é o objetivo declarado da tarefa | — |
| 4 | Volume incompatível com verificação | 15–25 \+ 30–50 \+ Tier 3, todos com metadados completos. É o vetor de fabricação mais conhecido em literaturas de nicho | — |
| 5 | §12 pede ao motor que avalie o enquadramento do próprio projeto | "State which parts are strongly supported…" — pergunta de validação, não de literatura. Motores respondem a isso com complacência | Aproxima-se da Regra 7 por procuração |
| 6 | Ancoragem em autores | Bloco G nomeia Palminteri, Wyart e Koechlin em literatura metodológica de milhares de itens. Não é critério científico; é o laboratório-alvo | Risco de viés (não coberto por regra canônica) |
| 7 | Sem log de buscas | Sem as queries executadas e as que voltaram vazias, a Etapa 3 não consegue auditar cobertura — só consegue auditar o que foi entregue | — |

**Defeito de governança verificado agora**, não por memória: o próprio `Regras_para_o_Manual_do_Orquestrador.pdf` numera as regras de duas formas incompatíveis. A lista de cabeçalho tem 5 regras ("anti-nomenclatura vazia" \= 5, sem regra interface/backend); a lista consolidada tem 7 ("interface/backend" \= 5, "anti-nomenclatura vazia" \= 6, "anti-autoauditoria" \= 7). Qualquer citação "Regra N" é ambígua até isso ser resolvido. Não há Regra 10 canônica: o limite de \~2k tokens para o Perplexity é prosa dentro da Regra 4, não regra numerada.

Na matriz, duas linhas cobrem esta tarefa e discordam: *"Deep Research / revisão bibliográfica → Gemini DR → ChatGPT/Claude auditor"* e *"Deep Research Acadêmico → Gemini → Claude → ChatGPT"*. Adote a primeira aqui — o produto é bibliografia verificável, não um artefato a ser reconsolidado pelo ChatGPT.

## **Edição 1 — substitui o bloco `DELIVERABLE`**

DELIVERABLE — OUTPUT DISCIPLINE

Produce output in this exact order. If budget runs short, truncate from the END,

never from the beginning.

1\. Search log: every query executed, index/source queried, number of usable hits.

&nbsp;&nbsp;&nbsp;Report queries that returned nothing.

2\. Claims-to-sources audit table, restricted to claims the proposed project depends on.

3\. Tier 1 reading list — MAXIMUM 20 papers. Full APA citation, identifiers,

&nbsp;&nbsp;&nbsp;Retrieval Status, 2-4 sentence summary, project component informed.

4\. Competing-model table (strategic/foraging vs representational/random-walk).

5\. Tier 2 (max 40\) and Tier 3 (max 30): citation \+ identifier ONLY.

&nbsp;&nbsp;&nbsp;No summaries, no annotations.

6\. Executive synthesis, maximum 1,200 words.

7\. Remaining analytical sections in the original order.

8\. BibTeX for Tier 1 only.

Hard constraints:

\- Never exceed 20 annotated papers. Volume of annotated references is not a

&nbsp;&nbsp;quality signal; unverifiable metadata is a disqualifying defect.

\- Do NOT evaluate, endorse or rank the proposed M2 framing. Replace that section with:

&nbsp;&nbsp;"Elements of the proposed framing that the retrieved literature does NOT support."

&nbsp;&nbsp;List only unsupported or contested elements. If you find none, say so explicitly

&nbsp;&nbsp;and state what evidence would have been required to find one.

\- State the actual execution date and report coverage relative to it. Do not claim

&nbsp;&nbsp;coverage of a period you did not search.

## **Edição 2 — substitui o bloco `CITATION VERIFICATION`**

CITATION VERIFICATION — SCOPE LIMIT

You cannot verify a DOI. Resolving an identifier requires a request to a resolver,

which you are not performing. Do not state or imply that any identifier is verified.

Assign every reference a Retrieval Status:

\- RETRIEVED — metadata read from a page you opened in this session. Give URL \+ access date.

\- INDEXED   — metadata from a search result, aggregator or reference list, source page not opened.

\- RECALLED  — metadata produced without retrieval in this session.

RECALLED references are inadmissible in Tier 1 and go to a separate list:

"Unretrieved — requires external verification."

Never write an identifier you did not read on a page you opened. Otherwise write

"DOI: not retrieved."

Do not produce a self-assessment, confidence score, readiness statement, or quality

rating of your own output. Report Retrieval Status and nothing else.

A resolução real dos DOIs sai daqui e vai para o Perplexity, um claim por chamada — que é exatamente o uso permitido pela Regra 4, e nunca com este prompt inteiro colado.

Duas edições. Zero regeneração. Roteamento: Gemini Deep Research, single-shot, prompt fechado → Etapa 3 comigo sobre o Evidence Ledger → Perplexity para os identificadores do Tier 1\.

## **O ponto que importa mais que a auditoria**

Este prompt não decide nada. Rodá-lo produz uma bibliografia excelente para uma proposta que ainda não tem interlocutor, e nenhum dos seus 16 blocos altera a resposta à única pergunta aberta hoje: existe janela no LNC² para janeiro de 2027\.

O caminho crítico tem dois itens, ambos verificáveis sem financiamento e sem ética:

1. A análise de identificabilidade nos dados públicos do `forager-analyses` (Hills et al. 2012, Lundin et al. 2020). Se as matrizes de confusão saírem turvas, a pergunta central muda — e isso você descobre em outubro, com uma figura na mão para a reunião, em vez de descobrir em abril.  
2. Os dois e-mails redigidos em 4 de setembro — Palminteri/Wyart e o coordenador DMH — que, até onde este pipeline registra, não saíram. É o mesmo estado do e-mail ao Benchenane, que atravessa sessões sem bloqueador declarado.

Gerar um novo artefato de pesquisa enquanto dois e-mails prontos esperam é o padrão que a **Regra 2 (anti-meta-trabalho)** nomeia. O gargalo não é a qualidade do prompt.

## **Entrada para o log de governança**

\[2026-09-05\] Auditoria — prompt Deep Research "Semantic exploration / construct validity"

Autor do artefato: ChatGPT 5.6. Auditor: Claude. Conflito de interesse DECLARADO

(o núcleo teórico auditado tem origem em outputs do próprio Claude; validação de

conteúdo não homologada por Claude isoladamente).

Veredito: apto após 2 edições cirúrgicas. Sem regeneração.

Violações: Regra 7 (autocertificação "Pronto para execução" pelo motor gerador;

verificação de DOI delegada ao motor executor). Defeitos: ordenação do deliverable

expõe a bibliografia a truncamento; volume de referências anotadas incompatível

com verificação; ausência de log de queries; ancoragem em autores do laboratório-alvo.

Roteamento aplicado: Gemini DR single-shot \-\> auditoria Claude (Etapa 3\) \-\>

Perplexity para identificadores Tier 1 (1 claim/chamada, Regra 4).

Defeito de governança CONFIRMADO em fonte: numeração de regras divergente dentro do

próprio Regras\_para\_o\_Manual\_do\_Orquestrador.pdf (lista de cabeçalho \= 5 regras;

lista consolidada \= 7, com "interface/backend" ausente da primeira). Citações "Regra N"

ambíguas até correção. Não existe Regra 10 canônica; o limite de 2k tokens do Perplexity

é prosa interna à Regra 4\.

Matriz: duas linhas conflitantes para "Deep Research / revisão bibliográfica" vs

"Deep Research Acadêmico". Precedência aplicada ad hoc; defeito de precedência permanece aberto.

Prioridade declarada: execução do prompt NÃO está no caminho crítico. Itens bloqueantes:

(a) recovery/identificabilidade em forager-analyses; (b) envio dos e-mails Palminteri/Wyart

e coordenador DMH, redigidos em 04/09 e não enviados.

# ChatGPT 5.6 Deep Guide diz: [link removido]

### **1\) Diagnóstico 3D**

**Ambiguidade: 1/5. Risco: 3/5.** Interpreto que você quer saber se a auditoria do Claude deve ser aceita antes de executar a pesquisa.

Meu veredito é: **aceitar a direção da auditoria, mas não aceitar literalmente as duas edições como escritas**. Há correções importantes no parecer do Claude — e uma delas muda o protocolo de referências.

| Ponto do Claude | Parecer |
| ----- | ----- |
| Autocertificação do meu Quality Gate | **Procede em parte.** Eu não deveria ter usado meu próprio Quality Gate como certificação independente. Um checklist determinístico pode continuar existindo; “clareza alta / robustez forte” não deve funcionar como homologação externa. |
| “Você não pode verificar um DOI” | **Não procede como regra geral.** Um agente com web pode efetivamente testar resolução de DOI. |
| Bibliografia no fim | **Procede.** O objetivo principal é bibliografia; entregáveis críticos devem vir cedo. A alegação específica de que “Deep Research trunca pelo fim” não foi demonstrada e deve ser tratada como hipótese operacional, não fato. |
| 15–25 \+ 30–50 \+ Tier 3 anotados | **Procede.** Era volume excessivo para anotação rigorosa. |
| §12 convidava validação complacente | **Procede como risco de viés**, embora não seja tecnicamente “autoauditoria”. Reformular como busca ativa de elementos não sustentados é melhor. |
| Ancoragem Palminteri/Wyart/Koechlin | **Procede.** O laboratório-alvo não deve determinar a literatura metodológica recuperada. |
| Falta de search log | **Procede no objetivo**, mas a solução do Claude é forte demais: o sistema pode não expor todas as queries internas nem contagem de hits. Não deve inventá-las. |
| Numeração inconsistente do Manual | **Confirmado.** |

Sobre este último ponto: há efetivamente versões incompatíveis dentro do material. Uma seção identificada como **“Manual do Orquestrador v1.0 — 11 maio 2026”** apresenta cinco regras, terminando em anti-nomenclatura vazia. Em outra consolidação aparecem sete regras, sendo a sétima anti-autoauditoria. E o mesmo corpus ainda contém uma tabela posterior de “regras adicionais” numeradas 8–13, incluindo uma “Regra 10” sobre Perplexity ≥2k tokens.

Portanto, Claude está certo na conclusão prática: **não cite “Regra 7”, “Regra 10” etc. como se a numeração fosse canônica**. Cite pelo nome da regra até o Manual ser normalizado.

Há, porém, uma nuance: a regra anti-autoauditoria consolidada diz que o problema ocorre quando **o motor é também o objeto avaliado** — Claude avaliando Claude, ChatGPT avaliando ChatGPT etc. Nesta pesquisa, Claude não é o objeto científico. O problema é mais sutil: parte da tese foi formulada por Claude e Claude depois a audita. Isso justifica um auditor independente, mas é uma **extensão prudencial** da regra, não sua aplicação literal.

---

### **2\) Arquitetura & Seleção (modelo/pipeline \+ técnica)**

A escolha de **Gemini Deep Research single-shot** é coerente com o seu corpus operacional, que explicitamente reserva Gemini para scoping, exploração ampla e Deep Research com prompt fechado. A sua própria matriz também tem uma linha específica para “Deep Research / revisão bibliográfica” que começa com Gemini Deep Research; a existência de outra linha “Deep Research Acadêmico” com sequência diferente confirma o defeito de precedência apontado pelo Claude.

Eu usaria, para esta tarefa:

**Gemini Deep Research → auditor independente do Evidence Ledger → resolução dos identificadores problemáticos.**

Não transformaria **Perplexity** em etapa obrigatória para todos os DOIs. O Manual sustenta seu uso para “busca factual pontual” e “descoberta de fontes”, mas não estabelece de forma canônica “um DOI por chamada”.

Mais importante: a Edição 2 do Claude confunde **recuperar metadata** com **resolver um DOI**. Hoje, a documentação oficial do Gemini confirma que Deep Research usa Google Search como fonte por padrão e realiza pesquisa web em tempo real. ([Ajuda do Google](https://support.google.com/gemini/answer/15719111?hl=en&utm_source=chatgpt.com)) E a própria Crossref diz que a forma mais rápida de verificar se um DOI está ativo é abrir o link `doi.org/...` e verificar se ele resolve corretamente. ([www.crossref.org](https://www.crossref.org/documentation/register-maintain-records/verify-your-registration/?utm_source=chatgpt.com))

Logo, a regra correta não é:

> “You cannot verify a DOI.”

É:

> **“Do not claim that a DOI was resolved unless you actually opened/tested the DOI or inspected an authoritative DOI record during this research session.”**

Isso é muito mais auditável.

Também corrigiria o search log. Pedir “**every query executed \+ number of usable hits**” corre o risco de obrigar o modelo a inventar telemetria interna. A documentação oficial descreve plano de pesquisa, pesquisa em várias fontes e relatório, mas não promete exposição integral de todas as queries internas ou de suas contagens de resultados. ([Ajuda do Google](https://support.google.com/gemini/answer/15719111?hl=en&utm_source=chatgpt.com))

Há ainda um defeito lógico na própria auditoria do Claude: ele identifica a **ancoragem em autores do laboratório** como problema \#6, mas suas “duas edições cirúrgicas” **não removem o trecho original que nomeia Palminteri, Wyart e Koechlin**. Portanto, “duas edições e zero mais” deixa um defeito reconhecido pelo próprio auditor. A solução é incorporar a desancoragem dentro da Edição 1, sem criar uma terceira rodada.

Quanto ao parágrafo de Claude sobre e-mails e “caminho crítico”: eu o manteria **fora desta auditoria do prompt**. O anexo realmente chega a uma pergunta central estreita — policy/foraging versus representational/local-search, com keystrokes, recovery e specification curve — e identifica uma concept note ao PI como próximo artefato útil. Mas decidir que os e-mails têm prioridade sobre a revisão bibliográfica é uma decisão de gestão do projeto, não um defeito do prompt.

---

### **3\) Prompt Final (Template Mestre)**

Eu **não regeneraria o prompt**. Preservaria a Edição 1 do Claude, mas incorporaria nela a desancoragem e a correção do search log; e substituiria a Edição 2 pela versão abaixo.

## **DELTA PARA A EDIÇÃO 1**

Replace item 1 of DELIVERABLE with:

1. Search log: report the search queries, search terms, databases/indexes, websites, citation-chaining paths, and other retrieval actions that were explicitly issued or are observable during this research session.  
   * Do not invent hidden/internal queries, tool calls, search-result counts, or hit counts.  
   * If the research system does not expose an exact query or result count, write: "Not exposed by the research interface."  
   * Report deliberately attempted searches that returned no usable evidence when this information is observable.

Add to Hard constraints:

* Author names supplied in the research brief are search seeds, not preferred authorities. Do not privilege authors because of affiliation with the target laboratory. Include their work only when it satisfies the same relevance and evidence criteria applied to the rest of the literature.  
* Expand searches beyond the named authors and actively look for competing research groups, critiques, replications, alternative models, and null findings.

## **REPLACEMENT FOR EDIÇÃO 2**

CITATION & IDENTIFIER VERIFICATION — RETRIEVAL STATES

Do not describe an identifier as verified merely because it appears in generated text, a search snippet, a bibliography, or an aggregator.

Assign every Tier 1 reference one Retrieval Status:

* RESOLVED — the DOI URL was actually opened/tested during this research session and resolved to a landing page whose bibliographic metadata is consistent with the cited work. Report DOI URL \+ landing-page source \+ access date.  
* RETRIEVED\_PRIMARY — the article page, publisher page, journal page, Crossref record, PubMed record, or other authoritative bibliographic record was opened during this research session and its metadata was read directly. If the DOI itself was not tested through a resolver, write "DOI resolution: not tested."  
* INDEXED — metadata was obtained only from a search result, secondary index, aggregator, citation list, or another paper; the authoritative record was not opened.  
* UNRETRIEVED — the reference originated from model recall or could not be retrieved during this research session.

Tier 1 may contain only RESOLVED or RETRIEVED\_PRIMARY references.

INDEXED references may appear in Tier 2 or Tier 3 only when clearly labeled.

UNRETRIEVED references must be moved to a separate section:  
"Unretrieved — requires external verification."

Never write a DOI that was not read from an opened source during this research session.

If an identifier was not retrieved, write:  
"DOI: not retrieved."

If a DOI was retrieved but its resolver was not tested, write:  
"DOI resolution: not tested."

Do not infer, reconstruct, autocomplete, or guess DOI strings.

Do not produce a confidence score, readiness rating, self-approval statement, or independent quality certification of your own report. Provide the evidence states above so that a separate auditor can evaluate the output.

Esse delta mantém a intenção do Claude, mas separa quatro coisas que estavam misturadas: **retrieval**, **fonte primária**, **DOI recuperado** e **DOI efetivamente resolvido**.

---

### **4\) Auditoria (Quality Gate)**

Aqui eu não usaria este bloco como “aprovação pelo próprio gerador”. O resultado verificável é o seguinte: a **Edição 1 corrigida** cobre ordenação, volume, search log, §12 e ancoragem; a **Edição 2 corrigida** impede DOI inventado sem proibir uma verificação que o executor pode realmente executar; e a nomenclatura das regras deixa de depender da numeração inconsistente do Manual.

Há uma segunda melhora importante: o relatório não deve prometer “cobertura até setembro de 2026” abstratamente. Ele deve registrar a **data real da execução** e quais bases/fontes foram efetivamente pesquisadas. Isso preserva a boa correção do Claude.

Também concordo em não fazer nova rodada de reformulação científica do prompt. A pergunta central já está estabilizada no próprio projeto como disputa entre **foraging/policy** e **representational/local-search**, com uma segunda linha de evidência baseada em generalização para exploração não linguística. Agora o valor marginal está no relatório e no Evidence Ledger, não em uma v2 do superprompt.

**Do ponto de vista da engenharia do prompt: pronto para execução.** Isso significa “o artefato está fechado”, não “a hipótese científica foi validada”.

# Claude Opus 5 Deep Guide diz: [link removido]

## **Veredito**

Aceito a auditoria da auditoria: recuo em quatro pontos, um deles um erro factual meu que verifiquei agora. O artefato fecha aqui — a Regra de parada 2/3 dispara e a próxima ação é executar, não revisar.

## **Onde recuo**

| Ponto | Estado |
| ----- | ----- |
| "You cannot verify a DOI" | **Recuo integral.** A instrução era falsa para um executor com navegação. Confundi *recuperar metadado* com *resolver identificador*. A taxonomia de quatro estados (RESOLVED / RETRIEVED\_PRIMARY / INDEXED / UNRETRIEVED) é superior à minha de três e resolve o problema real sem proibir o que o motor consegue fazer. |
| Search log com "every query \+ hit counts" | **Recuo.** Eu exigi telemetria que a interface pode não expor — isto é, criei um incentivo à confabulação dentro de um bloco cuja função era impedi-la. Defeito do mesmo tipo que audito nos outros. |
| Ancoragem em autores não removida pelas minhas duas edições | **Recuo.** Nomeei o defeito \#6 e nenhuma das edições o tocava. "Duas edições, zero regeneração" deixava um defeito reconhecido em aberto. A desancoragem entra na Edição 1 sem abrir rodada nova. |
| "Deep Research trunca pelo fim" | **Reclassificado para Fato B.** Não demonstrei. A reordenação permanece porque não depende do mecanismo: entregável crítico primeiro é correto sob qualquer hipótese de corte. |

## **Erro factual meu**

Escrevi: *"Não existe Regra 10 canônica."* É falso, e a verificação está no próprio arquivo. Havia uma tabela adicional numerada 8–13 que meu grep anterior não pegou, porque as linhas usam o número nu, sem a palavra "Regra":

* **8** — "Em pipelines onde Claude é simultaneamente auditor e tema, exigir auditor externo cego." Origem: Bias \#7. Status: Fato B.  
* **9** — "Gargalo do orquestrador: se 2 motores sinalizaram parada e você ainda quer iterar, anote a iteração como decisão humana." Status: **Fato A**, empírico, 4/4 conversas.  
* **10** — "Perplexity excluído da classe 'revisão de prompts ≥ 2k tokens' até resolver truncamento." Status: **Fato A**.  
* **12** — anti-nomenclatura sem definição operacional (duplica em conteúdo a regra 6 da lista consolidada).  
* **13** — Gemini em consulta única para scoping, dispensado a partir do turno 2\. Status: Fato A.

O fecho daquela seção diz explicitamente: *"as 7 regras do ChatGPT \+ as 6 acima"*. O conjunto pretendido é de 13 regras. O ChatGPT está certo, eu estava errado, e o defeito de numeração é pior do que descrevi: **três** conjuntos incompatíveis no mesmo arquivo (cabeçalho com 5, consolidação com 7, complemento 8–13), com duplicação de conteúdo entre 6 e 12\. A recomendação prática dele — citar pelo nome até normalizar — fica mantida e reforçada.

## **Onde não recuo**

**Conflito de interesse.** Ele acertou que a Regra anti-autoauditoria não se aplica literalmente — Claude não é o objeto científico aqui. Mas nós dois erramos o instrumento: existe a **Regra 8**, que cobre "Claude simultaneamente auditor e tema" e exige auditor externo cego. Não precisa de regra nova. Precisa de uma emenda de uma cláusula, porque "tema" ainda não é exatamente o caso: aqui Claude é auditor e **originador da tese auditada**. Emenda proposta, para colar:

> **Regra 8 (emenda):** vale também quando o motor não é o tema, mas é autor de parte substantiva da tese, do desenho ou do critério que está auditando. Nesse caso a auditoria estrutural é admissível; a homologação do conteúdo exige segundo auditor.

**Prioridade de execução.** Ele diz que é decisão de gestão, não defeito do prompt. Concedo a colocação: não era defeito do prompt e não devia estar na tabela de defeitos. Não concedo a substância — a Regra 9 é Fato A com base empírica de 4/4, e sinalizar isso é função do auditor, não editorial. Fica no log de governança, fora da auditoria do artefato.

**Quality Gate.** Ele recusou explicitamente usar o próprio bloco 4 como homologação e qualificou o "pronto para execução" como fechamento de artefato, não validação de hipótese. Isso corrige o comportamento que flaguei. Sem violação nesta rodada.

## **Uma linha acrescentada, e é a última**

O estado RESOLVED dele exige metadado "consistent with the cited work", mas não diz o que fazer quando o DOI resolve para **outro** trabalho. Esse é o padrão exato da fabricação plausível: identificador válido, artigo errado. Silenciosamente descartado, some do relatório; reportado, é o sinal mais barato de alucinação que existe.

## **Patch consolidado — colar no prompt**

DELIVERABLE — OUTPUT DISCIPLINE

Produce output in this exact order. If budget runs short, truncate from the END,

never from the beginning.

1\. Search log: report the search queries, search terms, databases/indexes, websites,

&nbsp;&nbsp;&nbsp;citation-chaining paths, and other retrieval actions explicitly issued or observable

&nbsp;&nbsp;&nbsp;during this research session. Do not invent hidden/internal queries, tool calls, or

&nbsp;&nbsp;&nbsp;result counts. Where the research system does not expose an exact query or count,

&nbsp;&nbsp;&nbsp;write: "Not exposed by the research interface." Report deliberate searches that

&nbsp;&nbsp;&nbsp;returned no usable evidence when observable.

2\. Claims-to-sources audit table, restricted to claims the proposed project depends on.

3\. Tier 1 reading list — MAXIMUM 20 papers. Full APA citation, identifiers,

&nbsp;&nbsp;&nbsp;Retrieval Status, 2-4 sentence summary, project component informed.

4\. Competing-model table (strategic/foraging vs representational/random-walk).

5\. Tier 2 (max 40\) and Tier 3 (max 30): citation \+ identifier ONLY. No annotations.

6\. Executive synthesis, maximum 1,200 words.

7\. Remaining analytical sections in the original order.

8\. BibTeX for Tier 1 only.

Hard constraints:

\- Never exceed 20 annotated papers. Volume of annotated references is not a quality

&nbsp;&nbsp;signal; unverifiable metadata is a disqualifying defect.

\- Author names supplied in this brief are search seeds, not preferred authorities. Do

&nbsp;&nbsp;not privilege authors because of affiliation with any target laboratory. Include their

&nbsp;&nbsp;work only when it meets the same relevance and evidence criteria as everything else.

&nbsp;&nbsp;Actively search beyond the named authors for competing groups, critiques,

&nbsp;&nbsp;replications, alternative models and null findings.

\- Do NOT evaluate, endorse or rank the proposed M2 framing. Replace that section with:

&nbsp;&nbsp;"Elements of the proposed framing that the retrieved literature does NOT support."

&nbsp;&nbsp;List only unsupported or contested elements. If you find none, say so explicitly and

&nbsp;&nbsp;state what evidence would have been required to find one.

\- State the actual execution date and which sources/indexes were in fact searched. Do

&nbsp;&nbsp;not claim coverage of a period you did not search.

CITATION & IDENTIFIER VERIFICATION — RETRIEVAL STATES

Do not describe an identifier as verified merely because it appears in generated text,

a search snippet, a bibliography, or an aggregator.

Assign every Tier 1 reference one Retrieval Status:

RESOLVED — the DOI URL was opened/tested during this session and resolved to a landing

&nbsp;&nbsp;page whose bibliographic metadata matches the cited work. Report DOI URL \+

&nbsp;&nbsp;landing-page source \+ access date.

RETRIEVED\_PRIMARY — the article page, publisher page, Crossref record, PubMed record or

&nbsp;&nbsp;other authoritative bibliographic record was opened this session and its metadata read

&nbsp;&nbsp;directly. If the DOI itself was not tested, write "DOI resolution: not tested."

INDEXED — metadata obtained only from a search result, secondary index, aggregator,

&nbsp;&nbsp;citation list or another paper; the authoritative record was not opened.

UNRETRIEVED — the reference came from model recall or could not be retrieved this session.

MISMATCH — the identifier resolved, but to a work other than the one cited. Report the

&nbsp;&nbsp;attempted identifier, the work it actually resolved to, and the citation that produced

&nbsp;&nbsp;it. Never silently drop or repair a mismatch.

Tier 1 may contain only RESOLVED or RETRIEVED\_PRIMARY references.

INDEXED references may appear in Tier 2 or 3 only when clearly labeled.

UNRETRIEVED and MISMATCH references go to a separate section:

"Unretrieved — requires external verification."

Never write a DOI that was not read from a source opened this session. If not retrieved,

write "DOI: not retrieved." If retrieved but the resolver was not tested, write

"DOI resolution: not tested." Do not infer, reconstruct, autocomplete or guess DOI strings.

Do not produce a confidence score, readiness rating, self-approval statement or quality

certification of your own report. Provide the evidence states above so that a separate

auditor can evaluate the output.

## **Parada**

Dois motores convergiram sobre a mesma arquitetura de patch e o delta desta rodada foi correção de execução, não de estrutura. A Regra de parada 2/3 proíbe a próxima iteração. Roteamento: Gemini Deep Research, single-shot, prompt fechado com os dois blocos acima substituídos. O output volta para auditoria do Evidence Ledger — e, pela emenda à Regra 8, a homologação do conteúdo teórico não é minha.

\[2026-09-05\] Correção da entrada anterior — mesma auditoria

ERRO FACTUAL CORRIGIDO: a entrada de 05/09 afirmou "não existe Regra 10 canônica".

Falso. Verificado em Regras\_para\_o\_Manual\_do\_Orquestrador.pdf: tabela complementar

numerada 8-13, de autoria Claude em sessão anterior, com item 9 (gargalo do

orquestrador, Fato A, 4/4 conversas), item 10 (Perplexity excluído de "revisão de

prompts \>=2k tokens", Fato A), item 13 (Gemini dispensado a partir do turno 2, Fato A).

Conjunto pretendido \= 7 (ChatGPT) \+ 6 (Claude) \= 13 regras.

Causa do erro: grep por "Regra 1\[0-9\]"; a tabela usa numeração nua. Padrão documentado

de near-miss do Claude; detectado por auditor externo (ChatGPT 5.6), não por autoauditoria.

DEFEITO DE NUMERAÇÃO AGRAVADO: três conjuntos incompatíveis no mesmo arquivo (5 / 7 / 8-13),

com duplicação de conteúdo entre a regra 6 e o item 12\. Citar regras por NOME até normalizar.

CONFLITO DE INTERESSE RECLASSIFICADO: instrumento correto e a Regra 8 (Claude auditor e tema,

auditor externo cego), nao a regra anti-autoauditoria. Emenda proposta: estender a Regra 8

ao caso de auditor que e originador da tese. Auditoria estrutural admissivel; homologacao

de conteudo exige segundo auditor.

RECUOS ACEITOS: proibicao de verificar DOI (falsa); search log com contagem de hits

(convidava telemetria inventada); desancoragem de autores ausente das duas edicoes

(defeito logico proprio); "DR trunca pelo fim" reclassificado Fato A \-\> Fato B.

ADICAO FINAL: estado MISMATCH (identificador resolve para obra diferente da citada).

STATUS: artefato fechado. Regra de parada 2/3 disparada. Proxima acao \= executar em

Gemini Deep Research. Nova rodada de refinamento do prompt \= decisao humana registravel

sob a regra do gargalo do orquestrador, nao necessidade metodologica.

# ChatGPT 5.6 Deep Guide diz: [link removido]

### **1\) Diagnóstico 3D**

**Ambiguidade: 1/5. Risco: 3/5.**

Concordo com o fechamento do Claude. Nesta rodada houve **convergência substantiva entre dois motores**, e o único delta novo — `MISMATCH` — corrige um caso real de falha sem alterar a arquitetura do prompt.

Não vejo justificativa metodológica para uma nova rodada de refinamento.

### **2\) Arquitetura & Seleção (modelo/pipeline \+ técnica)**

O pipeline final fica bem definido:

**Gemini Deep Research — single-shot, prompt fechado**  
→ **Evidence Ledger / relatório com estados de recuperação**  
→ **auditoria independente do conteúdo teórico**  
→ verificação externa apenas dos identificadores que permanecerem problemáticos.

A taxonomia final ficou especialmente boa porque agora distingue cinco estados operacionais:

* `RESOLVED`  
* `RETRIEVED_PRIMARY`  
* `INDEXED`  
* `UNRETRIEVED`  
* `MISMATCH`

O `MISMATCH` é importante porque impede um erro silencioso particularmente perigoso: **DOI sintaticamente válido que leva a outro artigo**.

Também considero acertado o abandono de citações do tipo “Regra 7” ou “Regra 10” enquanto o Manual não tiver uma numeração normalizada. Até lá, use os **nomes operacionais das regras**.

### **3\) Prompt Final (Template Mestre)**

**Não faria nova regeneração.**

A versão final deve ser exatamente:

1. o prompt mestre anterior;  
2. com `DELIVERABLE` substituído pelo bloco consolidado do Claude;  
3. com `CITATION & IDENTIFIER VERIFICATION` substituído pelo bloco consolidado que inclui `MISMATCH`;  
4. sem outras mudanças científicas, estilísticas ou estruturais.

Há apenas um detalhe editorial que eu **não corrigiria agora**, justamente pela regra de parada: `MISMATCH` é colocado sob o cabeçalho `"Unretrieved — requires external verification"`, embora tecnicamente tenha sido recuperado e resolvido. É semanticamente imperfeito, mas não prejudica execução nem auditabilidade. Mexer nisso agora seria refinamento cosmético.

### **4\) Auditoria (Quality Gate)**

O estado atual atende aos requisitos funcionais importantes:

**Objetivo protegido:** a bibliografia e o ledger aparecem antes das seções discursivas.

**Controle de fabricação:** referências Tier 1 precisam ter evidência recuperada em sessão.

**DOI:** não pode ser reconstruído ou adivinhado.

**DOI errado:** passa a ser explicitamente registrado como `MISMATCH`.

**Telemetria:** o executor não é obrigado a inventar queries ou contagens que a interface não revela.

**Viés de autoridade:** autores nomeados são seeds, não autoridades preferenciais.

**Viés confirmatório:** o executor deve buscar críticas, modelos concorrentes, replicações e resultados nulos.

**Auto-homologação:** removida.

**Volume:** limitado a um número verificável de referências anotadas.

**Cobertura temporal:** deve refletir o que realmente foi pesquisado, não uma promessa abstrata.

O ponto mais importante é que uma terceira rodada provavelmente produziria apenas alterações de redação, não aumento material de rigor.

**Pronto para execução.**

# Tab 31

# **SYSTEM ROLE**

You are a senior interdisciplinary research analyst specializing in cognitive science, computational cognitive neuroscience, psycholinguistics, semantic memory, reinforcement learning, computational psychiatry, and research methodology.

Your task is to conduct a rigorous, source-driven literature review that can support the theoretical framework and bibliography of an M2 research project.

Do not assume that the project's central hypothesis is true. Treat competing theoretical explanations symmetrically and actively search for evidence that could falsify each account.

# **CONTEXT**

The proposed project sits at the intersection of:

* semantic/verbal fluency;  
* semantic memory and lexical-semantic search;  
* exploration–exploitation and decision-making;  
* computational modeling;  
* individual differences;  
* reliability and construct validity;  
* language-derived digital phenotyping;  
* mental health as a secondary/translational application.

The scientific question is primarily one of **computational cognition**.

Language/semantic fluency is the **experimental system**.

Digital mental health is the **translational motivation**, not the primary clinical endpoint.

The central theoretical problem is:

> Does the apparently exploratory structure of semantic search require an individual strategic exploration policy, or can it emerge from the structure of semantic representations and local sampling/search alone?

A related cross-domain question is:

> If an individual-specific strategic exploration component exists in semantic search, does it converge with independently measured exploration in non-linguistic decision-making tasks?

A downstream, exploratory question is:

> What are the implications for interpreting language-derived measures as computational or digital phenotypes in mental-health research?

Do NOT presuppose that “lexical exploration” is already a validated construct.

# **RESEARCH OBJECTIVES**

Conduct a deep literature review that establishes the theoretical, empirical and methodological foundations necessary to evaluate this project.

The review must cover the following research streams.

## **A. Semantic search and semantic fluency**

Map the major theories and empirical findings concerning:

* semantic fluency;  
* category fluency;  
* clustering;  
* switching;  
* inter-response times / IRTs;  
* semantic distance;  
* semantic similarity;  
* lexical frequency effects;  
* semantic memory structure;  
* individual differences in semantic search.

Identify the seminal literature as well as major developments through **September 2026**.

Determine which behavioral signatures have traditionally been interpreted as evidence of strategic search.

## **B. Competing generative accounts of semantic search**

Investigate in depth the theoretical dispute between explanations based on:

### **Account 1 — Strategic / foraging-style exploration**

Including work related to:

* optimal foraging;  
* semantic foraging;  
* patch exploitation;  
* depletion;  
* switching;  
* search policies.

Pay particular attention to the work of Hills, Jones, Todd and related authors.

### **Account 2 — Representational / local-search emergence**

Including:

* semantic networks;  
* random walks;  
* censored random walks;  
* local sampling;  
* network topology;  
* representational structure.

Pay particular attention to Abbott, Austerweil, Griffiths and subsequent work building on or testing these models.

For these two model families:

1. explain their mathematical/computational assumptions;  
2. identify which empirical phenomena each model reproduces;  
3. determine whether the same behavioral signatures can be generated by both;  
4. identify existing direct model-comparison studies;  
5. identify findings that discriminate between them;  
6. identify unresolved controversies;  
7. determine what data would provide the strongest falsification test.

Do not infer a strategic cognitive mechanism merely because a model reproduces clustering or switching.

## **C. Exploration–exploitation outside language**

Review the computational literature on human exploration–exploitation, including:

* directed exploration;  
* random exploration;  
* information seeking;  
* uncertainty;  
* decision noise;  
* reward sensitivity;  
* explore–exploit tasks;  
* multi-armed bandits;  
* Horizon-task paradigms;  
* computational decomposition of exploration.

Pay particular attention to work associated with Wilson, Gershman and related researchers.

Explain which parameters or behavioral measures plausibly represent:

* directed exploration;  
* random exploration;  
* reward sensitivity;  
* uncertainty sensitivity.

Then investigate whether exploration parameters behave as stable **individual-difference measures**.

## **D. Cross-domain exploration**

Search specifically for evidence testing whether exploration is:

* domain-general;  
* domain-specific;  
* trait-like;  
* context-dependent.

Look for studies correlating exploration across:

* reinforcement-learning tasks;  
* bandit tasks;  
* information search;  
* semantic search;  
* memory search;  
* curiosity;  
* creativity/divergent thinking;  
* foraging;  
* other cognitive domains.

A key question is:

> Is there credible evidence for a shared individual-level exploration mechanism across semantic and non-semantic domains?

Report positive, null and contradictory evidence.

Do not interpret absence of correlation without considering measurement reliability.

## **E. Reliability and individual-difference measurement**

Review the literature on the reliability of cognitive-task parameters and individual differences.

Include:

* test–retest reliability;  
* internal reliability;  
* parameter uncertainty;  
* reliability paradox;  
* attenuation of correlations;  
* task impurity;  
* hierarchical estimation / partial pooling;  
* latent-variable approaches where appropriate.

Explicitly investigate work by Hedge et al., Enkavi et al., and later work that evaluates or challenges their conclusions.

Answer:

1. How reliable are behavioral measures of exploration?  
2. How reliable are computational model parameters?  
3. What reliability levels are necessary for credible cross-task correlations?  
4. What methodological solutions are recommended?  
5. Which proposed solutions do NOT actually solve the reliability problem?

Explain the implications for testing convergent and discriminant validity.

## **F. Dependence on semantic representation**

Investigate how measures of semantic search depend on the representation used to define semantic similarity or distance.

Compare at minimum:

* human association networks;  
* semantic networks;  
* LSA or related distributional methods;  
* static embeddings such as word2vec/GloVe;  
* contextual embeddings;  
* other commonly used semantic representations.

Search for evidence that conclusions about:

* clusters;  
* switches;  
* semantic distance;  
* individual rankings;  
* search strategies

change as a function of the chosen semantic representation.

Determine whether a **multiverse/specification-curve analysis across semantic representations** has been used or proposed.

Identify methodological recommendations for representation-robust inference.

## **G. Computational model evaluation**

Review best practices relevant to comparing the competing models.

Include:

* generative modeling;  
* model recovery;  
* parameter recovery;  
* identifiability;  
* posterior predictive checks;  
* simulation-based calibration where relevant;  
* cross-validation;  
* out-of-sample prediction;  
* model complexity;  
* model mimicry;  
* falsification;  
* hierarchical Bayesian modeling.

Explain which methods are essential for determining whether the strategic and representational models are empirically distinguishable.

Search for methodological literature in computational cognitive modeling, including work involving Palminteri, Wyart, Koechlin and other relevant authors where appropriate.

## **H. Timing and process-level data**

Investigate the evidential role of:

* inter-response times;  
* keystroke-level timing;  
* temporal dynamics;  
* pauses before switches;  
* response-order information.

Determine whether timing data discriminate strategic-foraging models from representational/random-walk accounts better than word sequences alone.

## **I. Existing datasets, software and reproducibility resources**

Identify existing open datasets, codebases and tools suitable for testing the project before new data collection.

Investigate, but do not limit the search to:

* semantic-fluency datasets;  
* Hills et al. datasets;  
* Abbott/Austerweil-related implementations;  
* forager / forager-analyses;  
* SNAFU or related semantic-network tools;  
* SWOW;  
* semantic association datasets;  
* Horizon-task implementations or datasets.

For every resource report:

* what it contains;  
* population/sample;  
* variables available;  
* whether individual-level data are available;  
* whether timing/IRT information is available;  
* license/access conditions;  
* code repository or persistent URL;  
* scientific papers describing the dataset/software.

Verify current software capabilities from the official repository/documentation rather than relying on secondary descriptions.

## **J. Mental health and digital phenotyping — secondary layer**

Only after establishing the computational and measurement literature, review how semantic/language measures have been used in:

* digital phenotyping;  
* computational psychiatry;  
* speech/language biomarkers;  
* depression;  
* anhedonia;  
* psychosis/schizophrenia;  
* negative symptoms;  
* cognitive dysfunction.

Distinguish carefully between:

1. predictive associations;  
2. diagnostic classification;  
3. symptom correlations;  
4. longitudinal sensitivity;  
5. mechanistic interpretation.

The key question is NOT:

> “Can language predict mental illness?”

The key question is:

> “Do language-derived computational markers used or proposed in digital mental health have a defensible interpretation in terms of underlying cognitive mechanisms?”

Identify studies that directly address construct/mechanistic validity rather than classification accuracy alone.

Treat mental-health associations as an exploratory or translational layer.

Do not imply that a language measure is a clinical biomarker merely because it correlates with symptoms.

# **SEARCH STRATEGY**

Use multiple complementary searches rather than a single query.

Search major scholarly sources and indexes accessible through the web, including where possible:

* PubMed;  
* PubMed Central;  
* Google Scholar records;  
* Crossref;  
* Semantic Scholar;  
* PsycINFO-related records;  
* Web of Science/Scopus metadata when accessible;  
* arXiv only when peer-reviewed versions are unavailable;  
* journal websites;  
* university repositories;  
* official GitHub repositories for software.

Use citation chaining:

1. identify seminal papers;  
2. inspect papers that cite them;  
3. inspect their reference lists;  
4. search for direct replications, critiques and competing models.

Use combinations of search terms such as:

"semantic fluency" AND exploration  
"semantic foraging"  
"optimal foraging" AND verbal fluency  
"semantic search" AND computational model  
"censored random walk" AND semantic fluency  
"semantic network" AND verbal fluency  
"semantic search" AND random walk  
"semantic search" AND individual differences  
"semantic fluency" AND inter-response time  
"exploration exploitation" AND individual differences  
"directed exploration" AND reliability  
"random exploration" AND reliability  
"Horizon task" AND test-retest  
"computational parameters" AND reliability  
"reliability paradox" cognitive tasks  
"semantic embeddings" AND fluency  
"semantic representation" AND clustering AND fluency  
"digital phenotyping" AND language AND construct validity  
"language biomarkers" AND mechanistic validation  
"speech biomarkers" AND computational psychiatry

Expand and modify these terms as the literature requires.

# **EVIDENCE RULES**

Classify important claims internally as:

**Fact A:** directly supported by a primary source, official repository/documentation, dataset paper, systematic review, or authoritative current source.

**Fact B:** supported by credible secondary literature or reasonable synthesis across sources.

**Fact C:** hypothesis, inference, speculation or unverified claim.

Do not present Fact C as established knowledge.

For disputed findings, show competing evidence.

For null findings, distinguish:

* evidence of absence;  
* absence of evidence;  
* inconclusive results due to low reliability or poor identifiability.

# **SOURCE PRIORITY**

Prioritize:

1. peer-reviewed primary research;  
2. systematic reviews/meta-analyses;  
3. seminal theoretical papers;  
4. methodological papers;  
5. official datasets/software documentation.

Use preprints when they are scientifically important or represent the most recent evidence, but clearly label them as preprints.

Avoid relying on:

* generic blogs;  
* SEO summaries;  
* unsourced websites;  
* AI-generated literature summaries.

# **CITATION & IDENTIFIER VERIFICATION — RETRIEVAL STATES**

Do not describe an identifier as verified merely because it appears in generated text, a search snippet, a bibliography, or an aggregator.

Assign every Tier 1 reference one Retrieval Status:

* RESOLVED — the DOI URL was actually opened/tested during this research session and resolved to a landing page whose bibliographic metadata is consistent with the cited work. Report DOI URL \+ landing-page source \+ access date.  
* RETRIEVED\_PRIMARY — the article page, publisher page, journal page, Crossref record, PubMed record, or other authoritative bibliographic record was opened during this research session and its metadata was read directly. If the DOI itself was not tested through a resolver, write "DOI resolution: not tested."  
* INDEXED — metadata was obtained only from a search result, secondary index, aggregator, citation list, or another paper; the authoritative record was not opened.  
* UNRETRIEVED — the reference originated from model recall or could not be retrieved during this research session.

Tier 1 may contain only RESOLVED or RETRIEVED\_PRIMARY references.

INDEXED references may appear in Tier 2 or Tier 3 only when clearly labeled.

UNRETRIEVED references must be moved to a separate section:  
"Unretrieved — requires external verification."

Never write a DOI that was not read from an opened source during this research session.

If an identifier was not retrieved, write:  
"DOI: not retrieved."

If a DOI was retrieved but its resolver was not tested, write:  
"DOI resolution: not tested."

Do not infer, reconstruct, autocomplete, or guess DOI strings.

Do not produce a confidence score, readiness rating, self-approval statement, or independent quality certification of your own report. Provide the evidence states above so that a separate auditor can evaluate the output.

# **DELIVERABLE — OUTPUT DISCIPLINE**

Produce output in this exact order. If budget runs short, truncate from the END,

never from the beginning.

1\. Search log: report the search queries, search terms, databases/indexes, websites, citation-chaining paths, and other retrieval actions that were explicitly issued or are observable during this research session.

* Do not invent hidden/internal queries, tool calls, search-result counts, or hit counts.  
* If the research system does not expose an exact query or result count, write: "Not exposed by the research interface."  
* Report deliberately attempted searches that returned no usable evidence when this information is observable.

2\. Claims-to-sources audit table, restricted to claims the proposed project depends on.

3\. Tier 1 reading list — MAXIMUM 20 papers. Full APA citation, identifiers,

&nbsp;&nbsp;&nbsp;Retrieval Status, 2-4 sentence summary, project component informed.

4\. Competing-model table (strategic/foraging vs representational/random-walk).

5\. Tier 2 (max 40\) and Tier 3 (max 30): citation \+ identifier ONLY.

&nbsp;&nbsp;&nbsp;No summaries, no annotations.

6\. Executive synthesis, maximum 1,200 words.

7\. Remaining analytical sections in the original order.

8\. BibTeX for Tier 1 only.

Hard constraints:

\- Never exceed 20 annotated papers. Volume of annotated references is not a quality signal; unverifiable metadata is a disqualifying defect.

\- Do NOT evaluate, endorse or rank the proposed M2 framing. Replace that section with:

&nbsp;&nbsp;"Elements of the proposed framing that the retrieved literature does NOT support."

&nbsp;&nbsp;List only unsupported or contested elements. If you find none, say so explicitly and state what evidence would have been required to find one.

\- State the actual execution date and report coverage relative to it. Do not claim coverage of a period you did not search.

\- Author names supplied in the research brief are search seeds, not preferred authorities. Do not privilege authors because of affiliation with the target laboratory. Include their work only when it satisfies the same relevance and evidence criteria applied to the rest of the literature.

\- Expand searches beyond the named authors and actively look for competing research groups, critiques, replications, alternative models, and null findings.

# **FINAL QUALITY CHECK**

Before finishing, verify that:

* both competing theoretical accounts received serious treatment;  
* null and contradictory evidence was included;  
* no association was transformed into a causal claim;  
* no DOI or reference was fabricated;  
* seminal literature was not omitted merely because it is old;  
* recent literature through September 2026 was actively searched;  
* preprints are clearly labeled;  
* the distinction between prediction and mechanistic explanation is preserved;  
* reliability and identifiability are treated as central, not peripheral;  
* the bibliography is actually useful for writing a research proposal rather than merely long.

If important evidence cannot be verified, explicitly write:

**Não verificado.**

The purpose of this research is not to prove the project correct. It is to determine whether the project is theoretically justified, experimentally discriminating, methodologically feasible, and grounded in the strongest available literature.
