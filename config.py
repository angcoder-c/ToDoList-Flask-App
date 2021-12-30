from flask import g, url_for
import os

root_dir = os.path.abspath(os.path.dirname(__file__)).replace('\\', '/')

class DefaultConfig:
    SECRET_KEY = 'SUPER_SECRET'
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI= 'sqlite:///' + os.path.join(root_dir, 'app/todos.db').replace('\\', '/')
    ROOT_DIR = root_dir
    SQLALCHEMY_TRACK_MODIFICATIONS = False