# Copyright (c) 2023 Daniel Gabay

from dotenv import load_dotenv
from flask import Flask
from flask_injector import FlaskInjector
from flask_jwt_extended import JWTManager
from flask_smorest import Api

from di.configuration_module import ConfigurationModule
from resources import AuthenticationBlueprint


def create_app():
    app = Flask(__name__)

    # Load environment variables from existing '.env' files
    load_dotenv()

    # Flask
    app.config["PROPOGATE_EXCEPTION"] = True

    # API info
    app.config["API_TITLE"] = "Authentication service REST API"
    app.config["API_VERSION"] = "v1"

    # Open API
    app.config["OPENAPI_VERSION"] = "3.0.0"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    # Flask-smorest documentation
    api = Api(app)
    api.register_blueprint(AuthenticationBlueprint)

    # JWT - Will set on code for now for developing purposes
    app.config['JWT_SECRET_KEY'] = "255173194567594702208572596592176805026"
    jwt = JWTManager(app)

    # Dependency injection
    FlaskInjector(app=app, modules=[ConfigurationModule])

    return app
