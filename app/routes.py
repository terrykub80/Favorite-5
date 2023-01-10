from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fav_rappers')
def fav_rappers():
    rappers = ['Dylan', 'Dylan', 'Dylan', 'Dylan', 'Dylan']
    return render_template('fav_rappers.html', rappers=rappers)