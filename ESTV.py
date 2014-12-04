import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='ESTV - Index')
@app.route('/event')
def event():
    return 'ESL ONE!'

@app.route('/team')
def team():
    return 'Evil Geniuses!!'


if __name__ == '__main__':
    app.run()
