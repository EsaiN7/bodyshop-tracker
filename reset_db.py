from app import create_app, objDB
from app.models import User, Vehicle, ProgressNote

app = create_app()

with app.app_context():
    # Wipe existing data
    ProgressNote.query.delete()
    Vehicle.query.delete()
    User.query.delete()
    objDB.session.commit()

    # Seed fresh data
    test_user = User(username="testuser", role="employee")
    test_user.set_password("password123")
    objDB.session.add(test_user)
    objDB.session.commit()

    vehicles = [
        Vehicle(make="Suzuki", model="Motorcycle", vin="1", status="Pending", assigned_to=test_user.id),
        Vehicle(make="Toyota", model="Tacomaaa", vin="2", status="In Progress", assigned_to=test_user.id),
        Vehicle(make="Honda", model="Accord", vin="3", status="Completed", assigned_to=test_user.id)
    ]
    objDB.session.add_all(vehicles)
    objDB.session.commit()

    print("Database wiped and seeded fresh!")