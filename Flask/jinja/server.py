from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/repeat/<word>/<int:times>")
def repeat(word, times):
    return render_template("repeat.html",word=word, times=times)

@app.route("/box/<color>")
def colored_box(color):
    return render_template("box.html", color=color)

if __name__ == "__main__":
    app.run(debug=True)