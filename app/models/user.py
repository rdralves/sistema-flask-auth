from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # Adicionamos o campo senha
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False) 

    def __repr__(self):
        return f'<User {self.username}>'
