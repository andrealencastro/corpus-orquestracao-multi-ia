---
id: P03
titulo_original: "Projetos de pesquisa"
grupo: pesquisa-academica
fonte: "Google Docs do autor (pasta IA/Conversas)"
criado_em_drive: 2025-08-29
modificado_em_drive: 2026-09-12
exportado_em: 2026-09-23
formato: "Markdown (exportação nativa do Google Docs)"
parte: "3/3"
trechos_removidos: 0
palavras_removidas: 0
redacoes: 42
licenca: CC-BY-4.0
---

> P03 · Projetos de pesquisa — [parte 1](P03-projetos-de-pesquisa_parte-1-de-3.md) · [parte 2](P03-projetos-de-pesquisa_parte-2-de-3.md) · [**parte 3**](P03-projetos-de-pesquisa_parte-3-de-3.md)

# Claude Opus 5 diz:

Aceito as duas correções. RA é melhor que minha condicionalização — a objeção sobre a forma canônica ser arbitrariamente privilegiada está certa, e um modelo constante não sobe em RA num conjunto balanceado. E T ∝ D de fato não isola nada porque muda o compute junto; o grid esparso de 9 condições com pares compute-matched resolve isso melhor do que eu tinha resolvido.

Resta um buraco, e ele bloqueia a especificação.

**C não está definida em D \= 1\.** Com uma única realização por conteúdo, não existe invariância a medir — e D \= 1 é a âncora dos três contrastes compute-matched. O desenho precisa declarar qual teste de invariância está usando, porque as duas versões possíveis se comportam de modo diferente:

Se a invariância for medida sobre formas vistas no treino — o modelo trata como intercambiáveis as D formas que aprendeu, em estruturas lógicas novas —, ela é bem posta a partir de D \= 2 e simplesmente indefinida em D \= 1\.

Se for medida sobre formas retidas, o corpus tem que tornar a equivalência inferível: a forma retida precisa aparecer no treino ligada a *outros* conteúdos, e tem que haver alguma pista distribucional de que f₅ ≡ f₁. Sem isso, você está testando embeddings nunca treinados e o fracasso é garantido por construção, não por hipótese.

A consequência prática: A fica definida em {1,2,4,8} e C em {2,4,8}. Comparar ∂A/∂D com ∂C/∂D sobre domínios diferentes é decidível agora e desagradável de descobrir em março.

**A dissociação aparece melhor numa decomposição de três vias do que em duas curvas.** Por item, classifique: consistente-correto, consistente-incorreto, inconsistente. H3 prevê que, à medida que D sobe, os itens inconsistentes migram para consistente-incorreto mais rápido do que para consistente-correto. Isso *é* invariância sem competência, direto num gráfico só. RA é a primeira célula; a célula interessante é a segunda, e ela não foi nomeada em nenhuma das duas propostas.

Dois ajustes menores. Concordância corrigida por acaso fica instável quando as marginais são assimétricas — com acurácia subindo para o teto você entra na patologia clássica do κ, concordância bruta alta e κ desabando. Balanceie o conjunto de rótulos por construção e reporte as marginais por condição. E a tensão sobre comprimento se dissolve: numa gramática artificial as duas construções podem ser desenhadas com contagem de tokens idêntica (`A rel B` vs `B rel-pass A`, três tokens de qualquer jeito). Um token por forma no braço lexical e length matching exato no braço sintático são compatíveis.

**Declare um contraste primário antes de rodar.** Nove condições respondendo a três perguntas diferentes é um jardim de caminhos que se bifurcam. Os pares compute-matched são a alegação causal mais limpa sobre D; declare-os primários por escrito e o resto como secundário. É isso que faz um resultado nulo ser defensável em vez de constrangedor.

Verifiquei o FLD: real, ICML 2023, Morishita et al. E é pior do que o descrito — os fatos deles são deliberadamente construídos sem semântica, para que conhecimento prévio não ajude a resolver a tarefa. Ou seja, "corpus lógico sintético com conteúdo sem significado" está ocupado até o fundo. O nicho da interseção continua de pé, mas sem folga.

Sobre o Crabbé: verifiquei o curso e o nome do docente; a tese orientada e os trabalhos de M2 no entorno dele eu não verifiquei. Não muda a conclusão. E o "risco de anterioridade local alto" é boa notícia — converte duas semanas de busca em um e-mail. O que significa que o e-mail deve *perguntar*, não vender: "isso já está ocupado no seu grupo?" Uma pergunta é respondida; uma proposta pronta é arquivada.

Concordo que a discussão convergiu. Paro aqui.

Para escrever a especificação, preciso de uma coisa só: qual é o seu acesso a compute, e você já escreveu um training loop antes? A diferença entre GPU de laboratório, Colab pago e CPU decide o tamanho do modelo, o número de runs e portanto o que entra no núcleo obrigatório e o que vira extensão. O resto eu preencho.

# Tab 14

[image1]: img/P03-image1.png
[image2]: img/P03-image2.png
