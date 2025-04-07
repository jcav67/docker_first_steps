from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import text
from sqlalchemy.exc import OperationalError

db = SQLAlchemy()
ma = Marshmallow()


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config")  # o usar un diccionario

    if app.config.get("DEBUG"):
        app.debug = True  # activa el modo debug explícitamente

    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        try:
            # Ping explícito a la base de datos
            db.session.execute(text("SELECT 1"))
            print("✅ Conexión a la base de datos verificada.")
        except OperationalError as e:
            print("❌ No se pudo conectar a la base de datos:")
            print(e)

    from .routes import register_blueprints

    register_blueprints(app)

    return app
