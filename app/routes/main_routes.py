from flask import Blueprint

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return 'Bem vindo a página inicial...segundo ponto add'

@bp.route('/sobre')
def sobre():
    return 'Bem vindo a página Sobre'