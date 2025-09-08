from app import create_app, objDB
from app.models import Vehicle

app = create_app()
app.app_context().push()

vehicles = [
    Vehicle(make="Suzuki", model="Motorcycle", vin="1", status="Pending", assigned_to=2),
    Vehicle(make="Toyota", model="Tacomaaa", vin="2", status="In Progress", assigned_to=2),
    Vehicle(make="Honda", model="Accord", vin="3", status="Completed", assigned_to=2)
]

objDB.session.add_all(vehicles)
objDB.session.commit()
print("3 sample vehicles created!")
