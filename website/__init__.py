from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path


db = SQLAlchemy()
DB_NAME = "newzio.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ittook2monthstocreatethisproject'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import news
    from .auth import auth

    app.register_blueprint(news,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    from .models import User, Following

    create_database(app)

    return app

def create_database(app):
    if not path.exists('website/'+ DB_NAME):
        db.create_all(app=app)
        print('Database Created!')         
