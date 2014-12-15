from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Event(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String(120), index=True, unique=True)
    stub    = db.Column(db.String(120), index=True, unique=True)
#    game = db.relationship('Game', backref ='event', lazy='dynamic')
    game    = db.Column(db.String(120), index=True)
    stream  = db.Column(db.String(1024), index=True)
    teams   = db.Column(db.String(1024), index=True)
    twURL   = db.Column(db.String(120), index=True)
    twID    = db.Column(db.String(120), index=True)
    bracket = db.Column(db.String(8000), index=True)

    def __repr__(self):
        return self.name


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=True)
    shortname = db.Column(db.String(120), index=True, unique=True)
    icon = db.Column(db.LargeBinary)

    def __repr__(self):
        return self.name

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=True)
    #game = db.relationship('Game', backref='team', lazy='dynamic')
    #players = db.relationship('Player', backref='team', lazy='dynamic')

    def __repr__(self):
        return self.name

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=True)
    #team = db.relationship('Team', backref='player', lazy='dynamic')

    def __repr__(self):
        return self.name

