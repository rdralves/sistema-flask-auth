from flask import Blueprint, render_template
from app.models.movimento_estoque import MovimentoEstoque
from app.models.produtos import Product
from sqlalchemy import func
from app import db

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')


@bp.route('/estoque')
def estoque_dashboard():
    total_entradas = db.session.query(
        func.sum(MovimentoEstoque.quantidade)).filter_by(tipo='entrada').scalar() or 0
    total_saidas = db.session.query(
        func.sum(MovimentoEstoque.quantidade)).filter_by(tipo='saida').scalar() or 0

    produtos = Product.query.all()

    return render_template('dashboard/estoque.html', total_entradas=total_entradas,
                           total_saidas=total_saidas, produtos=produtos)
