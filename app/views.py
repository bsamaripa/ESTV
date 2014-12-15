from app import app, db, models
from flask import render_template, flash, redirect, request, jsonify
from .forms import CreateEvent, CreatePlayer, CreateTeam, CreateGame
# from flask.ext.restful import Api, Resource, reqparse, fields, marshal
# from flask.ext.httpauth import HTTPBasicAuth

# api = Api(app)
# auth = HTTPBasicAuth()

@app.route('/')
@app.route('/index.html')
@app.route('/index')
def index():
    return render_template("index.html",
                            title='Home',)
@app.route('/login.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html',
                            title='Login')

@app.route('/about.html')
@app.route('/about')
def about():
    return render_template("about.html",
                            title="About")

@app.route('/help.html')
@app.route('/help')
def help():
    return render_template("help.html",
                            title="Help")

@app.route('/event-theater.html')
@app.route('/event-theater')
def eventTheater():
    return render_template("event-theater.html",
                            title="Event")

@app.route('/event/<string:EventStub>')
def eventInfo(EventStub):
    event = models.Event.query.filter_by(stub=EventStub).first()
    return render_template("event-info.html",
                            title = event.name,
                            event = event)

@app.route('/admin.html')
@app.route('/admin', methods=['GET', 'POST', 'DELETE'])
def admin():
    newEvent = CreateEvent()
    newTeam = CreateTeam()
    newPlayer = CreatePlayer()
    newGame = CreateGame()
    return render_template("admin.html",
                            title="Admin",
                            newEvent=newEvent,
                            newTeam=newTeam,
                            newPlayer=newPlayer,
                            newGame=newGame)

@app.route('/user.html')
@app.route('/user')
def user():
    return render_template("user.html",
                            title="User")

@app.route('/team.html')
@app.route('/team')
def team():
    return render_template("team.html",
                            title="Team")

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


#  RESTful API
# @auth.error_handler
# def unauthorized():
#     return make_response(jsonify( { 'message': 'Unauthorized access' } ), 403)
#     # return 403 instead of 401 to prevent browsers from displaying the default auth dialog
# class eventAPI(Resource):
#     def get(self):
#         pass

#     def post(self):
#         pass

#     def delete(self):
#         pass

# class teamAPI(Resource):
#     def get(self):
#         pass

#     def post(self):
#         pass

#     def delete(self):
#         pass

# class gameAPI(Resource):
#     def get(self):
#         pass

#     def post(self):
#         pass

#     def delete(self):
#         pass

# api.add_resource(eventAPI, '/api/v1/event')
# api.add_resource(teamAPI, '/api/v1/team')
 #api.add_resource(gameAPI, '/api/v1/game')
