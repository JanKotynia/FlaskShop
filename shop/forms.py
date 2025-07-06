from dns.dnssec import validate
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.fields.numeric import IntegerField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError, NumberRange
from shop.models import User

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')

    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Length(min=2), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=1), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')


class ItemForm(FlaskForm):
    name = StringField(label='Product Name:', validators=[DataRequired()])
    price = IntegerField(label="Price: ",validators=[DataRequired(), NumberRange(0,None,None)])
    barcode = StringField(label='Barcode: ', validators=[DataRequired()])
    description = StringField(label='Description:')
    amount = IntegerField(label="Price: ",validators=[DataRequired()])
    img = FileField('Product Image', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Only images are allowed!')])

    submit = SubmitField('Add')