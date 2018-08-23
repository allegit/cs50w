from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("links1.html")

@app.route("/bye")
def bye():
    headline = "Goodbye!"
    return render_template("index.html", headline=headline)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0")
