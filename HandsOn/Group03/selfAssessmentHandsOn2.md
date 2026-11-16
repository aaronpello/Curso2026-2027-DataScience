# Self-assessment Hands-on 2 - Group03

## The "analysis.html" file
- [x] Includes the potential license of the dataset to be generated
- [x] Includes the resource naming strategy

## The resource naming strategy
- [x] Uses a domain that is not the one given by default in Protégé
- [x] Uses different paths for ontology resources (i.e., classes and properties) and individuals
- [x] Ensures that the paths for individuals of different classes are not the same
- [x] Defines property URIs independently of class URIs

## The ontology file
- [x] Uses the .ttl extension
- [x] Is serialized in the Turtle format
- [x] Follows the resource naming strategy
- [x] Contains at least one class
- [x] Contains at least one object property (where the value of the property is a resource)
- [x] Contains at least one datatype property (where the value of the property is a string literal, usually typed)
- [x] Defines the domain of all the properties (the origin of the property)
- [x] Defines the range of all the properties (the destination of the property)
- [x] Defines all class names starting with a capital letter
- [x] Defines all property names starting with a non-capital letter
- [x] Does not mix labels in different languages (e.g., Spanish and English)
- [x] Does not define multiple domains or multiple ranges in properties
- [x] Contains at least one class that will be used to link to other entities

## The sample instantiation file
- [x] Uses the .ttl extension
- [x] Is serialized in the Turtle format
- [x] Follows the resource naming strategy
- [x] Does not include the definition of ontology terms

## Comments on the self-assessment (If required)

- We checked the two Turtle files by parsing them with a script: both load without errors, every property has exactly one domain and one range, all labels of the ontology are in English, and the sample file only uses terms that exist in the ontology and respects their domains and ranges.
- The domain `airquality.group03.example.org` is a reserved example domain, because the group does not own one. The URIs are therefore not dereferenceable; content negotiation is described in `analysis.html` as a design for a later assignment.
- In the sample file, the names of the individuals are plain literals without language tag (for example the station name "Plaza de España"), because they are proper names. The language rule was applied to the ontology file.
- The meaning of the magnitude codes 7, 8 and 12 and the meaning of the flags (V, N, M) of the hourly dataset are not confirmed by the files; `analysis.html` explains what we could and could not confirm, and the sample instantiation only uses magnitude 6 (CO), which the data confirm.
- The linking candidates are described in `analysis.html` (section 4) in terms of entities, following the feedback of Hands-on 1. Linking is not part of this assignment.
- The group leader prepared the deliverables and the other members take part by reviewing them in the pull request.
