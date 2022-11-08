from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! Dit is de tweede commit</p>"

@app.route("/andereURL")
def hello_world2():
    return "<p>World, Hello!</p>"