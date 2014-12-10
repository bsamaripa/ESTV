from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=True)
    game = db.relationship('Game', backref ='event', lazy='dynamic')
    teams = db.Column(db.String(1024), index=True, unique=True)
    bracket = db.Column(db.String(8000), index=True, unique=True)

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=True)
    icon = db.Column(db.LargeBinary)

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=True)
    game = db.relationship('Game', backref='team', lazy='dynamic')
    players = db.relationship('Player', backref='team', lazy='dynamic')

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=True)
    team = db.relationship('Team', backref='player', lazy='dynamic')


