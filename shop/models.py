from wtforms.validators import length

from shop import db, login_manager
from shop import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=50), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=50), nullable=False)
    prof_img = db.Column(db.String(length=300))

    @property
    def password(self):
        raise AttributeError("No readable")

    @password.setter
    def password(self, password_plain):
        self.password_hash = bcrypt.generate_password_hash(password_plain).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024))
    amount = db.Column(db.Integer(), nullable=False)
    img = db.Column(db.String(length=300))
