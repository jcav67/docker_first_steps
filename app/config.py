import os

SQLALCHEMY_DATABASE_URI = (
    f"mysql+pymysql://{os.environ.get('MARIADB_USER')}:"
    f"{os.environ.get('MARIADB_PASSWORD')}@"
    f"{os.environ.get('MARIADB_HOST', 'localhost')}/"
    f"{os.environ.get('MARIADB_DATABASE', 'rick_and_morty')}"
)
print(SQLALCHEMY_DATABASE_URI)
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
PORT = int(os.environ.get("PORT", 5000))
