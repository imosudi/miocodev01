from flask import render_template, Blueprint, request, flash, redirect, url_for

from app import app

from datetime import datetime

codeall =  Blueprint('codeall', __name__)

loggedin =  Blueprint('loggedin', __name__)






@codeall.route('/', methods=['POST', 'GET'])
def home():
	pageName='home'
	#return render_template('home.html')
	return '<h1> This is Flask App </h1>'
