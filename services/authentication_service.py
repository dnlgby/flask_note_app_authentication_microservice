# Copyright (c) 2023 Daniel Gabay

from flask_jwt_extended import create_access_token
from injector import inject

from data.data_access.authentication_data_access import AuthenticationDataAccess


class AuthenticationService:

    @inject
    def __init__(self, authentication_data_access: AuthenticationDataAccess):
        self._authentication_dal = authentication_data_access

    def login(self, username: str, password: str) -> dict:
        if self._authentication_dal.login(username, password):
            return {"access_token": create_access_token(identity=username)}

    def register(self, username: str, password: str) -> dict:
        return self._authentication_dal.register(username, password)
