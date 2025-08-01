from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def homePage():
    return "<h1 style = 'text-align:center'>Hello People</h1>\
                <p>This is a paragraph</p>\
                <img src = 'https://d2zp5xs5cp8zlg.cloudfront.net/image-61785-800.jpg' alt='kitten image' >\
            "

app.run(debug=True)