#-*- coding: utf-8 -*-
import pymongo, datetime, string, rdflib as r, time
T=time.time()
client=pymongo.MongoClient("mongodb://labmacambira:macambira00@ds031948.mongolab.com:31948/aaserver")
shouts=client.aaserver.shouts.find({})
shouts_=[shout for shout in shouts]

g = r.Graph()
g.load("aaStore.rdf")
print time.time()-T; T=time.time()
g.namespace_manager.bind("xsd", r.namespace.XSD)    
g.namespace_manager.bind("aa", "http://purl.org/socialparticipation/aa/")    
rdf = r.namespace.RDF
aa = r.Namespace("http://purl.org/socialparticipation/aa/")
xsd = r.namespace.XSD


aam = aa.Shout
aas = aa.Session
aap = aa.User
count=0
count2=0
for shout in shouts_:
    uri=aam+"#"+str(shout["_id"])
    g.add((uri,rdf.type,aa.Shout))
    g.add((uri,aa.provenance,r.Literal("MongoDB")))
    user=aap+"#"+shout["nick"]
    if user not in g.subjects(rdf.type, aa.User):
        print user
        g.add((user,rdf.type,aa.User))
        g.add((user, aa.nick, r.Literal(shout["nick"]) ))
    else:
        print user +" jah tem"
    g.add((uri,aa.user,user))
    # pulado task_id pois nao há mais dados
    # na base para relacionar com ele
    message=shout["shout"]
    g.add((uri,aa.shoutMessage,r.Literal(message)))
    created=shout["time"]
    g.add((uri,aa.created,r.Literal(created,datatype= xsd.dateTime)))

print time.time()-T; T=time.time()
print "muito bem"
# gravar grafo,
f=open("aaStoreMongo.rdf","wb")
f.write(g.serialize())
f.close()
print time.time()-T; T=time.time()
f=open("aaStoreMongo.ttl","wb")
f.write(g.serialize(format="turtle"))
f.close()
print time.time()-T; T=time.time()


