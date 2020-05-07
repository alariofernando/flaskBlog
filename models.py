from app import db

class Users(db.Model):
    # See http://flask-sqlalchemy.pocoo.org/2.0/models/#simple-example
    # for details on the column types.

    __table_args__ = {'extend_existing': True}

    # We always need an id
    id = db.Column(db.Integer, primary_key=True)

    # Users will have an username and an email
    username = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

def create_user(username, email, password):
    # This function is called to create an user in the database

    user = Users(username=username, email=email, password=password)

    db.session.add(user)

    db.session.commit()

    return user

if __name__ == "__main__":

    # Run this file directly to recreate the database model

    print("Creating database tables...")
    db.reflect()
    db.drop_all()
    print("Metadata clear")
    db.create_all()
    print("Done")