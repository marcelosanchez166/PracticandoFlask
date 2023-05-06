from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#Para correr la aplicacion en modo desarrollo puedo ejecutarla de la siguiente manera
    #flask --app app run
#Si deseo que se pueda acceder desde cualquier pc que este en la red debo ejecutarla de la siguiente forma
    #flask run --host=0.0.0.0
# Comando para habiliar el modo debug en la app, para que tome cada cambio que se haga en la app y lo cargue automaticamente
    # flask --app hello run --debug


# @app.route("/<name>")#Al crear esta ruta estoy esperando que el usuario ingrese algo, o que al ejecutar cierta accion sea pasada como ruta y la tome la variable del metodo hello
# def hello(name):
#     return f"Hello, {escape(name)}!"


@app.route('/')#Como ya existe una ruta raiz arriba se mostrara esa, por lo que deducimos que si existe mas de una ruta que sea igual, se mostrara la primera que encuentre
def index():
    return 'Index Page'

@app.route('/hello')#Si ingreso a la ruta completa http://127.0.0.1:5000/hello retornara el hello world de la funcion hi
def hi():
    return 'Hello, World'


@app.route('/user/<username>')#Esta ruta espera dos valores la ruta y el nombre del usuario asi http://127.0.0.1:5000/user/Marcelo
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')#Esta ruta espera dos valores la ruta y un numero, asi http://127.0.0.1:5000/post/19 ya que espera un entero si se le pasa un string dara error
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')#Esta ruta espera dos valores la ruta path y la subpath http://127.0.0.1:5000/path/hello
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'



@app.route('/projects/')#Retornara el string The project page cargando la siguiente ruta http://127.0.0.1:5000/projects/
def projects():
    return 'The project page'

@app.route('/about')#Retornara el string The about page cargando la siguiente ruta http://127.0.0.1:5000/about
def about():
    return 'The about page'