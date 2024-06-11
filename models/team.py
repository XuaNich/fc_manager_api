from db import db


class TeamModel(db.Model):
    __tablename__: "teams"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    league = db.Column(db.String(50), nullable=False)
    club_id = db.Column(db.Integer, nullable=False)
    managers = db.Column(db.Integer, nullable=False)
