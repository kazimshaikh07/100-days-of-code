from flask import Flask
import random

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1>\
        <img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='0-9 number range gif'>"

@app.route("/<int:guess>")
def guess(guess):
    if guess<random_number:
        return "<h3>is too low:</h3>\
            <img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    
    elif guess> random_number:
        return "<h3>ito high:</h3>\
            <img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
            
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"

app.run(debug=True)