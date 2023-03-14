# Copyright (c) 2023 Daniel Gabay

from flask_jwt_extended import create_access_token
from injector import inject

from data.dal.authentication_dal import AuthenticationDal


class AuthenticationService:

    @inject
    def __init__(self, authentication_dal: AuthenticationDal):
        self._authentication_dal = authentication_dal

    def login(self, username: str, password: str) -> str:
        if self._authentication_dal.login(username, password):
            return create_access_token(identity=username)

    def register(self, username: str, password: str) -> None:
        self._authentication_dal.register(username, password)