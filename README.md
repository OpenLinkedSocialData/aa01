aa01
====

aa 0.1 é o aa em flask e mongo via http na url mesmo, + facinho

1. Descrição

1.1. Formatação da mesagem

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








==========

Questões: convencionamos tags de 1 letra só ou fica muito difícil de ler?

