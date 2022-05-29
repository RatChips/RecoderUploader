from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["POST"])
def index():
    print(request.json)
    return "ok"


if __name__ == "__main__":
    app.run(port=9999, debug=True)
