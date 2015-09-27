#-*- coding: utf-8 -*-                                                 
import datetime, string, rdflib as r, time,urllib, uuid, re
from dateutil.parser import parse
T=time.time()
f=open("/disco/repos/ensaaio/data/labmacambira_lalenia3.txt")
lines=f.readlines()
l=[i for i in lines if ";aa" in i]
lfoo=[i for i in lines if "aa;" in i]
##p=re.compile("(?P<year>[1-9][0-9]{3}-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9])")
##p=re.compile("(?P<year>[1-9][0-9]{3}-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9])\s+<(?P<nick>\S+)>")
p=re.compile("(?P<datetime>[1-9][0-9]{3}-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9])\s+<(?P<nick>\S+)>\s+;aa\s+(?P<shout>[\s\S]+)")
shLL=[]
lN=[]
for ll in l:
    m=p.search(ll)
    if "group" in dir(m):
        dt=m.group("datetime")
        nick=m.group("nick")
        shout=m.group("shout").strip()
        shLL+=[(dt,nick,shout)]
    else:
        lN.append(ll)
#f=open("./pickle/shLL.pickle", 'wb')
#pickle.dump(shLL,f)
#f.close()
#
g = r.Graph()
#g.load("aaStore.rdf")
print time.time()-T; T=time.time()
g.namespace_manager.bind("xsd", r.namespace.XSD)    
g.namespace_manager.bind("aa", "http://purl.org/socialparticipation/aa/")    
rdf = r.namespace.RDF
aa = r.Namespace("http://purl.org/socialparticipation/aa/")
xsd = r.namespace.XSD


aam = aa.Shout
aas = aa.Session
aap = aa.User
shouts_=shLL
count=0
for shout in shouts_:
    count+=1
    uri=aam+"#"+str(uuid.uuid4())
    #print uri
    g.add((uri,rdf.type,aa.Shout))
    g.add((uri,aa.provenance,r.Literal("IRC")))
    # acha user pelo nick, usa uri. Caso contrario monta
    uri_=aap+"#"+urllib.quote(shout[1])
    if uri_ not in g.subjects(rdf.type, aa.User):
        g.add((uri_,rdf.type,aa.User))
        g.add((uri_, aa.nick, r.Literal(shout[1],datatype=xsd.string) ))
    #    print uri_ +" n tem"
    else:
        pass #print uri_ +" jah tem"
    g.add((uri,aa.user,uri_))
    # pulado task_id pois nao há mais dados
    # na base para relacionar com ele
    message=shout[2].decode("iso-8859-1")
    g.add((uri,aa.shoutMessage,r.Literal(message,datatype=xsd.string)))
    created=parse(shout[0])
    g.add((uri,aa.created,r.Literal(created,datatype= xsd.dateTime)))

# See this git repo for data binaries:
# https://github.com/ttm/ensaaio

#f=open("/disco/repos/ensaaio/scripts/pickle/um_ss_.pickle", 'rb')
#um_,ss_,shd_,shLL_=pickle.load(f)
#print(time.time()-T)

# gravar grafo,
f=open("aaStoreIRC.rdf","wb")
f.write(g.serialize())
f.close()
print time.time()-T; T=time.time()
f=open("aaStoreIRC.ttl","wb")
f.write(g.serialize(format="turtle"))
f.close()
print time.time()-T; T=time.time()
print("triplifique tb o que estah no mongodb e mysql")
