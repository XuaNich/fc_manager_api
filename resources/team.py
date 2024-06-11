from flask.views import MethodView
from flask_smorest import Blueprint
from db import db


blp = Blueprint("teams", __name__, decription="Operations on the teams")


@blp.route("/teams/<int:team_id>")
class Team(MethodView):
    def get(self, team_id):
        pass


@blp.route("/teams/")
class TeamList(MethodView):
    def get(self):
        pass
    def post(self):
        pass