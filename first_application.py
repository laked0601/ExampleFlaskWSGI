from WebserverApp import wsapp
from flask import send_file


@wsapp.route("/application-1/index.html")
def app1():
    # this is a static page and includes no server side rendered content
    return send_file("static/application-1/index.html")
