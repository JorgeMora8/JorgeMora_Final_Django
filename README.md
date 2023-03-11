# JorgeMora_Final_Django
Proyecto final de Coderhouse

Mediante este documento se especifica todo lo relacionado al proyecto final del curso de Python en coderhouse, desde 
su correcta instalación hasta posibles situaciones de uso de la aplicación.

## Sobre El Proyecto: 
### CrossFit
El CrossFit es una modalidad de deporte que tiene como objetivo promover la mejoría de la capacidad cardiorrespiratoria, acondicionamiento físico y de la resistencia muscular, a través de la combinación de ejercicios funcionales, que son aquellos cuyos movimientos son realizados a diario, y ejercicios aeróbicos, los cuales son ejecutados a una alta intensidad.

En este proyecto tendremos funcionalidades tales como proceso de registro de competencias y contenido a disposición sobre el mundo del CrossFit 
Como nutrición, entrenamiento y más. 

### Librerías en uso: 
Al ser un proyecto elaborado en lenguaje de programación de tipado dinámico como Python, a su vez se empleó el framework de Django para la realización del proyecto. 
También se usaron librerías y recursos para llevar a cabo este proyecto de manera correcta y eficiente. 



#### Librerías & Framework
```
asgiref==3.6.0
Django==4.1.7
Pillow==9.4.0
sqlparse==0.4.3
tzdata==2022.7
```


# Proceso De Instalación: 
1. Dirigirse al repositorio de GitHub, hacer click en la opción "code" y copiar el link del repositorio. 
2. En nuestra computadora crear una carpeta, luego copiar y abrir la carpeta creada en nuestra terminal(CMD)
3. copiar el siguiente comando:
```
git clone https://github.com/JorgeMora8/JorgeMora_Final_Django.git
```
5. Abrir nuestro VSCODE y abrir la carpeta que contiene el repositorio
6. Copiar el siguiente comando para instalar las librerias y dependencias: 
```
pip install -r requirements.txt
```
7. Por ultimo, iniciar el proyecto con el siguiente comando: 
```
python manage.py runserver
```


## Registro
En el proceso de registro se **requerirán** los campos de: 
1. Nombre
2. Apellido
3. Email
4. Contraseña.  **"La contraseña será encriptada en la base de datos"**
5. Username

## Login: 
Para el proceso de login únicamente serán **necesarios** los campos de: 
1. Username
2. Password

## Competencias: 
El proyecto cuenta con la funcionalidad de competencias, donde el usuario ya registrado o logeado tendrá la opción de registrarse en cualquiera de 
Las competencias actualmente disponibles. Serán nuevamente **para confirmar** sus datos, personas y será registrado en la competencia. 
#### Datos Requeridos: 
1. Nombre
2. Apellido
3. Edad 
4. Nombre de competencia
5. Imagen de avatar
6. Usuario relacionado (Referido al nombre de usuario que creo la inscripción a la competencia)
> El usuario relacionado está presente, ya que su función es identificar si el usuario registrado es el mismo que creo la inscripción, otorgando la 
> posibilidad de eliminar su inscripción en caso de que lo desee.

***Es importante recalcar que el usuario no podrá registrarse dos o más veces en la competencia, si el usuario trata de registrarse nuevamente solo 
tendrá una inscripción registrada a su nombre***

## Blogs
También el usuario podrá disfrutar de contenido relacionado con el mundo del CrossFit y al fitness. Está presente contenido de **Salud, Entrenamiento y Competencias**, 
esto para instruir al usuario de información útil y palpable del CrossFit

### Reviews
Una vez el usuario finalice la lectura, este tendrá la opción de dejar una review expresando su opinión respecto al post. ***Opcional, no es necesario***
Esta funcionalidad tendrá como requerimientos que el usuario deposite datos como:
1. Nombre 
2. Texto 
3. Nombre del post 

