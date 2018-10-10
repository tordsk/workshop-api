import json, os
from flask import Flask, Response, abort

app = Flask(__name__)

@app.route('/')
def home():
    response = "OK"
    return response

@app.route('/env')
def env():
    try:
        env = os.environ['FLASK_ENV']
    except:
        env = 'unset'
    response = "Environment: " + env
    return response


@app.errorhandler(404)
def not_found(e):
    return '', 404
