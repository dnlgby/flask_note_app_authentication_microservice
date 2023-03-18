# Copyright (c) 2023 Daniel Gabay

from injector import singleton, Module

from app.data.data_access.user_authentication_data_access import UserAuthenticationDataAccess
from app.di.wrappers import DatabaseServiceUrlStringWrapper
from app.services.authentication_service import AuthenticationService


class ServiceModule(Module):
    def configure(self, binder):
        binder.bind(DatabaseServiceUrlStringWrapper, to=DatabaseServiceUrlStringWrapper, scope=singleton)
        binder.bind(UserAuthenticationDataAccess, to=UserAuthenticationDataAccess, scope=singleton)
        binder.bind(AuthenticationService, to=AuthenticationService, scope=singleton)
