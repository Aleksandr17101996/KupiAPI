from jsonschema import validate
from data.schemas.schemas_account import SING_UP_SCHEMAS


class ValidateSingUp:
    def sing_up_validation(self, response):
        validate(response, SING_UP_SCHEMAS)
