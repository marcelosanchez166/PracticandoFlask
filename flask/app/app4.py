from flask import request, Flask, render_template

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