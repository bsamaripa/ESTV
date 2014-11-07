from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/event')
def event():
    return 'ESL ONE!'

@app.route('/team')
def team():
    return 'Evil Geniuses!!'


if __name__ == '__main__':
    app.run()
