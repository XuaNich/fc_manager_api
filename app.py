import os

from flask import Flask, jsonify
from dotenv import load_dotenv


from flask_smorest import Api
from db import db
from resources.team import blp as TeamBlueprint
from resources.player import blp as PlayerBlueprint
from resources.club import blp as ClubBlueprint
from resources.user import blp as UserBlueprint
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from blocklist import BLOCKLIST

def create_app():
    load_dotenv()


    app = Flask(__name__)
    app.config["API_TITLE"] = "FC Manager REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPEN_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")


    app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///db.sqlite3")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    jwt = JWTManager(app)
    api = Api(app)
    db.init_app(app)


    api.register_blueprint(TeamBlueprint)
    api.register_blueprint(PlayerBlueprint)
    api.register_blueprint(ClubBlueprint)
    api.register_blueprint(UserBlueprint)

    with app.app_context():
        db.create_all()


    @jwt.additional_claims_loader
    def add_claims_to_jwt(identity):
        if identity == 1:
            return {"is_admin": True}
        return {"is_admin": False}


    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        return jwt_payload["jit"] in BLOCKLIST


    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"message": "The token has expired.", "error": "token_expired"}),
            401,
        )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message": "Signature verification failed.", "error": "token_expired"}),
            401,
        )

    return app


app = create_app()
migrate = Migrate(app, db)

