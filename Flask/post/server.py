from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route("/")
def form_page():
    return render_template("form_page.html")

@app.route("/sundaes/submit", methods=["POST"])
def submit_sundae():
    print("form has been submitted!")
    print(request.form["name"])
    print(request.form["flavor"])
    print(request.form["numScoops"])
    print(request.form["topping1"])
    print(request.form["topping2"])
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)