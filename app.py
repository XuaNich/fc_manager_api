import os


from flask import Flask
from dotenv import load_dotenv


from flask_smorest import Api
from db import db
from resources.team import blp as TeamBlueprint
from resources.player import blp as PlayerBlueprint
from resources.club import blp as ClubBlueprint
from resources.user import blp as UserBlueprint
from flask_migrate import Migrate


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
    api.register_blueprint(TeamBlueprint)
    api.register_blueprint(PlayerBlueprint)
    api.register_blueprint(ClubBlueprint)
    api.register_blueprint(UserBlueprint)
    with app.app_context():
        db.create_all()
    return app


app = create_app()


migrate = Migrate(app, db)
