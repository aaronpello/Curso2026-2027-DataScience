# Hands-on assignment 2 – Self assessment

## Checklist

**The “analysis.html” file:**

- [X] Includes the potential license of the dataset to be generated
- [X] Includes the resource naming strategy

**The resource naming strategy:**

- [X] Uses a domain that is not the one given by default in Protégé
- [X] Uses different paths for ontology resources (i.e., classes and properties) and individuals
- [X] Ensures that the paths for individuals of different classes are not the same
- [X] Defines individual URIs independently of class URIs

**The ontology file:**

- [X] Uses the .ttl extension
- [X] Is serialized in the Turtle format
- [X] Follows the resource naming strategy
- [X] Contains at least one class
- [X] Contains at least one object property (where the value of the property is a resource)
- [X] Contains at least one datatype property (where the value of the property is a string literal, usually typed)
- [X] Defines the domain of all the properties (the origin of the property)
- [X] Defines the range of all the properties (the destination of the property)
- [X] Defines all class names starting with a capital letter
- [X] Defines all property names starting with a non-capital letter
- [X] Does not mix labels in different languages (e.g., Spanish and English)
- [X] Does not define multiple domains or multiple ranges in properties
- [X] Contains at least one class that will be used to link to other entities

## Comments on the self-assessment
Como la web oficial de Chowlk estaba fallando y no nos dejaba hacer la conversión, descargamos el repositorio
oficial de GitHub de Chowlk (OEG-UPM) y generamos el archivo ".ttl" de manera local en el ordenador. 
Además, como la herramienta OOPS! tampoco funcionaba bien por errores del servidor en el momento de revisar la ontología,
hemos verificado y validado todo el código manualmente para asegurarnos de que cumple estrictamente con todos los puntos
de la rúbrica.
