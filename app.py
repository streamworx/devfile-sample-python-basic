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
    return "Hello World! kojek alo jkt on dev-post2 setelah beres req"


@app.route('/sensors', methods=['GET', 'POST'])
def get_sensors():
    if flask_request.method == 'GET':
        sensors = Sensor.query.all()
        system_status = []
        for sensor in sensors:
            system_status.append(sensor.serialize())
        app.logger.info(f'Sensors GET called with a total of {len(system_status)}')
        return jsonify({'sensor_count': len(system_status),
                        'system_status': system_status})
    elif flask_request.method == 'POST':
        sensors.append({'sensor_no': len(sensors) + 1, 'value': random.randint(1,100)})
        return jsonify(sensors)
    else:
        err = jsonify({'error': 'Invalid request method'})
        err.status_code = 405
        return err
        
if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
