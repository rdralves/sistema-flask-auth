from app import create_app, db
from app.models.user import User  # 👈 necessário importar o modelo!

app = create_app()

with app.app_context():
    db.create_all()
    print("Banco de dados e tabelas criados com sucesso!")
