from flask import Blueprint, render_template, request, session, redirect, url_for
from app.models.user import User
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    mensagem = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['usuario_id'] = user.id
            session['usuario_nome'] = user.username
            session['is_admin'] = user.is_admin
            return redirect(url_for('main.dashboard'))
        else:
            mensagem = "Usuário ou senha inválidos."

    return render_template('login.html', mensagem=mensagem)


@bp.route('/logout')
def logout():
    session.clear()  # limpa a sessão
    return redirect(url_for('auth.login'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    mensagem = None
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # verificar se o usuário ou e-mail já existem
        if User.query.filter_by(username=username).first():
            mensagem = "Usuário já cadastrado."
        elif User.query.filter_by(email=email).first():
            mensagem = "Email já cadastrado."
        else:
            hashed_pw = generate_password_hash(password)
            novo_user = User(username=username, email=email,
                             password=hashed_pw)
            db.session.add(novo_user)
            db.session.commit()
            return redirect(url_for('auth.login'))

    return render_template('register.html', mensagem=mensagem)
