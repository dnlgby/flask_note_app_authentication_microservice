#   Copyright (c) 2023 Daniel Gabay


class Response:
    def __init__(self, code, message, content):
        self._code = code
        self._message = message
        self._content = content

    @staticmethod
    def create(code, message, content):
        return Response(code=code, message=message, content=content)

    @staticmethod
    def create_no_content(code, message):
        return Response(code=code, message=message, content=None)

    @property
    def code(self):
        return self._code

    @property
    def message(self):
        return self._message

    @property
    def content(self):
        return self._content
