import logging

from flask import Flask
from waitress import serve

from app import configuration
from app.blueprints.weight_blueprint import weight_blueprint
from app.weight.weight_reader import start_weight_gobbler


def flask_app():
    app = Flask('__main__')

    @app.route("/")
    def hello_world():
        message = 'Hello World from scale driver!'
        logging.info(message)
        return message

    app.register_blueprint(weight_blueprint)

    @app.route("/api/weight")
    def weight():
        return

    return app


def server():
    manager_app = flask_app()
    start_weight_gobbler()
    host = configuration.config.HOST
    port = configuration.config.PORT
    logging.info(f"Serving on http://{host}:{port}")
    serve(manager_app,  port=port)
