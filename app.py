from flask import Flask

app = flask(__name__)

@app.route("/")
def index():
    return "welcome to the index page"


@app.route("/hi/")
def who():
    return"who are you?"

@app.route("/hi/<username>")
def greet(username):
    return f"hi there, {username}"
