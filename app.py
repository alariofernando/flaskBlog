from flask import Flask, render_template


# Configure Application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def index():
    '''Will return an index page!'''
    return render_template("index.html")


@app.route("/login")
def login():
    return "Login"

@app.errorhandler(404)
def notFound(e):
    '''Will return an error page after this'''
    return "Four oh four"
