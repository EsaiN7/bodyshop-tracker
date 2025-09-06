from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


#create DB object (not linked yet)

objDB = SQLAlchemy()

objMigrate  = Migrate()

objLogin = LoginManager()
objLogin.login_view = 'auth.login'


def create_app():
    objApp = Flask(__name__)

    # Basic config
    objApp.config['SECRET_KEY'] = 'dev'
    objApp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bodyshop.db'
    objApp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize DB and migration
    objDB.init_app(objApp)
    objMigrate.init_app(objApp, objDB)

    # Register blueprints
    from app import routes
    objApp.register_blueprint(routes.objBP)

    from app import auth
    objApp.register_blueprint(auth.objBluePrint)

    # Initialize login manager
    objLogin.init_app(objApp)

    return objApp


from app.models import User
@objLogin.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))