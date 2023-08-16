from flask import Flask
from api.characters.characters_blueprint import characters_blueprint

app = Flask("wow-raiders")
app.register_blueprint(characters_blueprint)

@app.route("/", methods=["GET"])
def main():
    return "Welcome"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
