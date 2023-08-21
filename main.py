from WebserverApp import wsapp, THIS_SERVER_DIR
import first_application
import second_application
from flask import send_file


@wsapp.route("/")
def hello_world():
    return send_file('static/index.html')


if __name__ == "__main__":
    wsapp.run()
