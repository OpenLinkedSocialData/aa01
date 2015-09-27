#! /usr/bin/env python3
#-*- coding: utf8 -*-
# use com:
# sudo cp aa.py /usr/local/bin/aa
# aí na linha de comando:
# $aa fazendo x pq y

# Configuration:
NICK="anonymous"
OReDIR="/home/r/repos/ORe/python/hooks/aa"
aamongo=True
ORe=True


import sys, string, urllib
import datetime, random, rdflib as r
aa = r.Namespace("http://purl.org/socialparticipation/aa/")
xsd = r.namespace.XSD
rdf = r.namespace.RDF
if len(sys.argv)==1:
    print("usage: aa this is a aa shout, for registering ongoing work")
else:
    shout=" ".join(sys.argv[1:])
    if aamongo:
        urllib.request.urlretrieve("http://aaserver.herokuapp.com/shout?nick=%s&shout=%s"%(NICK,urllib.parse.quote(shout)))
        print("shout mongo logged")
    if ORe:
        g=r.Graph()
        # ID is datetime with milisseconds and 5 digit random number
        tid=str(datetime.datetime.now().timestamp())
        tid+=''.join(["%s" % random.randint(0, 9) for num in range(0, 5)])
        uri=aa.Shout+"#"+tid
        g.add((uri,rdf.type,aa.Shout))
        g.add((uri,aa.provenance,r.Literal("ORe",datatype=xsd.string)))
        uri_=aa.User+"#"+NICK
        g.add((uri_,rdf.type,aa.User))
        g.add((uri_, aa.nick, r.Literal(NICK,datatype=xsd.string) ))
        g.add((uri,aa.shoutMessage,r.Literal(shout,datatype=xsd.string)))
        g.add((uri,aa.created,r.Literal(datetime.datetime.now(),datatype= xsd.dateTime)))
        if aamongo:
            g.add((uri,aa.mongoDuplicate,r.Literal(True,datatype=xsd.boolean)))

        filename="{}/{}.ttl".format(OReDIR,tid)
        f=open(filename,"wb")
        f.write(g.serialize(format="turtle"))
        f.close()
        print("shout ORe logged at {}".format(filename))
