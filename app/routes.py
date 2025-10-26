from flask import redirect, render_template, Blueprint, url_for, flash
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

    vehicles = Vehicle.query.filter_by(assigned_to=current_user.id).all()

    # Example protected page
   
    return render_template('dashboard.html',username = current_user.username, role = current_user.role, vehicles=vehicles)



from flask import request  # add this import at top

@objBP.route('/add_vehicle', methods=['POST'])
@login_required
def add_vehicle():
    make = request.form['make']
    model = request.form['model']
    vin = request.form['vin']

    new_vehicle = Vehicle(
        make=make,
        model=model,
        vin=vin,
        assigned_to=current_user.id
    )

    objDB.session.add(new_vehicle)
    objDB.session.commit()

    return redirect(url_for('main.dashboard'))

@objBP.route('/remove_vehicle', methods=['POST'])
@login_required
def remove_vehicle():
    # Get a list of selected vehicle IDs
    vehicle_ids = request.form.getlist('vehicle_ids')
    
    if not vehicle_ids:
        flash("No vehicles selected for removal.")
        return redirect(url_for('main.dashboard'))

    # Delete all selected vehicles
    for vid in vehicle_ids:
        vehicle = Vehicle.query.get(int(vid))
        if vehicle:
            objDB.session.delete(vehicle)
    objDB.session.commit()
    
    flash(f"Removed {len(vehicle_ids)} vehicle(s).")
    return redirect(url_for('main.dashboard'))


@objBP.route('/edit_vehicle', methods=['POST'])
@login_required
def edit_vehicle():
    vehicle_id = request.form.get('vehicle_id')
    vehicle = Vehicle.query.get(vehicle_id)
    if vehicle:
        vehicle.make = request.form.get('make')
        vehicle.model = request.form.get('model')
        vehicle.vin = request.form.get('vin')
        vehicle.status = request.form.get('status')
        objDB.session.commit()
        flash("Vehicle updated successfully!")
    return redirect(url_for('main.dashboard'))

@objBP.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))  