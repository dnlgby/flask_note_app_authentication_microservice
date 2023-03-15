# Copyright (c) 2023 Daniel Gabay

from functools import wraps
from http import HTTPStatus

from flask_smorest import abort

from exceptions.authentication_data_access_layer_exceptions import *


def view_exception_handler(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except ServiceInternalException as ex:
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, message=str(ex))
        except AuthenticationError as ex:
            abort(HTTPStatus.UNAUTHORIZED, message=str(ex))
        except UserAlreadyExistError as ex:
            abort(HTTPStatus.CONFLICT, message=str(ex))
        except RegistrationValidationError as ex:
            abort(HTTPStatus.BAD_REQUEST, message=str(ex))

    return decorated_function
