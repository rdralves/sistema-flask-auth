from flask import Blueprint, render_template, request, redirect, url_for
from app.models.produtos import Product
from app import db

bp = Blueprint('products', __name__, url_prefix='/produtos')

@bp.route('/')
def listar():
    produtos = Product.query.all()
    return render_template('products/list.html', produtos=produtos)

@bp.route('/novo', methods=['GET', 'POST'])
def criar():
    if request.method == 'POST':
        nome = request.form['nome']
        preco = float(request.form['preco'])
        estoque = int(request.form['estoque'])
        produto = Product(nome=nome, preco=preco, estoque=estoque)
        db.session.add(produto)
        db.session.commit()
        return redirect(url_for('products.listar'))
    return render_template('products/create.html')

@bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    produto = Product.query.get_or_404(id)
    if request.method == 'POST':
        produto.nome = request.form['nome']
        produto.preco = float(request.form['preco'])
        produto.estoque = int(request.form['estoque'])
        db.session.commit()
        return redirect(url_for('products.listar'))
    return render_template('products/edit.html', produto=produto)

@bp.route('/deletar/<int:id>')
def deletar(id):
    produto = Product.query.get_or_404(id)
    db.session.delete(produto)
    db.session.commit()
    return redirect(url_for('products.listar'))
