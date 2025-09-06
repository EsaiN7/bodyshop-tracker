from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User
from app import objDB

# Create the blueprint
objBluePrint = Blueprint('auth', __name__, url_prefix='/auth')


@objBluePrint.route('/login', methods=['GET', 'POST'])
def login():
    # If user is already logged in, redirect them
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    # Handle POST request
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        # Lookup the user in the database
        user = User.query.filter_by(username=username).first()  # .first() returns a single object

        # Check password and login
        if user and user.check_password(password):
            login_user(user)
            # Redirect to next page if specified, otherwise index
            next_page = request.args.get('next')
            return redirect(next_page or url_for('main.index'))
        else:
            flash('Invalid username or password', 'danger')
            return render_template('auth/login.html')

    #If GET request, render login form
    return render_template('auth/login.html')


@objBluePrint.route('/logout')
@login_required
def logout():
    # Log the user out
    logout_user()
    return redirect(url_for('main.index'))
