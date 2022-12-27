from flask import Flask, send_from_directory
from flask_wtf.csrf import CSRFProtect

import os

app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)

mimetype = 'application/json'


def execute():
    """
    Main function to start Flask application
    """
    app.run(host='0.0.0.0', port='8080')


@app.route('/health/readiness', methods=["GET"])
def readiness():
    """
    Текущее состояние готовности сервиса
    """
    return app.response_class(
        response={"status": "UP"},
        status=200,
        mimetype=mimetype
    )


@app.route('/health/liveness', methods=["GET"])
def liveness():
    """
    Возвращает информацию о работоспособности сервиса
    """
    return app.response_class(
        response={"status": "UP"},
        status=200,
        mimetype=mimetype
    )


@app.route('/data/<path:path>', methods=["GET"])
def data(path):
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)) + '/../../data', path)
