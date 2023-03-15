# Copyright (c) 2023 Daniel Gabay

import os


class DatabaseServiceUrlStringWrapper:
    def __init__(self):
        self.value = os.getenv("DATABASE_SERVICE_URL")
