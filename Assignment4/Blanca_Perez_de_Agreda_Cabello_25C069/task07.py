# -*- coding: utf-8 -*-


# **Task 07: Querying RDF(s)**

# Instalación previa, si hace falta: pip install rdflib oeg-sw-class
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2026-2027-DataScience/refs/heads/master/Assignment4/course_materials"


# Spanish: Primero leemos los ficheros RDF
#
# English: First let's read the RDF file

from pathlib import Path
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
from oeg_sw_class import Report

g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
# Usar el fichero del curso si está disponible; en Colab, leerlo de GitHub.
local_paths = [
    Path("data07.ttl"),
    Path("data/data07.ttl"),
    Path("Assignment4/course_materials/rdf/data07.ttl"),
    Path("../course_materials/rdf/data07.ttl"),
]
for path in local_paths:
    if path.is_file():
        g.parse(path, format="turtle")
        break
else:
    g.parse(github_storage + "/rdf/data07.ttl", format="turtle")
report = Report()


# **TASK 7.1a:**
#
# Spanish: Para todas las clases, enumera cada classURI. Si la clase pertenece a otra clase, indica su superclase. Realiza el ejercicio en RDFLib devolviendo una lista de tuplas: (clase, superclase) denominada "result". Si una clase no tiene superclase, devuelve None como superclase.
#
# English: For all classes, list each classURI. If the class belogs to another class, then list its superclass. Do the exercise in RDFLib returning a list of Tuples: (class, superclass) called "result". If a class does not have a super class, then return None as the superclass

result = []
for cls in sorted(set(g.subjects(RDF.type, RDFS.Class))):
    superclasses = list(g.objects(cls, RDFS.subClassOf))
    if superclasses:
        for superclass in sorted(superclasses):
            result.append((cls, superclass))
    else:
        result.append((cls, None))

for r in result:
    print(r)


## Validation: Do not remove
report.validate_07_1a(result)

# **TASK 7.1b:**
#
# Spanish: Repite el mismo ejercicio en SPARQL, devolviendo las variables ?c (clase) y ?sc (superclase)
#
# English: Repeat the same exercise in SPARQL, returning the variables ?c (class) and ?sc (superclass)

query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?c ?sc WHERE {
    ?c rdf:type rdfs:Class .
    OPTIONAL { ?c rdfs:subClassOf ?sc . }
}
ORDER BY ?c ?sc
"""

for r in g.query(query):
    print(r.c, r.sc)


## Validation: Do not remove
report.validate_07_1b(query,g)

# **TASK 7.2a:**
#
# Spanish: Enumera todos los individuos de "Person" con RDFLib (ten en cuenta las subclases). Devuelve los URI de los individuos en una lista llamada "individuals".
#
# English: List all individuals of "Person" with RDFLib (remember the subClasses). Return the individual URIs in a list called "individuals"

ns = Namespace("http://oeg.fi.upm.es/def/people#")

# Incluye Person y todas sus subclases, aunque haya varios niveles.
person_classes = set(g.transitive_subjects(RDFS.subClassOf, ns.Person))
people = set()
for cls in person_classes:
    people.update(g.subjects(RDF.type, cls))
individuals = sorted(people)

for i in individuals:
    print(i)


# validation. Do not remove
report.validate_07_02a(individuals)

# **TASK 7.2b:**
#
# Spanish: Repite el mismo ejercicio en SPARQL, devolviendo los URI individuales en una variable ?ind.
#
# English: Repeat the same exercise in SPARQL, returning the individual URIs in a variable ?ind

query = """
PREFIX ns: <http://oeg.fi.upm.es/def/people#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT DISTINCT ?ind WHERE {
    ?ind rdf:type ?class .
    ?class rdfs:subClassOf* ns:Person .
}
ORDER BY ?ind
"""

for r in g.query(query):
    print(r.ind)


## Validation: Do not remove
report.validate_07_02b(g, query)

# **TASK 7.3:**
#
# Spanish: Enumera el nombre y el tipo de quienes conocen a Curry (solo en SPARQL). Utiliza el nombre y el tipo como variables en la consulta.
#
# English: List the name and type of those who know Curry (in SPARQL only). Use name and type as variables in the query

query = """
PREFIX ns: <http://oeg.fi.upm.es/def/people#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT DISTINCT ?name ?type WHERE {
    ?person ns:knows ns:Curry ;
            rdfs:label ?name ;
            rdf:type ?type .
}
ORDER BY ?name ?type
"""

for r in g.query(query):
    print(r.name, r.type)


## Validation: Do not remove
report.validate_07_03(g, query)

# **Task 7.4:**
#
# Spanish: Enumera los nombres de aquellas entidades que tengan un compañero de trabajo que tenga un perro, o que tengan un compañero de trabajo que tenga un compañero de trabajo que tenga un perro (en SPARQL). Devuelve los resultados en una variable llamada «name».
#
# English: List the name of those entities who have a colleague with a dog, or that have a collegue who has a colleague who has a dog (in SPARQL). Return the results in a variable called name

# Los perros del ejercicio están declarados como ns:Animal en data07.ttl.
query = """
PREFIX ns: <http://oeg.fi.upm.es/def/people#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT DISTINCT ?name WHERE {
    ?person rdfs:label ?name .
    {
        ?person ns:hasColleague ?colleague .
    }
    UNION
    {
        ?person ns:hasColleague ?otherColleague .
        ?otherColleague ns:hasColleague ?colleague .
    }
    ?colleague ns:ownsPet ?dog .
    ?dog rdf:type ns:Animal .
}
ORDER BY ?name
"""

for r in g.query(query):
    print(r.name)


## Validation: Do not remove
report.validate_07_04(g,query)
report.save_report("_Task_07")
