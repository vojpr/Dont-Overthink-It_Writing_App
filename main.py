from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/write", methods=["GET", "POST"])
def write():
    seconds = 5
    if request.method == "POST":
        seconds = request.form["seconds-selector"]
        if seconds == "":
            seconds = 5
    return render_template("write.html", seconds=int(seconds))


if __name__ == "__main__":
    app.run(debug=True)
