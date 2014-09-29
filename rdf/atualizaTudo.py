import os
os.system("python triplificaAA.py")
os.system("python triplificaAAmongo.py")
os.system("python fazOntologiaa.py")
os.system("mv aaStoreMongo.rdf aaTriplestore.rdf")
os.system("mv aaStoreMongo.ttl aaTriplestore.ttl")
print("verifique os arquivos aaTriplestore.rdf e aaTriplestore.ttl")
