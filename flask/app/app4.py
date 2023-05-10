from flask import request, Flask, render_template, redirect, url_for

app = Flask(__name__)


# Contextos locales
# Básicamente puedes ignorar por completo que esto es así a menos que estés haciendo algo como pruebas unitarias. 
# Te darás cuenta de que el código que depende de un objeto request se romperá de repente porque no hay un objeto request. 
# La solución es crear un objeto request y vincularlo al contexto. La solución más fácil para las pruebas unitarias es utilizar el gestor de contexto test_request_context(). 
# En combinación con la sentencia with vinculará una petición de prueba para que puedas interactuar con ella. Aquí hay un ejemplo:

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)#Llamando a la plantilla hello.html, y en esa plantilla hay un if si en la ruta no le paso un valor solo coloco http://127.0.0.1:5000/hello
#retornara lo que este en el if de la plantilla hello.html, si la ruta la mando asi http://127.0.0.1:5000/hello/Marcelo entrara en el if de la plantilla hello.html y me mostrara 
#hello Marcelo!


with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'

# La otra posibilidad es pasar todo un entorno WSGI al método request_context():

# with app.request_context(environ):
#     assert request.method == 'POST'




# El objeto Request
# El objeto request está documentado en la sección API y no lo cubriremos aquí en detalle (ver Request). A continuación, un amplio resumen de algunas de las operaciones más comunes.
# En primer lugar tienes que importarlo desde el módulo flask:

from flask import request

# El método de solicitud actual está disponible utilizando el atributo method. Para acceder a los datos del formulario (datos transmitidos en una petición POST o PUT) 
# se puede utilizar el atributo form. He aquí un ejemplo completo de los dos atributos mencionados anteriormente:

def valid_login():
    if request.form['username']=="Marcelo" and request.form['password'] =="123456":
        redirect(url_for("login"))



@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                    request.form['password']):
            return request.form['username']
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

# ¿Qué ocurre si la clave no existe en el atributo form? En ese caso se produce un KeyError especial. Puedes cogerlo como un KeyError estándar, pero si no lo haces, 
# se muestra una página de error HTTP 400 Bad Request en su lugar. Así que para muchas situaciones no tienes que lidiar con ese problema.

# Para acceder a los parámetros enviados en la URL (?key=value) puede utilizar el atributo args:

searchword = request.args.get('key', '')

# Recomendamos acceder a los parámetros de la URL con get o capturando el KeyError porque los usuarios podrían cambiar la URL y presentarles una página 400 de solicitud 
# incorrecta en ese caso no es amigable para el usuario.

# Para una lista completa de métodos y atributos del objeto request, dirígete a la documentación de Request.