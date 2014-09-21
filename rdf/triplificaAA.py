#!/usr/bin/python
#-*- coding: utf-8 -*-
import rdflib as r
import _mysql
import time
T=time.time()
db=_mysql.connect(user="root",passwd="foobar",db="fbdb")
db.query("SET NAMES 'utf8'")
db.query('SET character_set_connection=utf8')
db.query('SET character_set_client=utf8')
db.query('SET character_set_results=utf8')

db.query("show tables;")
res=db.store_result()
aa_tables=[res.fetch_row()[0][0] for i in xrange(res.num_rows())]

d={}
for tt in aa_tables:
    db.query("select column_name from information_schema.columns where table_name='%s';"%(tt,))
    res=db.store_result()
    d["h"+tt]=[res.fetch_row()[0][0] for i in xrange(res.num_rows())]
    db.query("select * from %s;"%(tt,))
    res=db.store_result()
    d[tt]=[res.fetch_row()[0] for i in xrange(res.num_rows())]

aat=[i for i in aa_tables if d[i]]
print time.time()-T; T=time.time()

g = r.Graph()

#g.namespace_manager.bind("foaf", r.namespace.FOAF)    
#g.namespace_manager.bind("opa", "http://purl.org/socialparticipation/opa#")    
#g.namespace_manager.bind("ops", "http://purl.org/socialparticipation/ops#")    
#g.namespace_manager.bind("dce", "http://purl.org/dc/elements/1.1/")    
#g.namespace_manager.bind("dc", "http://purl.org/dc/terms/")    
g.namespace_manager.bind("xsd", r.namespace.XSD)    
g.namespace_manager.bind("aa", "http://purl.org/socialparticipation/aa/")    
rdf = r.namespace.RDF
#opa = r.Namespace("http://purl.org/socialparticipation/opa#")
#ops = r.Namespace("http://purl.org/socialparticipation/ops#")
aa = r.Namespace("http://purl.org/socialparticipation/aa/")
#foaf = r.namespace.FOAF
xsd = r.namespace.XSD
# registrar todos os nicks como participants
# colocar foaf nick e email neles
# dar URI http://purl.org/socialparticipation/aa#<nick>
aap = aa.User
du={}
count=0
for user in d["users"]:
    email=user[1]
    nick=user[2]
    if nick:
        uri=aap+"#"+nick
        du[user[0]]=uri
        g.add((uri,rdf.type,aa.User))
        g.add((uri,aa.mbox,r.URIRef("mailto:%s"%(email,)) ))
        g.add((uri, aa.nick, r.Literal(nick) ))
    count+=1

print time.time()-T; T=time.time()
# ver sessions, talvez já passar para RDF
aas = aa.Session
for session in d["sessions"]:
    uri=aas+"#"+session[0]
    g.add((uri,rdf.type,aa.Session))
    user=du[session[1]]
    g.add((uri,aa.user,user))
    created=session[2]
    g.add((uri,aa.created,r.Literal(created,datatype= xsd.dateTime)))
    if session[3]:
        if session[3] in du.keys():
            checker=du[session[3]]
            g.add((uri,aa.checker,checker))
        else:
            print "sem checker reconhecido"
    else:
        print "no checker"
    if session[4]:
        message=session[4]
        g.add((uri,aa.checkMessage,r.Literal(message)))
    else:
        print "no message"
    if session[5]:
        score=session[5]
        g.add((uri,aa.score,r.Literal(score,datatype=xsd.integer)))
    else:
        print "no score"
    if session[6]:
        sc=session[6]
        g.add((uri,aa.screencast,r.Literal(sc)))
    else:
        print "no screencast"
print time.time()-T; T=time.time()
# registrar mensagens finalmente
# todas as msgs estão registradas como shouts
aam = aa.Shout
count=0
count2=0
for shout in d["messages"]:
    uri=aam+"#"+shout[0]
    g.add((uri,rdf.type,aa.Shout))
    if int(shout[1]):
        uri_=aas+"#"+shout[1]
        g.add((uri,aa.session,uri_))
    uri_=aap+"#"+shout[1]
    if shout[2] in du.keys():
        user=du[shout[2]]
        g.add((uri,aa.user,user))
        count2+=1
    else:
        uri=aap+"#anon-"+shout[2]
        g.add((uri,aa.user,uri))
        count+=1
    # pulado task_id pois nao há mais dados
    # na base para relacionar com ele
    message=shout[4]
    g.add((uri,aa.shoutMessage,r.Literal(message)))
    created=shout[5]
    g.add((uri,aa.created,r.Literal(created,datatype= xsd.dateTime)))
    valid=shout[6]
    g.add((uri, aa.valid, r.Literal(valid,datatype=xsd.boolean)))

print time.time()-T; T=time.time()
print "muito bem"
# gravar grafo,
f=open("aaStore.rdf","wb")
f.write(g.serialize())
f.close()
print time.time()-T; T=time.time()
f=open("aaStore.ttl","wb")
f.write(g.serialize(format="turtle"))
f.close()
print time.time()-T; T=time.time()

# colocar online
# fazer diagrama dos dados
