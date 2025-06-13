from shop import app
from flask import render_template

@app.route("/")
def home():
    return render_template('welcome.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')