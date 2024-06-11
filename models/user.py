from db import db


class UserModel(db.Model):
    __tablename__: "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    teams = db.relationship("TeamModel", back_populates="managers", secondary="teams_managers")
