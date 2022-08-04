from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main_page():
    return "main page here"

@app.route("/second")
def second_page():
    return "this is indeed the second page!"

@app.route("/repeat/<phrase>/<int:times>")
def repeat(phrase, times):
    complete = "your phrase is: " + phrase
    return complete * times

@app.route("/marquee")
def marquee_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)