#!/usr/bin/python
#-*- coding: utf-8 -*-
import rdflib as r
import time
T=time.time()

aa = r.Namespace("http://purl.org/socialparticipation/aa/")
rdf = r.namespace.RDF
rdfs = r.namespace.RDFS
foaf = r.namespace.FOAF
owl = r.namespace.OWL
dc=r.namespace.DC
dct=r.namespace.DCTERMS
dcty=r.Namespace("http://purl.org/dc/dcmitype/")
gndo=r.Namespace("http://d-nb.info/standards/elementset/gnd#")
sc=r.Namespace("http://schema.org/")
ops = r.Namespace("http://purl.org/socialparticipation/ops#")
sioc = r.Namespace("http://rdfs.org/sioc/ns#")
xsd = r.namespace.XSD

g = r.Graph()
g.namespace_manager.bind("ops", "http://purl.org/socialparticipation/ops#")    
g.namespace_manager.bind("rdf", r.namespace.RDF)    
g.namespace_manager.bind("rdfs", r.namespace.RDFS)    
g.namespace_manager.bind("foaf", r.namespace.FOAF)    
g.namespace_manager.bind("xsd", r.namespace.XSD)    
g.namespace_manager.bind("owl", r.namespace.OWL)    
g.namespace_manager.bind("ops", "http://purl.org/socialparticipation/ops#")
g.namespace_manager.bind("dc", "http://purl.org/dc/elements/1.1/")    
g.namespace_manager.bind("dct", "http://purl.org/dc/terms/")    
g.namespace_manager.bind("dcty", "http://purl.org/dc/dcmitype/")    
g.namespace_manager.bind("gndo", "http://d-nb.info/standards/elementset/gnd#")    
g.namespace_manager.bind("schema", "http://schema.org/")
g.namespace_manager.bind("sioc", "http://rdfs.org/sioc/ns#")    

# faz ontologia:
# 1) info sobre esta ontologia
ouri=aa.ontologiaa+".owl"
g.add((ouri,rdf.type,owl.Ontology))
g.add((ouri,dct.title,r.Literal("Ontologiaa")))
g.add((ouri,owl.versionInfo,r.Literal("0.01a")))
g.add((ouri,dct.description,r.Literal("Ontologia enxuta do AA para conectar o namespace da ontologia com outros namespaces")))

# 2) adicionadas classes pai das classes do aa
g.add((aa.User,    rdfs.subClassOf, foaf.Person))
g.add((aa.User,    rdfs.subClassOf, dc.Agent))
g.add((aa.User,    rdfs.subClassOf, ops.Participant))
g.add((aa.Shout,   rdfs.subClassOf, foaf.Document))
g.add((aa.Shout,   rdfs.subClassOf, sioc.Port))
g.add((aa.Session, rdfs.subClassOf, dcty.Collection))
g.add((aa.Session, rdfs.subClassOf, dcty.Event))

# 3) declaradas propriedades funcionais

# 4) adicionadas propriedades pai das propriedades
g.add((aa.checker, rdfs.subPropertyOf, gndo.revisor))
g.add((aa.session, rdfs.subPropertyOf, sc.collection))
g.add((aa.user, rdfs.subPropertyOf, foaf.maker))


g.add((aa.checkMessage, rdfs.subPropertyOf, sc.text))
g.add((aa.shoutMessage, rdfs.subPropertyOf, sc.text))
g.add((aa.screencast, rdfs.subPropertyOf, sc.video))

g.add((aa.created, owl.equivalentProperty, dct.created))
g.add((aa.nick, owl.equivalentProperty, foaf.nick))
g.add((aa.email, owl.equivalentProperty, foaf.created))

# ficaram sem: score
# 5) especificadas características das funções
g.add((aa.checker, rdf.type, owl.FunctionalProperty))
g.add((aa.checker, rdf.type, owl.ObjectProperty))
g.add((aa.session, rdf.type, owl.FunctionalProperty))
g.add((aa.session, rdf.type, owl.ObjectProperty))
g.add((aa.user, rdf.type, owl.FunctionalProperty))
g.add((aa.user, rdf.type, owl.ObjectProperty))

g.add((aa.checkMessage, rdf.type, owl.FunctionalProperty))
g.add((aa.checkMessage, rdf.type, owl.DataProperty))
g.add((aa.shoutMessage, rdf.type, owl.FunctionalProperty))
g.add((aa.shoutMessage, rdf.type, owl.DataProperty))
g.add((aa.screencast, rdf.type, owl.FunctionalProperty))
g.add((aa.screencast, rdf.type, owl.DataProperty))

g.add((aa.created, rdf.type, owl.FunctionalProperty))
g.add((aa.created, rdf.type, owl.DataProperty))
g.add((aa.nick, rdf.type, owl.FunctionalProperty))
g.add((aa.nick, rdf.type, owl.DataProperty))
g.add((aa.email, rdf.type, owl.FunctionalProperty))
g.add((aa.email, rdf.type, owl.DataProperty))

# 6) declaradas restricoes existenciais
# object property somente o aa:user
b_=r.BNode()
g.add((aa.Shout, rdfs.subClassOf, b_))
g.add((b_,rdf.type,owl.Restriction))
g.add((b_,owl.onProperty,aa.user))
g.add((b_,owl.someValuesFrom,aa.User))

# data property
# são existenciais, shoutMessage, created nos dois casos, nick
b_=r.BNode()
g.add((aa.Shout, owl.subClassOf, b_))
g.add((b_,rdf.type,owl.Restriction))
g.add((b_,owl.onProperty,aa.shoutMessage))
g.add((b_,owl.someValuesFrom,xsd.string))

b_=r.BNode()
g.add((aa.Shout, owl.subClassOf, b_))
g.add((b_,rdf.type,owl.Restriction))
g.add((b_,owl.onProperty,aa.created))
g.add((b_,owl.someValuesFrom,xsd.dateTime))

b_=r.BNode()
g.add((aa.Session, owl.subClassOf, b_))
g.add((b_,rdf.type,owl.Restriction))
g.add((b_,owl.onProperty,aa.created))
g.add((b_,owl.someValuesFrom,xsd.dateTime))

b_=r.BNode()
g.add((aa.User, owl.subClassOf, b_))
g.add((b_,rdf.type,owl.Restriction))
g.add((b_,owl.onProperty,aa.nick))
g.add((b_,owl.someValuesFrom,xsd.string))

f=open("ontologiaa.owl","wb")
f.write(g.serialize(format="turtle"))
f.close()
