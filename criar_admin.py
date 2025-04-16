from app import create_app, db
from app.models.user import User
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    admin = User(
        username='admin',
        email='admin@sistema.com',
        password=generate_password_hash('123'),
        is_admin=True
    )
    db.session.add(admin)
    db.session.commit()
    print("Usuário administrador criado com sucesso!")
