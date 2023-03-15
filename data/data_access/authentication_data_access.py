# Copyright (c) 2023 Daniel Gabay

from http import HTTPStatus

import requests
from flask_injector import inject

from di.wrappers import DatabaseServiceUrlStringWrapper
from exceptions.authentication_data_access_layer_exceptions import AuthenticationError, \
    ServiceInternalException, UserAlreadyExistError, RegistrationValidationError


class AuthenticationDataAccess:

    @inject
    def __init__(self, database_service_url: DatabaseServiceUrlStringWrapper):
        self._database_service_url = database_service_url.value

    def _perform_post_request(self, endpoint: str, payload: dict) -> requests.Response:
        return requests.post(f"{self._database_service_url}/{endpoint}", json=payload)

    def login(self, username: str, password: str) -> bool:
        payload = {"username": username, "password": password}
        response = self._perform_post_request(endpoint='user/validate', payload=payload)

        # User logged in successfully
        if response.status_code == HTTPStatus.NO_CONTENT:
            return True
        elif response.status_code in (HTTPStatus.NOT_FOUND, HTTPStatus.UNAUTHORIZED):
            raise AuthenticationError(
                "Login failed. Please check your login information and ensure that your account is still active.")
        else:
            raise ServiceInternalException(response.json().get("message"))

    def register(self, username: str, password: str) -> dict:
        payload = {"username": username, "password": password}
        response = self._perform_post_request(endpoint='user', payload=payload)

        # User registered successfully
        if response.status_code == HTTPStatus.CREATED:
            return response.json()
        elif response.status_code == HTTPStatus.CONFLICT:
            raise UserAlreadyExistError("User with that name is already exist.")
        elif response.status_code == HTTPStatus.BAD_REQUEST:
            raise RegistrationValidationError(response.json().get("message", "registration validation error"))
        else:
            raise ServiceInternalException(response.json().get("message", "registration error"))
