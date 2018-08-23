from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world!"

@app.route("/<string:name>")
def welcome(name):
    name = name.capitalize()
    return f"<h1>Welcome, {name}!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
