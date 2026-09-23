---
id: M09
titulo_original: "How to build Gems"
grupo: metodologia-multi-ia
fonte: "Google Docs do autor (pasta IA/Conversas)"
criado_em_drive: 2025-11-16
modificado_em_drive: 2026-06-28
exportado_em: 2026-09-23
formato: "HTML do Google Docs convertido para Markdown com pandoc"
trechos_removidos: 0
palavras_removidas: 0
redacoes: 0
licenca: CC-BY-4.0
---

# 28/06/2026

# Eu:

Por favor, me ajude a fazer um prompt para fazer uma Deep Research sobre como fazer Google Gems

# ChatGPT 5.5 Deep Guide diz:

### 1) Diagnóstico 3D

**Ambiguidade: 3/5.** Vou assumir que “Google Gems” = **Gems do Gemini**, isto é, versões personalizadas do Gemini para tarefas repetitivas ou especializadas. O prompt também manda diferenciar **Gems no Gemini Apps/Workspace** de **Gems from Google Labs/Opal**, porque o Google trata esses fluxos de dados de forma diferente. ([Ajuda Google](https://support.google.com/gemini/answer/15146780?co=GENIE.Platform%3DAndroid&hl=en))

**Risco: 2/5.** Baixo a moderado: envolve uso de ferramenta de IA, produtividade, privacidade e governança leve. O prompt força fontes oficiais, data de atualização, limites, privacidade e verificação.

### 2) Arquitetura & Seleção (modelo/pipeline + técnica)

Use **Deep Research com navegação web**, priorizando documentação oficial do Google, Google Workspace, Gemini Help, Google Blog e fontes secundárias apenas para exemplos práticos. Deep Research é adequado porque a tarefa exige pesquisa multi-etapas, comparação de fontes e síntese com citações.

Técnica aplicada: **pesquisa em três passagens** — escopo, análise profunda e validação. Também uso “chaining” conceitual: primeiro mapear o produto, depois transformar em guia prático, depois auditar lacunas e claims. Esse padrão é útil para pesquisa, síntese e tarefas com várias transformações.

### 3) Prompt Final (Template Mestre)

Copie e cole:

\# SYSTEM ROLE

Você é um analista sênior de pesquisa em IA aplicada, produtividade e ferramentas Google. Sua tarefa é produzir uma Deep Research completa, atualizada e verificável sobre como criar, configurar, testar e governar Google Gems/Gemini Gems.

\# CONTEXT

Tema da pesquisa: Como fazer Google Gems, com foco em Gems do Gemini.

Objetivo do usuário:

Criar um guia prático e confiável para entender:

1\. O que são Google Gems/Gemini Gems.

2\. Quem pode criar, editar, usar e compartilhar Gems.

3\. Como criar uma Gem passo a passo.

4\. Como escrever boas instruções para uma Gem.

5\. Como usar arquivos, Google Drive, conhecimento anexado e contexto.

6\. Quais são os limites, planos, restrições, riscos de privacidade e diferenças entre contas pessoais, Workspace, escola/empresa e Google Labs/Opal.

7\. Quais casos de uso funcionam melhor.

8\. Como testar, avaliar e melhorar uma Gem antes de usar em produção.

Escopo:

\- Priorize informações atuais de 2024 a 2026.

\- Priorize fontes oficiais do Google: Gemini Help, Google Workspace Help, Google Workspace Updates, Google Blog, Google Privacy/Terms/Policies.

\- Use fontes secundárias apenas para exemplos, práticas de mercado ou tutoriais, sempre separando fato oficial de interpretação.

\- Cubra diferenças entre:

  - Gems no Gemini Apps.

  - Gems em Google Workspace.

  - Gems from Google Labs/Opal, se forem relevantes.

\- Não assuma capacidades não verificadas, como API, automações externas, Gemini Live, compartilhamento externo, integração com Drive ou limites de uso, sem fonte oficial atual.

Fora de escopo:

\- Não fazer propaganda de planos pagos.

\- Não inventar preços, limites, disponibilidade regional ou nomes de recursos.

\- Não afirmar que uma Gem consegue fazer automações, integrações, chamadas de API ou acesso a dados privados se isso não estiver confirmado por fonte oficial.

\- Não confundir Gems com GPTs, agentes autônomos completos, extensões, NotebookLM ou Gemini Enterprise sem explicar as diferenças.

\# TASK

Produza um relatório de pesquisa em português do Brasil sobre “Como fazer Google Gems/Gemini Gems”, voltado para usuários avançados, educadores, consultores, equipes de marketing, produtividade e pequenos negócios.

\# RESEARCH WORKFLOW

Faça a pesquisa em 4 passagens:

\## Passagem 1 — Mapeamento oficial

Identifique e resuma:

\- Definição oficial de Gems.

\- Onde ficam no Gemini.

\- Quem pode criar, editar, apagar, usar e compartilhar.

\- Diferenças entre web app, mobile app e Workspace.

\- Recursos confirmados: instruções, preview, arquivos, Drive, conhecimento, citações, Gems pré-criadas, compartilhamento.

\- Limitações confirmadas: Gemini Live, tipos de conta, políticas, dados, Workspace admin, Drive, Opal/Gems from Google Labs.

\## Passagem 2 — Guia prático

Crie um guia passo a passo:

1\. Como planejar uma Gem.

2\. Como nomear a Gem.

3\. Como escrever instruções.

4\. Como anexar arquivos ou conhecimento, se disponível.

5\. Como testar no preview.

6\. Como iterar.

7\. Como usar no dia a dia.

8\. Como compartilhar com segurança, se aplicável.

9\. Como manter e atualizar a Gem.

Inclua exemplos de Gems:

\- Tutor de estudo.

\- Analista de marketing.

\- Revisor de texto.

\- Assistente de vendas.

\- Analista de feedback/sentimento.

\- Coach de entrevista.

\- Gerador de prompts.

\- Assistente de atendimento.

Para cada exemplo, forneça:

\- Objetivo.

\- Público.

\- Instruções-base.

\- Dados que podem ser anexados.

\- Testes de qualidade.

\- Riscos e limites.

\## Passagem 3 — Engenharia de instruções para Gems

Explique como escrever boas instruções de Gem usando este padrão:

1\. Papel da Gem.

2\. Usuário-alvo.

3\. Tarefa principal.

4\. Entradas esperadas.

5\. Processo de trabalho.

6\. Regras de evidência.

7\. Tom e estilo.

8\. Formato de saída.

9\. Restrições e coisas que a Gem não deve fazer.

10\. Critérios de qualidade.

Crie pelo menos 5 templates prontos de instruções para Gems:

\- Template universal.

\- Template para educação.

\- Template para marketing.

\- Template para consultoria/negócios.

\- Template para análise de documentos.

\- Template para uso com arquivos de marca, se suportado.

\## Passagem 4 — Validação crítica

Atue como auditor cético:

\- Liste claims que dependem de confirmação oficial.

\- Separe fatos em:

  - Fato oficial confirmado.

  - Inferência razoável.

  - Não verificado.

\- Aponte conflitos entre fontes.

\- Identifique recursos que podem ter mudado recentemente.

\- Liste perguntas que o usuário deve verificar dentro da própria conta Gemini/Workspace.

\- Informe riscos de privacidade, dados empresariais, arquivos anexados, compartilhamento e uso por estudantes/empresas.

\# EVIDENCE RULES

\- Cite todas as afirmações não óbvias.

\- Cada afirmação sobre disponibilidade, planos, limites, compartilhamento, Drive, mobile, Workspace, privacidade, Opal ou Gemini Live precisa de fonte oficial datada.

\- Quando a fonte for de fórum/comunidade, marque como “relato de usuário” e não como regra oficial.

\- Se uma informação não puder ser verificada, escreva “Não verificado”.

\- Não coloque informação “Não verificada” no resumo executivo como se fosse fato.

\# OUTPUT FORMAT

Entregue em Markdown com esta estrutura:

\## 1. Resumo executivo

\- O que são Gems.

\- Para quem servem.

\- O que é possível fazer hoje.

\- Principais limitações.

\- Principais riscos.

\- 5 recomendações práticas.

\## 2. Definição e funcionamento

Inclua uma tabela:

\| Item \| O que é \| Fonte \| Status \|

\|---\|---\|---\|---\|

\## 3. Como criar uma Gem passo a passo

Inclua passos numerados e observações por tipo de conta/dispositivo.

\## 4. Anatomia de uma boa Gem

Explique os blocos de instrução recomendados.

\## 5. Templates prontos de Gems

Inclua templates copiáveis.

\## 6. Casos de uso recomendados

Inclua tabela:

\| Caso de uso \| Valor \| Dados úteis \| Riscos \| Como testar \|

\|---\|---\|---\|---\|---\|

\## 7. Limitações, privacidade e governança

Cubra:

\- Contas pessoais.

\- Workspace.

\- Escola/empresa.

\- Compartilhamento.

\- Google Drive.

\- Arquivos anexados.

\- Gems from Google Labs/Opal.

\- Políticas de uso.

\## 8. Checklist de qualidade antes de usar uma Gem

Crie um checklist objetivo com critérios de teste.

\## 9. Tabela claims-to-sources

Inclua:

\| Claim \| Fonte \| Tipo de fonte \| Data/última atualização \| Confiança \|

\|---\|---\|---\|---\|---\|

\## 10. Lacunas e próximas pesquisas

Liste o que ainda precisa ser verificado manualmente.

\# QUALITY BAR

O relatório deve ser:

\- Prático o suficiente para alguém criar uma Gem no mesmo dia.

\- Rigoroso o suficiente para não inventar recursos.

\- Útil para usuários pessoais e equipes Workspace.

\- Atualizado com fontes oficiais.

\- Claro sobre o que é fato, inferência e não verificado.

### 4) Auditoria (Quality Gate)

**Clareza:** objetivo, público e entregável estão explícitos.  
**Especificidade:** cobre criação, instruções, arquivos, Drive, Workspace, privacidade, Opal e validação.  
**Segurança:** bloqueia invenção de planos, limites, APIs e recursos não confirmados.  
**Grounding:** exige fonte oficial para claims voláteis.  
**Auditabilidade:** inclui tabela claims-to-sources e classificação “oficial / inferência / não verificado”.  
**Eficiência:** usa uma única execução de Deep Research, mas com passagens internas bem separadas.

pronto para execução

# Claude Opus 4.8 Deep Guide diz:

## Veredito

O prompt do ChatGPT 5.5 é **executável**, mas tem 4 anti-padrões nomeados no Manual que você deve corrigir antes de rodar. Não é caso de reescrita — são patches cirúrgicos.

E uma observação de roteamento que ninguém apontou: pela **Matriz atualizada**, "como fazer Google Gems" é pesquisa de produto. O pipeline correto é Gemini Deep Research single-shot → Claude audita o **output**. Não há razão para rodar este prompt em três motores para convergência — Gems é tema circunscrito, não exige cross-engine.

------------------------------------------------------------------------

## Auditoria mapeada às regras do Manual

### Falha 1 — Autoauditoria embutida (viola Regra 4 anti-autoauditoria performática)

A "Passagem 4 — Validação crítica" instrui o **mesmo motor** que executa as Passagens 1-3 a "Atuar como auditor cético" das próprias saídas anteriores. Isso é o motor avaliando a si mesmo dentro da mesma execução. É exatamente o que Gemini fez quando criou "Evidence Ledger da Auditoria do Protocolo" — Bias \#7 (auto-auditoria assimétrica) e Bias \#1 (ritualização). O fato de aparecer agora em prompt do ChatGPT é informativo: o anti-padrão não é exclusivo do Gemini.

**Patch**: renomear "Passagem 4 — Validação crítica" para "**Passagem 4 — Marcação para auditoria externa**". A passagem 4 não audita; apenas marca explicitamente quais claims requerem checagem por outro motor (Perplexity para spot-check de URLs/datas, Claude para auditoria estrutural do relatório).

### Falha 2 — Bloco \# QUALITY BAR é autoauditoria positiva (Regra 4)

O bloco final ("O relatório deve ser: prático o suficiente... rigoroso o suficiente... claro sobre o que é fato...") é o motor declarando ao próprio output que ele atende critérios. Não é guardrail (restrição negativa); é autovalidação positiva. Mesma raiz da Falha 1.

**Patch**: substituir o bloco por critérios de auditoria externa explícita:

\# CRITÉRIOS DE AUDITORIA EXTERNA (não declare aderência)

Este relatório será auditado por outro motor contra:

\- Toda afirmação volátil (preço, limite, disponibilidade regional, plano) tem URL oficial Google datada nos últimos 18 meses

\- Nenhuma afirmação sobre "API de Gems" ou "integração com Drive" sem fonte primária

\- Separação explícita Gemini App vs. Gemini API vs. Vertex AI em cada claim de capacidade

### Falha 3 — Ausência da Regra interface ↔ backend (Regra 11 do Manual)

O prompt menciona "web app, mobile app e Workspace" mas não impõe as 6 camadas de disambiguação que o Manual exige para produto de IA. Risco específico aqui: confundir "feature do Gemini App" (Gems criáveis pelo usuário) com "capacidade do modelo Gemini" (não há "Gems API" — Gems é feature de produto, não capacidade do modelo). Sem essa separação, o relatório pode afirmar que "Gems estão disponíveis na API" quando estão disponíveis apenas no app.

**Patch**: adicionar ao \# EVIDENCE RULES:

\- Toda afirmação de capacidade Gems deve indicar explicitamente a camada:

  \[Interface/App \| Modelo (backend) \| API/Dev \| Plano \| Região/Status \| Data do claim\]

\- Distinguir: Gemini App (gemini.google.com) vs. Gemini API (ai.google.dev) vs. Vertex AI vs. Workspace add-on.

\- "Gems é feature de produto, não capacidade do modelo Gemini." Confirmar separadamente em qual superfície a Gem existe.

### Falha 4 — Taxonomia divergente do canônico Fato A/B/C (Regra 5 — não vazia, mas inconsistente)

ChatGPT introduziu **sua própria** classificação: "Fato oficial confirmado / Inferência razoável / Não verificado". Tem definição operacional, então não cai na proibição da Regra 5 anti-nomenclatura vazia. Mas diverge do **Fato A/B/C canônico** estabelecido no Manual. Se você for cruzar este relatório com outra Deep Research do seu pipeline, vai precisar traduzir as três categorias — fricção desnecessária.

**Patch**: trocar as três categorias por:

\- Fato A: fonte oficial primária Google datada (Gemini Help, Workspace Help, Google Blog oficial)

\- Fato B: inferência razoável a partir de A, ou fonte secundária de autoridade datada

\- Fato C: não verificado / em rollout / beta limitado. Não usar Fato C no Sumário Executivo.

### Falhas menores (não obrigatórias)

- **Diagnóstico 3D inicial** (ambiguidade 3/5, risco 2/5): Bias \#1 ritualização. Fora do bloco copiável, não afeta execução. Sem patch.
- **8 exemplos hard-coded de Gems**: "Tutor de estudo, Analista de marketing... Assistente de atendimento". Risco baixo, mas dois deles (Coach de entrevista, Gerador de prompts) podem coincidir com Gems pré-criadas oficiais do Google. Se quiser parametrizar: peça primeiro o mapeamento das Gems pré-criadas oficiais e depois 5 lacunas onde Gems customizadas fazem sentido.

------------------------------------------------------------------------

## Próximo passo

1.  Aplique os patches 1, 2 e 3 (obrigatórios). Patch 4 é recomendado por consistência com o resto do seu pipeline.
2.  Rode **uma vez** no Gemini Deep Research em sessão limpa, sem corpus do orquestrador anexado (Regra Gemini do Manual — single-shot fechado).
3.  Quando o relatório voltar, traga-o aqui para auditoria claim-por-claim com Fato A/B/C. É aí que eu agrego valor inequívoco — não em mais uma rodada de revisão do prompt.

------------------------------------------------------------------------

## Entrada de governança (se quiser versionar)

Bias \#9 (ChatGPT) — Auto-Quality-Bar embutida.

Padrão observado: ChatGPT termina prompts longos com bloco "# QUALITY BAR" listando

critérios que o próprio output deve cumprir, sem auditor externo. Operacionalmente

equivalente ao autoauditoria do Gemini (Bias \#1), porém em formato declarativo positivo

em vez de tabela. Não confundir com guardrails (restrições negativas externas).

Mitigação: substituir por bloco "# CRITÉRIOS DE AUDITORIA EXTERNA" explicitando que

a validação será feita por outro motor.

Fato A — evidenciado em prompt "Deep Research Google Gems", ChatGPT 5.5 Deep Guide,

28 jun 2026.

# ChatGPT 5.5 Deep Guide diz:

### 1) Diagnóstico 3D

**Ambiguidade: 2/5.** A tarefa agora é clara: aplicar os patches ao prompt anterior, sem reescrever tudo desnecessariamente.

**Risco: 2/5.** Tema de produto IA com risco de erro factual sobre planos, API, Workspace, região, rollout e privacidade. O prompt precisa forçar verificação oficial e separação entre interface, backend, API e produto.

### 2) Arquitetura & Seleção (modelo/pipeline + técnica)

Concordo com a correção: o melhor pipeline é:

**Gemini Deep Research single-shot → Claude/ChatGPT audita o relatório depois.**

Não faz sentido pedir convergência entre três motores antes da pesquisa. O tema é circunscrito: **como fazer Google/Gemini Gems**. O ganho real vem de uma pesquisa oficial atualizada e depois uma auditoria claim-by-claim.

Abaixo está o prompt corrigido com os patches 1, 2, 3 e 4 aplicados.

### 3) Prompt Final (Template Mestre)

\# SYSTEM ROLE

Você é um analista sênior de pesquisa em IA aplicada, produtividade e ferramentas Google. Sua tarefa é produzir uma Deep Research completa, atualizada e verificável sobre como criar, configurar, testar e governar Google Gems/Gemini Gems.

\# CONTEXT

Tema da pesquisa: Como fazer Google Gems, com foco em Gems do Gemini.

Objetivo do usuário:

Criar um guia prático e confiável para entender:

1\. O que são Google Gems/Gemini Gems.

2\. Quem pode criar, editar, usar e compartilhar Gems.

3\. Como criar uma Gem passo a passo.

4\. Como escrever boas instruções para uma Gem.

5\. Como usar arquivos, Google Drive, conhecimento anexado e contexto, se esses recursos estiverem oficialmente disponíveis.

6\. Quais são os limites, planos, restrições, riscos de privacidade e diferenças entre contas pessoais, Workspace, escola/empresa e Google Labs/Opal.

7\. Quais casos de uso funcionam melhor.

8\. Como testar, avaliar e melhorar uma Gem antes de usar em produção.

Escopo:

\- Priorize informações atuais de 2024 a 2026.

\- Priorize fontes oficiais do Google: Gemini Help, Google Workspace Help, Google Workspace Updates, Google Blog, Google Privacy/Terms/Policies e documentação oficial de produto.

\- Use fontes secundárias apenas para exemplos, práticas de mercado ou tutoriais, sempre separando fato oficial de interpretação.

\- Cubra diferenças entre:

  - Gems no Gemini App / Gemini web app.

  - Gems em contexto Google Workspace, se aplicável.

  - Gems from Google Labs / Opal, se relevantes.

  - Gemini API e Vertex AI apenas para esclarecer se Gems existem ou não nessas superfícies.

\- Não assuma capacidades não verificadas, como API, automações externas, Gemini Live, compartilhamento externo, integração com Drive ou limites de uso, sem fonte oficial atual.

Fora de escopo:

\- Não fazer propaganda de planos pagos.

\- Não inventar preços, limites, disponibilidade regional ou nomes de recursos.

\- Não afirmar que uma Gem consegue fazer automações, integrações, chamadas de API ou acesso a dados privados se isso não estiver confirmado por fonte oficial.

\- Não confundir Gems com GPTs, agentes autônomos completos, extensões, NotebookLM, Gemini API, Vertex AI ou Gemini Enterprise sem explicar as diferenças.

\# TASK

Produza um relatório de pesquisa em português do Brasil sobre “Como fazer Google Gems/Gemini Gems”, voltado para usuários avançados, educadores, consultores, equipes de marketing, produtividade e pequenos negócios.

\# RESEARCH WORKFLOW

Faça a pesquisa em 4 passagens:

\## Passagem 1 — Mapeamento oficial

Identifique e resuma:

\- Definição oficial de Gems.

\- Onde ficam no Gemini.

\- Quem pode criar, editar, apagar, usar e compartilhar.

\- Diferenças entre web app, mobile app e Workspace.

\- Recursos confirmados: instruções, preview, arquivos, Drive, conhecimento, citações, Gems pré-criadas, compartilhamento.

\- Limitações confirmadas: Gemini Live, tipos de conta, políticas, dados, Workspace admin, Drive, Opal/Gems from Google Labs.

\- Para cada claim de capacidade, indique a camada:

  \[Interface/App \| Modelo/backend \| API/Dev \| Plano \| Região/Status \| Data do claim\]

\## Passagem 2 — Guia prático

Crie um guia passo a passo:

1\. Como planejar uma Gem.

2\. Como nomear a Gem.

3\. Como escrever instruções.

4\. Como anexar arquivos ou conhecimento, se disponível.

5\. Como testar no preview.

6\. Como iterar.

7\. Como usar no dia a dia.

8\. Como compartilhar com segurança, se aplicável.

9\. Como manter e atualizar a Gem.

Antes de criar exemplos próprios, mapeie primeiro as Gems pré-criadas oficiais do Google, se existirem, e diferencie:

\- Gems oficiais/pré-criadas.

\- Gems customizadas pelo usuário.

\- Templates sugeridos pelo relatório.

Depois, crie exemplos apenas para lacunas úteis onde Gems customizadas façam sentido. Para cada exemplo, forneça:

\- Objetivo.

\- Público.

\- Instruções-base.

\- Dados que podem ser anexados, se o recurso for confirmado.

\- Testes de qualidade.

\- Riscos e limites.

\## Passagem 3 — Engenharia de instruções para Gems

Explique como escrever boas instruções de Gem usando este padrão:

1\. Papel da Gem.

2\. Usuário-alvo.

3\. Tarefa principal.

4\. Entradas esperadas.

5\. Processo de trabalho.

6\. Regras de evidência.

7\. Tom e estilo.

8\. Formato de saída.

9\. Restrições e coisas que a Gem não deve fazer.

10\. Critérios de qualidade.

Crie templates prontos de instruções para Gems:

\- Template universal.

\- Template para educação.

\- Template para marketing.

\- Template para consultoria/negócios.

\- Template para análise de documentos.

\- Template para uso com arquivos de marca, somente se o uso de arquivos/conhecimento for confirmado por fonte oficial.

\## Passagem 4 — Marcação para auditoria externa

Não audite seu próprio relatório como se fosse validação final. Em vez disso, marque explicitamente o que outro motor ou revisor humano deve verificar.

Liste:

\- Claims que dependem de confirmação oficial.

\- Claims voláteis sobre preço, plano, limite, região, rollout, disponibilidade, Workspace, arquivos, Drive, compartilhamento, Gemini Live, API, Vertex AI ou Opal.

\- URLs que devem ser spot-checkadas por outro motor ou revisor humano.

\- Claims que parecem depender de inferência, não de fonte primária.

\- Conflitos entre fontes.

\- Recursos que podem ter mudado recentemente.

\- Perguntas que o usuário deve verificar dentro da própria conta Gemini/Workspace.

\- Riscos de privacidade, dados empresariais, arquivos anexados, compartilhamento e uso por estudantes/empresas.

\# EVIDENCE RULES

\- Cite todas as afirmações não óbvias.

\- Cada afirmação sobre disponibilidade, planos, limites, compartilhamento, Drive, mobile, Workspace, privacidade, Opal, Gemini Live, API ou Vertex AI precisa de fonte oficial datada.

\- Toda afirmação de capacidade Gems deve indicar explicitamente a camada:

  \[Interface/App \| Modelo/backend \| API/Dev \| Plano \| Região/Status \| Data do claim\]

\- Distinguir sempre:

  - Gemini App / gemini.google.com.

  - Gemini API / ai.google.dev.

  - Vertex AI.

  - Google Workspace add-on ou integração Workspace.

  - Google Labs / Opal.

\- Trate “Gems” como feature de produto/interface, não como capacidade intrínseca do modelo Gemini, salvo se fonte oficial disser o contrário.

\- Confirme separadamente em qual superfície a Gem existe.

\- Quando a fonte for de fórum/comunidade, marque como “relato de usuário” e não como regra oficial.

\- Se uma informação não puder ser verificada, classifique como Fato C.

\- Não coloque Fato C no resumo executivo como se fosse fato.

\# FACT CLASSIFICATION

Classifique claims relevantes assim:

\- Fato A: fonte oficial primária Google datada, como Gemini Help, Workspace Help, Google Blog oficial, Google Workspace Updates, Google Privacy/Terms/Policies ou documentação oficial Google.

\- Fato B: inferência razoável a partir de Fato A, ou fonte secundária de autoridade datada.

\- Fato C: não verificado, em rollout, beta limitado, relato de usuário, fonte não oficial, fonte desatualizada ou claim sem confirmação suficiente.

Regras:

\- Não usar Fato C no Sumário Executivo.

\- Não transformar Fato B em certeza operacional.

\- Claims críticos de produto devem buscar Fato A.

\- Se houver conflito entre Fato A e Fato B/C, prevalece Fato A, salvo se houver evidência oficial mais recente.

\# OUTPUT FORMAT

Entregue em Markdown com esta estrutura:

\## 1. Resumo executivo

Inclua apenas Fato A e, quando necessário, Fato B claramente marcado.

Cubra:

\- O que são Gems.

\- Para quem servem.

\- O que é possível fazer hoje.

\- Principais limitações.

\- Principais riscos.

\- 5 recomendações práticas.

\## 2. Definição e funcionamento

Inclua uma tabela:

\| Item \| O que é \| Camada \| Fonte \| Status Fato A/B/C \|

\|---\|---\|---\|---\|---\|

\## 3. Mapa de superfícies Google

Inclua uma tabela:

\| Superfície \| Gems existem aqui? \| O que é possível fazer \| O que não está confirmado \| Fonte \|

\|---\|---:\|---\|---\|---\|

\| Gemini App / web \| \| \| \| \|

\| Gemini mobile app \| \| \| \| \|

\| Google Workspace \| \| \| \| \|

\| Gemini API \| \| \| \| \|

\| Vertex AI \| \| \| \| \|

\| Google Labs / Opal \| \| \| \| \|

\## 4. Como criar uma Gem passo a passo

Inclua passos numerados e observações por tipo de conta, dispositivo e superfície.

\## 5. Anatomia de uma boa Gem

Explique os blocos de instrução recomendados.

\## 6. Templates prontos de Gems

Inclua templates copiáveis.

Antes dos templates, diga quais exemplos são oficiais e quais são templates sugeridos pelo relatório.

\## 7. Casos de uso recomendados

Inclua tabela:

\| Caso de uso \| Valor \| Dados úteis \| Riscos \| Como testar \| Status Fato A/B/C \|

\|---\|---\|---\|---\|---\|---\|

\## 8. Limitações, privacidade e governança

Cubra:

\- Contas pessoais.

\- Workspace.

\- Escola/empresa.

\- Compartilhamento.

\- Google Drive.

\- Arquivos anexados.

\- Gems from Google Labs/Opal.

\- Gemini API.

\- Vertex AI.

\- Políticas de uso.

\- Dados sensíveis e dados empresariais.

\## 9. Checklist de qualidade antes de usar uma Gem

Crie um checklist objetivo com critérios de teste.

Não declare que o relatório passou no checklist. O checklist é para o usuário ou auditor externo aplicar.

\## 10. Tabela claims-to-sources

Inclua:

\| Claim \| Camada \| Fonte \| Tipo de fonte \| Data/última atualização \| Fato A/B/C \| Confiança \|

\|---\|---\|---\|---\|---\|---\|---\|

\## 11. Marcação para auditoria externa

Inclua:

\| Claim a auditar \| Por que precisa de auditoria \| Fonte atual \| Verificação recomendada \|

\|---\|---\|---\|---\|

\## 12. Lacunas e próximas pesquisas

Liste o que ainda precisa ser verificado manualmente.

\# CRITÉRIOS DE AUDITORIA EXTERNA

Não declare aderência a estes critérios. O relatório será auditado por outro motor ou revisor humano contra:

\- Toda afirmação volátil sobre preço, limite, disponibilidade regional, plano, rollout, Workspace, compartilhamento, arquivos, Drive, Gemini Live, API, Vertex AI ou Opal tem URL oficial Google datada, preferencialmente dos últimos 18 meses.

\- Nenhuma afirmação sobre “API de Gems”, “Gems no Vertex AI”, “integração com Drive”, “uso de arquivos”, “compartilhamento” ou “automação externa” aparece sem fonte primária.

\- Toda claim de capacidade separa explicitamente:

  \[Interface/App \| Modelo/backend \| API/Dev \| Plano \| Região/Status \| Data do claim\]

\- O relatório distingue Gemini App, Gemini API, Vertex AI, Workspace e Google Labs/Opal.

\- Fato C não aparece no Sumário Executivo como fato.

\- Relatos de usuários, blogs e fóruns não são tratados como documentação oficial.

\- Onde houver conflito entre fontes, o relatório mostra o conflito e privilegia a fonte oficial mais recente.

### 4) Auditoria (Quality Gate)

Patches aplicados:

1.  **Autoauditoria removida:** “Validação crítica” virou **Marcação para auditoria externa**.
2.  **Quality Bar corrigido:** virou **Critérios de auditoria externa**, com instrução explícita para não declarar aderência.
3.  **Interface ↔ backend incluído:** agora cada claim precisa marcar camada: App, modelo/backend, API/dev, plano, região/status e data.
4.  **Fato A/B/C padronizado:** substituí a taxonomia divergente por Fato A, B e C.

pronto para execução.

# Claude Opus 4.8 Deep Guide diz:

## Veredito

Os 4 patches foram aplicados corretamente. O prompt está **pronto para execução** — sem ressalvas obrigatórias. ChatGPT 5.5 não regrediu, não reintroduziu autoauditoria, e a tabela "Mapa de superfícies Google" (Seção 3) é um delta próprio genuíno que melhora o original além do que pedi. Registro isso como contraevidência ao viés de autoavaliação: quando confrontado em texto, ChatGPT corrige de forma limpa.

Aplica-se aqui a **Regra de parada 2/3 + Regra anti-meta-trabalho**. Você tem prompt limpo. Pedir mais uma rodada de revisão de prompt agora seria o anti-padrão que o Manual proíbe (ritualização da orquestração). A próxima ação é executar, não refinar.

------------------------------------------------------------------------

## Verificação patch-por-patch

**Patch 1 (autoauditoria → marcação externa)** — Aplicado. "Passagem 4 — Marcação para auditoria externa" agora abre com instrução negativa explícita ("Não audite seu próprio relatório como se fosse validação final"). Conforme Regra 4. ✓

**Patch 2 (Quality Bar → Critérios de auditoria externa)** — Aplicado, e bem. O bloco final inverteu de declaração positiva para restrições verificáveis por terceiro, com a trava "Não declare aderência a estes critérios" no topo. Reforçado ainda na Seção 9 ("Não declare que o relatório passou no checklist"). ✓

**Patch 3 (interface ↔ backend)** — Aplicado em três lugares: Passagem 1, EVIDENCE RULES, e operacionalizado como coluna "Camada" nas tabelas das Seções 2, 3 e 10. A linha "Trate 'Gems' como feature de produto/interface, não como capacidade intrínseca do modelo" fecha o risco específico que eu apontei (afirmar "Gems na API" quando Gems é feature de app). Conforme Regra 11. ✓

**Patch 4 (Fato A/B/C canônico)** — Aplicado. Bloco \# FACT CLASSIFICATION substituiu a taxonomia divergente e adicionou regras de precedência (A \> B/C salvo evidência mais recente) que não estavam no meu patch — adição válida. ✓

------------------------------------------------------------------------

## Observações não-bloqueantes

Nenhuma exige ação antes de rodar. Registro para transparência:

O prompt cresceu de forma significativa (12 seções de output + 6 tabelas). Risco operacional: Gemini Deep Research pode truncar ou priorizar amplitude sobre profundidade em algumas células. Não é defeito do prompt — é característica do motor. Se o relatório voltar com tabelas incompletas (células vazias em "Vertex AI" / "Opal"), isso é sinal de que a fonte oficial não existe, não de falha do prompt. Trate célula vazia como Fato C, não como erro a corrigir no prompt.

Mantenha a sessão Gemini **limpa** — sem o corpus do orquestrador, sem este histórico de auditoria anexado (Regra Gemini: single-shot fechado). Anexar a meta-discussão arrisca Bias \#8 (ancoragem em fonte secundária mais citável).

------------------------------------------------------------------------

## Stop Rule — declarada

Convergência atingida: ChatGPT entregou prompt limpo, eu confirmo limpo. Não há terceiro motor necessário para esta etapa — tema circunscrito, pipeline de produto é Gemini → auditor, não convergência tripla.

**Recuso a próxima iteração de revisão de prompt.** Se você voltar com "o ChatGPT/Gemini sugeriu mais um ajuste no prompt", a resposta já está dada: aplique se for erro factual crítico, caso contrário é decisão sua de orquestrador, não necessidade metodológica.

A próxima conversa produtiva sobre isto começa com: *"Aqui está o relatório de Deep Research sobre Gems que o Gemini produziu — audite claim por claim."* Esse é o uso onde eu tenho valor inequívoco: classificação Fato A/B/C linha a linha, flag de overclaim, checagem da separação de camadas que o prompt agora exige.

# Tab 2

\# SYSTEM ROLE

Você é um analista sênior de pesquisa em IA aplicada, produtividade e ferramentas Google. Sua tarefa é produzir uma Deep Research completa, atualizada e verificável sobre como criar, configurar, testar e governar Google Gems/Gemini Gems.

\# CONTEXT

Tema da pesquisa: Como fazer Google Gems, com foco em Gems do Gemini.

Objetivo do usuário:

Criar um guia prático e confiável para entender:

1\. O que são Google Gems/Gemini Gems.

2\. Quem pode criar, editar, usar e compartilhar Gems.

3\. Como criar uma Gem passo a passo.

4\. Como escrever boas instruções para uma Gem.

5\. Como usar arquivos, Google Drive, conhecimento anexado e contexto, se esses recursos estiverem oficialmente disponíveis.

6\. Quais são os limites, planos, restrições, riscos de privacidade e diferenças entre contas pessoais, Workspace, escola/empresa e Google Labs/Opal.

7\. Quais casos de uso funcionam melhor.

8\. Como testar, avaliar e melhorar uma Gem antes de usar em produção.

Escopo:

\- Priorize informações atuais de 2024 a 2026.

\- Priorize fontes oficiais do Google: Gemini Help, Google Workspace Help, Google Workspace Updates, Google Blog, Google Privacy/Terms/Policies e documentação oficial de produto.

\- Use fontes secundárias apenas para exemplos, práticas de mercado ou tutoriais, sempre separando fato oficial de interpretação.

\- Cubra diferenças entre:

  - Gems no Gemini App / Gemini web app.

  - Gems em contexto Google Workspace, se aplicável.

  - Gems from Google Labs / Opal, se relevantes.

  - Gemini API e Vertex AI apenas para esclarecer se Gems existem ou não nessas superfícies.

\- Não assuma capacidades não verificadas, como API, automações externas, Gemini Live, compartilhamento externo, integração com Drive ou limites de uso, sem fonte oficial atual.

Fora de escopo:

\- Não fazer propaganda de planos pagos.

\- Não inventar preços, limites, disponibilidade regional ou nomes de recursos.

\- Não afirmar que uma Gem consegue fazer automações, integrações, chamadas de API ou acesso a dados privados se isso não estiver confirmado por fonte oficial.

\- Não confundir Gems com GPTs, agentes autônomos completos, extensões, NotebookLM, Gemini API, Vertex AI ou Gemini Enterprise sem explicar as diferenças.

\# TASK

Produza um relatório de pesquisa em português do Brasil sobre “Como fazer Google Gems/Gemini Gems”, voltado para usuários avançados, educadores, consultores, equipes de marketing, produtividade e pequenos negócios.

\# RESEARCH WORKFLOW

Faça a pesquisa em 4 passagens:

\## Passagem 1 — Mapeamento oficial

Identifique e resuma:

\- Definição oficial de Gems.

\- Onde ficam no Gemini.

\- Quem pode criar, editar, apagar, usar e compartilhar.

\- Diferenças entre web app, mobile app e Workspace.

\- Recursos confirmados: instruções, preview, arquivos, Drive, conhecimento, citações, Gems pré-criadas, compartilhamento.

\- Limitações confirmadas: Gemini Live, tipos de conta, políticas, dados, Workspace admin, Drive, Opal/Gems from Google Labs.

\- Para cada claim de capacidade, indique a camada:

  \[Interface/App \| Modelo/backend \| API/Dev \| Plano \| Região/Status \| Data do claim\]

\## Passagem 2 — Guia prático

Crie um guia passo a passo:

1\. Como planejar uma Gem.

2\. Como nomear a Gem.

3\. Como escrever instruções.

4\. Como anexar arquivos ou conhecimento, se disponível.

5\. Como testar no preview.

6\. Como iterar.

7\. Como usar no dia a dia.

8\. Como compartilhar com segurança, se aplicável.

9\. Como manter e atualizar a Gem.

Antes de criar exemplos próprios, mapeie primeiro as Gems pré-criadas oficiais do Google, se existirem, e diferencie:

\- Gems oficiais/pré-criadas.

\- Gems customizadas pelo usuário.

\- Templates sugeridos pelo relatório.

Depois, crie exemplos apenas para lacunas úteis onde Gems customizadas façam sentido. Para cada exemplo, forneça:

\- Objetivo.

\- Público.

\- Instruções-base.

\- Dados que podem ser anexados, se o recurso for confirmado.

\- Testes de qualidade.

\- Riscos e limites.

\## Passagem 3 — Engenharia de instruções para Gems

Explique como escrever boas instruções de Gem usando este padrão:

1\. Papel da Gem.

2\. Usuário-alvo.

3\. Tarefa principal.

4\. Entradas esperadas.

5\. Processo de trabalho.

6\. Regras de evidência.

7\. Tom e estilo.

8\. Formato de saída.

9\. Restrições e coisas que a Gem não deve fazer.

10\. Critérios de qualidade.

Crie templates prontos de instruções para Gems:

\- Template universal.

\- Template para educação.

\- Template para marketing.

\- Template para consultoria/negócios.

\- Template para análise de documentos.

\- Template para uso com arquivos de marca, somente se o uso de arquivos/conhecimento for confirmado por fonte oficial.

\## Passagem 4 — Marcação para auditoria externa

Não audite seu próprio relatório como se fosse validação final. Em vez disso, marque explicitamente o que outro motor ou revisor humano deve verificar.

Liste:

\- Claims que dependem de confirmação oficial.

\- Claims voláteis sobre preço, plano, limite, região, rollout, disponibilidade, Workspace, arquivos, Drive, compartilhamento, Gemini Live, API, Vertex AI ou Opal.

\- URLs que devem ser spot-checkadas por outro motor ou revisor humano.

\- Claims que parecem depender de inferência, não de fonte primária.

\- Conflitos entre fontes.

\- Recursos que podem ter mudado recentemente.

\- Perguntas que o usuário deve verificar dentro da própria conta Gemini/Workspace.

\- Riscos de privacidade, dados empresariais, arquivos anexados, compartilhamento e uso por estudantes/empresas.

\# EVIDENCE RULES

\- Cite todas as afirmações não óbvias.

\- Cada afirmação sobre disponibilidade, planos, limites, compartilhamento, Drive, mobile, Workspace, privacidade, Opal, Gemini Live, API ou Vertex AI precisa de fonte oficial datada.

\- Toda afirmação de capacidade Gems deve indicar explicitamente a camada:

  \[Interface/App \| Modelo/backend \| API/Dev \| Plano \| Região/Status \| Data do claim\]

\- Distinguir sempre:

  - Gemini App / gemini.google.com.

  - Gemini API / ai.google.dev.

  - Vertex AI.

  - Google Workspace add-on ou integração Workspace.

  - Google Labs / Opal.

\- Trate “Gems” como feature de produto/interface, não como capacidade intrínseca do modelo Gemini, salvo se fonte oficial disser o contrário.

\- Confirme separadamente em qual superfície a Gem existe.

\- Quando a fonte for de fórum/comunidade, marque como “relato de usuário” e não como regra oficial.

\- Se uma informação não puder ser verificada, classifique como Fato C.

\- Não coloque Fato C no resumo executivo como se fosse fato.

\# FACT CLASSIFICATION

Classifique claims relevantes assim:

\- Fato A: fonte oficial primária Google datada, como Gemini Help, Workspace Help, Google Blog oficial, Google Workspace Updates, Google Privacy/Terms/Policies ou documentação oficial Google.

\- Fato B: inferência razoável a partir de Fato A, ou fonte secundária de autoridade datada.

\- Fato C: não verificado, em rollout, beta limitado, relato de usuário, fonte não oficial, fonte desatualizada ou claim sem confirmação suficiente.

Regras:

\- Não usar Fato C no Sumário Executivo.

\- Não transformar Fato B em certeza operacional.

\- Claims críticos de produto devem buscar Fato A.

\- Se houver conflito entre Fato A e Fato B/C, prevalece Fato A, salvo se houver evidência oficial mais recente.

\# OUTPUT FORMAT

Entregue em Markdown com esta estrutura:

\## 1. Resumo executivo

Inclua apenas Fato A e, quando necessário, Fato B claramente marcado.

Cubra:

\- O que são Gems.

\- Para quem servem.

\- O que é possível fazer hoje.

\- Principais limitações.

\- Principais riscos.

\- 5 recomendações práticas.

\## 2. Definição e funcionamento

Inclua uma tabela:

\| Item \| O que é \| Camada \| Fonte \| Status Fato A/B/C \|

\|---\|---\|---\|---\|---\|

\## 3. Mapa de superfícies Google

Inclua uma tabela:

\| Superfície \| Gems existem aqui? \| O que é possível fazer \| O que não está confirmado \| Fonte \|

\|---\|---:\|---\|---\|---\|

\| Gemini App / web \| \| \| \| \|

\| Gemini mobile app \| \| \| \| \|

\| Google Workspace \| \| \| \| \|

\| Gemini API \| \| \| \| \|

\| Vertex AI \| \| \| \| \|

\| Google Labs / Opal \| \| \| \| \|

\## 4. Como criar uma Gem passo a passo

Inclua passos numerados e observações por tipo de conta, dispositivo e superfície.

\## 5. Anatomia de uma boa Gem

Explique os blocos de instrução recomendados.

\## 6. Templates prontos de Gems

Inclua templates copiáveis.

Antes dos templates, diga quais exemplos são oficiais e quais são templates sugeridos pelo relatório.

\## 7. Casos de uso recomendados

Inclua tabela:

\| Caso de uso \| Valor \| Dados úteis \| Riscos \| Como testar \| Status Fato A/B/C \|

\|---\|---\|---\|---\|---\|---\|

\## 8. Limitações, privacidade e governança

Cubra:

\- Contas pessoais.

\- Workspace.

\- Escola/empresa.

\- Compartilhamento.

\- Google Drive.

\- Arquivos anexados.

\- Gems from Google Labs/Opal.

\- Gemini API.

\- Vertex AI.

\- Políticas de uso.

\- Dados sensíveis e dados empresariais.

\## 9. Checklist de qualidade antes de usar uma Gem

Crie um checklist objetivo com critérios de teste.

Não declare que o relatório passou no checklist. O checklist é para o usuário ou auditor externo aplicar.

\## 10. Tabela claims-to-sources

Inclua:

\| Claim \| Camada \| Fonte \| Tipo de fonte \| Data/última atualização \| Fato A/B/C \| Confiança \|

\|---\|---\|---\|---\|---\|---\|---\|

\## 11. Marcação para auditoria externa

Inclua:

\| Claim a auditar \| Por que precisa de auditoria \| Fonte atual \| Verificação recomendada \|

\|---\|---\|---\|---\|

\## 12. Lacunas e próximas pesquisas

Liste o que ainda precisa ser verificado manualmente.

\# CRITÉRIOS DE AUDITORIA EXTERNA

Não declare aderência a estes critérios. O relatório será auditado por outro motor ou revisor humano contra:

\- Toda afirmação volátil sobre preço, limite, disponibilidade regional, plano, rollout, Workspace, compartilhamento, arquivos, Drive, Gemini Live, API, Vertex AI ou Opal tem URL oficial Google datada, preferencialmente dos últimos 18 meses.

\- Nenhuma afirmação sobre “API de Gems”, “Gems no Vertex AI”, “integração com Drive”, “uso de arquivos”, “compartilhamento” ou “automação externa” aparece sem fonte primária.

\- Toda claim de capacidade separa explicitamente:

  \[Interface/App \| Modelo/backend \| API/Dev \| Plano \| Região/Status \| Data do claim\]

\- O relatório distingue Gemini App, Gemini API, Vertex AI, Workspace e Google Labs/Opal.

\- Fato C não aparece no Sumário Executivo como fato.

\- Relatos de usuários, blogs e fóruns não são tratados como documentação oficial.

\- Onde houver conflito entre fontes, o relatório mostra o conflito e privilegia a fonte oficial mais recente.
