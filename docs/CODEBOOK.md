# Codebook

Convenções do texto, papéis de assistente e campos das tabelas em `dados/`.

## Rótulos de falante no texto

O autor registrou cada fala com um rótulo em linha própria, em geral como título Markdown:

| Rótulo no texto | Significado |
|---|---|
| `# Eu:` (ou `I:`) | fala do autor |
| `# ChatGPT 5.6 Deep Guide diz:` | fala de IA: modelo + versão + papel (opcional) + verbo (`diz`, `says`) |
| `# Claude Opus 4.7 diz:` | fala de IA sem papel específico |
| `# Gemini 3 Pro:` | fala de IA sem verbo |
| `# Prompt Instructor 5 diz:` | fala de IA sem fornecedor explícito (fornecedor `desconhecido` nas tabelas) |

Títulos que antecedem um `Eu:` (por exemplo, `# DG Análise Internet/Empresas` ou uma data) funcionam como títulos de sessão.

## Papéis de assistente

| Papel (`papel`) | O que faz no corpus | Turnos |
|---|---|---:|
| `deep_guide` | *Deep Guide*: define como executar uma pesquisa — diagnóstico da tarefa, escolha de modelo/pipeline e prompt final para *deep research* | 418 |
| `prompt_instructor` | *Prompt Instructor*: produz ou refina o prompt pedido pelo autor | 191 |
| `gpt_builder` | *GPT Builder*: projeta GPTs personalizados (instruções, descrição, *conversation starters*) | 65 |
| `gems_builder` | *Gems Builder*: o mesmo para Gems do Gemini | 43 |
| (vazio) | modelo usado diretamente, sem papel | 1334 |

Estruturas recorrentes nas respostas: **Diagnóstico 3D** (ambiguidade e risco de 1 a 5, e tipo de tarefa), **Arquitetura & Seleção** (modelo/pipeline + técnica), **Prompt Final / Template Mestre**, **Evidence Ledger** e taxonomia de evidência **Fato A/B/C** (A: fonte primária ou verificável; B: fonte secundária confiável ou inferência sustentada; C: hipótese ou informação não verificável).

## `dados/turnos.csv`

| Campo | Descrição |
|---|---|
| `doc_id` | ID do documento (M01–M14, P01–P06, S01–S05) |
| `arquivo` | arquivo onde o turno está |
| `linha` | linha do rótulo no arquivo (contando o cabeçalho YAML) |
| `turno` | posição do turno no documento (1, 2, 3…) |
| `falante` | `humano` ou `ia` |
| `rotulo_original` | rótulo como escrito pelo autor, sem marcação Markdown |
| `fornecedor` | `openai`, `anthropic`, `google`, `perplexity`, `xai` ou `desconhecido` |
| `modelo` | nome e versão do modelo extraídos do rótulo (vazio quando não há fornecedor explícito) |
| `papel` | `deep_guide`, `prompt_instructor`, `gpt_builder`, `gems_builder` ou vazio |
| `palavras` | número de palavras do turno (tokens `\w+`) |

## `dados/catalogo.csv`

| Campo | Descrição |
|---|---|
| `doc_id`, `titulo_original`, `grupo` | identificação do documento |
| `arquivos` | arquivo(s) do documento, separados por espaço |
| `criado_em_drive`, `modificado_em_drive` | datas do Google Drive |
| `palavras`, `turnos_humano`, `turnos_ia` | contagens |
| `turnos_ia_por_fornecedor` | ex.: `openai:106;google:94` |
| `modelos_distintos` | número de rótulos de modelo diferentes |
| `idioma_principal`, `prop_pt`, `prop_en`, `prop_fr` | estimativa por palavras funcionais |
| `trechos_removidos`, `palavras_removidas`, `redacoes` | anonimização (ver `ANONIMIZACAO.md`) |

## Fornecedores e modelos (como rotulados)

A versão é a que o autor escreveu; não foi conferida com os provedores.

