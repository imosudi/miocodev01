from flask import Flask, render_template, Blueprint, request, flash, redirect, url_for

from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

import pymysql
pymysql.install_as_MySQLdb()

#from flask_bootstrap import Bootstrap

#from application import application
#import config

application = Flask(__name__)
application.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(application)
#application = Bootstrap(application)

application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:0yadunfe@miocodedbv02.cw8is49lrvxb.us-east-2.rds.amazonaws.com/miocodedbv02'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

"""
host: 		miocodedbv01.cw8is49lrvxb.us-east-2.rds.amazonaws.com
		miocodedbv01.cw8is49lrvxb.us-east-2.rds.amazonaws.com
		miocodedbv01
database:	miocodedbv01
dbusername:	admin
dbpassword:	0LUWAseyi
"""

db = SQLAlchemy(application)


#to be moved to models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

admin = User('admin', 'admin@example.com')
#end lines to be moved to models

db.create_all()



codeall =  Blueprint('codeall', __name__)

loggedin =  Blueprint('loggedin', __name__)




#from .views import codeall
application.register_blueprint(codeall)

#from app import views

@application.route('/', methods=['POST', 'GET'])
def home():
	pageName='home'
	return render_template('home.html', methods=['GET', 'POST'])
	#return '<h1> This is Flask App not Application With init</h1>'




