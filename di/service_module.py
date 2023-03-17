# Copyright (c) 2023 Daniel Gabay

from injector import singleton, Module

from data.data_access.user_authentication_data_access import UserAuthenticationDataAccess
from services.authentication_service import AuthenticationService
from di.wrappers import DatabaseServiceUrlStringWrapper


class ServiceModule(Module):
    def configure(self, binder):
        binder.bind(DatabaseServiceUrlStringWrapper, to=DatabaseServiceUrlStringWrapper, scope=singleton)
        binder.bind(UserAuthenticationDataAccess, to=UserAuthenticationDataAccess, scope=singleton)
        binder.bind(AuthenticationService, to=AuthenticationService, scope=singleton)
