from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/snake")
def snake():
    return render_template("snake.html")


@app.route("/tetris")
def tetris():
    return render_template("tetris.html")


@app.route("/battleship")
def battleship():
    return render_template("battleship.html")


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
