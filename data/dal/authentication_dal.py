# Copyright (c) 2023 Daniel Gabay

from http import HTTPStatus

import requests
from flask_injector import inject

from common.response import Response


class AuthenticationDal:

    @inject
    def __init__(self, database_service_url: str):
        self._database_service_url = database_service_url

    def login(self, username: str, password: str) -> Response:
        payload = {"username": username, "password": password}
        response = requests.get(
            "{service_url}/user".format(service_url=self._database_service_url),
            json=payload)

        # User logged in successfully
        if response.status_code == HTTPStatus.NO_CONTENT:
            return Response.create_no_content(response.status_code, message="user logged-in successfully")

        # Error occurred
        else:
            return Response.create_no_content(response.status_code, message=response.text)

    def register(self, username: str, password: str) -> Response:
        payload = {"username": username, "password": password}
        response = requests.post(
            "{service_url}/user".format(service_url=self._database_service_url),
            json=payload)

        # User registered successfully
        if response.status_code == HTTPStatus.CREATED:
            return Response.create(response.status_code, "User registered successfully", response.json())
        # Error occurred
        else:
            return Response.create_no_content(response.status_code, message=response.text)
