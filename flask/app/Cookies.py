# Cookies
# Para acceder a las cookies se puede utilizar el atributo cookies. Para establecer las cookies se puede utilizar el método set_cookie de los objetos de respuesta. 
# El atributo cookies de los objetos request es un diccionario con todas las cookies que transmite el cliente. Si quieres utilizar sesiones, no utilices las cookies directamente, 
# sino que utiliza la Sesiones de Flask que añade algo de seguridad sobre las cookies por ti

# Leyendo cookies:

from flask import request, Flask, make_response,render_template

app=Flask(__name__)

@app.route('/')
def index():
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.
    return username

# from flask import make_response

@app.route('/indexa')
def indexa():
    resp = make_response(render_template('login.html'))
    resp.set_cookie('username', 'the username')
    return resp
