import os
from fileinput import filename

from flask_login import login_user, logout_user
from werkzeug.utils import secure_filename

from shop import app
from flask import render_template, flash, redirect, url_for, session, request
from shop import db
from shop.forms import RegisterForm, LoginForm, ItemForm
from shop.models import User, Item


@app.route("/", methods=['GET', 'POST'])
def home():
    items = Item.query.all()
    form_register = RegisterForm()
    if form_register.validate_on_submit():
        user_to_create = User(username=form_register.username.data,email_address=form_register.email_address.data,password=form_register.password1.data,prof_img=None)
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
            session.pop('_flashes', None)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            if attempted_user.username == "Admin":
                return redirect(url_for('shop_admin'))
            else:
                return redirect(url_for('shop'))
        else:
            session.pop('_flashes', None)
            flash('Wrong username or password! Try again!', category='danger')

    return render_template('welcome.html', form_login=form_login, form_register=form_register, items=items)

@app.route("/shop", methods=['GET'])
def shop():
    items = Item.query.all()
    return render_template('main_page.html', items=items, db=db)

@app.route('/buy/<int:item_id>', methods=['POST'])
def buy_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('shop'))


@app.route("/admin_panel", methods=['GET', 'POST'])
def shop_admin():
    form_item = ItemForm()
    if form_item.validate_on_submit():
        image = form_item.img.data
        print(image)
        print(form_item.img.default)
        if image:
            item_to_create = Item(name = form_item.name.data,
                              price = form_item.price.data, barcode = form_item.barcode.data,
                              description = form_item.description.data, amount = form_item.amount.data, img = image)
        else:
            item_to_create = Item(name = form_item.name.data,
                              price = form_item.price.data, barcode = form_item.barcode.data,
                              description = form_item.description.data, amount = form_item.amount.data, img = None)
        db.session.add(item_to_create)
        db.session.commit()
        print("item created")
        flash("Item added!", category='success')

    if form_item.errors != {}:
        for err_msg in form_item.errors.values():
            print("err_item")
            flash(f'Create item ERROR: {err_msg}', category='danger')

    return render_template('admin_panel.html', form_item=form_item)

@app.route('/logout')
def logout_page():
    logout_user()
    session.pop('_flashes', None)
    flash("You have been logged out!", category='info')
    return redirect(url_for("home"))