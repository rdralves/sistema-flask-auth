from app.models.movimento_estoque import MovimentoEstoque
from app import create_app, db
from app.models.user import User  

app = create_app()

with app.app_context():
    db.create_all()
    print("Banco de dados e tabelas criados com sucesso!")
