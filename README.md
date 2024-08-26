# Resumo do Artigo 'Análise das Plublicações de Mídias ALternativas Compartildas em Paginas Piloticas no Facebook'

O artigo em questão apresentou como objetivo analisar as paginas de orinetação posliticas de esquerda e direitas no facebook, com o intuito de revelar mudanças nos temas mais discutidos antes do periodo eleirotal ( janiro a julho de 2022) e duranto ( agosto a outubro de 2022), dando um destaque para o aumento alarmante do tópico durante o periodo eleitoral.
Para a coleta, modelagem e pré-processamentos dos dados, foi ultilizado o algorimo _Latent Dirichlet Allocation_ (LDA) para a identificação de tópicos.

### introdução

Aprensentando dados do IBGE de 2022 sobre a população brasileira e o panorama digital no Brasil.

- Dos **185,4** milhões de individios com 10 anos ou mais,
  **87,2%**ultilizao a Internet.
- **98,9%** de ultilizacao pelo telefone móvel celular.
  Assim o engajamento em redes sociais se destaca com **83,6%** dos internautas.

Contudo, eessa expansão do cenário nao esta livre de problemas, como a influencia dos algoritimos, que por sua vez, embora propoe uma rotatividade de conteudo, tambem tendem a direcionar o usuario a informacoes que confirmam suas crencas e opinioes pre-estabelecidas, o que pode levar a uma polarização politica. Outro desafio apresntados no artigo, se trata das pessoas que sao mais receptivas a informaçoes falsas e tendem a compartilha-las, o que pode ser um problema para a democracia.

> É neste contexto, que o artigo apresneta um estudo que combinou tecnicas de mineração de dados e repcessamento de linguagem natural para analisar a discussao politica conduzida pelas midias alternativas no Facebook, no ano de 2022.
> O facebooc foi escolhido por ser uma das redes sociais mais populares no Brasil, e por ser um ambiente onde as pessoas podem compartilhar informaçoes e discutir sobre politica. E tambem, devido a sua vasa base de dados de usuario e à acessibilidade dos dados atraves da ferramentea _CrowdTangle_.

### Metodologia

<!-- #### Coleta de Dados -------------------------

FOi efetuada a coleta de postagens entre 01 de janeiro de 2022 e 30 de outubro de 2022, de paginas brasileiras classificadas com posição politica de esquerda ou direita.

- Fram analisadas **78** paginas.
  - **35** de direita.
  - **43** de esquerda.

Os dados foram coletados usando a platafirma _CrowdTangle_, uma ferramentea de analise de dados publicos da _Meta_ que simplifica o monitoramento, analise e relatorio de enventos, como os enventos etudadados no artigo.
A aplicação libera ate **300.000** postagens, realizadas num peiodo pre selecionado, e permite a exportação de dados em formato CSV.
Cabe resaltar que todas as postagens analisadas sao publicas e estao disponiveis para qualquer usuario do Facebook e todas as analises foram feitas anonimizadas e sem a identificação de usuarios. -->

<!-- TODO: Adicionar mais informações sobre a plataforma _CrowdTangle_. -->

A plataforma _CrowdTangle_ disponibiliza diversas informaçoes, das quals foram selecionadas as seguintes:

- **Type**: Tipo de postagem (foto, video, link, status).
- **Post Created Date**: Data de criação da postagem, indentificando o mes de criação da postagem, possibilitando a fiferenciação entre o conteudo veiculado antes e duranto o periodo eleitoral.
- **Link**: fornecendo a URL postada. Quando a URL ́e encurtada, a versão original e apresentada no campo Final Link. Ambos utilizados para determinar o dominio ao qual o link postado pertence.
- **Link Text**: contendo o tıtulo do link postado, geralmente correspondente ao tıtulo da pagina em questao. Seu conteudo foi empregado na modelagem dos topicos.

<!-- #### Pre-processamento -------------------------

A _LDA_ gera os topicos, que passam por varias etapas para garantir a qualidade e coerencia.
Foi observado que fontes como _Campo Grande News_ e o _Noticias Concursos_
Continham grate quantidade de postagens de temas diversos, como politica, economia, saude, entre outros, o que poderia prejudicar a qualidade dos topicos gerados. Assim, essas fontes foram removidas da analise, por demontrarem um percentual revelante de postagens do total de postagens analisadas.
Em seguida foi realizada uma concatenação de nomes propios aos seus sobrenomes, como por exemplo, _PAULO_ que pode se referir a _PAULO GUEDES_, _PAULO FREIRE_ ou _PAULO GUSTAVO_. Alem disso, consideream se as variacoes de entidades como a ciade de _São Paulo_, que pode ser referida como _SP_, _Sampa_ ou _SP_.
Essas medidas foram feitas para facilitar a identificacao especifica dos elementos que compes cada topico, reduzindo a ambiguidades na interpretação dos resultados.
Foi tabem realizado um refinamento no contexto dos titulos, para identificar evitar e suprimir termos desnecessarios, como _Fotos_, _Videos_, _Clique aqui_ ou _Leia mais_. Alem disso, foram removidos os chamados _stopwords_, que sao palavras comuns que nao contribuem para a identificacao de topicos, como _e_, _ou_, _de_, _para_, _com_, _em_, _por_, _na_, _no_, _da_, _do_, _das_, _dos_, _que_, _se_, _nao_, _como_, _uma_, _um_, _as_, _os_, _ao_, _aos_, _as_, _mas_, _pelo_, _pela_, _pelos_, _pelas_, _entre_, _sobre_, _sob_, _apos_, _ante_, _ate_, _apos_. Por fim, aseegurando a uniformidade e coesa dos dados, foram eliminatos caracteres especiaciais, numeros, emojis e pontuacoes. -->

