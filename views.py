from flask import render_template, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash

from models import Users, create_user
from app import app

@app.route("/")
def index():
    '''Will return an index page!'''
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return "WIP"
    else:
        return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm = request.form.get("confirm")

        #Check if passwords match
        if confirm != password:
            return render_template("error.html", error="Passwords must match. This will be handled by javascript and not let you click the button until it matches.")
        
        #Try to create the user
        try:
            hashed = generate_password_hash(password)
            create_user(username=username, email=email, password=hashed)
        except Exception as e:
            return render_template("error.html", error=e)

        return redirect("/")
    else:
        return render_template("register.html")


@app.errorhandler(404)
def notFound(e):
    '''Will return an error page after this'''
    return "Four oh four"
