from flask import Blueprint, render_template, request
from app.models.user import User
from app import db

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    mensagem = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(
            username=username, password=password).first()

        if user:
            mensagem = f"Bem-vindo, {user.username}!"
        else:
            mensagem = "Usuário ou senha inválidos."

    return render_template('login.html', mensagem=mensagem)
