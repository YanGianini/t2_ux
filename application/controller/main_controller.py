from application import app

from flask import render_template, url_for

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/cadastrar", methods=["GET"])
def cadastro():
    return render_template("cadastro_op.html")

@app.route("/entrar")
def entrar():
    return render_template("entrar_op.html")

@app.route("/cadastrar/usuario", methods=['GET', 'POST'])
def cadastrar_user():
    return render_template("form_user.html")

@app.route("/cadastrar/empresa", methods=['GET', 'POST'])
def cadastrar_emp():
    return render_template("form_emp.html")

