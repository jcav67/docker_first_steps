from .characters_view import characters_bp


def register_blueprints(app):
    app.register_blueprint(characters_bp)
