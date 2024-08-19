from flask import Flask,render_template, request # importar la libreria flask, la libreria render_template es para poder hacer uso de plantillas de hmtl

# Variable para almacenar una aplicacion utilizando la instancia de Flask
app = Flask(__name__)

#Los callbacks son metodos que se pueden ejecutar antes o despues de las peticiones que se realicen en la app
@app.before_request#La funcion before_request no necesita parametro
def before_request():
    print("Antes de la peticion")


@app.after_request
def after_request(response):#LA funcion after_request se le debe pasar una respuesta que debe retornar para que funcione
    print("despues de la peticion")
    return response#Retornando la respuesta del after_request

# Crear una vista, vista uno
# @app.route("/")#Esta linea indica que el metodo o funcion de abajo respondera o sera visible desde la raiz que estara despues del puerto http://127.0.0.1:5000/
# def index():
#     return "Mi primer codigo en Flask"

# Existe otra forma de exponer las rutas, la cual se agrega en el if __name__ == '__main__': dicha linea es la siguiente app.add_url_rule("/",view_func=index2)
# vista dos

@app.route("/")
def index2():
    print("Estamos realizando la peticion.... ")
    #return "Mi primer codigo en Flask2"
    #return render_template('index.html', titulo="index")#Sirve para llamar plantillas hmtl con solo colocar el nombre de la plantilla se mostrara en el navegador 
#ya que la carpeta que contiene la plantilla esta en el mismo nivel que el archivo app.py y la plantilla index.html le coloque el texto que quiero que se muestre 
#en un parrafo dentro del body, tambien podemos enviar informacion desde la vista a la plantilla, por ejemplo con la variable titulo="index" enviamos que el titulo de la pagina 
#sera index y quitaremos el valor que tenga la etiqueta title en la plantilla html y colocaremos entre dobles llaves el nombre de la variable que contiene lo que queremos colocar 
#en el titulo de esta forma {{titulo}} en la plantilla index.html
    data={
        "titulo":"IndexDiccionario",
        "encabezado":"Bienvenid@"}
    return render_template('index.html', data=data)#Tambien se pueden enviar varios datos y hacer uso solamente del que se va usar por ejemplo en la etiqueta title usaremos la llave
#del diccionario titulo que tiene como valor IndexDiccionario y desde la plantilla se llamaria a dicho valor de la siguiente manera data.titulo
#La llave encabezado del diccionario se lo mande a la plantilla index.html en una etiqueta h1


@app.route("/holamundo")
def hola_mundo():
    return "Hola Mundo"


@app.route("/contacto")
def contacto():
    data={
    "titulo":"Plantilla Contacto",
    "encabezado":"Bienvenid@"}
    return render_template('contacto.html', data=data)


#Esta vista tendra un enfoque dinamico recibira un parametro y se le pasara al metodo de dicha vista para que cuando se coloque 
#el valor en la variable se muestre en el saludo de la vista saludo
@app.route("/saludo/<nombre>")
def saludo(nombre):
    # return "Hola Marcelo"
    return "Hola {}".format(nombre)


#Ejemplo de rutas dinamicas con suma
@app.route("/suma/<int:valor1>/<int:valor2>")#En este caso y con flask si es necesario colocar que tipo de variable estoy esperando en este caso enteros(numeros)
def suma(valor1,valor2):
    return "La suma de los valores que ingreso son {}".format(valor1+valor2)#Mas sin embargo si yo solo hago la operacion de valor1+valor2 en el return da error porque debe devolver
#un string, tupla, lista o dicccionario o algun objeto llamable

@app.route("/perfil/<nombre>/<int:edad>")
def perfil(nombre,edad):
    return "Su nombre es {} tienes {} años".format(nombre,edad)


@app.route("/lenguajes")
def lenguajes():
    lenguaje={
        "Hay_lenguajes":False,
        "lenguajes":["PHP","JavaScript","Java","Kotlin","C#","C++"]
        }
    return render_template('lenguajes.html',data=lenguaje)


"""Queries string"""
#HTTP: HyperText Transfer Protocol
#Metodos: GET, POST, PUT, DELETE

@app.route("/datos")
def datos():
    #print(request.args)#Esta libreria debe importarse es para poder usar el metodo GET y poder enviar argumentos de una solicitud, estos datos en este caso se mostraran en la terminal 
    valor=request.args.get("valor")#De esta forma podemos capturar lo que se envia en la url con el metodo GET
    valor2=request.args.get("valor2")#lo que va dentro del parentesis debe ser lo mismo que se manda en la url 
    return "Estos son los datos {} {}".format(valor,valor2)

if __name__ == '__main__':  # Sirve para decir que esta es el archivo principal si es asi corre el app.run()
    app.add_url_rule("/", view_func=index2)#Crear plantillas de HMTL con Jinja2 para que sea devuelta por una vista 
    app.run(debug=True, port=5005)# Con el debug=True hago que el server se exponga en modo debug para poder ver los cambios sin necesidad de detener la ejecucion del programa cada vez que se realice un cambio
# el parametro port=5005 sirve para cambiar el puerto por defecto que es 5000 al puerto de mi eleccion
