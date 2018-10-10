import json
from flask import Flask, Response, abort

app = Flask(__name__)

@app.route('/')
def book_list():
    response = "OK"
    return response


@app.errorhandler(404)
def not_found(e):
    return '', 404
