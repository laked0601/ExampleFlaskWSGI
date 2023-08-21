from WebserverApp import wsapp
from flask import render_template


@wsapp.route("/application-2/index.html")
def app2():
    # server side processing like getting data from sql, etc
    return render_template("application-2/index.html", variable=123)
