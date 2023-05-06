from flask import Flask,render_template

app=Flask(__name__)


@app.route("/login", methods=["GET", "POST"] )
def login():
    render_template("auth/login.html")


def inicializar_app(config):
    return app