
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html", message="")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if username != "" and password != "":
        return render_template("login.html", message="Login Successful!")

    return render_template("login.html", message="Please enter all details")


if __name__ == "__main__":
    app.run(debug=True)
