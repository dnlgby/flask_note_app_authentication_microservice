# Copyright (c) 2023 Daniel Gabay

class User:
    def __init__(self, username: str, password: str):
        self._username = username
        self._password = password

    @staticmethod
    def from_json(json_data):
        return User(json_data['username'], json_data['password'])

    def validate_password(self, password):
        return self._password == password

    def __str__(self):
        return f"User(username={self._username})"

    def __repr__(self):
        return f"User(username={self._username}, password={self._password})"
