**Nombre del Proyecto:** Aplicación de Gastronomía en Madrid
**Grupo:** GROUP08
**Miembros del grupo:** Yaoyao Ji, Jiamin Wang, Erika He, Siyue Chen, Xinru Wu
**Fecha:** 2026/10/26

## 1. ¿Qué hemos hecho en esta primera práctica?
En este primer hands-on, nos hemos centrado en definir el alcance de nuestro proyecto y buscar los conjuntos de datos necesarios.
Hemos elegido el tema: una aplicación para promover la gastronomía en Madrid, que más adelante añadiremos más funcionalidades como check-in, dejar más reseñas, buscar restaurantes según categorías, etc.
En este primer trabajo, hemos buscado y seleccionado tres conjuntos de datos principales que cumplen los requisitos:
  1. Reseñas de restaurantes de TripAdvisor en la zona de Madrid (Como es un dato muy grande, acorté para que solo tenga las 10.000 primeras reseñas).
  2. El censo oficial de locales de hostelería y restauración del Ayuntamiento de Madrid (Datos Abiertos) para las ubicaciones.
  3. El conjunto de datos oficial de los barrios de Madrid para la interfaz del mapa.

## 2. Dificultades que hemos encontrado
* **Tamaño de datos:** El dataset inicial de TripAdvisor era extremadamente grande (más de 400MB), lo que causó problemas al intentar subirlo a GitHub. Tuvimos que escribir un script en Python para extraer una muestra más pequeña (10.000 filas) que sigue representando los datos pero es manejable para el repositorio.
* **Formatos de archivo:** Algunos datasets estaban inicialmente en XML o KML, por lo que tuvimos que asegurarnos de descargar las versiones en CSV para cumplir con los requisitos.


## 3. Conclusión
Finalmente, en este trabajo, hemos aprendido a buscar fuentes de Datos Abiertos, a evaluar si un conjunto de datos tiene una licencia abierta y a manejar archivos CSV grandes. También hemos entendido la importancia de enlazar los datos con entidades del mundo real (como coordenadas) para construir aplicaciones útiles.


