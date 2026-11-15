# **Task 07: Querying RDF(s)**

# !pip install rdflib
# !pip install oeg-sw-class
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2026-2027-Datascience/refs/heads/master/Assignment4/course_materials"

# Spanish: Primero leemos los ficheros RDF
# 
# English: First let's read the RDF file

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
from oeg_sw_class import Report
# Do not change the name of the variables
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.parse(github_storage+"/rdf/data07.ttl", format="TTL")
report = Report()

# **TASK 7.1a:**
# 
# Spanish: Para todas las clases, enumera cada classURI. Si la clase pertenece a otra clase, indica su superclase. Realiza el ejercicio en RDFLib devolviendo una lista de tuplas: (clase, superclase) denominada "result". Si una clase no tiene superclase, devuelve None como superclase.
# 
# English: For all classes, list each classURI. If the class belogs to another class, then list its superclass. Do the exercise in RDFLib returning a list of Tuples: (class, superclass) called "result". If a class does not have a super class, then return None as the superclass

# OPTIONAL equivale a conservar tambien las clases sin superclase.
result = []
for cls in g.subjects(RDF.type, RDFS.Class):
    parents = list(g.objects(cls, RDFS.subClassOf))
    result.extend((cls, parent) for parent in parents) if parents else result.append((cls, None))
for row in result:
    print(row)

## Validation: Do not remove
report.validate_07_1a(result)

# **TASK 7.1b:**
# 
# Spanish: Repite el mismo ejercicio en SPARQL, devolviendo las variables ?c (clase) y ?sc (superclase)
# 
# English: Repeat the same exercise in SPARQL, returning the variables ?c (class) and ?sc (superclass)

query = """
SELECT ?c ?sc WHERE {
    ?c a rdfs:Class .
    OPTIONAL { ?c rdfs:subClassOf ?sc . }
}
"""
for row in g.query(query):
    print(row.c, row.sc)

## Validation: Do not remove
report.validate_07_1b(query,g)

# **TASK 7.2a:**
# 
# Spanish: Enumera todos los individuos de "Person" con RDFLib (ten en cuenta las subclases). Devuelve los URI de los individuos en una lista llamada "individuals".
# 
# English: List all individuals of "Person" with RDFLib (remember the subClasses). Return the individual URIs in a list called "individuals"

ns = Namespace("http://oeg.fi.upm.es/def/people#")
# Incluye Person y todas sus subclases, a cualquier profundidad.
person_classes = {ns.Person}
pending = [ns.Person]
while pending:
    parent = pending.pop()
    for child in g.subjects(RDFS.subClassOf, parent):
        if child not in person_classes:
            person_classes.add(child)
            pending.append(child)
individuals = list({subject for cls in person_classes for subject in g.subjects(RDF.type, cls)})
for individual in individuals:
    print(individual)

# validation. Do not remove
report.validate_07_02a(individuals)

# **TASK 7.2b:**
# 
# Spanish: Repite el mismo ejercicio en SPARQL, devolviendo los URI individuales en una variable ?ind.
# 
# English: Repeat the same exercise in SPARQL, returning the individual URIs in a variable ?ind

query = """
PREFIX ns: <http://oeg.fi.upm.es/def/people#>
SELECT DISTINCT ?ind WHERE {
    ?ind rdf:type/rdfs:subClassOf* ns:Person .
}
"""
for row in g.query(query):
    print(row.ind)

## Validation: Do not remove
report.validate_07_02b(g, query)

# **TASK 7.3:**
# 
# Spanish: Enumera el nombre y el tipo de quienes conocen a Curry (solo en SPARQL). Utiliza el nombre y el tipo como variables en la consulta.
# 
# English: List the name and type of those who know Curry (in SPARQL only). Use name and type as variables in the query

query = """
PREFIX ns: <http://oeg.fi.upm.es/def/people#>
SELECT DISTINCT ?name ?type WHERE {
    ?individual ns:knows ns:Curry ;
                rdfs:label ?name ;
                rdf:type ?type .
}
"""
for row in g.query(query):
    print(row.name, row.type)

## Validation: Do not remove
report.validate_07_03(g, query)

# **Task 7.4:**
# 
# Spanish: Enumera los nombres de aquellas entidades que tengan un compaÃ±ero de trabajo que tenga un perro, o que tengan un compaÃ±ero de trabajo que tenga un compaÃ±ero de trabajo que tenga un perro (en SPARQL). Devuelve los resultados en una variable llamada Â«nameÂ».
# 
# English: List the name of those entities who have a colleague with a dog, or that have a collegue who has a colleague who has a dog (in SPARQL). Return the results in a variable called name

# El fichero representa las mascotas con ownsPet y Animal (no existe Dog).
query = """
PREFIX ns: <http://oeg.fi.upm.es/def/people#>
SELECT DISTINCT ?name WHERE {
    ?individual rdfs:label ?name .
    ?individual (ns:hasColleague|ns:hasColleague/ns:hasColleague) ?colleague .
    ?colleague ns:ownsPet ?pet .
}
"""
for row in g.query(query):
    print(row.name)

## Validation: Do not remove
report.validate_07_04(g,query)
report.save_report("_Task_07")
