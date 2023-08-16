from flask import Blueprint
from .routes import add_character


characters_blueprint = Blueprint("characters_blueprint", __name__, url_prefix="/characters")

characters_blueprint.add_url_rule("/", view_func=add_character, methods=["POST"])

