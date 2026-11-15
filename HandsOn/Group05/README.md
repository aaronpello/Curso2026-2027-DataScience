# Group05 — Paseo Verde Madrid — Hands-on 1

**Entrega:** selección de datos y requisitos de la aplicación. Los cinco integrantes y sus usuarios de GitHub están completos.

## Integrantes

| Integrante | Nombre y apellidos | Usuario de GitHub |
| --- | --- | --- |
| 1 | Blanca Maria Pérez de Ágreda Cabello | [blancaperezdeagreda](https://github.com/blancaperezdeagreda) |
| 2 | Maria Uribazo Anton | [mariiauribazo](https://github.com/mariiauribazo) |
| 3 | Blanca Ramos Oltra | [blancaramos](https://github.com/blancaramos) |
| 4 | Sergio Coello Perez-Durantez | [scoello14](https://github.com/scoello14) |
| 5 | Fernando Izquierdo Garcia | [fernando133131](https://github.com/fernando133131) |

**Número del grupo:** Group05. Los materiales se organizan en `HandsOn/Group05/`.

## Propuesta

Paseo Verde Madrid permitirá consultar parques, jardines y áreas caninas municipales, filtrar por distrito y revisar qué áreas caninas hay cerca de un parque. Se combinarán los inventarios mediante distritos normalizados y consultas espaciales. En fases posteriores se enlazarán distritos y parques concretos con entidades de Wikidata verificadas.

Esta primera entrega define datos, requisitos y bocetos. La aplicación y el grafo RDF todavía no están implementados. El alcance no incluye rutas, tiempos a pie, ocupación ni apertura en tiempo real.

## Documentación

- [Requisitos y evaluación de los datos](requirements/datasetRequirements.html).
- [Requisitos de la aplicación y bocetos](requirements/applicationRequirements.html).
- [Autoevaluación](selfAssessmentHandsOn1.md).
- [Procedencia de las descargas](csv/procedencia.json).

Los HTML se pueden abrir directamente en el navegador; los estilos y bocetos se incluyen localmente en `requirements/assets/`. No requieren instalación ni conexión para su lectura, salvo al abrir enlaces externos.

## Datos

| Archivo | Registros | Columnas | Codificación | Separador |
| --- | ---: | ---: | --- | --- |
| `csv/parques_jardines.csv` | 208 | 32 | Windows-1252 | `;` |
| `csv/areas_caninas.csv` | 113 | 23 | UTF-8 con BOM | `;` |

Son copias originales sin cambios en el contenido, descargadas el 26/10/2026 y renombradas. Se mantienen los registros con campos vacíos. El detalle de las incidencias y de su tratamiento previsto figura en los requisitos.

## Atribución de los datos

Ayuntamiento de Madrid, Portal de Datos Abiertos:

- [Principales parques y jardines municipales](https://datos.madrid.es/dataset/200761-0-parques-jardines).
- [Áreas caninas](https://datos.madrid.es/dataset/300094-0-areas-caninas).

Ambos recursos se publican bajo [Creative Commons Attribution 4.0 International — CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Se conserva el contenido original. Las transformaciones que se realicen en fases posteriores deberán señalar sus cambios y conservar la atribución. La información puede contener ausencias o errores y no garantiza disponibilidad actual de los equipamientos.

## Organización de la carpeta

```text
Group05/
├── README.md
├── csv/
│   ├── parques_jardines.csv
│   ├── areas_caninas.csv
│   └── procedencia.json
├── requirements/
│   ├── datasetRequirements.html
│   ├── applicationRequirements.html
│   └── assets/
│       ├── style.css
│       ├── busqueda.svg
│       ├── ficha.svg
│       └── movil_estados.svg
└── selfAssessmentHandsOn1.md
```

## Organización de la entrega

Los materiales de esta primera entrega se encuentran en `HandsOn/Group05/`. Según las instrucciones de `HandsOn`, el líder crea su fork del repositorio principal y el resto del grupo trabaja a partir del fork del líder. La entrega del grupo se organiza en una rama específica y mediante un pull request separado de las tareas individuales.
