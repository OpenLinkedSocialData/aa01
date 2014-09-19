## Anotações sobre a triplificação dos dados do AA

### Roteiro de triplificação:
* Cria base de dados e restaura do .sql
    $ tar zxvf dump.tar.gz
    $ mysql -u root -p
    create database fbdb
    <Ctrl+c> (sai do mysql)
    $ mysql -u root -D fbdb -p < dump.sql
* abre script triplificaAA.py para ver se o acesso ao BD está ok, basta esta linha:
    db=_mysql.connect(user="root",passwd="foobar",db="fbdb")
* executa script com:
    $ python triplificaAA.py
* caso necessário, instale as bibliotecas:
    $ pip install rdflib MySQL-python
Pode ser necessário também instalar o via pip o pacote: mysql-connector-python.

### Data-driven ontology development
Nesta triplificação que ficou claro o seguinte procedimento
para levantamento de vocabulários e ontologias voltado para os dados:
* Os dados são analisados, as tabelas, e já classificados e relacionados em um namespace interno.
 * No caso do aa é: http://purl.org/socialparticipation/aa/
 * Os itens são decididos na escrita do script. O namespace interno permite revisão dos nomes e definições sem problema. Os dados existem e receberão tipos e terão relacionentos.
* Toda equivalência com namespaces como OPA, OPS, DC, FOAF, é feita em uma ontologia. Assim, os dados encontrados são triplificados e integram os recursos disponibilizados em RDF e ontologias.

Por exemplo, para o Cidade Democrática:
* Analisar as tabelas, já relacionando em um namespace interno: http://purl.org/socialparticipation/ocd/ em um script de triplificação.
* Relacionar os itens do namespace entre si e com outros namespaces na ontologia ocd: opa, ops, dc, foaf, viac, etc.

São 3 grafos principais: dos dados triplificados da instância, da ontologia da instância, e de ambos os grafos em conjunto, que permite ao reasoner inferir respostas às queries sparql. Há um quarto grafo: o que é disponibilizado para o cliente que faz a query. Ele consiste em todas as triplas declaradas em ambos os grafos da triplificação e da ontologia, e ainda de todas as triplas fruto das inferências.
