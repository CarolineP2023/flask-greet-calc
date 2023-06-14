from flask import Flask, request

app = Flask(__name__)

@app.route("/welcome")
"""greets welcome"""
def welcome():
    return "welcome"

@app.route("/welcome/home")
"""greets welcome home"""
def welcome_home():
    return "welcome home"

@app.route("/welcome/back")
"""greets welcome back"""
def welcome_back():
    return "welcome back"