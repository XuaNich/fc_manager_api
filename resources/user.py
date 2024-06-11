from flask.views import MethodView
from flask_smorest import Blueprint
from db import db


blp = Blueprint("Users", __name__, description="Operaions on the users")


@blp.route("/users/<int:user_id>")
class User(MethodView):
    def get(self, user_id):
        pass


@blp.route("/users/")
class UserList(MethodView):
    def get(self):
        pass