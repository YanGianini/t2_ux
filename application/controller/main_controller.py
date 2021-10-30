import re
from flask.wrappers import Request
from application import app
from flask import render_template, url_for, redirect, request, session
from application.model.entity.usuario import Usuario
from application.model.dao.usuariodao import UsuarioDao
from application.model.entity.empresa import Empresa
from application.model.dao.empresadao import EmpresaDao
from application.model.dao.pontoDao import PontoDao

app.secret_key = "lorem ipsum"
usuariodao = UsuarioDao()
lista_user = usuariodao.getlista_user()
empresadao = EmpresaDao()
lista_emp = empresadao.getlista_emp()
pontodao = PontoDao()
lista_pontos = pontodao.lista_ponto()

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/cadastrar", methods=["GET"])
def cadastro():
    return render_template("cadastro_op.html")

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

@app.route("/entrar")
def entrar():
    return render_template("entrar_op.html")

@app.route("/entrar/<tipo>/form", methods=['POST', 'GET'])
def entrar_tipo(tipo):
    return render_template("form_entrar.html", tipo=tipo)

@app.route("/entrar/<tipo>/login", methods=["GET", "POST"])
def entrar_action(tipo):
    if tipo == 'usuario':
        email = request.form.get('email', None)
        senha = request.form.get('senha', None)
        for e in lista_user:
            if e.get_email() == email:
                if e.get_senha() == senha:
                    session['usuario']= e.get_nome()
                    session['emp']= None
                    return redirect(url_for('home'))
        return render_template('form_entrar.html', tipo=tipo)
    
    elif tipo == 'empresa':
        email = request.form.get('email', None)
        senha = request.form.get('senha', None)
        for e in lista_emp:
            if e.get_email() == email:
                if e.get_senha() == senha:
                    session['emp']= e.get_cnpj()
                    session['usuario']= None
                    return redirect(url_for('home'))
        return render_template('form_entrar.html', tipo=tipo)



@app.route("/home")
def home():
    return render_template("home.html", lista_user=lista_user, lista_emp=lista_emp)
    
@app.route("/buscar")
def buscar():
    pontos = []
    busca_txt = request.args.get('search')
    for p in lista_pontos:
        if p.get_nome() == busca_txt:
            pontos.append(p)
            return render_template("home.html", lista_user=lista_user, lista_emp=lista_emp, pontos=pontos)
        return redirect(url_for('home'))