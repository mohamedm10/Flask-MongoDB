from application import app
from flask import render_template

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html')
        
@app.route('/login')
def login():
    pass

@app.route('/register')
def register():
    pass


@app.route('/courses')
def courses():
    pass
