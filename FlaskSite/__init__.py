from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from FlaskSite.Config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.jinja_env.auto_reload = True
db = SQLAlchemy(app)

from FlaskSite.main.Routes import main

app.register_blueprint(main)

import FlaskSite.admins.Admin