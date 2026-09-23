# Anonimização

Como o repositório é público, os textos passaram por três etapas antes da publicação.

## 1. Seleção de documentos

A pasta original tinha 32 documentos. Entraram 25: os de metodologia multi-IA, pesquisa acadêmica e sessões mistas. Ficaram de fora 7 documentos sobre assuntos pessoais, administrativos ou de negócios.

## 2. Remoção de trocas inteiras

Uma "troca" vai de uma fala do autor (`Eu:`) até a próxima. Foram retiradas **24 trocas (~152.000 palavras)** que continham dados pessoais sensíveis do autor ou de terceiros. Cada uma foi substituída por um aviso no próprio texto:

> **[Trecho removido antes da publicação]** Esta troca (N palavras) continha dados pessoais sensíveis…

A identificação combinou busca por palavras-chave e revisão manual de cada caso; a decisão final foi do autor. O conteúdo removido não é publicado.

| Documento | Nº da troca | Palavras |
|---|---:|---:|
| S02 | 2 | 7.853 |
| S02 | 3 | 1.936 |
| S02 | 5 | 113 |
| S02 | 6 | 12.053 |
| S02 | 28 | 1.426 |
| S02 | 29 | 2.355 |
| S03 | 1 | 2.097 |
| S03 | 2 | 17.603 |
| S03 | 3 | 5.824 |
| S03 | 4 | 13.936 |
| S03 | 5 | 4.316 |
| S03 | 6 | 3.619 |
| S03 | 25 | 2.653 |
| S03 | 26 | 19.092 |
| S03 | 27 | 18.163 |
| S04 | 17 | 3.350 |
| S04 | 18 | 3.541 |
| S04 | 19 | 3.483 |
| S04 | 20 | 2.686 |
| S04 | 21 | 4.218 |
| S05 | 20 | 3.794 |
| S05 | 30 | 5.401 |
| S05 | 31 | 4.369 |
| S05 | 35 | 7.666 |

## 3. Mascaramento automático

Expressões regulares substituíram os seguintes itens em todo o corpus, com revisão dos resultados:

| Marca no texto | O que substitui | Ocorrências |
|---|---|---:|
| `[link removido]` | links para arquivos ou conversas privadas: Google Docs/Drive/Planilhas, anexos com URL assinada, conversas compartilhadas do ChatGPT, Claude, Gemini e Perplexity | 950 |
| `[e-mail removido]` | endereços de e-mail (exceto exemplos fictícios como `@example.com`) | 51 |
| `[endereço removido]`, `[residência]` | endereço e nome da residência do autor | 20 |
| `[ID do Drive removido]` | identificadores de arquivos do Google Drive | 4 |
| `[telefone removido]` | números de telefone | 1 |
| `[CPF removido]` | números no formato de CPF (eram exemplos fictícios em casos de teste; mascarados por precaução) | 4 |

Links públicos (artigos, sites institucionais, documentação) foram mantidos.

## Por documento

| Documento | Trocas removidas | Palavras removidas | Links | E-mails | Endereço/residência | Outros |
|---|---:|---:|---:|---:|---:|---:|
| M01 | 0 | 0 | 109 | 0 | 0 | 0 |
| M02 | 0 | 0 | 0 | 0 | 0 | 0 |
| M03 | 0 | 0 | 140 | 0 | 0 | 0 |
| M04 | 0 | 0 | 0 | 0 | 0 | 0 |
| M05 | 0 | 0 | 1 | 0 | 0 | 0 |
| M06 | 0 | 0 | 0 | 8 | 0 | 4 |
| M07 | 0 | 0 | 0 | 2 | 0 | 0 |
| M08 | 0 | 0 | 0 | 0 | 0 | 0 |
| M09 | 0 | 0 | 0 | 0 | 0 | 0 |
| M10 | 0 | 0 | 31 | 0 | 0 | 0 |
| M11 | 0 | 0 | 0 | 0 | 0 | 0 |
| M12 | 0 | 0 | 2 | 0 | 0 | 0 |
| M13 | 0 | 0 | 0 | 0 | 0 | 0 |
| M14 | 0 | 0 | 0 | 0 | 0 | 0 |
| P01 | 0 | 0 | 0 | 0 | 0 | 0 |
| P02 | 0 | 0 | 0 | 0 | 0 | 0 |
| P03 | 0 | 0 | 35 | 7 | 0 | 0 |
| P04 | 0 | 0 | 5 | 6 | 0 | 0 |
| P05 | 0 | 0 | 242 | 7 | 0 | 0 |
| P06 | 0 | 0 | 0 | 0 | 0 | 0 |
| S01 | 0 | 0 | 45 | 6 | 0 | 0 |
| S02 | 6 | 25.736 | 241 | 10 | 0 | 0 |
| S03 | 9 | 87.303 | 18 | 0 | 0 | 0 |
| S04 | 5 | 17.278 | 56 | 3 | 20 | 5 |
| S05 | 4 | 21.230 | 25 | 2 | 0 | 0 |

## O que foi mantido de propósito

- O nome do autor, sua formação e suas candidaturas acadêmicas, que fazem parte do contexto das sessões.
- Nomes de instituições, professores e pesquisadores citados em contexto acadêmico público.
- Menções genéricas a temas de saúde quando são objeto de pesquisa (por exemplo, propostas sobre biomarcadores digitais em saúde mental).

## Risco residual

A anonimização automática não é perfeita. Se você encontrar um dado pessoal, abra uma *issue* descrevendo onde está (arquivo e linha), sem copiar o dado. O autor corrige e publica uma nova versão.
