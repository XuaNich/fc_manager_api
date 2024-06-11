from flask.views import MethodView
from flask_smorest import Blueprint
from db import db


blp = Blueprint("players", __name__, description="Operations on the players")
class Player(MethodView):
    def get(self, player_id):
        pass
    def delete(self, player_id):
        pass
    def put(self, player_id):
        pass


@blp.route("/players/")
class  PlayerList(MethodView):
    def get(self):
        pass
    def post(self):
        pass