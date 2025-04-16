from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from app.routes.main_routes import bp as main_bp
    from app.routes.auth_routes import bp as auth_bp
    from app.routes.produtos_routes import bp as products_bp
    from app.routes.estoque_routes import bp as estoque_bp
    from app.routes.dashboard_routes import bp as dashboard_bp


    app.register_blueprint(dashboard_bp)
    app.register_blueprint(estoque_bp)    
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(products_bp)
    

    return app
