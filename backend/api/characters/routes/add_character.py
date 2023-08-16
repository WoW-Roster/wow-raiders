from ..add_character_form import AddCharacterForm
from flask import request


def add_character():
    add_character_form = AddCharacterForm(request.form)
    if add_character_form.validate():
        return "Valid"
    return "Invalid"