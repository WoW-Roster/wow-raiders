from flask import Flask

app = Flask("wow-raiders")

@app.route("/", methods=["GET"])
def main():
    return "Welcome"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
