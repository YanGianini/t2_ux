from flask.wrappers import Request
from application import app
from flask import render_template, url_for, redirect, request, session
from application.model.entity.usuario import Usuario
from application.model.dao.usuariodao import UsuarioDao
from application.model.entity.empresa import Empresa
from application.model.dao.empresadao import EmpresaDao

app.secret_key = "lorem ipsum"
usuariodao = UsuarioDao()
lista_user = usuariodao.getlista_user()
empresadao = EmpresaDao()
lista_emp = empresadao.getlista_emp()

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/cadastrar", methods=["GET"])
def cadastro():
    return render_template("cadastro_op.html")

@app.route("/entrar")
def entrar():
    return render_template("entrar_op.html")

@app.route("/cadastrar/usuario-form")
def cadastrar_user():
    return render_template("form_user.html")


@app.route("/cadastrar/usuario", methods=['GET', 'POST'])
def cadastrar_user_action():
    nome = request.form.get('user_nome', None)
    email = request.form.get('user_email', None)
    senha = request.form.get('user_senha', None)
    senhaC = request.form.get('user_senha_c', None)
    if senha == senhaC:
        usuario = Usuario(nome, email, senha)
        lista_user.append(usuario)
        session['usuario'] = nome
        session['emp'] = None
        return redirect(url_for('home'))
    else:
        return render_template("form_user.html")
    

@app.route("/cadastrar/empresa-form", methods=['GET', 'POST'])
def cadastrar_emp():
    return render_template("form_emp.html")

@app.route("/cadastrar/empresa", methods=['GET', 'POST'])
def cadastrar_emp_action():
    email = request.form.get('emp_email', None)
    senha = request.form.get('emp_senha', None)
    senhaC = request.form.get('emp_senha_c', None)
    CNPJ = request.form.get('emp_cnpj', None)
    if senha == senhaC:
        empresa = Empresa(email, senha, CNPJ)
        lista_emp.append(empresa)
        session['emp'] = CNPJ
        session['usuario'] = None
        return redirect(url_for('home'))
    else:
        return render_template("form_emp.html")

@app.route("/home")
def home():
    return render_template("home.html", lista_user=lista_user, lista_emp=lista_emp)