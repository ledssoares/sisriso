import os
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, HiddenField
from wtforms.validators import DataRequired, NumberRange
from wtforms.widgets.html5 import NumberInput
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, upgrade


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Pacientes(db.Model):
    __tablename__ = 'PACIENTES'
    id = db.Column(db.String(4), primary_key=True)
    nome = db.Column(db.String(64))
    tipoSanguinio = db.Column(db.String(3))
    idade = db.Column(db.Integer)
    sexo = db.Column(db.String(1))
    rg = db.Column(db.String(14))
    cpf = db.Column(db.String(14))
    profissao = db.Column(db.String(64))
    indicacao = db.Column(db.Column(64))
    # endereco
    rua = db.Column(db.String(64))
    bairo = db.Column(db.String(64))
    cep = db.Column(db.String(9))
    numero = db.Column(db.String(5))
    cidade = db.Column(db.String(34))
    estado = db.Column(db.String(34))
    # fim endereco
    #urgencia
    
    '''@staticmethod
    def inserir_tipos():
        db.session.add(Dentista(nome="Ismael"))
        db.session.add(Dentista(nome="Alves"))
        db.session.add(Dentista(nome="Lima"))
        db.session.commit()'''

        
class Convenios(db.Model):
    id = db.Column(db.String(4), primary_key=True)
    tipoPlano = db.Column(db.String(32))
    matr = db.Column(db.String(14))
    

class Contatos(db.Model):
    pass

class Anamneses(db.Model):
    pass

class Doencas(db.Model):
    pass

@app.route('/')
def inicio():
    return render_template("base.html")


@app.route('/clientes')
def clientes():
    return render_template('clientes/clientes.html')


@app.route('/dentista/cadastro')
def cadastroDentista():
    return render_template('dentistas/cadastro_dentista.html')


@app.route('/procedimentos')
def procedimentos():
    return render_template('procedimentos/procedimentos.html')


@app.route('/secretaria/cadastro')
def cadastroSecretaria():
    return render_template('secretaria/cadastroSecretaria.html')


'''@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Dentista=Dentista)

@app.cli.command()
def deploy():
    """Run deployment tasks."""
    upgrade()
    Dentista.inserir_tipos()'''
