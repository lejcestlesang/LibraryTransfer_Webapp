from flask import Blueprint, render_template, request,flash,redirect,url_for
from .models import User
from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import login_user,login_required,logout_user,current_user

auth = Blueprint('auth', __name__)

@auth.route('/sign-in', methods = ['GET','POST'])
def signin():
    if request.method == 'POST':
        #get user input
        email = request.form.get('email')
        pwd = request.form.get('password')
        
        #query db
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, pwd):
                flash('Logging successfully!', category='success')
                login_user(user,remember=True)
                return redirect(url_for('views.transfer'))
            else:
                flash('Incorrect password, try again.',category='error')
        else:
            flash('Email does not exist.',category='error')
    #print(data)
    return render_template('login.html', user=current_user)

@auth.route('/sign-up',methods = ['GET','POST'])
def signup():
    if request.method == 'POST':
        #get user data
        email = request.form.get('email')
        pwd1 = request.form.get('password1')
        pwd2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.',category='succes')
        elif len(email)<4:
            flash('Email must ne greater than 4 characters.', category = 'error')
        elif pwd1 != pwd2:
            flash('Passwords don\'t match.', category = 'error')
        elif len(pwd1)< 7:
            flash('Password must be at least 7 characters.', category = 'error')
        else:
            new_user = User(email=email,password=generate_password_hash(pwd1,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category = 'success_account_creation')
            return redirect(url_for('views.home'))

    return render_template('sign_up.html',user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('logout.html', user=current_user)



