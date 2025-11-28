from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("Login.html")

@app.route("/homepage")
def homepage():
    name = request.args.get("name", )
