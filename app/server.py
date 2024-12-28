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
        logging.info("Hello World!")
        return configuration.hello_message

    app.register_blueprint(weight_blueprint)

    @app.route("/api/weight")
    def weight():
        return

    return app

def server(host: str = "127.0.0.1", port: int = 80, ssl: bool = False):
    manager_app = flask_app()
    start_weight_gobbler()
    logging.info("Serving on http://"+configuration.host+":"+str(port))
    serve(manager_app,  port=port)