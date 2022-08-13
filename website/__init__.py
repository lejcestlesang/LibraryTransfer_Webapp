from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

#initiate the db
db = SQLAlchemy()
DB_NAME = 'database_v3.db'


def create_app():
    #init app
    app = Flask(__name__)
    # secret key of app
    app.config['SECRET_KEY'] = 'yhoifnwx8_8eS2"'

    # locate the db
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///Data/{DB_NAME}'
    # initiate the app
    db.init_app(app)

    #initiate the log manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.sign-up'
    login_manager.init_app(app)

    # import python script for all the website pages
    from .views import views
    from .auth import auth

    # register the two main section of the website
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    # import the db models
    from .models import User,Track,Album

    #create the db
    create_database(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    """ create the database by checking if it already exist

    Args:
        app : flask app
    """
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database !')
