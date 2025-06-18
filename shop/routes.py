from flask_login import login_user, logout_user
from shop import app
from flask import render_template, flash, redirect, url_for, session
from shop import db
from shop.forms import RegisterForm, LoginForm
from shop.models import User



@app.route("/", methods=['GET', 'POST'])
def home():
    form_register = RegisterForm()
    if form_register.validate_on_submit():
        user_to_create = User(username=form_register.username.data,email_address=form_register.email_address.data,password=form_register.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        print("created")
        flash(f"Account created! Welcome {user_to_create.username}", category='success')
        return redirect(url_for('shop'))

    if form_register.errors != {}:
        for err_msg in form_register.errors.values():
            print("err")
            flash(f'Create user ERROR: {err_msg}', category='danger')

    form_login = LoginForm()
    if form_login.validate_on_submit():
        attempted_user = User.query.filter_by(username=form_login.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form_login.password.data
        ):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            if attempted_user.username == "Admin":
                return redirect(url_for('shop_admin'))
            else:
                return redirect(url_for('shop'))
        else:
            flash('Wrong username or password! Try again!', category='danger')

    return render_template('welcome.html', form_login=form_login, form_register=form_register)

@app.route("/shop")
def shop():
    return render_template('main_page.html')

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home"))