# Hands-on assignment 1 – Self assessment

## Checklist

**The “README.md” file:**

- [x] Includes the names and GitHub users of all the members of the group

**The "csv" directory:**

- [x] Contains at least one CSV file
- [x] The CSV files belong to one of the selected domains

**The "datasetRequirements.html" file:**

- [x] Identifies the licenses of all the selected datasets
- [x] Identifies those entities in the selected datasets that can be linked with entities in other datasets
- [x] Identifies those entities in other datasets that can be linked with entities in the selected datasets

**The "applicationRequirements.html” file:**

- [x] Includes a description of the application user interface

## Comments on the self-assessment

La selección, el análisis de los datos y los documentos de requisitos están preparados. Se incluyen dos CSV municipales sin modificar y tres bocetos propios de la interfaz.

El README incluye los nombres y usuarios de GitHub de los cinco integrantes. La revisión previa de la propuesta está completada y los materiales se organizan en `HandsOn/Group05/`.

R1–R4 se justifican en datasetRequirements.html. R5 es parcial porque la documentación de áreas caninas describe un esquema anterior al actual; R6 también es parcial, ya que los dos inventarios proceden del mismo editor municipal. Wikidata se propone para enlazado posterior, sin afirmar que ya esté integrado.

La revisión de la copia detectó 185 parques sin horario, cinco sin latitud/longitud, 14 sin código de distrito y tres con la etiqueta anómala «DISTRITO». En áreas caninas faltan 110 pares latitud/longitud, pero existen 113 pares X/Y completos. Se ha contrastado la conversión EPSG:25830 → EPSG:4326 con los tres pares geográficos publicados, con diferencias inferiores a 0,00001 grados.

Los bocetos definen el diseño previsto. No se afirma que la aplicación, las consultas SPARQL o la transformación RDF estén implementadas en esta primera fase.
