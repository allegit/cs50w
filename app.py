from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world!"

@app.route("/<string:name>")
def welcome(name):
    name = name.capitalize()
    return f"Welcome, {name}!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
