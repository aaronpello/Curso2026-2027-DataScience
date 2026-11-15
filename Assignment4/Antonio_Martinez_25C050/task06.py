from rdflib import Graph, Namespace, Literal, XSD
from rdflib.namespace import RDF, RDFS
from oeg_sw_class import Report

g = Graph()
g.namespace_manager.bind("ns", Namespace("http://somewhere#"), override=False)
r = Report()

ns = Namespace("http://mydomain.org#")
g.add((ns.Researcher, RDF.type, RDFS.Class))

person = Namespace("http://oeg.fi.upm.es/resource/person/")
organization = Namespace("http://oeg.fi.upm.es/resource/organization/")
ontology = Namespace("http://oeg.fi.upm.es/def/people#")

g.bind("person", person)
g.bind("organization", organization)
g.bind("ontology", ontology)

clases = [
    "Person",
    "Professor",
    "FullProfessor",
    "AssistantProfessor",
    "AssociateProfessor",
    "InterimAssociateProfessor"
]

for clase in clases:
    g.add((ontology[clase], RDF.type, RDFS.Class))
    g.add((ontology[clase], RDFS.label, Literal(clase, datatype=XSD.string)))

subclases = [
    ("Professor", "Person"),
    ("FullProfessor", "Professor"),
    ("AssistantProfessor", "Professor"),
    ("AssociateProfessor", "Professor"),
    ("InterimAssociateProfessor", "AssociateProfessor")
]

for subclase, superclase in subclases:
    g.add((ontology[subclase], RDFS.subClassOf, ontology[superclase]))

r.validate_task_06_01(g)

g.add((ontology.University, RDF.type, RDFS.Class))
g.add((ontology.University, RDFS.label, Literal("University", datatype=XSD.string)))

r.validate_task_06_02(g)

propiedades = {
    "hasName": (ontology.Person, RDFS.Literal),
    "hasColleague": (ontology.Person, ontology.Person),
    "hasHomePage": (ontology.FullProfessor, RDFS.Literal),
    "affiliatedWith": (ontology.Person, ontology.University)
}

for nombre, (dominio, rango) in propiedades.items():
    propiedad = ontology[nombre]
    g.add((propiedad, RDF.type, RDF.Property))
    g.add((propiedad, RDFS.label, Literal(nombre, datatype=XSD.string)))
    g.add((propiedad, RDFS.domain, dominio))
    g.add((propiedad, RDFS.range, rango))

r.validate_task_06_03(g)

university = Namespace("http://oeg.fi.upm.es/resource/university/")
g.bind("university", university)

g.add((person.Raul, RDF.type, ontology.FullProfessor))
g.add((person.Juan, RDF.type, ontology.AssistantProfessor))
g.add((person.Sven, RDF.type, ontology.Person))
g.add((university.Mannheim, RDF.type, ontology.University))

g.add((person.Raul, RDFS.label, Literal("Raúl", datatype=XSD.string)))
g.add((person.Juan, RDFS.label, Literal("Juan", datatype=XSD.string)))
g.add((person.Sven, RDFS.label, Literal("Sven", datatype=XSD.string)))

g.add((person.Raul, ontology.hasColleague, person.Juan))
g.add((person.Juan, ontology.hasColleague, person.Sven))
g.add((person.Sven, ontology.affiliatedWith, university.Mannheim))

g.add((person.Raul, ontology.hasHomePage, Literal("http://oeg.fi.upm.es", datatype=XSD.string)))
g.add((person.Juan, ontology.hasName, Literal("Juan Cano de Benito", datatype=XSD.string)))

r.validate_task_06_04(g)

foaf = Namespace("http://xmlns.com/foaf/0.1/")
g.bind("foaf", foaf)

g.add((person.Juan, foaf.mbox, Literal("juan.cano@upm.es", datatype=XSD.string)))
g.add((person.Juan, foaf.givenName, Literal("Juan", datatype=XSD.string)))
g.add((person.Juan, foaf.familyName, Literal("Cano de Benito", datatype=XSD.string)))

r.validate_task_06_05(g)

g.add((university.UPM, RDF.type, ontology.University))
g.add((university.UPM, RDFS.label, Literal("UPM", datatype=XSD.string)))

g.add((person.Juan, ontology.affiliatedWith, university.UPM))
g.add((person.Raul, ontology.affiliatedWith, university.UPM))
g.add((person.Sven, RDF.type, ontology.InterimAssociateProfessor))

r.validate_task_06_06(g)

g.add((university.UPM, RDF.type, ontology.University))
g.add((university.Mannheim, RDF.type, ontology.University))

r.validate_task_06_07(g)
r.save_report("_Task_06")
