#   Copyright (c) 2023 Daniel Gabay

from http import HTTPStatus

from flask.views import MethodView
from flask_injector import inject
from flask_smorest import Blueprint

from schemes import UserSchema
from services.authentication_service import AuthenticationService

blp = Blueprint("auth", __name__, description="Authentication operations")


@blp.route("/auth")
class AuthView(MethodView):

    @inject
    def __init__(self, authentication_service: AuthenticationService):
        super().__init__()
        self._authentication_service = authentication_service

    @blp.arguments(UserSchema)
    def get(self, user_data: dict) -> None:
        access_token = self._authentication_service.login(**user_data)
        return {"access_token": access_token}

    @blp.arguments(UserSchema)
    @blp.response(HTTPStatus.NO_CONTENT, UserSchema)
    def post(self, user_data: dict) -> None:
        self._authentication_service.register(**user_data)
