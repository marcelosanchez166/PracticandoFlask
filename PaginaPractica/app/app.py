from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method=="POST":
        if request.form["usuario"]=="Marcelo" and request.form["password"]=="123456":
            return  redirect(url_for("index"))
        else:   
            return render_template("auth/login.html")
    else:
        print("Error de credenciales")
        return render_template("auth/login.html")
    

@app.route("/")
def index():
    return redirect(url_for('login'))

if __name__ == '__main__':  # Sirve para decir que esta es el archivo principal si es asi corre el app.run()
    app.run(debug=True, port=5005)