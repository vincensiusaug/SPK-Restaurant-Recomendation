import os
from sqlalchemy import or_
from flask import url_for, render_template, flash, redirect, request, abort, Blueprint
from FlaskSite import app, db
import Utils

recommendationName, recommendationScore = Utils.recommendation()
main = Blueprint('main', __name__)

@main.route('/')
def Home():
    return render_template('index.html', title='SPK')

@main.route('/UserData')
def InputUserData():
    return render_template('index.html', title='SPK')

@main.route('/map')
def ShowMap():
    lat = -7.258206
    lng = 112.754206
    name = "GusJek"
    return render_template('map.html', title='SPK-Map', lat=lat, lng=lng, name=name)

@main.route('/graph')
def ShowGraph():
    restaurant_name = recommendationName
    restaurant_percent = recommendationScore
    return render_template('graph.html', title='SPK', rest_name=restaurant_name, rest_percent=restaurant_percent)