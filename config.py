# config.py
class Config:
    SECRET_KEY = 'chave_secreta_muito_segura'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///meubanco.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
