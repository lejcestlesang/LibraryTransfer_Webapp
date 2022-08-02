from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
#DB_NAME = 'database_v2.db' #v2
DB_NAME = 'database_v3.db'


def create_app():
    #init app
    app = Flask(__name__)
    # secret key of app
    app.config['SECRET_KEY'] = 'yhoifnwx8_8eS2"'


    # create and initialize db
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///Data/{DB_NAME}'
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.sign-up'
    login_manager.init_app(app)

    from .views import views
    from .auth import auth

    
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    from .models import User,Track,Album


    create_database(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database !')