| Fornecedor | Modelo | Turnos |
|---|---|---:|
| Anthropic (Claude) | Claude Opus 4.7 | 117 |
| Anthropic (Claude) | Claude Opus 5 | 81 |
| Anthropic (Claude) | Claude Opus 4.1 | 80 |
| Anthropic (Claude) | Claude Sonnet 4 | 59 |
| Anthropic (Claude) | Claude Opus 4.5 | 58 |
| Anthropic (Claude) | Claude Opus 4.8 | 43 |
| Anthropic (Claude) | Claude Sonnet 4.5 | 42 |
| Anthropic (Claude) | Claude Opus 4 | 21 |
| Anthropic (Claude) | Claude Fable 5 | 20 |
| Anthropic (Claude) | Claude Opus 4.6 | 13 |
| Anthropic (Claude) | Claude | 7 |
| Anthropic (Claude) | Claude Sonnet 4.6 | 6 |
| Anthropic (Claude) | Claude Opus 4.8 DG | 5 |
| Anthropic (Claude) | Claude Opus 4.8 PI | 3 |
| Anthropic (Claude) | Claude Opus | 2 |
| Anthropic (Claude) | Claude Opu 4.7 | 1 |
| Anthropic (Claude) | Claude Sonnet 4.1 | 1 |
| Anthropic (Claude) | O desenho do Claude | 1 |
| Anthropic (Claude) | Claude escreve | 1 |
| Anthropic (Claude) | Claude está certo sobre | 1 |
| Anthropic (Claude) | Claude 5 Opus | 1 |
| Anthropic (Claude) | Claude 6 Astra | 1 |
| Anthropic (Claude) | Claude 4 Framework | 1 |
| Anthropic (Claude) | Claude é melhor para | 1 |
| Anthropic (Claude) | Claude is correct that | 1 |
| Anthropic (Claude) | Claude is also correct that | 1 |
| Google (Gemini) | Gemini 2.5 Pro | 245 |
| Google (Gemini) | Gemini 3 Pro | 203 |
| Google (Gemini) | Gemini 3.5 Flash | 28 |
| Google (Gemini) | Gemini 2.5 | 15 |
| Google (Gemini) | Gemini | 10 |
| Google (Gemini) | Gemini 3.1 Pro | 8 |
| Google (Gemini) | Gemini 3.5 Flash DG | 5 |
| Google (Gemini) | Gemini 3 | 4 |
| Google (Gemini) | Gemini 3.5 Flash PI | 3 |
| Google (Gemini) | Gemini 3.5 flash | 3 |
| Google (Gemini) | Gemini for long-horizon research. Document | 2 |
| Google (Gemini) | Gemini 3.6 Flash | 2 |
| Google (Gemini) | Gemini acertou a estrutura dos três buckets | 1 |
| Google (Gemini) | Promp Instructor Gemini 2.5 Pro | 1 |
| Google (Gemini) | Gemini 3.5 Flash Deep Research | 1 |
| Google (Gemini) | > Gemini 2.5 Pro | 1 |
| Google (Gemini) | Gemini 2.5 pro | 1 |
| Google (Gemini) | Gemini 2.5 Pro Framework | 1 |
| Google (Gemini) | Gemini é melhor para | 1 |
| Google (Gemini) | Gemini contributed an important operational improvement | 1 |
| OpenAI (ChatGPT) | ChatGPT 5.2 | 214 |
| OpenAI (ChatGPT) | ChatGPT 5 | 137 |
| OpenAI (ChatGPT) | ChatGPT 5.6 | 100 |
| OpenAI (ChatGPT) | ChatGPT o3 | 98 |
| OpenAI (ChatGPT) | ChatGPT 5.5 | 64 |
| OpenAI (ChatGPT) | ChatGPT 6 Astra | 15 |
| OpenAI (ChatGPT) | ChatGPT | 14 |
| OpenAI (ChatGPT) | ChatGPT 5.1 | 11 |
| OpenAI (ChatGPT) | Gemini 3 Pro | 9 |
| OpenAI (ChatGPT) | Gemini 2.5 Pro | 5 |
| OpenAI (ChatGPT) | ChatGPT 5.5 DG | 5 |
| OpenAI (ChatGPT) | ChatGPT 5.4 | 3 |
| OpenAI (ChatGPT) | ChatGPT 5.5 PI | 3 |
| OpenAI (ChatGPT) | ChagGPT 5.1 | 2 |
| OpenAI (ChatGPT) | ChagGPT 5.2 | 2 |
| OpenAI (ChatGPT) | Gemini | 2 |
| OpenAI (ChatGPT) | ChatGPT 4 | 2 |
| OpenAI (ChatGPT) | Chatgpt o3 | 1 |
| OpenAI (ChatGPT) | ChagGPT 5 | 1 |
| OpenAI (ChatGPT) | > ChatGPT o3 | 1 |
| OpenAI (ChatGPT) | ChatGPT 6 Astra 6 | 1 |
| OpenAI (ChatGPT) | ChatGPT 5.2 Promp Instructor | 1 |
| OpenAI (ChatGPT) | GPT Builer ChatGPT 5 | 1 |
| OpenAI (ChatGPT) | ChatGPT é melhor para | 1 |
| OpenAI (ChatGPT) | ChatGPT 5.6 Deep Gudie | 1 |
| Perplexity | Perplexity | 182 |
| Perplexity | Perplexity Pro | 15 |
| Perplexity | Perplexity não deve ser usado para | 1 |
| Perplexity | Perplexity 5 | 1 |

## Como regenerar as tabelas

```bash
python3 scripts/extrair_turnos.py
```
