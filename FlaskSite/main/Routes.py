import os
from sqlalchemy import or_
from flask import url_for, render_template, flash, redirect, request, abort, Blueprint
from FlaskSite import app, db

main = Blueprint('main', __name__)

@main.route('/')
def Home():
    return render_template('index.html', title='SPK')

@main.route('/UserData')
def InputUserData():
    return render_template('index.html', title='SPK')

@main.route('/map')
def ShowMap():
    return render_template('map.html', title='SPK')

@main.route('/graph')
def ShowGraph():
    restaurant_name = ['MCD', 'KFC', 'AW']
    restaurant_percent = [0.3, 0.3, 0.1]
    return render_template('graph.html', title='SPK', rest_name=restaurant_name, rest_percent=restaurant_percent)