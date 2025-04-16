from flask import Blueprint, render_template, request, redirect, url_for
from app.models.produtos import Product
from app.models.movimento_estoque import MovimentoEstoque
from app import db

bp = Blueprint('estoque', __name__, url_prefix='/estoque')


@bp.route('/')
def listar_movimentos():
    movimentos = MovimentoEstoque.query.order_by(
        MovimentoEstoque.data.desc()).all()
    return render_template('estoque/listar.html', movimentos=movimentos)


@bp.route('/entrada', methods=['GET', 'POST'])
def entrada():
    produtos = Product.query.all()
    if request.method == 'POST':
        produto_id = request.form['produto_id']
        quantidade = int(request.form['quantidade'])

        movimento = MovimentoEstoque(
            produto_id=produto_id, tipo='entrada', quantidade=quantidade)
        db.session.add(movimento)

        produto = Product.query.get(produto_id)
        produto.estoque += quantidade

        db.session.commit()
        return redirect(url_for('estoque.listar_movimentos'))

    return render_template('estoque/entrada.html', produtos=produtos)


@bp.route('/saida', methods=['GET', 'POST'])
def saida():
    produtos = Product.query.all()
    if request.method == 'POST':
        produto_id = request.form['produto_id']
        quantidade = int(request.form['quantidade'])

        produto = Product.query.get(produto_id)
        if produto.estoque >= quantidade:
            movimento = MovimentoEstoque(
                produto_id=produto_id, tipo='saida', quantidade=quantidade)
            db.session.add(movimento)

            produto.estoque -= quantidade

            db.session.commit()
            return redirect(url_for('estoque.listar_movimentos'))
        else:
            return "Estoque insuficiente!", 400

    return render_template('estoque/saida.html', produtos=produtos)
