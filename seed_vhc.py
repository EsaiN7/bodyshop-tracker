from app import create_app, objDB
from app.models import Vehicle

app = create_app()
app.app_context().push()

vehicles = [
    Vehicle(make="Suzuki", model="Motorcycle", vin="09845328907", status="Pending", assigned_to=1),
    Vehicle(make="Toyota", model="Tacomaaa", vin="897534683", status="In Progress", assigned_to=1),
    Vehicle(make="Honda", model="Accord", vin="235409878974", status="Completed", assigned_to=1)
]

objDB.session.add_all(vehicles)
objDB.session.commit()
print("3 sample vehicles created!")
