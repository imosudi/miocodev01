#import virtualenv python library directory
import os
import sys

from app import application

if __name__ == '__main__':
	application.debug = True
	application.run()
"""
host: 		miocodedbv01.cw8is49lrvxb.us-east-2.rds.amazonaws.com
database:	miocodedbv01
dbusername:	admin
dbpassword:	0LUWAseyi
"""	
	
#import virtualenv python library directory
import os
import sys
#sys.path.insert(0, 'venv/lib/python3.8/site-packages')
from flask import Flask, render_template, Blueprint, request, flash, redirect, url_for



if __name__ == '__main__':
	application.debug = True
	application.run()
