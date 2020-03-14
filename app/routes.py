from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Alex'}
    posts = [
        {
            'author': {'username': 'Margaret'},
            'body': 'Beautiful day in Minneapolis!'
        },
        {
            'author': {'username': 'Adam'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)