# Copyright (c) 2023 Daniel Gabay

from app.exceptions.authentication_service_exception import AuthenticationServiceException


class DataAccessLayerException(AuthenticationServiceException):
    def __init__(self, message):
        self.message = message


class ServiceInternalException(DataAccessLayerException):
    def __str__(self):
        return f"ServiceInternalException: {self.message}"


class AuthenticationError(DataAccessLayerException):
    def __str__(self):
        return f"AuthenticationError: {self.message}"


class RegistrationError(DataAccessLayerException):
    def __str__(self):
        return f"RegistrationError: {self.message}"


class UserAlreadyExistError(RegistrationError):
    def __str__(self):
        return f"UserAlreadyExistError: {self.message}"


class RegistrationValidationError(RegistrationError):
    def __str__(self):
        return f"RegistrationValidationError: {self.message}"
