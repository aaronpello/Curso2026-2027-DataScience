from rdflib import Graph, Namespace
from rdflib.namespace import RDF, RDFS
from oeg_sw_class import Report

github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2026-2027-Datascience/refs/heads/master/Assignment4/course_materials"

g = Graph()
g.namespace_manager.bind("ns", Namespace("http://somewhere#"), override=False)
g.parse(github_storage + "/rdf/data07.ttl", format="turtle")

report = Report()
ns = Namespace("http://oeg.fi.upm.es/def/people#")

result = []

for clase in g.subjects(RDF.type, RDFS.Class):
    superclases = list(g.objects(clase, RDFS.subClassOf))

    if superclases:
        for superclase in superclases:
            result.append((clase, superclase))
    else:
        result.append((clase, None))

for elemento in result:
    print(elemento)

report.validate_07_1a(result)

query = """
SELECT ?c ?sc
WHERE {
    ?c rdf:type rdfs:Class .
    OPTIONAL {
        ?c rdfs:subClassOf ?sc .
    }
}
"""

for fila in g.query(query):
    print(fila.c, fila.sc)

report.validate_07_1b(query, g)

individuals = []
clases = {ns.Person}
pendientes = [ns.Person]

while pendientes:
    clase_actual = pendientes.pop()

    for subclase in g.subjects(RDFS.subClassOf, clase_actual):
        if subclase not in clases:
            clases.add(subclase)
            pendientes.append(subclase)

individuos_encontrados = set()

for clase in clases:
    for individuo in g.subjects(RDF.type, clase):
        individuos_encontrados.add(individuo)

individuals = list(individuos_encontrados)

for individuo in individuals:
    print(individuo)

report.validate_07_02a(individuals)

query = """
PREFIX people: <http://oeg.fi.upm.es/def/people#>

SELECT DISTINCT ?ind
WHERE {
    ?ind rdf:type ?clase .
    ?clase rdfs:subClassOf* people:Person .
}
"""

for fila in g.query(query):
    print(fila.ind)

report.validate_07_02b(g, query)

query = """
PREFIX people: <http://oeg.fi.upm.es/def/people#>

SELECT ?name ?type
WHERE {
    ?person people:knows people:Curry .
    ?person rdfs:label ?name .
    ?person rdf:type ?type .
}
"""

for fila in g.query(query):
    print(fila.name, fila.type)

report.validate_07_03(g, query)

query = """
PREFIX people: <http://oeg.fi.upm.es/def/people#>

SELECT DISTINCT ?name
WHERE {
    ?person rdfs:label ?name .

    {
        ?person people:hasColleague ?colleague1 .
        ?colleague1 people:ownsPet ?pet .
    }
    UNION
    {
        ?person people:hasColleague ?colleague1 .
        ?colleague1 people:hasColleague ?colleague2 .
        ?colleague2 people:ownsPet ?pet .
    }
}
"""

for fila in g.query(query):
    print(fila.name)

report.validate_07_04(g, query)
report.save_report("_Task_07")
