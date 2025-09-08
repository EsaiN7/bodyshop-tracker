from flask import redirect, render_template, Blueprint, url_for
from app.models import Vehicle
from flask_login import login_required, current_user, logout_user
from app import objDB
from sqlalchemy import text

objBP = Blueprint('main', __name__)

@objBP.route('/')
def index():
    
    return render_template('index.html')


@objBP.route('/dashboard')
@login_required
def dashboard():

    vhcSql = "SELECT * FROM Vehicle WHERE assigned_to = :user_id"

    print ("bro")

    vehicles = objDB.session.execute(text(vhcSql), {"user_id": current_user.id}).fetchall()
    # Example protected page

    print ("bro1")
   
    return render_template('dashboard.html',username = current_user.username, role = current_user.role, vehicles=vehicles)
    

@objBP.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))  