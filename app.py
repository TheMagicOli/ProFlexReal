from flask import Flask, render_template
from flask import Flask, url_for, render_template, request, url_for, redirect, send_file
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
#Several different methods for database/Oauth logins
import sqlite3
from oauthlib.oauth2 import WebApplicationClient
from markupsafe import escape
#System methods
import os, time, json, requests, random, string
import os
app = Flask(__name__)

#Now, let's get an OAuth2 client running

#Initialise flask app, which will be accessed by other apps
app = Flask(__name__)



########################
# Flask Page Requests #
#######################



##############################
# FIle Manager Configuration #
##############################

@app.route("/d")
def getData():
    return send_file("static/data.json")

@app.route("/p")
def getPData():
    return send_file("static/products.json")

@app.route("/hotbar")
def hotbar():
    return render_template("hotbar.html")


@app.route("/printme")
def printme():
    return render_template("printable.html")

@app.route("/docs")
def docs():
    return render_template("docs.html")

@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/editor")
def editor():
    return render_template("editor.html")

@app.route("/mobile")
def mobile():
    return render_template("mobile.html")

@app.route("/click.mp3")
def click():
    return send_file("static/click.mp3")

@app.route("/click2.wav")
def click2():
    return send_file("static/click2.wav")

@app.route("/err.wav")
def err():
    return send_file("static/err.wav")

@app.route("/delete.mp3")
def delete():
    return send_file("static/delete.mp3")

@app.route("/make.mp3")
def make():
    return send_file("static/make.mp3")


@app.route('/')
def hello_world():
    return render_template("main.html")

if __name__ == "__main__":
    app.run(ssl_context="adhoc", host="0.0.0.0", port=8000)
