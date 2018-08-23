import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    my_birthday = now.month == 8 and now.day == 7
    my_birthday = True
    return render_template("index.html", my_birthday=my_birthday)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
