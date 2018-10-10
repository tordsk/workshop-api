import json, os
from flask import Flask, Response, abort

app = Flask(__name__)

@app.route('/')
def home():
    response = "OK"
    return response

@app.route('/pod-info')
def env():
    response={}
    try:
        response["Pod Name"] = str(os.environ['POD_NAME'])
        response["Namespace"] = str(os.environ['NAMESPACE'])
    except:
        pass

    return json.dumps(response)

@app.route('/healthy')
def healthy():
    response = "OK"
    return response, 200

@app.route('/nonhealthy')
def nonhealthy():
    response = "NO"
    return response, 418


@app.errorhandler(404)
def not_found(e):
    return 'try /env', 404
