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
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
                            title='Home',
                            user=user,
                            posts=posts)
@app.route('/login.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
            (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                            title='Sign In',
                            form=form,
                            providers=app.config['OPENID_PROVIDERS'])

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
