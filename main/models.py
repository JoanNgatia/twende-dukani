from flask_sqlalchemy import SQLAlchemy

from app import app

# configure database to be used
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dukani.sqlite3'
db = SQLAlchemy(app)


class User(db.Model):
    """User model for app."""

    id = db.Column('student_id', db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self, username, password):
        """New user initialization details."""
        self.username = username
        self.password = password
