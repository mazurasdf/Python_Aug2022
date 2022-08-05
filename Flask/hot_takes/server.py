from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "It's a secret to everybody"

@app.route("/")
def login_page():
    return render_template("login.html")

@app.route("/login", methods=["post"])
def login():
    session["user_name"] = request.form["user_name"]
    return redirect("/main")

@app.route("/logout")
def logout():
    if "user_name" in session:
        del session["user_name"]
    return redirect("/")

@app.route("/main")
def main_page():
    if "user_name" not in session:
        return redirect("/")
    test_data = [
        {"poster":"mike","take":"the first avengers movie is the worst mcu movie","votes":200},
        {"poster":"ian","take":"ketchup on pizza is good","votes":99},
        {"poster":"kevin","take":"water is not wet","votes":1},
        {"poster":"julio","take":"billie eilish is overrated!!","votes":101},
        {"poster":"mike","take":"last of us 2 is good","votes":100}
    ]
    return render_template("main.html",takes=test_data)

if __name__ == "__main__":
    app.run(debug=True)