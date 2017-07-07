from flask import Flask, render_template, Blueprint
from wfdb.models import db
from wfdb.controllers.main import main_blueprint
from wfdb.controllers.blog import blog_blueprint

import datetime

def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)

    db.init_app(app)

    app.register_blueprint(main_blueprint)
    app.register_blueprint(blog_blueprint)

    return app