from pathlib import Path
from rdflib import Graph, Namespace
from rdflib.namespace import RDF, RDFS
from oeg_sw_class import Report


url = ("https://raw.githubusercontent.com/FacultadInformatica-LinkedData/"
       "Curso2026-2027-DataScience/master/Assignment4/course_materials/rdf/data07.ttl")
local = Path(__file__).resolve().parent.parent / "course_materials" / "rdf" / "data07.ttl"

g = Graph()
g.parse(local if local.is_file() else url, format="turtle")
r = Report()
ns = Namespace("http://oeg.fi.upm.es/def/people#")

# Task 7.1a
result = []
for cls in sorted(g.subjects(RDF.type, RDFS.Class), key=str):
    parent = g.value(cls, RDFS.subClassOf)
    result.append((cls, parent))

r.validate_07_1a(result)

# Task 7.1b
query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?c ?sc WHERE {
    ?c rdf:type rdfs:Class .
    OPTIONAL { ?c rdfs:subClassOf ?sc . }
}
"""
r.validate_07_1b(query, g)

# Task 7.2a
person_classes = {ns.Person}
changed = True
while changed:
    previous = len(person_classes)
    for subclass, superclass in g.subject_objects(RDFS.subClassOf):
        if superclass in person_classes:
            person_classes.add(subclass)
    changed = len(person_classes) != previous

individuals = []
for person_class in person_classes:
    for ind in g.subjects(RDF.type, person_class):
        if ind not in individuals:
            individuals.append(ind)

individuals.sort(key=str)
r.validate_07_02a(individuals)

# Task 7.2b
query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ns: <http://oeg.fi.upm.es/def/people#>
SELECT DISTINCT ?ind WHERE {
    ?ind rdf:type ?class .
    ?class rdfs:subClassOf* ns:Person .
}
"""
r.validate_07_02b(g, query)

# Task 7.3
query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ns: <http://oeg.fi.upm.es/def/people#>
SELECT DISTINCT ?name ?type WHERE {
    ?person ns:knows ns:Curry .
    ?person rdfs:label ?name .
    ?person rdf:type ?type .
}
"""
r.validate_07_03(g, query)

# Task 7.4
query = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ns: <http://oeg.fi.upm.es/def/people#>
SELECT DISTINCT ?name WHERE {
    ?person rdfs:label ?name .
    ?person ns:hasColleague/ns:hasColleague? ?colleague .
    ?colleague ns:ownsPet ?pet .
}
"""
r.validate_07_04(g, query)

r.save_report("_Task_07")
print("Task 07:", len(g), "triples")
