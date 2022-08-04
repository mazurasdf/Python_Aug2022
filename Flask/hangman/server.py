from flask import Flask, request, redirect, render_template, session
app = Flask(__name__)
app.secret_key = "It's a secret to everybody"

@app.route("/")
def start_page():
    return render_template("start.html")

@app.route("/submit_answer", methods=["POST"])
def submit_answer():
    print(request.form["answer"])
    session["answer"] = request.form["answer"]
    session["incorrect_guesses"] = ""
    progress = ""
    for i in range(0,len(request.form["answer"])):
        if request.form["answer"][i] == " ":
            progress += " "
        else:
            progress += "_"
    session["progress"] = progress
    return redirect("/game")

@app.route("/game")
def game_page():
    answer = session["answer"]
    return render_template("game.html")

@app.route("/submit_guess", methods=["POST"])
def submit_guess():
    # print("your guess is: " + request.form["guess"])
    if request.form["guess"] in session["answer"]:
        old_progress = session["progress"]
        new_progress = ""

        for i in range(0, len(session["answer"])):
            if session["answer"][i] == request.form["guess"]:
                new_progress += request.form["guess"]
            else:
                new_progress += old_progress[i]
        session["progress"] = new_progress
    else:
        session["incorrect_guesses"] += request.form["guess"]
    return redirect("/game")

if __name__ == "__main__":
    app.run(debug=True)