#### Modelagem de Tópicos

O algoritimo do _LDA_ oderece uma abordagem probalbilistica para a indentificacao de topicos subjacentes em determinado documento, gerando a distribuição de palavras-chave associadas a cada topica, juntamente com sua probabilidade de ocorrencia.

> Para surtir o efeiro esperado na identificacao de assuntos depende da definicao adequada dos numeros de topicos para a badse de dados, tornando a selecao de paremetros um desafio e uma tarefa muito importante, que vem a impactar diretamente na qualidade do modelo e a imterpretabilidade dos tópicos gerados.

Auxiliando a decisao detes parametros foi utilizado o metodo de _Coerencia_ Cv. A _Coerencia_ Cv e uma metrica que avalia a interpretabilidade dos topicos gerados pela LDA, a partir da avaliacao da semantica das palavras-chave associadas a cada topico.
A metrica e calculada a partir da media dos scores de _Coerencia_ de cada topico, que por sua vez, e calculado a partir da media dos scores de _Coerencia_ de cada par de palavras-chave associadas a cada topico. A _Coerencia_ de um par de palavras e calculada a partir da probabilidade de co-ocorrencia das palavras no corpus de texto, e a _Coerencia_ de um topico e calculada a partir da media das _Coerencias_ de todos os pares de palavras-chave associadas ao topico.

> Seguindo a recomendacao de [Hagen 2018], optou-se por limitar o numero de topicos a **50**, uma medida preventiva para garantir a viabilidade da analise dos topicos por especialistas hu-manos.
> A fim de encontrar o melhor valor, variou-se o numero de topicos em incrementos de 5 e a cada variacao, o modelo LDA era ajustado com numeros de passos de 10 a 100,
> com incrementados a cada 10. Tal abordagem visou aprimorar a qualidade e a estabilidade da geracao de topicos. ![alt text](image.png)

> Quanto maio a pontuacao de _Coerencia_ C<sub>v</sub>, melhor a qualidade do modelo, com uma forte associacao semanticaentre as palavas de um topico, contribuindo para uma interpretação mais clara e siginificativa.
> Com uma analise da **`FIGURA 1`** notou se que o numero ideal de topicos para os dados da esquer é de 50 topicos, com 01 passos. para a direira é de 35 topicos, com 10 passos (embora a direita tenha apresentado estabilidade em relacao a coerencia, uma menor numro de topicos resultou em uma mistura de temas como eleicoes e politica, dificuldanto a distincao entre eles).
> Apos definir o numro orimo de topocos para a LDA, dividiu a bade de dados de cada posicao entre preriodos pre-eleitoral e eleirotal. Por fim execultando o algooritim ao gerando os topicos de cada epoca.

### Rotulagem de Tópicos

No processo de atribuicao de rotulos aos topicos, utilizou-se uma abordagem de especialistas humanos para associar significado a eles. Essa metodologia envolveu a analise dos topicos gerados pelo LDA, considerando a distribuicao de palavras-chave em cada um. Nesse processo, o especialista examinou a coesao semantica das palavras para identificar o tema principal de cada topico. Essa rotulagem permitiu agregacao dos topicos em temas de forma mais ampla. ![alt text](image-1.png)

### Resultados

- ### Enfoque nos topicos eleicoes e politica

Durante os 10 meses de 2022 analisados, as mencoes aos temas de Eleicoes e Polıtica em publicacoes associadas a direita e a esquerda revelam padroes distios.

media mensal de referecias somando ambos:

##### - Direita: 27,2%

      - minimo de `21,6% em fevereiro`;
      - maximo de `36,3% em outubro`.

##### - Esquerda: 48,8&

      - minimo `35,9% em março`;
      - maximo `73,1% em outubro`;

Essa ocilação é evidenciada pela variabilidade expressa nos devios padrçao, registrando: - 4,4% para a **Direita**. - 14,9% para a **Esquerda**.

# Topico especifico de **_Eleicoes_**.

### media mensal de mencoes

- ## Direita
  - `mensal de 19,2%`com desvio padrao de 6,5%.
  - menor registro de `13,1% em fevereiro`
  - mair registro de `32,1% em outubro`
- ## Esquerda
  - `mensal de 26,5%` com desvio padrao de 12,1%.
  - menor registro de `16,8% em março`
  - maior registro de `45,6% em outubro`

# Topico espefico de **_Politica_**

### Media Mensal de postagens

- ## Direita
  - 8,0% com desvio pardrao de 2,5%
  - menor registro de `4,3% em outubro`
  - maior registro de `10,4% em março`
- ## Esquerda
  - 22,4% com desvio padrao de 3,1%
  - menor registro de `18,8% em janeiro`
  - maior registro de `27,5% em outubro`

![alt text](image-2.png)

> O topico **_Pilitica_** teve menos ocilacoes sendo abordadas por ambos de maniera mais consistente
> O topico **_Eleições_** apresentou mais oscilação, especialmente para a **Esquerda** durante o periodo eleirotal.

> Essa variabilidade resalta como as elecoes presidenciais podem desemcadear mudancas nas discurssoes online, resaltando a importancia que tem sido dado por parte das midas alternativs.

### outro enfoque

Em resumo, ambos os espectros polıticos aumentaram seu envolvimento com Eleicoes durante as eleicoes presidenciais de 2022, com a esquerda demonstrando um aumento mais expressivo em termos relativos, enquanto a direita exibiu uma resposta mais variada e moderada em comparacao
