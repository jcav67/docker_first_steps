from flask import Blueprint, request, jsonify
import requests

from app.models.character_model import CharacterSchema

characters_bp = Blueprint("characters", __name__, url_prefix="/character/v1")


@characters_bp.route("/character", methods=["GET"])
def add_character():
    character_schema = CharacterSchema()
    rick_morty_api_response = requests.get(
        "https://rickandmortyapi.com/api/character/2"
    )
    api_data = rick_morty_api_response.json()
    data = character_schema.load(api_data)

    return jsonify({"id": data}), 200
