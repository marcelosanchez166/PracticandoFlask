from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))


# Métodos HTTP
# Las aplicaciones web utilizan diferentes métodos HTTP para acceder a las URL. Debes familiarizarte con los métodos HTTP mientras trabajas con Flask. Por defecto, 
# una ruta sólo responde a peticiones GET. Puedes utilizar el argumento methods del decorador route() para manejar diferentes métodos HTTP:

from flask import request

#@app.route("/do_the_login") #En este caso se cargara esta ruta si el metodo por el que consulto o hago la peticion es POST
def do_the_login():
    return "Haciendo el logueo "

#@app.route("/return show_the_login_form") #En este caso se cargara esta ruta si el metodo por el que consulto o hago la peticion es GET
def show_the_login_form():
    return render_template("login.html")

@app.route('/logins', methods=['GET', 'POST'])
def logins():
    if request.method == 'POST':#Si el metodo es POST returnara la ruta do_the_login la cual en su interior tiene en su interior tiene en su interior un texto para que muestre que se haga el login
        return do_the_login()
    else:
        return show_the_login_form()#Si el metodo es GET returnara la ruta show_the_login_form la cual en su interior tiene en su interior un texto para que muestre el login
    

# Archivos estáticos
# Las aplicaciones web dinámicas también necesitan archivos estáticos. Por lo general, de ahí vienen los archivos CSS y JavaScript. 
# Idealmente tu servidor web está configurado para servirlos por ti, pero durante el desarrollo Flask puede hacerlo también. Simplemente crea una carpeta llamada static 
# en tu paquete o junto a tu módulo y estará disponible en /static en la aplicación.

# Para generar URLs para archivos estáticos, utilice el nombre de endpoint especial 'static':
# El archivo debe ser almacenado en el sistema de archivos como static/style.css.


url_for('static', filename='style.css') 


