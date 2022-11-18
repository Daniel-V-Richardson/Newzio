from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('views', __name__)


@auth.route('/signin', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in Successfully', category='success')
            else:
                flash('Incorrect Password, try again', category='error')
        else:
            flash('Email Does not exist', category='error')

    return render_template('/components/signin.html')


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        
        user = User.query.filter_by(email= email).first()
        
        if user:
            flash('Email Already exists', category='error')


        new_user = User(email=email, name=name, password=generate_password_hash(password,method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        flash('Account Created Successfully !', category='success')
        return redirect(url_for('news.home'))


    return render_template('/components/register.html')
