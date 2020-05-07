from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Configure Application
app = Flask(__name__)

#Configure database variables
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

from views import *

if __name__ == "__main__":

    app.run(debug=True)