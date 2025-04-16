from flask import Blueprint, render_template, session,redirect,url_for

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/sobre')
def sobre():
    return render_template('sobre.html')


@bp.route('/dashboard')
def dashboard():
    if 'usuario_id' not in session:
        return redirect(url_for('auth.login'))

    nome = session.get('usuario_nome')
    return render_template('dashboard.html', nome=nome)

@bp.route('/admin')
def admin_dashboard():
    if not session.get('usuario_id') or not session.get('is_admin'):
        return redirect(url_for('auth.login'))  # Protege a rota
    return render_template('admin/dashboard.html')