import os
import requests

from flask import Flask, Response, jsonify
from flask import request as flask_request

from ddtrace import tracer

from bootstrap import create_app, db
from models import Network, Sensor

import random


# app = Flask(__name__)
sensors = []

app = create_app()

@app.route('/')
def hello():
    return "Hello World! kojek alo jkt on dev-post2"

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
