from app import create_app, objDB
from app.models import User, Vehicle, ProgressNote

# Create app context
objApp = create_app()
with objApp.app_context():

    # --- Query all users ---
    users = User.query.all()
    print("Users:")
    for u in users:
        print(f"{u.id}: {u.username} ({u.role})")

    # --- Query all vehicles ---
    vehicles = Vehicle.query.all()
    print("\nVehicles:")
    for v in vehicles:
        print(f"{v.id}: {v.make} {v.model}, VIN: {v.vin}, Status: {v.status}")

    # --- Query all notes ---
    notes = ProgressNote.query.all()
    print("\nProgress Notes:")
    for n in notes:
        print(f"Vehicle {n.vehicle.vin}, by {n.user.username}: {n.note} at {n.timestamp}")
