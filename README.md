
# Entregable 0 del Máster en Data Analytics

Este entregable consta de tres niveles:
1. Maggie
2. Lisa
3. Bart
<br>
<br>


## **Maggie Level**




El enunciado de este nivel es:

1. Usando Google colab crear un notebook que consuma la api de los Simpsons y haga una consulta cada 30seg a la API.

2. El código debe guardar cada quote en un csv dentro de una carpeta con el nombre del personaje (Lisa y Homer) y en un fichero que llamaremos general (Todos).

3. Generar un fichero Docker que copie el código dentro del contenedor y se ejecute de manera autónoma. El Docker debe tener el código en una carpeta app.

4. El fichero docker debe crear al menos las carpetas Lisa y Homer e inicialmente solo coger citas de ellos dos.

<br>

El directorio esta organizaado de la siguiente manera:

| Carpeta | Contenido |
|---------------|---------------|
| Homer | Contiene un csv con las frases que hemos leido de Homer|
| Lisa | Contiene un csv con las frases que hemos leido de Lisa|
| Resto | Contiene un csv con las frases que hemos leido del Resto de los personajes|

| Archivo | ¿Qué es? |
|---------------|---------------|
| Dockerfile | Código para poder construir la imagen con nuestro código python|
| main.py | Código python que lee de la API de los Simpsons|
| requirements.txt | Archivo que contiene las dependencias del código python|

<br>
<br>

## **Lisa Level**

El enunciado de este nivel es:

1. Mejorad el código para descargar la imagen del personaje y guardadla en la carpeta del mismo.

2. El código debe mantener un diccionario de palabras y escribir en cada iteración en un fichero el conteo de palabras que lleva.

    a. The;1

    b. Great;2


3. El código debe crear de manera dinámica las carpetas con nuevos personajes
  
<br>


El directorio esta organizaado de la siguiente manera:

| Archivo | Contenido |
|---------------|---------------|
| Dockerfile |  Código para poder construir la imagen con nuestro código python|
| main.py | Código python que lee de la API de los Simpsons |
| requirements.txt | Archivo que contiene las dependencias del código python|

<br>
<br>

## **Bart Level**

El enunciado de este nivel es::

1. Construid un Docker-compose con una imagen de un contenedor de Jupyter

2. Dentro del Jupyter generad un notebook con una gráfica mostrando las
palabras más habituales en las quotes

3. Mostrar un listado de las carpetas y las fotos de los personajes en el jupyter

4. Docker-compose debe ser capaz de hacer build del contenedor original

<br>

Dentro de mi repositorio este directorio se organiza de la siguiente manera:

| Carpeta | Contenido |
|---------------|---------------|
| Jupyter | Carpeta que contiene todo lo necesario para construir el contenedor Jupyter. Un Dockerfile, un archivo tipo notebook 'plots.ipynb', el archivo requirements.txt y una carpeta donde se almacena toda la información de los personajes.|
| Python | Carpeta que contiene todo lo relacionado con el código python. |
| docker-compose.yml | Código de docker-compose para levantar el contenedor con jupyter y otro con el código python. |
