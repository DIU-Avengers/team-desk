
from flask import Flask
from config import Config
from app.models import db


def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    # registering blueprints here:-
    # main blueprint:
    from app.main import main_bp
    app.register_blueprint(main_bp)

    # authentication blueprint:
    from app.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
