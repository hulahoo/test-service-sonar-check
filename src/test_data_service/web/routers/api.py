import os

from flask import Flask, send_from_directory, request

from test_data_service.apps.models.provider import TestDataProvider
from test_data_service.apps.models.models import TestData

app = Flask(__name__)

mimetype = 'application/json'
base_path = os.path.dirname(os.path.abspath(__file__)) + '/../../data'
test_data_provider = TestDataProvider()


def execute():
    """
    Main function to start Flask application
    """
    app.run(host='0.0.0.0', port=8080)


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
    return send_from_directory(base_path, path)


@app.route('/api/context-source-<value>', methods=["GET"])
def whois(value):
    return send_from_directory(base_path, f'context-source-{value}.json')


@app.route('/api/siem', methods=["POST"])
def siem():
    test_data_provider.add(TestData(
        key='publish-to-siem',
        value=request.get_json()
    ))

    return app.response_class(
        response={"status": "OK"},
        status=200,
        mimetype=mimetype
    )
