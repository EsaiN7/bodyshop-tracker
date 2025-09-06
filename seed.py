from app import create_app, objDB
from app.models import User, Vehicle, ProgressNote
from werkzeug.security import generate_password_hash

# Create app context
objApp = create_app()
with objApp.app_context():
    
    # Clear existing data (optional, for repeatability)
    objDB.drop_all()
    objDB.create_all()

    # --- Create Users ---
    manager = User(username="manager1", password_hash=generate_password_hash("password"), role="manager")
    employee1 = User(username="tech1", password_hash=generate_password_hash("password"), role="employee")
    employee2 = User(username="tech2", password_hash=generate_password_hash("password"), role="employee")

    objDB.session.add_all([manager, employee1, employee2])
    objDB.session.commit()

    # --- Create Vehicles ---
    vehicle1 = Vehicle(make="Toyota", model="Camry", vin="VIN1234", status="Pending", assigned_to=employee1.id)
    vehicle2 = Vehicle(make="Ford", model="F-150", vin="VIN5678", status="In Progress", assigned_to=employee2.id)
    vehicle3 = Vehicle(make="Honda", model="Civic", vin="VIN9012", status="Completed", assigned_to=employee1.id)

    objDB.session.add_all([vehicle1, vehicle2, vehicle3])
    objDB.session.commit()

    # --- Add Notes ---
    note1 = ProgressNote(vehicle_id=vehicle1.id, user_id=employee1.id, note="Checked in, awaiting parts.")
    note2 = ProgressNote(vehicle_id=vehicle2.id, user_id=employee2.id, note="Started bodywork, sanding complete.")
    note3 = ProgressNote(vehicle_id=vehicle3.id, user_id=employee1.id, note="Polish and detailing done.")

    objDB.session.add_all([note1, note2, note3])
    objDB.session.commit()

    print("Sample data seeded successfully!")