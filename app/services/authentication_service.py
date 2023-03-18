# Copyright (c) 2023 Daniel Gabay

from flask_jwt_extended import create_access_token
from injector import inject

from app.data.data_access.user_authentication_data_access import UserAuthenticationDataAccess


class AuthenticationService:

    @inject
    def __init__(self, authentication_data_access: UserAuthenticationDataAccess):
        self._authentication_data_access = authentication_data_access

    def login(self, username: str, password: str) -> dict:
        if self._authentication_data_access.login(username, password):
            return {"access_token": create_access_token(identity=username)}

    def register(self, username: str, password: str) -> dict:
        return self._authentication_data_access.register(username, password)
