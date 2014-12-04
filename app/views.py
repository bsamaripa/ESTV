from app import app

@app.route('/')
@app.route('/index')
def index():
    return 'INDEX!'

@app.route('/event')
def event():
    return 'ESL ONE!'

@app.route('/team')
def team():
    return 'Evil Geniuses!!'

