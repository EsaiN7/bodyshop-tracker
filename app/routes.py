from flask import redirect, render_template, Blueprint, url_for
from app.models import Vehicle
from flask_login import login_required, current_user, logout_user

objBP = Blueprint('main', __name__)

@objBP.route('/')
def index():
    vehicles = Vehicle.query.all()
    return render_template('index.html', vehicles=vehicles)


@objBP.route('/dashboard')
@login_required
def dashboard():
    # Example protected page
    return f"Welcome {current_user.username}! You are logged in as {current_user.role}."

@objBP.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))  