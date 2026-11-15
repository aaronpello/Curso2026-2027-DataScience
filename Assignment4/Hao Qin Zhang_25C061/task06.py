from rdflib import Graph, Namespace, Literal, URIRef, XSD
from rdflib.namespace import RDF, RDFS, FOAF
from oeg_sw_class import Report


g = Graph()
r = Report()

# Task 6.0
ontology = Namespace("http://oeg.fi.upm.es/def/people#")
organization = Namespace("http://oeg.fi.upm.es/resource/organization/")
person = Namespace("http://oeg.fi.upm.es/resource/person/")
university = Namespace("http://oeg.fi.upm.es/resource/university/")

for prefix, namespace in [("ontology", ontology), ("organization", organization),
                          ("person", person), ("university", university)]:
    g.bind(prefix, namespace)

# Task 6.1
classes = ["Person", "Professor", "FullProfessor", "AssistantProfessor",
           "AssociateProfessor", "InterimAssociateProfessor"]

for name in classes:
    g.add((ontology[name], RDF.type, RDFS.Class))
    g.add((ontology[name], RDFS.label, Literal(name, datatype=XSD.string)))

subclasses = [
    ("Professor", "Person"),
    ("FullProfessor", "Professor"),
    ("AssistantProfessor", "Professor"),
    ("AssociateProfessor", "Professor"),
    ("InterimAssociateProfessor", "AssociateProfessor")
]
for child, parent in subclasses:
    g.add((ontology[child], RDFS.subClassOf, ontology[parent]))

r.validate_task_06_01(g)

# Task 6.2
g.add((ontology.University, RDF.type, RDFS.Class))
g.add((ontology.University, RDFS.label, Literal("University", datatype=XSD.string)))
r.validate_task_06_02(g)

# Task 6.3
properties = [
    ("hasName", ontology.Person, RDFS.Literal),
    ("hasColleague", ontology.Person, ontology.Person),
    ("hasHomePage", ontology.FullProfessor, RDFS.Literal),
    ("affiliatedWith", ontology.Person, ontology.University)
]
for name, domain, range_ in properties:
    prop = ontology[name]
    g.add((prop, RDF.type, RDF.Property))
    g.add((prop, RDFS.label, Literal(name, datatype=XSD.string)))
    g.add((prop, RDFS.domain, domain))
    g.add((prop, RDFS.range, range_))

r.validate_task_06_03(g)

# Task 6.4
g.add((person.Raul, RDF.type, ontology.FullProfessor))
g.add((person.Juan, RDF.type, ontology.AssistantProfessor))
g.add((person.Raul, ontology.hasColleague, person.Juan))
g.add((person.Juan, ontology.hasColleague, person.Sven))
g.add((person.Sven, ontology.affiliatedWith, university.Mannheim))
g.add((person.Raul, ontology.hasHomePage, Literal("http://oeg.fi.upm.es", datatype=XSD.string)))
g.add((person.Juan, ontology.hasName, Literal("Juan Cano de Benito", datatype=XSD.string)))

for individual, name in [(person.Raul, "Raúl"), (person.Juan, "Juan"), (person.Sven, "Sven")]:
    g.add((individual, RDFS.label, Literal(name, datatype=XSD.string)))

r.validate_task_06_04(g)

# Task 6.5
g.add((person.Juan, FOAF.givenName, Literal("Juan", datatype=XSD.string)))
g.add((person.Juan, FOAF.familyName, Literal("Cano de Benito", datatype=XSD.string)))
g.add((person.Juan, FOAF.mbox, URIRef("mailto:juan.cano@upm.es")))
r.validate_task_06_05(g)

# Task 6.6
g.add((person.Juan, ontology.affiliatedWith, university.UPM))
g.add((person.Raul, ontology.affiliatedWith, university.UPM))
g.add((person.Sven, RDF.type, ontology.InterimAssociateProfessor))
r.validate_task_06_06(g)

# Task 6.7
g.add((university.UPM, RDF.type, ontology.University))
g.add((university.Mannheim, RDF.type, ontology.University))
r.validate_task_06_07(g)

r.save_report("_Task_06")
print("Task 06:", len(g), "triples")
