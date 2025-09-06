from flask import render_template, Blueprint
from app.models import Vehicle

objBP = Blueprint('main', __name__)

@objBP.route('/')
def index():
    vehicles = Vehicle.query.all()
    return render_template('index.html', vehicles=vehicles)