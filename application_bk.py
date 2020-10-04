#import virtualenv python library directory
import os
import sys
#sys.path.insert(0, 'venv/lib/python3.8/site-packages')
from flask import Flask, render_template, Blueprint, request, flash, redirect, url_for

from flask_bootstrap import Bootstrap

#from app import app
#import config

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
#app = Bootstrap(app)



@app.route('/')
def home():
	pageName='home'
	#return render_template('home.html')
	return '<h1> This is Flask App </h1>'
	

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=1)
