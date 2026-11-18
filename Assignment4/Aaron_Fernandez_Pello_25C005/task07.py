github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2026-2027-Datascience/refs/heads/master/Assignment4/course_materials"

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
from oeg_sw_class import Report
# Do not change the name of the variables
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.parse(github_storage+"/rdf/data07.ttl", format="TTL")
report = Report()

#TODO
result=[]
for s in g.subjects(RDF.type, RDFS.Class):
    superclass=g.value(s, RDFS.subClassOf)
    result.append((s, superclass))
for r in result:
  print(r)

## Validation: Do not remove
report.validate_07_1a(result)

query =  """
SELECT ?c ?sc WHERE{
  ?c a rdfs:Class.
  OPTIONAL{?c rdfs:subClassOf ?sc}.
} """

for r in g.query(query):
  print(r.c, r.sc)
## Validation: Do not remove
report.validate_07_1b(query,g)


ns = Namespace("http://oeg.fi.upm.es/def/people#")

# variable to return
individuals = []

#TODO
individuals = []
def get_subclases(cls):
    subclases = {cls}
    for s, p, o in g.triples((None, RDFS.subClassOf, cls)):
        subclases.update(get_subclases(s))
    return subclases

clases_persona=get_subclases(ns.Person)

for cls in clases_persona:
    for s, p, o in g.triples((None, RDF.type, cls)):
        if s not in individuals:
            individuals.append(s)

# visualize results
for i in individuals:
  print(i)
# validation. Do not remove
report.validate_07_02a(individuals)

#TODO
query = """
PREFIX ns: <http://oeg.fi.upm.es/def/people#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?ind WHERE {
  ?ind a ?type .
  ?type rdfs:subClassOf* ns:Person .
}
"""
# Visualize the results
for r in g.query(query):
  print(r.ind)

## Validation: Do not remove
report.validate_07_02b(g, query)

#TODO
query = """
PREFIX ns: <http://oeg.fi.upm.es/def/people#>
PREFIX vcard: <http://www.w3.org/2001/vcard-rdf/3.0#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?name ?type WHERE {
  { ?person foaf:knows ns:Curry } UNION { ?person ns:knows ns:Curry }
  ?person a ?type .
  { ?person vcard:Given ?name } 
  UNION { ?person vcard:FN ?name } 
  UNION { ?person foaf:givenName ?name }
  UNION { ?person rdfs:label ?name }
}
"""

# Visualize the results
for r in g.query(query):
  print(r.name, r.type)
## Validation: Do not remove
report.validate_07_03(g, query)

#TODO
query = """
PREFIX ns: <http://oeg.fi.upm.es/def/people#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT DISTINCT ?name WHERE {
  { ?x ns:hasColleague ?y .
    ?y ns:ownsPet ?pet .
    ?pet a ns:Animal . }
  UNION
  { ?x ns:hasColleague ?y .
    ?y ns:hasColleague ?z .
    ?z ns:ownsPet ?pet .
    ?pet a ns:Animal . }
  ?x rdfs:label ?name .
}
"""

# Visualize the results
for r in g.query(query):
  print(r.name)
## Validation: Do not remove
report.validate_07_04(g, query)
report.save_report("_Task_07")


