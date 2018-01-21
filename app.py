# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash


app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , flaskr.py

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/generic')
def generic():
	return render_template('board.html')

@app.route('/elements')
def elements():
	return render_template('donate.html')

@app.route('/apply')
def apply():
	return render_template('apply.html')

@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)