from app import app
from flask import render_template, flash, redirect, request, jsonify
from .forms import LoginForm
from flask.ext.restful import Api, Resource, reqparse, fields, marshal
from flask.ext.httpauth import HTTPBasicAuth

api = Api(app)
auth = HTTPBasicAuth()

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
def eventYheater():
    return render_template("event-theater.html",
                            title="Event")

@app.route('/event-info.html')
@app.route('/event-info')
def eventInfo():
    return render_template("event-info.html",
                            title="Event")

@app.route('/user')
def user():
    return 'Users coming soon!'

#  RESTful API
@auth.error_handler
def unauthorized():
    return make_response(jsonify( { 'message': 'Unauthorized access' } ), 403)
    # return 403 instead of 401 to prevent browsers from displaying the default auth dialog
class eventAPI(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass

class teamAPI(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass

class gameAPI(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass

api.add_resource(eventAPI, '/api/v1/event')
api.add_resource(teamAPI, '/api/v1/team')
api.add_resource(gameAPI, '/api/v1/game')
