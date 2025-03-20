from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Edgar'}
    posts = [
        {
            'author': {'username': 'Michael'},
            'body': 'My dogs are chirpin!'
        },
        {
            'author': {'username': 'Carla'},
            'body': 'F*** my chungus life man..'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)