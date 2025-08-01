from flask import Flask,render_template, url_for
from markupsafe import escape
import requests

app = Flask(__name__)

@app.route('/user/<name>')
def show_user_profile(name):
    
    gender_url=f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    
    age_url =f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]
    
    return render_template("index.html",name=name, gender=gender, age=age)



@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(blog_url)
    all_blog = blog_response.json()
    return render_template("blog.html",posts= all_blog)

app.run(debug=True)