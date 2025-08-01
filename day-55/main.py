from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/username/<name>/<int:number>")
def name(name,number):
    return f"Hello there {name}, you are {number} year old"

app.run(debug=True)