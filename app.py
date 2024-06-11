import os


from flask import Flask
from dotenv import load_dotenv


from flask_smorest import Api
from db import db


def create_app():
    load_dotenv()


    app = Flask(__name__)
    app.config["API_TITLE"] = "FC Manager REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPEN_URL_PREFIX"] = "/"


    app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///db.sqlite3")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    api = Api(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app


app = create_app()
