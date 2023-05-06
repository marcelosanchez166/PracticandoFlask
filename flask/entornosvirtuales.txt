
#Los entorno virtuales son directorios de instalación aislados. Este aislamiento te permite localizar la instalación de las dependencias de tu proyecto, 
#sin obligarte a instalarlas en todo el sistema.

#Beneficios:

#Puedes tener varios entornos, con varios conjuntos de paquetes, sin conflictos entre ellos. De esta manera, los requisitos de diferentes proyectos se pueden satisfacer al mismo tiempo.
#Puedes lanzar fácilmente tu proyecto con sus propios módulos dependientes.

"""Virtualenv
virtualenv es una herramienta que se utiliza para crear entornos Python aislados. Crea una carpeta que contiene todos los ejecutables necesarios para usar los paquetes 
que necesitaría un proyecto de Python.

Puedes instalarlo con pip:

pip install virtualenv

Verifica la instalación con el siguiente comando:

virtualenv --version
Crear un entorno
Para crear un entorno virtual utiliza:

virtualenv --no-site-packages my-env

Esto crea una carpeta en el directorio actual con el nombre del entorno (my-env/). Esta carpeta contiene los directorios para instalar módulos y ejecutables de Python.

También puedes especificar la versión de Python con la que quieres trabajar. Simplemente usa el argumento --python=/ruta/a/la/version/de/python. Por ejemplo, python2.7:

virtualenv --python=/usr/bin/python2.7 my-env

Lista de entornos: Puedes enumerar los entornos disponibles con:

lsvirtualenv

Activar un entorno: Antes de utilizar el entorno, debes activarlo:

source my-env/bin/activate
Esto asegura que solo se usen los paquetes bajo my-env/. (Notarás que el nombre del entorno se muestra a la izquierda de la línea de comandos. De esta forma puedes ver cuál es el entorno activo.)


Instalar paquetes: Puede instalar paquetes uno por uno o configurando un archivo requirements.txt para tu proyecto.

pip install algun-paquete
pip install -r requirements.txt

Si quieres crear un archivo requirements.txt  a partir de los paquetes ya instalados, ejecuta el siguiente comando:

pip freeze > requirements.txt

El archivo contendrá la lista de todos los paquetes instalados en el entorno actual y sus respectivas versiones. Esto te ayudará a lanzar tu proyecto con sus propios módulos dependientes.

Desactivar un entorno: Si has terminado de trabajar con el entorno virtual, puedes desactivarlo con:

deactivate

Esto te devuelve al intérprete de Python predeterminado del sistema con todas sus bibliotecas instaladas.

Eliminar un entorno: Simplemente elimina la carpeta del entorno."""


#Cuando se crea el entorno vitual se creara una carpeta con el nombre que le hayamos puesto, dicha carpeta tendra mas carpetas dentro de ella como (lib, scripts, pyvenv.cfg y .gitignore)
#.gitignore: es como para control de versiones 
#lib: dentro de lib van estar todas las librerias que se descarguen y que se instalen para el entorno vitual en especifico
#scripts: estaran los comando para activar y desactivar el entorno virtual 

#Para poder activar el entorno virtual hay que ingresar a la carpeta scripts y ejecutar .\ENV_Prueba\Scripts\activate para activar el entorno virtual, pero nos puede dar el siguiente
#Error 

"""sistema. Para obtener más información, consulta el tema about_Execution_Policies en https:/go.microsoft.com/fwlink/?LinkID=135170.
En línea: 1 Carácter: 1
+ .\ENV_Prueba\Scripts\activate
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess"""
# El cual se soluciona ejecutando lo siguiente (Set-ExecutionPolicy Unrestricted) en una  ventana de powershell ejecutado como administrador cuando nos pregunte si 
# queremos hacer el cambio de direvtiva colocar la letra (S) para habilitar dicha opcion posterior a ello ejecutamos de nuevo el comando para activar el entorno virtual

#Para listar los paquetes instalados en mi entorno virtual ejecutamos pip list y mostrara los paquetes que tenemos instalados en dicho entorno

#Al ejecutar (pip list) ademas de mostrarnos los paquetes instalados tambien nos mostrara la version de pip que tenemos instalada y tambien no dira si la podemos actualizar 
# como en mi caso ejecutando el siguiente comando (python.exe -m pip install --upgrade pip)

#instalacion de Django en el entorno virtual creado 
#pip install Django==4.1.6

#instalacion de Flask en el entorno virtual creado 
#pip install flask

#crear archivo de dependencias "Requerimientos"
# #pip freeze > requirements.txt
# Esto me sirve si mi proyecto lo habro desde otra computadora creando un nuevo entorno virtual y solo copiaria mi aplicacion que estaria
#en una carpeta como (src,"source") luego de crear el nuevo entorno en la otra pc hay que instalar los requermientos que necesita mi app y que si estaban instalados en el primer entorno
#Para instalar todos los requerimientos(Dependencias) que necesita mi aplicacion y con las que fue creada debo ejecutar el siguiente comando 
"""pip install -r .\requirements.txt """#Esto hara la instalacion de todos los paquetes

