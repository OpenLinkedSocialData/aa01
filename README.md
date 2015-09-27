aa01
====

O AA é a Autorregulação Algorítmica.

O aa 0.1 é o AA em flask e mongo via http na url mesmo, + facinho.

- [Recursos](#)
	- [Scripts básicos](#)
		- [aaServer.py](#)
		- [aa.py](#)
		- [aaTwitter.py](#)
	- [Instância online para exibir e disponibilizar os dados](#)
- [Descrição](#)
	- [Formatação da mensagem](#)
	- [Exemplo de implementação em software](#)
- [Questões:](#)

# Recursos

## Scripts básicos
### aaServer.py

Um aplicativo mínimo em Flask cujos caminhos e funções são:

* /minimumClient/ -> exibe os shouts
* /allJson/ -> retorna os shouts todos como json
* /shout/ -> usado para registrar novo shout via GET, com ?nick=anonymous&shout=;aqui a mensagem de aa

### aaORe.py

Atual script mínimo para usar o aa via linha de comando
com possibilidades de publicar o shout em um cliente mongo
ou em RDF via ORe(\*). Pode ser usado com:

    $ sudo cp aaORe.py /usr/local/bin/aa
    $ aa primeira mensagem de aa, ainda anonima

Para colocar seu nick, abra o aa.py e mude o valor da variável NICK.
Caso use ORe, indique o caminho onde escreverá os RDFs de cada shout.

(\*) https://github.com/ttm/ORe

### Git hook para integrar os shouts ao trabalho sem overhead

    $ cp hooks/post-commit path_to_repo/.git/hooks

Pronto, ao commitar no repo, a mensagem de commit será
enviada aos bancos de AA com o início #gitcommit :: para
melhor identificação

### aa.py

Script mínimo para usar o aa via linha de comando.
Subsumido pelo aaORe.py.
 Pode ser usado com:

    $ sudo cp aa.py /usr/local/bin/aa
    $ aa primeira mensagem de aa, ainda anonima

Para colocar seu nick, abra o aa.py e mude o valor da variável NICK.

### aaTwitter.py

Registra as mensagem que usarem a hashtag #aao0 como shouts de aa.
Para subir, substitua Procfile e requirements.txt por BACK/Procfile.stream e BACK/requirements.txt.stream
respectivamente. Depois
    $ heroku login
    $ heroku create myaastreamer
    $ git push heroku master

## Instância online para exibir e disponibilizar os dados

Para subir, substitua Procfile e requirements.txt por BACK/Procfile.server e BACK/requirements.txt.server
respectivamente. Depois: 

    $ heroku login
    $ heroku create myaaserver # modifica o acesso no .git/config
    $ git push heroku master 

Provisório talvez, mas aqui está:
* http://aaserver.herokuapp.com/minimumClient/ para ver todos os shouts
* http://aaserver.herokuapp.com/allJson/ para receber todos os shouts via json
* http://aaserver.herokuapp.com/shout?nick=oNickOuAnonimo&shout=a mensagem de shout eh registrada como necessário => para registrar os shouts via http.
* No canal IRC #labmacambira/Freenode, os shouts são registrados pela lalenia sempre que a mensagem começa com ;aa
* Tweets que possuam a hashtag #aao0 são registradas pelo streamer.

# Descrição

## Formatação da mensagem

Uma mensagem de aa (um 'shout') possui 3 partes.

    __ __ __ ___ <!?.,;:> msg msg msg msg
    |------------|-------|---------------|
    |  Parte 1    Parte 2    Parte 3

Exemplo:

    bc rs jg rr: rascunhado sobre o jogo para a lista, incorporado recursos redes sociais, para batalha entre os tecidos de amigos

A primeira parte possui as classes (tags) "bc", "rs", "jg" e "rr". o ":", são classificadores da mensagem.
A segunda parte é o divisor entre a classificação e a mensagem em si.
A terceira parte é a mensagem propriamente dita, uma descrição em linguagem natural (ou da preferência do usuário) do que quer feito.

Restrições:
* Não deve haver pontuações de separação (nenhuma destas: !?.,;:) nos nomes das classes.
* As classes devem estar separadas por espaço simples " ", quantos forem.
* Qualquer uma das pontuações de separação (!?.,;:) sinaliza que o caracter seguinte é o início da mensagem de aa

Mais especificações e recursos:
* Na terceira parte do shout, palavras com # são classes (é removida cerquilha "#" inicial). Atenção: ##capimEfruta na terceira parte é a classe #capimEfruta.
* Como metadados da mensagem, além das classes (tags), há o nick/nome e o horário da mensagem.
* Nick anônimo e horário indefinido são especificações válidas.
* Pode-se especificar ou sobrescrever etiquetas/tags/classes com o comando separador composto :::>>>. Exemplos:

    jj :::>>> bc jg rs sl (jj é classe que é as outras quatro classes)
    
    ut :::>>> finalização, últimos retoques para terminar milestone ou projeto ou mídia (ut marca esta etapa)

Mundo aberto, ou seja, a ausência da classe não implica que a classe não seja aplicável.
* A classe aaaaaa é padrão para o usuário, e pode ser sobrescrita normalmente:

    aaaaaa :::>>> ut aa lm

e usada começando o shout com uma pontuação de separação:

    ; especificando protocolo de registro de atividade para o lm
* A sintaxe está em plena discussão e evolução.
* Este conjunto de classes é uma recomendação inicial, escrita aqui para uso, modificação e discussão:

| Classe/Etiqueta/Tag | Significado |
| ------------------- | ----------- |
| dl                  | dados linkados, web semântica |
| re                  | reuniões |
| dc                  | documentações |
| gv                  | governo, estado |
| in                  | institucional   |
| jd                  | jardinagem e trabalhos referentes à terra e cultivos |
| li                  | linguística |
| pr                  | programação de computadores |
| so                  | sociedade/ativismo/crítica social |  
| sa                  | referente ao sagrado |
| art                  | artes      |
| mu                  | música      |
| ma                  | matemática  |
| es                  | escrita     |
| eg                  | email group |
| id                  | identi.ca   |
| di                  | diaspora    |
| fb                  | facebook    |
| irc                 | irc         |
| vc                  | visão computacional |
| cc                  | criatividade computacional |
| rs                  | redes sociais |
| jg                  | jogos       |
| lm                  | referente ao labMacambira.sf.net |
| mm                  | mão na massa, fazeção   |
| bc                  | referente ao bem comum |
| aa                  | referente ao acrônimo ambíguo |


## Exemplo de implementação em software

O AA (autorregulação algorítmica) pode ser implementado de várias formas. Aqui está uma descrição como implementada neste repositório, para fins de uso do labMacambira.sf.net.

Esta implementação recebe mensagens (shouts) via HTTP. Por onde é fácil implementar facilidades em linha de comando, IRC, twitter, etc. As mensagens recebidas são enviadas para um BD mongo online (gratuíto pode-se usar 500mb, o que basta), usuário de Twitter. Há facilidades para envio da mensagem para repasse pela lalenia e para integração via dados linkados (triplas RDF, talvez em conjunto aos dados do particia.br, com as ontologias OPA e OPS).

Esquematicamente:

    IRC                       ->                    -> BD mongo
    linha de comando          ->      HTTP (flask)  -> triplas RDF
    Twitter                   ->                    -> Twitter
    (fb? identi.ca? diaspora) ->                    -> lalenia

Interfaces para visualização dos dados de AA acessam o BD mongo ou as triplas RDF via algum endpoint SparQL.


==========

#Questões: 
* Convencionamos tags de 1 letra só ou fica muito difícil de ler?
* Há já algum conjunto de tags que podemos usar? geekcode?
* Colocar reiniciar do streamador no cron?
