from app import app

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

