from wtforms import Form
from wtforms.fields import StringField, SelectField


class AddCharacterForm(Form):
    server = SelectField(
        choices=[("eu", "eu"), ("us", "us"), ("kr", "kr"), ("tw", "tw"), ("cn", "cn")]
    )
    realm = StringField()
    character_name = StringField()
    role = SelectField(choices=[("tank", "tank"), ("healer", "healer"), ("dps", "dps")])
