from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DefaultConfig

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config.from_object(DefaultConfig)

    db.init_app(app)

    @app.template_filter('datef')
    def date_format(date):
        if date is None:
            return ''
        return date.strftime('%m/%d/%Y')

    @app.template_filter('timef')
    def time_format(time):
        if time is None:
            return ''
        return time.strftime('%H:%M')

    from .public import bp_public
    app.register_blueprint(bp_public)

    return app

