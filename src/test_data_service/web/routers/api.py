import os

from flask_cors import cross_origin
from flask_wtf.csrf import CSRFProtect
from flask import Flask, send_from_directory, request
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

from test_data_service.config.config import settings
from test_data_service.config.log_conf import logger
from test_data_service.apps.models.provider import TestDataProvider
from test_data_service.apps.models.models import TestData

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config["SESSION_COOKIE_SECURE"] = settings.session_cookie_secure
app.config['WTF_CSRF_ENABLED'] = settings.csrf_enabled

csrf = CSRFProtect()
csrf.init_app(app)

mimetype = 'application/json'

base_path = os.path.dirname(os.path.abspath(__file__)) + '/../../data'
test_data_provider = TestDataProvider()


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
    logger.info("Readiness checking started")
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
    logger.info("Liveness checking started")
    return app.response_class(
        response={"status": "UP"},
        status=200,
        mimetype=mimetype
    )


@app.route('/metrics', methods=["GET"])
def metrics():
    """
    Возвращает метрики сервиса
    """
    return app.response_class(
        response=generate_latest(),
        status=200,
        mimetype='text/plain',
        content_type=CONTENT_TYPE_LATEST
    )


@app.route('/api', methods=["GET"])
def api_routes():
    return {
        "openapi:": "3.0.0",
        "info": {
            "title": "Событийный шлюз",
            "version": "0.0.3",
        },
        "paths": {}
        }


@app.route('/data/<path:path>', methods=["GET"])
def data(path):
    return send_from_directory(base_path, path)


@app.route('/api/context-source-<value>', methods=["GET"])
def whois(value):
    return send_from_directory(base_path, f'context-source-{value}.json')


@app.route('/api/siem', methods=["POST"])
@cross_origin(origins=["0.0.0.0"], methods=["POST", "OPTIONS"])
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
