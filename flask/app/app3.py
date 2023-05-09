from flask import Flask ,render_template

app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)#Llamando a la plantilla hello.html, y en esa plantilla hay un if si en la ruta no le paso un valor solo coloco http://127.0.0.1:5000/hello
#retornara lo que este en el if de la plantilla hello.html, si la ruta la mando asi http://127.0.0.1:5000/hello/Marcelo entrara en el if de la plantilla hello.html y me mostrara 
#hello Marcelo!

@app.route("/plantillahija")
def plantillahija():
    return render_template('plantillahija.html')