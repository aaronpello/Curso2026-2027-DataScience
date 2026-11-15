# # **Task 06: Modifying RDF(s)**

# !pip install rdflib
# !pip install oeg-sw-class

# Spanish: Importar la librerÃ­a RDFLib
# 
# English: Import RDFLib main methods

from rdflib import Graph, Namespace, Literal, XSD
from rdflib.namespace import RDF, RDFS
from oeg_sw_class import Report
# Do not change the name of the variables
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
r = Report()

# Spanish: Crear una nueva clase llamada "Researcher"
# 
# English: Create a new class named Researcher

ns = Namespace("http://mydomain.org#")
g.add((ns.Researcher, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)

# ### **Task 6.0:**
# 
# Spanish: Crea nuevos prefijos para "ontology", "organization" and "person", con la siguiente informaciÃ³n:
# 
# *   person: http://oeg.fi.upm.es/resource/person/
# *   organization: http://oeg.fi.upm.es/resource/organization/
# *   ontology: http://oeg.fi.upm.es/def/people#
# 
# English: Create new prefixes for "ontology", "organization" and "person", with the following information:
# 
# *   person: http://oeg.fi.upm.es/resource/person/
# *   organization: http://oeg.fi.upm.es/resource/organization/
# *   ontology: http://oeg.fi.upm.es/def/people#

organization = Namespace("http://oeg.fi.upm.es/resource/organization/")
person = Namespace("http://oeg.fi.upm.es/resource/person/")
ontology = Namespace("http://oeg.fi.upm.es/def/people#")
university = Namespace("http://oeg.fi.upm.es/resource/university/")
g.bind("university", university)
for prefix, namespace in [("organization", organization), ("person", person), ("ontology", ontology)]:
    g.bind(prefix, namespace)

# ### **Task 6.1**
# 
# Spanish: Reproduce la taxonomÃ­a de clases que aparece en el diagrama (`Assignment4/course_materials/diagram/diagram.jpg`). AÃ±ade etiquetas para cada una de ellas tal y como aparecen en el diagrama (exactamente), sin etiquetas de idioma. Recuerda aÃ±adir el tipo de datos correcto (xsd:String) cuando sea necesario.
# 
# English: Reproduce the taxonomy of classes shown in the diagram (`Assignment4/course_materials/diagram/diagram.jpg`). Add labels for each of them as they are in the diagram (exactly) with no language tags. Remember adding the correct datatype (xsd:String) when appropriate.

# Taxonomia del diagrama: cada clase tiene una etiqueta xsd:string.
classes = ["Person", "Professor", "FullProfessor", "AssistantProfessor", "AssociateProfessor", "InterimAssociateProfessor"]
for name in classes:
    g.add((ontology[name], RDF.type, RDFS.Class))
    g.add((ontology[name], RDFS.label, Literal(name, datatype=XSD.string)))
for child, parent in [("Professor", "Person"), ("FullProfessor", "Professor"), ("AssistantProfessor", "Professor"), ("AssociateProfessor", "Professor"), ("InterimAssociateProfessor", "AssociateProfessor")]:
    g.add((ontology[child], RDFS.subClassOf, ontology[parent]))

#Validation: Do not remove
r.validate_task_06_01(g)

# ### **Task 6.2**
# 
# Spanish: Crea la clase ontology:University.
# 
# English: Create the ontology:University class.

g.add((ontology.University, RDF.type, RDFS.Class))
g.add((ontology.University, RDFS.label, Literal("University", datatype=XSD.string)))

#Validation: Do not remove
r.validate_task_06_02(g)

# ### **Task 6.3**
# 
# Spanish: AÃ±ade las propiedades que aparecen en el diagrama. AÃ±ade etiquetas para cada una de ellas (exactamente como aparecen en la diapositiva, sin etiquetas de idioma), asÃ­ como sus dominios y rangos correspondientes utilizando RDFS. Recuerda aÃ±adir el tipo de datos correcto (xsd:String) cuando sea necesario. Si una propiedad no tiene rango, conviÃ©rtela en un literal (cadena de caracteres). Por otra parte, ontology:affiliatedWith tendrÃ¡ como dominio ontology:Person y rango ontology:University.
# 
# English: Add the properties shown in the previous diagram. Add labels for each of them (exactly as they are in the slide, with no language tags), and their corresponding domains and ranges using RDFS. Remember adding the correct datatype (xsd:String) when appropriate. If a property has no range, make it a literal (string). Furthermore, the ontology:affiliatedWith property will have ontology:Person as its domain and ontology:University as its range.

for name, domain, range_ in [
    ("hasName", ontology.Person, RDFS.Literal),
    ("hasColleague", ontology.Person, ontology.Person),
    ("hasHomePage", ontology.FullProfessor, RDFS.Literal),
    ("affiliatedWith", ontology.Person, ontology.University),
]:
    prop = ontology[name]
    g.add((prop, RDF.type, RDF.Property))
    g.add((prop, RDFS.label, Literal(name, datatype=XSD.string)))
    g.add((prop, RDFS.domain, domain))
    g.add((prop, RDFS.range, range_))

#Validation: Do not remove
r.validate_task_06_03(g)

# ### **Task 6.4**
# 
# Spanish: Crea los individuos que aparecen en el diagrama, en la secciÃ³n Â«DatosÂ». VincÃºlalos con las mismas relaciones que se muestran en el diagrama.
# 
# English: Create the individuals shown in the diagram under "Datos". Link them with the same relationships shown in the diagram."

for individual, name in [(person.Raul, "Raúl"), (person.Juan, "Juan"), (person.Sven, "Sven")]:
    g.add((individual, RDFS.label, Literal(name, datatype=XSD.string)))
g.add((person.Raul, RDF.type, ontology.FullProfessor))
g.add((person.Juan, RDF.type, ontology.AssistantProfessor))
g.add((person.Raul, ontology.hasColleague, person.Juan))
g.add((person.Juan, ontology.hasColleague, person.Sven))
g.add((person.Sven, ontology.affiliatedWith, university.Mannheim))
g.add((person.Raul, ontology.hasHomePage, Literal("http://oeg.fi.upm.es", datatype=XSD.string)))
g.add((person.Juan, ontology.hasName, Literal("Juan Cano de Benito", datatype=XSD.string)))

#Validation: Do not remove
r.validate_task_06_04(g)

# ### **Task 6.5**
# 
# Spanish: AÃ±adir a person:Juan la direcciÃ³n email (juan.cano@upm.es), el nombre (given) y los apellidos (family). Utiliza las propiedades que ya se incluyen en el ejemplo 4 para describir a Jane y John (https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2025-2026/master/Assignment4/course_materials/rdf/example4.rdf). No importes los espacios de nombres; aÃ±Ã¡delos manualmente.
# 
# English: Add to the individual person:Juan the email address (juan.cano@upm.es), given and family names. Use the properties already included in example 4 to describe Jane and John (https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2025-2026/master/Assignment4/course_materials/rdf/example4.rdf). Do not import the namespaces, add them manually.

foaf = Namespace("http://xmlns.com/foaf/0.1/")
g.bind("foaf", foaf)
g.add((person.Juan, foaf.mbox, Literal("juan.cano@upm.es", datatype=XSD.string)))
g.add((person.Juan, foaf.givenName, Literal("Juan", datatype=XSD.string)))
g.add((person.Juan, foaf.familyName, Literal("Cano de Benito", datatype=XSD.string)))

#Validation: Do not remove
r.validate_task_06_05(g)

# ### **Task 6.6**
# 
# Spanish: AÃ±ade que Juan y RaÃºl estÃ¡n afiliados (affiliatedWith) a university:UPM. TambiÃ©n que Sven es de tipo InterimAssociateProfessor.
# 
# English:  Add that Juan and RaÃºl are affiliated (affiliatedWith) with the university:UPM. Also add that Sven is a InterimAssociateProfessor

for individual in (person.Juan, person.Raul):
    g.add((individual, ontology.affiliatedWith, university.UPM))
g.add((person.Sven, RDF.type, ontology.InterimAssociateProfessor))

#Validation: Do not remove
r.validate_task_06_06(g)

# ### **Task 6.7**
# 
# Spanish: Tanto university:UPM como university:Mannheim son de tipo ontology:University.
# 
# English:  Both university:UPM and university:Mannheim are ontology:University type.

for institution in (university.UPM, university.Mannheim):
    g.add((institution, RDF.type, ontology.University))

#Validation: Do not remove
r.validate_task_06_07(g)
r.save_report("_Task_06")
