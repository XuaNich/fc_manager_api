import os

from SQLAlchemy_DB_ORM_Template.App import app
from flask import Flask
from dotenv import load_dotenv


from db import db


def create_app():
    load_dotenv()


    app = Flask(__name__)


    app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///db.sqlite3")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app


app = create_app()
