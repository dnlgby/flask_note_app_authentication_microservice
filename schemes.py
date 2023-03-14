#   Copyright (c) 2023 Daniel Gabay

from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.String(required=True)
    password = fields.String(load_only=True, required=True)
