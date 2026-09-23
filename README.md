# Corpus de Orquestração Multi-IA

[![Licença: CC BY 4.0](https://img.shields.io/badge/licen%C3%A7a-CC%20BY%204.0-blue.svg)](LICENSE)
[![Versão](https://img.shields.io/badge/vers%C3%A3o-1.0.0-green.svg)](CITATION.cff)

**Diálogos reais de um pesquisador com ChatGPT, Gemini, Claude e Perplexity, usados em conjunto para pesquisa acadêmica, engenharia de prompts e *deep research* (2025–2026).**

Este repositório reúne 25 documentos de trabalho em que o autor conduz sessões com vários modelos de linguagem na mesma tarefa: pede, compara, faz um modelo criticar o outro e consolida o resultado. Boa parte das sessões usa assistentes com papéis fixos criados pelo próprio autor — *Deep Guide*, *Prompt Instructor*, *GPT Builder* e *Gems Builder*. Os textos foram exportados do Google Docs, anonimizados e acompanhados de metadados por documento e por turno de fala.

## Em números

| | |
|---|---|
| Documentos | 25 (em 47 arquivos Markdown) |
| Palavras | ~2,44 milhões |
| Turnos de fala | 2.432 — 381 do autor e 2.051 de IAs |
| Turnos de IA por fornecedor | OpenAI (ChatGPT) 694, Anthropic (Claude) 568, Google (Gemini) 536, Perplexity 199, não identificado 54 |
| Modelos distintos (como rotulados) | 75 — mais frequentes: Gemini 2.5 Pro (245), ChatGPT 5.2 (214), Gemini 3 Pro (203), Perplexity (182), ChatGPT 5 (137), Claude Opus 4.7 (117), ChatGPT 5.6 (100), ChatGPT o3 (98) |
| Papéis de assistente | *Deep Guide* 418, *Prompt Instructor* 191, *GPT Builder* 65, *Gems Builder* 43 turnos |
| Idiomas (estimativa) | português 61%, inglês 27%, francês 12% |
| Período | documentos criados entre abr./2025 e set./2026 |

## Conteúdo

| Grupo | Documentos | Palavras | Do que trata |
|---|---:|---:|---|
| [Metodologia multi-IA](corpus/metodologia-multi-ia/) | 14 | 911.603 | orquestração de vários modelos, engenharia de prompts, *deep research* e criação de GPTs/Gems |
| [Pesquisa acadêmica](corpus/pesquisa-academica/) | 6 | 663.024 | projetos de mestrado, TCCs, propostas de pesquisa, problemas matemáticos e ementas |
| [Sessões mistas](corpus/sessoes-mistas/) | 5 | 867.920 | sessões de *Deep Guide*, *Prompt Instructor* e *Prompts e Respostas* sobre temas variados |

```
corpus/                 textos, um arquivo (ou partes) por documento, com cabeçalho YAML
  metodologia-multi-ia/
  pesquisa-academica/
  sessoes-mistas/
dados/
  catalogo.csv          uma linha por documento
  turnos.csv            uma linha por turno de fala (falante, fornecedor, modelo, papel, palavras, linha)
docs/
  DATASHEET.md          ficha técnica do corpus (modelo "Datasheets for Datasets")
  CODEBOOK.md           convenções de rótulo, papéis, campos das tabelas e lista de modelos
  ANONIMIZACAO.md       o que foi removido ou mascarado antes da publicação
scripts/
  extrair_turnos.py     regenera dados/ a partir de corpus/ (só biblioteca padrão do Python)
CITATION.cff            metadados de citação
```

## Como ler um documento

Cada arquivo começa com metadados (ID, título original, datas, formato de exportação, trechos removidos). No texto:

- `Eu:` marca uma fala do autor;
- `ChatGPT 5.6 Deep Guide diz:`, `Claude Opus 4.7 diz:`, `Gemini 3 Pro diz:` etc. marcam falas de IA — modelo, versão e papel exatamente como o autor os anotou;
- `[link removido]`, `[e-mail removido]` e similares indicam dados mascarados; `[Trecho removido antes da publicação]` indica uma troca inteira retirada.

Os IDs têm um prefixo por grupo: **M** (metodologia), **P** (pesquisa) e **S** (sessões mistas). Para citar um trecho, use o ID e o número do turno em `dados/turnos.csv` (ex.: *S02, turno 57*).

## Como o autor orquestra as IAs

O corpus documenta um método de trabalho que se repete ao longo dos documentos:

1. **Diagnóstico da tarefa.** Antes de responder, o assistente avalia a tarefa num "Diagnóstico 3D": ambiguidade e risco (de 1 a 5) e tipo de tarefa. O termo aparece em 18 dos 25 documentos.
2. **Escolha de modelos e técnica.** Uma seção "Arquitetura & Seleção" decide qual modelo ou pipeline usar e com que técnica; o documento M01 mostra uma versão inicial dessa ideia: um GPT que recomenda a ordem ótima de 1, 2 ou 3 modelos a partir de uma matriz Ambiguidade × Risco.
3. **Prompt final.** O resultado é um prompt pronto para uso ("Template Mestre"), às vezes executado em paralelo em mais de um motor de *deep research*.
4. **Crítica cruzada e consolidação.** O mesmo material circula entre modelos de fornecedores diferentes, que se criticam e se complementam; o autor decide o que fica.
5. **Rastreabilidade.** Os prompts exigem classificação de evidências (Fato A/B/C), um *Evidence Ledger* e regras de parada — elementos do *Manual do Orquestrador* do autor, citado em 15 documentos.

## Usos possíveis

- Comparar como modelos diferentes respondem à mesma tarefa, na mesma sessão.
- Estudar crítica cruzada, auditoria e adjudicação entre modelos.
- Acompanhar mudanças entre versões de modelos em 2025–2026 (por exemplo, Gemini 2.5 Pro → Gemini 3 Pro; ChatGPT o3 → ChatGPT 5.x; Claude Opus 4.x → Claude Opus 5).
- Analisar práticas de engenharia de prompts e de planejamento de pesquisa assistida por IA.
- Investigar bajulação (*sycophancy*), autoavaliação e calibração nas respostas dos modelos.
- Linguística de corpus em português, inglês e francês em contexto acadêmico e técnico.

```python
import pandas as pd

turnos = pd.read_csv("dados/turnos.csv")
ia = turnos[turnos.falante == "ia"]
print(ia.groupby("fornecedor")["palavras"].agg(["count", "sum"]))
print(ia.modelo.value_counts().head(10))
```

## Limitações

- **Um único autor (N = 1).** O corpus retrata a prática de uma pessoa, não de usuários em geral.
- **Seleção.** 7 dos 32 documentos da pasta original ficaram de fora (assuntos pessoais, administrativos ou de negócios), e 24 trocas com dados pessoais sensíveis foram retiradas.
- **Rótulos manuais.** Modelo, versão e papel foram digitados pelo autor e não foram conferidos com registros dos provedores (há grafias variantes, como "ChagGPT").
- **Segmentação automática.** Os turnos são detectados pelos rótulos; um rótulo citado dentro de um texto pode gerar um turno falso.
- **Sem anexos.** PDFs, planilhas e imagens citados nas conversas não fazem parte do corpus; links privados foram removidos.
- **Conteúdo não verificado.** Respostas de IA podem conter erros e referências inexistentes. Nada aqui deve ser tomado como fato sem checagem.
- **Artefatos de exportação.** A conversão do Google Docs para Markdown deixa escapes (`\*`, `\_`) e tabelas imperfeitas; o texto não foi corrigido.

## Ética e privacidade

O autor é o principal sujeito do corpus e autorizou a publicação. Antes de publicar, foram mascarados 51 e-mails, 950 links para arquivos ou conversas privadas, endereços e identificadores, e retiradas 24 trocas (~152.000 palavras) com dados pessoais sensíveis. O procedimento está descrito em [`docs/ANONIMIZACAO.md`](docs/ANONIMIZACAO.md). Se você encontrar algum dado pessoal que tenha escapado, abra uma *issue* sem copiar o dado.

Os textos incluem saídas de modelos de IA. Quem for usá-los para treinar ou avaliar modelos deve verificar os termos de uso da OpenAI, Google, Anthropic e Perplexity sobre o uso de conteúdo gerado.

## Como citar

Use o botão **"Cite this repository"** (gerado a partir de [`CITATION.cff`](CITATION.cff)) ou:

```bibtex
@misc{alencastro_corpus_2026,
  author       = {Alencastro Curado Filho, André},
  title        = {Corpus de Orquestração Multi-IA: diálogos de um pesquisador com ChatGPT, Gemini, Claude e Perplexity (2025--2026)},
  year         = {2026},
  version      = {1.0.0},
  howpublished = {GitHub},
  url          = {https://github.com/andrealencastro/corpus-orquestracao-multi-ia},
  note         = {Licença CC BY 4.0}
}
```

## Licença

Textos, seleção, anotações e metadados estão sob [Creative Commons Atribuição 4.0 Internacional (CC BY 4.0)](LICENSE): qualquer pessoa pode copiar, adaptar e redistribuir, inclusive comercialmente, desde que cite a fonte. O script em `scripts/` segue a mesma licença.

## Autor

**André Alencastro Curado Filho** — médico (UNIFESP) com formação em filosofia (USP e Sorbonne); pesquisa em ciência cognitiva, filosofia da mente e saúde mental digital.

---

## Abstract (English)

This repository contains a naturalistic corpus of 25 working documents (≈2.44 million words; 2,432 speaker turns) in which a single researcher orchestrates several large language models — OpenAI ChatGPT, Google Gemini, Anthropic Claude and Perplexity — within the same sessions, for academic research, prompt engineering and deep-research planning (documents created between April 2025 and September 2026). Turns are labelled with the model and version as recorded by the author and, where applicable, with custom assistant roles (*Deep Guide*, *Prompt Instructor*, *GPT Builder*, *Gems Builder*). The text is mostly Portuguese, with English and French. Personal data were masked or removed before release. Per-document and per-turn metadata are provided as CSV files, together with a datasheet, a codebook and a reproducible extraction script. Licensed under CC BY 4.0.
