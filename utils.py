import uuid
from enum import Enum


class ResponseCodes(Enum):

    fail_code = 204
    pass_code = 200


def is_uuid_valid(value):
    try:
        uuid.UUID(str(value))
        return True
    except ValueError:
        return False
