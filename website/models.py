from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# Here we will add id, price, adress of the favourite houses so they will be saved in a new database
#For now I leave the Note as an example but later we can delete it and just leave the Favourite database.
# class Favourites (db.Model):

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')