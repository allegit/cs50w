import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    mybirthday = now.month == 8 and now.day == 7
    return render_template("index.html", mybirthday=mybirthday)

if __name__ == "__main__":
    app.run(host="0.0.0.0")    
