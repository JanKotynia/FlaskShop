from flask_login import login_user
from shop import app
from flask import render_template, flash
from shop import db
from shop.forms import RegisterForm
from shop.models import User



@app.route("/", methods=['GET', 'POST'])
def home():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        print("created")
        flash(f"Created! {user_to_create}", category='success')

    if form.errors != {}:
        for err_msg in form.errors.values():
            print("err")
            flash(f'Create user ERROR: {err_msg}', category='danger')

    return render_template('welcome.html', form=form)
