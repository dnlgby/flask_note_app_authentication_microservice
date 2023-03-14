# Copyright (c) 2023 Daniel Gabay

import os

from injector import singleton, Module

from data.dal.authentication_dal import AuthenticationDal
from services.authentication_service import AuthenticationService

class ConfigurationModule(Module):
    def configure(self, binder):
        binder.bind(str, to=os.getenv("DATABASE_SERVICE_URL"))
        binder.bind(AuthenticationDal, AuthenticationDal, scope=singleton)
        binder.bind(AuthenticationService, AuthenticationService, scope=singleton)
