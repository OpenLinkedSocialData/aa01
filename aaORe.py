#! /usr/bin/env python
#-*- coding: utf8 -*-
# use com:
# sudo cp aa.py /usr/local/bin/aa
# aí na linha de comando:
# $aa fazendo x pq y

# Configuration:
NICK="anonymous"
OReDIR="repos/ore/python/hooks/aa"
aamongo=ORe=True

import sys, string, urllib
if len(sys.argv)==1:
    print("usage: aa this is a aa shout, for registering ongoing work")
else:
    shout=string.join(sys.argv[1:]," ")
    if aamongo:
        urllib.urlretrieve("http://aaserver.herokuapp.com/shout?nick=%s&shout=%s"%(NICK,urllib.quote(shout)))
        print "shout mongo logged"
    if ORe:
        # ID is datetime with milisseconds and 5 digit random number
        tid=str(datetime.datetime.now().timestamp())
        tid+=''.join(["%s" % randint(0, 9) for num in range(0, n)])
        uri=aa.Shout+"#"+tid
        g.add((uri,rdf.type,aa.Shout))
        g.add((uri,aa.provenance,r.Literal("ORe",datatype=xsd.string)))
        uri_=aa.User+"#"+nick
        g.add((uri_,rdf.type,aa.User))
        g.add((uri_, aa.nick, r.Literal("nick",datatype=xsd.string) ))
        g.add((uri,aa.user,uri_))
        g.add((uri,aa.shoutMessage,r.Literal(message,datatype=xsd.string)))
        g.add((uri,aa.created,r.Literal(datetime.datetime.now(),datatype= xsd.dateTime)))
        print "shout ORe logged"
