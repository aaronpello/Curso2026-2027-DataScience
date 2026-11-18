from rdflib import Graph, Namespace, Literal, XSD
from rdflib.namespace import RDF, RDFS
from oeg_sw_class import Report

g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
r = Report()

ns = Namespace("http://mydomain.org#")
g.add((ns.Researcher, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)




person = Namespace("http://oeg.fi.upm.es/resource/person/")
organization = Namespace("http://oeg.fi.upm.es/resource/organization/")
ontology = Namespace("http://oeg.fi.upm.es/def/people#")

g.bind("person", person)
g.bind("organization", organization)
g.bind("ontology", ontology)

# Person
g.add((ontology.Person, RDF.type, RDFS.Class))
g.add((ontology.Person, RDFS.label, Literal("Person", datatype=XSD.string)))

#TODO

# Profesor
g.add((ontology.Professor, RDF.type, RDFS.Class))
g.add((ontology.Professor, RDFS.label, Literal("Professor", datatype=XSD.string)))
g.add((ontology.Professor, RDFS.subClassOf, ontology.Person))

# FullProfessor
g.add((ontology.FullProfessor, RDF.type, RDFS.Class))
g.add((ontology.FullProfessor, RDFS.label, Literal("FullProfessor", datatype=XSD.string)))
g.add((ontology.FullProfessor, RDFS.subClassOf, ontology.Professor))

# AssistantProfessor
g.add((ontology.AssistantProfessor, RDF.type, RDFS.Class))
g.add((ontology.AssistantProfessor, RDFS.label, Literal("AssistantProfessor", datatype=XSD.string)))
g.add((ontology.AssistantProfessor, RDFS.subClassOf, ontology.Professor))

# AssociateProfessor
g.add((ontology.AssociateProfessor, RDF.type, RDFS.Class))
g.add((ontology.AssociateProfessor, RDFS.label, Literal("AssociateProfessor", datatype=XSD.string)))
g.add((ontology.AssociateProfessor, RDFS.subClassOf, ontology.Professor))

# InterimAssociateProfessor
g.add((ontology.InterimAssociateProfessor, RDF.type, RDFS.Class))
g.add((ontology.InterimAssociateProfessor, RDFS.label, Literal("InterimAssociateProfessor", datatype=XSD.string)))
g.add((ontology.InterimAssociateProfessor, RDFS.subClassOf, ontology.AssociateProfessor))

# Visualize the results
for s, p, o in g:
  print(s,p,o)

#Validation: Do not remove
r.validate_task_06_01(g)

#TODO
g.add((ontology.University, RDF.type, RDFS.Class))
g.add((ontology.University, RDFS.label, Literal("University", datatype=XSD.string)))

# Visualize the results
for s, p, o in g:
  print(s,p,o)

# Validation
r.validate_task_06_02(g)


#TODO

# hasName
g.add((ontology.hasName, RDF.type, RDF.Property))
g.add((ontology.hasName, RDFS.label, Literal("hasName", datatype=XSD.string)))
g.add((ontology.hasName, RDFS.domain, ontology.Person))
g.add((ontology.hasName, RDFS.range, RDFS.Literal))

# hasColleague
g.add((ontology.hasColleague, RDF.type, RDF.Property))
g.add((ontology.hasColleague, RDFS.label, Literal("hasColleague", datatype=XSD.string)))
g.add((ontology.hasColleague, RDFS.domain, ontology.Person))
g.add((ontology.hasColleague, RDFS.range, ontology.Person))

# hasHomePage
g.add((ontology.hasHomePage, RDF.type, RDF.Property))
g.add((ontology.hasHomePage, RDFS.label, Literal("hasHomePage", datatype=XSD.string)))
g.add((ontology.hasHomePage, RDFS.domain, ontology.FullProfessor))
g.add((ontology.hasHomePage, RDFS.range, RDFS.Literal))

# affiliatedWith
g.add((ontology.affiliatedWith, RDF.type, RDF.Property))
g.add((ontology.affiliatedWith, RDFS.label, Literal("affiliatedWith", datatype=XSD.string)))
g.add((ontology.affiliatedWith, RDFS.domain, ontology.Person))
g.add((ontology.affiliatedWith, RDFS.range, ontology.University))

# Visualize the results
for s, p, o in g:
    print(s, p, o)

# Validation
r.validate_task_06_03(g)

#TODO

# Raul (FullProfessor)
g.add((person.Raul, RDF.type, ontology.FullProfessor))
g.add((person.Raul, RDFS.label, Literal("Raúl", datatype=XSD.string)))
g.add((person.Raul, ontology.hasHomePage, Literal("http://oeg.fi.upm.es", datatype=XSD.string)))
g.add((person.Raul, ontology.hasColleague, person.Juan))

# Juan (AssistantProfessor)
g.add((person.Juan, RDF.type, ontology.AssistantProfessor))
g.add((person.Juan, RDFS.label, Literal("Juan", datatype=XSD.string)))
g.add((person.Juan, ontology.hasName, Literal("Juan Cano de Benito", datatype=XSD.string)))
g.add((person.Juan, ontology.hasColleague, person.Sven))

# Sven (Person)
g.add((person.Sven, RDF.type, ontology.Person))
g.add((person.Sven, RDFS.label, Literal("Sven", datatype=XSD.string)))

# Mannheim (University)
university = Namespace("http://oeg.fi.upm.es/resource/university/")
g.bind("university", university)

g.add((person.Sven, ontology.affiliatedWith, university.Mannheim))

# Visualize the results
for s, p, o in g:
    print(s, p, o)

# Validation
r.validate_task_06_04(g)


foaf = Namespace("http://xmlns.com/foaf/0.1/")
g.bind("foaf", foaf)

#TODO

foaf = Namespace("http://xmlns.com/foaf/0.1/")
g.bind("foaf", foaf)

# Añadir propiedades a person:Juan
g.add((person.Juan, foaf.mbox, Literal("juan.cano@upm.es", datatype=XSD.string)))
g.add((person.Juan, foaf.givenName, Literal("Juan", datatype=XSD.string)))
g.add((person.Juan, foaf.familyName, Literal("Cano de Benito", datatype=XSD.string)))

# Visualize the results
for s, p, o in g:
    print(s, p, o)

# Validation: Do not remove
r.validate_task_06_05(g)

#TODO

g.add((person.Juan, ontology.affiliatedWith, university.UPM))
g.add((person.Raul, ontology.affiliatedWith, university.UPM))

g.add((person.Sven, RDF.type, ontology.InterimAssociateProfessor))

# Visualize the results
for s, p, o in g:
  print(s, p, o)

# Validation: Do not remove
r.validate_task_06_06(g)


#TODO

g.add((university.UPM, RDF.type, ontology.University))
g.add((university.Mannheim, RDF.type, ontology.University))

# Visualize the results
for s, p, o in g:
  print(s, p, o)

# Validation: Do not remove
r.validate_task_06_07(g)
r.save_report("_Task_06")