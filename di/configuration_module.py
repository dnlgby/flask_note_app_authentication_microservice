# Copyright (c) 2023 Daniel Gabay

import os

from injector import singleton, Module

from data.data_access.authentication_data_access import AuthenticationDataAccess
from services.authentication_service import AuthenticationService


class DatabaseServiceUrlStringWrapper:
    def __init__(self):
        self.value = os.getenv("DATABASE_SERVICE_URL")


class ConfigurationModule(Module):
    def configure(self, binder):
        binder.bind(DatabaseServiceUrlStringWrapper, to=DatabaseServiceUrlStringWrapper, scope=singleton)
        binder.bind(AuthenticationDataAccess, AuthenticationDataAccess, scope=singleton)
        binder.bind(AuthenticationService, AuthenticationService, scope=singleton)
