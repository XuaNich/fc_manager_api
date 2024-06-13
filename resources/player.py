from flask import abort
from flask.views import MethodView
from flask_smorest import Blueprint
from db import db
from models import PlayerModel, player
from schemas import PlayerSchema
from sqlalchemy.exc import IntegrityError, SQLAlchemyError


blp = Blueprint("players", __name__, description="Operations on the players")
@blp.route("/players/<int:player_id>")
class Player(MethodView):
    @blp.response(200, PlayerSchema)
    def get(self, player_id):
        return PlayerModel.query.all()


    def delete(self, player_id):
        player = PlayerModel.query.get_or_404p(player_id)
        db.session.delete(player)
        db.session.commit()
        return {"message": "Player deleted"}


    @blp.arguments(PlayerUpdateSchema)
    @blp.response(200, PlayerSchema)
    def put(self, player_id, player_data):
        player = PlayerModel.query.get(player_id)

        if player:
            player.first_name = player_data["first_name"] or player.first_name
            player.last_name = player_data["last_name"] or player.last_name
            player.position = player_data["position"] or player.position
            player.number = player_data["number"] or player.number
        else:
            player = PlayerModel(**player_data)

            db.session.add(player)

        db.session.add(Player)
        return player

@blp.route("/players/")
class PlayerList(MethodView):
    def get(self):
        pass


    @blp.arguments(PlayerSchema)
    @blp.response(201, PlayerSchema)
    def post(self, player_data:
        player = PlayerModel(** player_data)

        try:
            db.session.add(player)
            db.session.commit()
        except IntegrityError as er:
            abort(400, message=er)
        except SQLAlchemyError as er:
            abort(500, message=er)
        return player


