# Copyright (c) 2023 Daniel Gabay

import os
import random
import string
import unittest
from http import HTTPStatus

import jwt
from flask import json

from app import app


def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


class AuthenticationResourcesTests(unittest.TestCase):

    @staticmethod
    def create_random_payload():
        return {
            'username': generate_random_string(8),
            'password': "password"
        }

    @staticmethod
    def jwt_is_valid(token, secret_key):
        try:
            payload = jwt.decode(token, secret_key, algorithms=['HS256'])
            return payload
        except Exception:
            return False

    def setUp(self):
        self._app = app.create_app().test_client()
        self._random_payload = self.create_random_payload()

    def test_register_success(self):
        response = self._app.post(
            '/auth/register',
            data=json.dumps(self._random_payload),
            content_type='application/json')
        data = json.loads(response.data)

        # Asserts
        self.assertEqual(response.status_code, HTTPStatus.CREATED)

        # Assert result format
        self.assertTrue('id' in data and type(data['id']) is int)
        self.assertTrue('username' in data and type(data['username']) is str)

    def test_login_success(self):

        # Create user (register)
        self._app.post(
            '/auth/register',
            data=json.dumps(self._random_payload),
            content_type='application/json')

        # Test login
        response = self._app.post(
            '/auth/login',
            data=json.dumps(self._random_payload),
            content_type='application/json')
        data = json.loads(response.data)

        # Asserts
        self.assertEqual(response.status_code, HTTPStatus.OK)

        # Assert result format
        self.assertTrue('access_token' in data)

        secret_key = os.getenv('JWT_SECRET_KEY')
        self.assertTrue(AuthenticationResourcesTests.jwt_is_valid(data['access_token'], secret_key))


if __name__ == '__main__':
    unittest.main()
