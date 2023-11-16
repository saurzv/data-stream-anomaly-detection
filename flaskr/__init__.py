import os
import json
import logging
from . import main
from flask import Flask
from dotenv import load_dotenv


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(main.bp)
    app.add_url_rule('/', endpoint='index')
    # app.config.from_mapping(
    #     SECRET_KEY='dev'
    # )
    load_dotenv()
    logging.basicConfig(filename='anomalies.log', level=logging.INFO)

    if test_config is None:
        app.config.from_file('config.json', load=json.load, silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app
