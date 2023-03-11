# JorgeMora_Final_Django
Proyecto final de Coderhouse

Mediante este documento se especifica todo lo relacionado al proyecto final del curso de Python en coderhouse, desde 
su correcta instalacion hasta posibles situaciones de uso de la aplicacion.

## Sobre El Proyecto: 
### Crossfit
El crossfit es una modalidad de deporte que tiene como objetivo promover la mejoría de la capacidad cardiorrespiratoria, acondicionamiento físico y de la resistencia muscular, a través de la combinación de ejercicios funcionales, que son aquellos cuyos movimientos son realizados a diario, y ejercicios aeróbicos, los cuales son ejecutados a una alta intensidad.

En este proyecto tendremos a disposicion funcionalidades tales como proceso de registro de competencias y contenido a disposicion sobre el mundo del crosffit tales 
como nutricion, entrenamiento y mas. 

### Librerias en uso: 
Al ser un proyecto elaborado en lenguaje de programacion de tipado dinamico como Python, a su vez se empleo el framework de Django para la realizacion del proyecto. 
Tambien se usaron librerias y recursos para llevar a cabo este proyecto de manera corecta y eficiente. 



## Lenguaje Programacion: Python 
#### Librerias & Framework
```
asgiref==3.6.0
Django==4.1.7
Pillow==9.4.0
sqlparse==0.4.3
tzdata==2022.7
```


# Proceso De Instalacion: 
1. Dirigirse al repositorio de GitHub, hacer click en la opcion "code" y copiar el link del repositorio. 
2. En nuestra computadora crear una carpeta, luego copiar y abrir la carpeta creada en nuestra terminal(CMD)
3. copiar el siguiente comando:
4. ```
5. git clone https://github.com/JorgeMora8/JorgeMora_Final_Django.git
```
5. Abrir nuestro VSCODE y abrir la carpeta que contiene el repositorio




## Registro
En el proceso de registro se requeriran los campos de : 
1. Nombre
2. Apellido
3. Email
4. Contrasena **La contrasena sera encriptada en la base de datos**
5. Username

## Login: 
Para el proceso de login unicamente seran necesarios los campos de: 
1. Username
2. Password

## Competencias: 
El proyecto cuenta con la funcionalidad de competencias, donde el usuario ya registrado o logeado tendra la opcion de registrarse en cualquiera de 
las competencias actualmente disponibles. Seran nuevamente **para confirmar** sus datos personas y sera registrado en la competencia. 
#### Datos Requeridos: 
1. Nombre
2. Apellido
3. Edad 
4. Nombre de competencia
5. Imagen de avatar
6. Usuario relacionado (Referido al nombre de usuario que creo la inscripcion a la competencia)
> El usuario relacionado esta presente ya que su funcion es identificar si el usuario registrado es el mismo que creo la inscripcion, otorgando la 
> posibilidad de eliminar su inscripcion en caso de que lo desee.

***Es importante recalcar que el usuario no podra registrarse dos o mas veces en la competencia, si el usuario trata de registrarse nuevamente solo 
tendra una inscripcion registrada a su nombre***

## Blogs
Tambien el usuario podra disfrutar de contenido relacionado al mundo del crossfit y al fitness. Esta presente contenido de **Salud, Entrenamiento y Competencias**, 
esto para instruir al usuario de informacion util y palpable del crossfit

### Reviews
Una vez el usuario finalize la lectura, este tendra la opcion de dejar una review expresando su opinion respecto al post. ***Opcional, no es necesario***
Esta funcionalidad tendra como requerimientos que el usuario deposite datos como:
1. Nombre 
2. Texto 
3. Nombre del post 



