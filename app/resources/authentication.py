# Copyright (c) 2023 Daniel Gabay

from http import HTTPStatus

from flask.views import MethodView
from flask_injector import inject
from flask_smorest import Blueprint

from app.decorators import view_exception_handler
from app.schemes import UserSchema
from app.services.authentication_service import AuthenticationService

blp = Blueprint("auth", __name__, description="Authentication operations")


class AuthView(MethodView):

    @inject
    def __init__(self, authentication_service: AuthenticationService):
        super().__init__()
        self._authentication_service = authentication_service


@blp.route("/auth/login")
class AuthLoginView(AuthView):

    @blp.arguments(UserSchema)
    @blp.response(HTTPStatus.OK)
    @view_exception_handler
    def post(self, user_data: dict) -> dict:
        return self._authentication_service.login(**user_data)


@blp.route("/auth/register")
class AuthRegisterView(AuthView):

    @blp.arguments(UserSchema)
    @blp.response(HTTPStatus.CREATED)
    @view_exception_handler
    def post(self, user_data: dict) -> dict:
        return self._authentication_service.register(**user_data)
