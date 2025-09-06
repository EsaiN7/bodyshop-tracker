from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#create DB object (not linked yet)

objDB = SQLAlchemy()

objMigrate  = Migrate()


def create_app():
    objApp = Flask(__name__)

    #basic config
    objApp.config['SECRET_KEY'] = 'dev' #will change later in Prod
    objApp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bodyshop.db'
    objApp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #initiialize db migratin with app
    objDB.init_app(objApp)
    objMigrate.init_app(objApp, objDB)

    
    from app import routes
    objApp.register_blueprint(routes.objBP)

    return objApp