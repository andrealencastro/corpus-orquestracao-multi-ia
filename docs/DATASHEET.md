# Datasheet do corpus

Ficha técnica no formato proposto por Gebru et al., *Datasheets for Datasets* (Communications of the ACM, 2021).

## Motivação

**Para que o corpus foi criado?**
Para documentar e disponibilizar, com fins de pesquisa, um registro real de trabalho acadêmico feito com vários modelos de linguagem ao mesmo tempo. O corpus permite estudar como um pesquisador distribui tarefas entre modelos, como os modelos se criticam e como prompts e planos de pesquisa são refinados ao longo do tempo.

**Quem criou?**
André Alencastro Curado Filho, autor das falas humanas e responsável pela seleção, anonimização e publicação.

**Financiamento.**
Nenhum.

## Composição

**O que é cada instância?**
Um *documento* é um Google Doc de trabalho do autor com uma ou mais sessões de conversa. Cada documento é dividido em *turnos* de fala, do autor (`humano`) ou de uma IA (`ia`).

**Quantas instâncias?**
25 documentos (47 arquivos Markdown, porque os documentos longos foram divididos em partes), cerca de 2,44 milhões de palavras e 2.432 turnos: 381 do autor e 2.051 de IAs.

| Grupo | Documentos | Palavras |
|---|---:|---:|
| Metodologia multi-IA (M01–M14) | 14 | 911.603 |
| Pesquisa acadêmica (P01–P06) | 6 | 663.018 |
| Sessões mistas (S01–S05) | 5 | 867.931 |

**É uma amostra?**
É uma seleção. A pasta de origem tinha 32 documentos; 7 foram excluídos por tratarem de assuntos pessoais, administrativos ou de negócios, e 24 trocas com dados pessoais sensíveis foram retiradas dos documentos incluídos (ver [`ANONIMIZACAO.md`](ANONIMIZACAO.md)).

**O que cada instância contém?**
Texto em Markdown com as falas do autor e as respostas das IAs, precedido de um cabeçalho YAML com metadados. Duas imagens (um diagrama e uma fórmula) acompanham o documento P03.

**Há rótulos?**
Sim. Os rótulos de falante (`Eu:`, `ChatGPT 5.6 Deep Guide diz:` etc.) foram escritos pelo próprio autor durante o trabalho. A partir deles, `scripts/extrair_turnos.py` deriva fornecedor, modelo e papel de cada turno. Não há outras anotações.

**Há informação faltando?**
- Anexos citados nas conversas (PDFs, planilhas, imagens) não estão incluídos.
- Links para arquivos e conversas privadas foram substituídos por `[link removido]`.
- Parte dos rótulos não indica o fornecedor (54 turnos, fornecedor `desconhecido`).

**Há relações entre instâncias?**
Sim. Vários documentos retomam o mesmo projeto (por exemplo, M06 *GPTBuilder* e M07 *Gems Builder* constroem o mesmo assistente em plataformas diferentes; P04 e P06 se referem ao mestrado ST4H). As relações não estão codificadas nas tabelas.

**Há divisões recomendadas (treino/teste)?**
Não.

**Erros, ruído e redundância.**
- Versões de modelo são as anotadas pelo autor, com grafias variantes ("ChagGPT", "Gemin").
- Alguns prompts aparecem mais de uma vez, em versões sucessivas, por natureza do processo de refinamento.
- A exportação do Google Docs deixa escapes de Markdown e tabelas imperfeitas.
- Respostas de IA podem conter erros factuais, citações inexistentes e afirmações não verificadas.

**O corpus depende de recursos externos?**
Mantém links públicos (artigos, sites institucionais, documentação), que podem deixar de funcionar. Nenhum recurso externo é necessário para usar o texto.

**Há dados confidenciais?**
Foram removidos ou mascarados na medida do possível (ver [`ANONIMIZACAO.md`](ANONIMIZACAO.md)).

**Há pessoas identificáveis?**
O autor, que é identificado de propósito. Professores, pesquisadores e instituições aparecem quando citados em contexto acadêmico público; contatos pessoais (e-mails, telefones) foram removidos.

## Processo de coleta

**Como os dados foram obtidos?**
Durante o trabalho, o autor registrou as sessões em documentos Google Docs, identificando cada fala com um rótulo digitado por ele. As conversas ocorreram nas interfaces dos próprios serviços (ChatGPT, Gemini, Claude, Perplexity), inclusive em assistentes personalizados criados pelo autor.

**Período.**
Documentos criados entre abril de 2025 e setembro de 2026 (datas do Google Drive em `dados/catalogo.csv`).

**Exportação.**
Em 23 de setembro de 2026, pela API do Google Drive: 21 documentos na exportação nativa para Markdown do Google Docs e 4 documentos curtos (M09, M11, M13, P06) em HTML, convertidos para Markdown com pandoc. O formato de cada um está no cabeçalho YAML.

**Consentimento.**
O autor é o sujeito principal e autorizou a publicação. Terceiros mencionados não foram consultados; por isso, seus contatos e dados pessoais foram removidos.

## Pré-processamento

1. Seleção dos documentos (25 de 32).
2. Remoção de 24 trocas com dados pessoais sensíveis, substituídas por um aviso no texto.
3. Mascaramento automático de links privados, e-mails, telefones, endereços e identificadores.
4. Remoção de linhas vazias (`&nbsp;`) herdadas do Google Docs.
5. Extração das imagens embutidas para `corpus/pesquisa-academica/img/`.
6. Divisão dos documentos com mais de ~900 KB em partes de até ~700 KB, sempre entre turnos.

O texto não foi corrigido nem normalizado. As versões originais permanecem no Google Drive do autor e não são publicadas.

## Usos

**Usos previstos.**
Pesquisa em interação humano-IA; comparação de modelos em tarefas idênticas; estudo de crítica cruzada e adjudicação entre modelos; engenharia de prompts; metodologia de pesquisa assistida por IA; linguística de corpus em português, inglês e francês.

**Usos desaconselhados.**
- Inferir características pessoais, de saúde ou de comportamento do autor ou de terceiros.
- Tratar respostas das IAs como fatos verificados.
- Generalizar para outros usuários: o corpus é de uma única pessoa.

**Treinamento de modelos.**
Os textos incluem saídas de serviços comerciais de IA. Antes de usá-los para treinar ou ajustar modelos, verifique os termos de uso dos provedores.

## Distribuição

Publicado no GitHub em [andrealencastro/corpus-orquestracao-multi-ia](https://github.com/andrealencastro/corpus-orquestracao-multi-ia), versão 1.0.0 (23/09/2026), sob licença [CC BY 4.0](../LICENSE).

## Manutenção

Mantido pelo autor. Correções e pedidos de remoção podem ser feitos por *issue*. Novas versões seguem versionamento semântico (mudanças de conteúdo sobem a versão menor; correções, a versão de correção) e ficam registradas no histórico do Git.
