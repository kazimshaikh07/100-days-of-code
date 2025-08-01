from flask import Flask, render_template
import random
import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    random_number = random.randint(0,10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num = random_number, year = current_year)

app.run(debug=True)