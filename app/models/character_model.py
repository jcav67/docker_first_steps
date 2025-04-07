from marshmallow import EXCLUDE, fields
from app import db, ma


class Character(db.Model):
    __tablename__ = "RICK_MORTY_CHARACTERS"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50))
    species = db.Column(db.String(50))
    gender = db.Column(db.String(50))
    origin = db.Column(db.String(100))


# Marshmallow class
class CharacterSchema(ma.Schema):
    class Meta:
        model = Character
        load_instance = True
        unknown = EXCLUDE

    id = fields.Int()
    name = fields.Str()
    status = fields.Str()
    species = fields.Str()
    gender = fields.Str()
    image = fields.Str()


class APIRickCharacterSchema(ma.Schema):
    id = fields.Int()
    name = fields.Str()
    status = fields.Str()
    species = fields.Str()
    gender = fields.Str()
    origin = fields.Dict()
    location = fields.Dict()
    image = fields.Str()
    episode = fields.List(fields.Str())
    url = fields.Str()
    created = fields.Str()
    type = fields.Str()
