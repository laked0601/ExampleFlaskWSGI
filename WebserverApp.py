from flask import Flask
from secrets import token_urlsafe
from os import path
THIS_SERVER_DIR = path.dirname(path.abspath(__file__)).replace('\\', '/') + '/'
wsapp = Flask(__name__,
              template_folder=THIS_SERVER_DIR + "templates",
              static_folder=THIS_SERVER_DIR + 'static')
wsapp.secret_key = token_urlsafe(16)
