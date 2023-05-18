from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS



def create_app():
    app = Flask(__name__)


    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///blood.sqlite"

    db = SQLAlchemy(app)
    app.config['SECRET_KEY'] = 'ajflseiuroe324803482572oflskdkfjuw45o80wrq80572soufose57o85u3048'
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    CORS(app)
    return app, db, login_manager


app, db, login_manager = create_app()
