from datetime import datetime
from flask_login import UserMixin
from app import objDB
from werkzeug.security import generate_password_hash, check_password_hash

# User roles: "manager" or "employee"
class User(UserMixin,objDB.Model):
    id = objDB.Column(objDB.Integer, primary_key = True)
    username = objDB.Column(objDB.String(64), unique = True, nullable = False)
    password_hash = objDB.Column(objDB.String(128), nullable = False)
    role = objDB.Column(objDB.String(20), nullable = False) #manager or employee

    #relationship to vehicles
    vehicles = objDB.relationship('Vehicle', backref = 'assigned_employee', lazy = True)

    #helper methods
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Vehicle(objDB.Model):
    id = objDB.Column(objDB.Integer, primary_key = True)
    make = objDB.Column(objDB.String(50))
    model = objDB.Column(objDB.String(50))
    vin = objDB.Column(objDB.String(20), unique = True, nullable = False)
    status = objDB.Column(objDB.String(20), default = 'Pending')
    assigned_to = objDB.Column(objDB.Integer, objDB.ForeignKey('user.id'))

    # Relationship to notes
    notes = objDB.relationship('ProgressNote', backref='vehicle', lazy=True)

class ProgressNote(objDB.Model):
    id = objDB.Column(objDB.Integer, primary_key=True)
    vehicle_id = objDB.Column(objDB.Integer, objDB.ForeignKey('vehicle.id'), nullable=False)
    user_id = objDB.Column(objDB.Integer, objDB.ForeignKey('user.id'), nullable=False)
    note = objDB.Column(objDB.Text, nullable=False)
    timestamp = objDB.Column(objDB.DateTime, default=datetime.utcnow)

    # link to user who made the note
    user = objDB.relationship('User', backref = 'notes')




