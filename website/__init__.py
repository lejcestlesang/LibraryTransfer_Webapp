from flask import Flask

def create_app():
    #init app
    app = Flask(__name__)
    # secret key of app
    app.config['SECRET_KEY'] = 'yhoifnwx8_8eS2"'

    from .views import views
    
    app.register_blueprint(views,url_prefix='/')

    return app
