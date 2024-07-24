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

@app.route('/')
def hello_world():
    return render_template("dynamicPorts.html")

@app.route('/webapp')
def test():
    return render_template("webapp.html")
GOOGLECLIENTID = os.environ.get("GOOGLECLIENTID")
GOOGLECLIENTSECRET = os.environ.get("GOOGLECLIENTSECRET")
print(GOOGLECLIENTID)
print(GOOGLECLIENTSECRET)
GOOGLEDISCOVERYURL = ("https://accounts.google.com/.well-known/openid-configuration")

#Now, let's get an OAuth2 client running
client = WebApplicationClient(GOOGLECLIENTID)

#Initialise flask app, which will be accessed by other apps
app = Flask(__name__)

#Initialise login manager
loginmanager = LoginManager()
loginmanager.init_app(app)

#########################
# Google OAuth Handler  #
#########################
def getGoogleProviderCFG(): #This returns the current authorisation end point for Google through an open updated page.
    #It returns it as a JSON object that is accessed in /login
    return requests.get(GOOGLEDISCOVERYURL).json()
#########################
# Loginmanager Requests #
#########################

@loginmanager.user_loader #Returns user data
def load_user(user):
    return User.get(user)

########################
# Flask Page Requests #
#######################

###### Home index /
@app.route('/') #Returns home HTML file
def index():
    if current_user.is_authenticated:
        return render_template("main.html")
    else:
        return render_template("loginask.html")


##############################
# FIle Manager Configuration #
##############################
    
def getstrEPOCHtime():
    return str(time.time())


@app.route("/login/callback")
def callback(): #This callback is complicated and tehnical. Here's the basic idea.
    code = request.args.get("code") #Here, we're trying to get the auth code that Google gave us to verify their identity.
    googleProviderCFG = getGoogleProviderCFG() #We're going to now verify their code with Google themselves
    tokenEndpoint =googleProviderCFG["token_endpoint"]
    #This block of code is the token request to Google
    #I'm mostly copying this from a code snippet, this is a complicated backend communication
    tokenURL, headers, body = client.prepare_token_request(
        tokenEndpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    tokenResponse - requests.post(
        tokenURL,
        headers=headers,
        data=body,
        auth=(GOOGLECLIENTID, GOOGLECLIENTSECRET)
    )
    client.parse_request_body_response(json.dumps(tokenResponse.json()))
    return render_template("redirect.html")
    
@app.route('/login')
def login():
    googleProviderCFG = getGoogleProviderCFG()
    authEndpoint = googleProviderCFG["authorization_endpoint"]
    #This prepares the request for google that gets the user's Google Profile
    request_uri = client.prepare_request_uri(
        authEndpoint,
        redirect_uri="https://127.0.0.1:500/login/callback", #The callback url to this app.
        scope=["openid", "email", "profile"]
    )
    return redirect(request_uri)
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
    return render_template("dynamicPorts.html")

@app.route("/mobile")
def mobile():
    return render_template("mobile.html")


if __name__ == "__main__":
    app.run(ssl_context="adhoc", host="0.0.0.0", port=8000)