from pydantic import BaseModel, model_validator
import json
from schemes.user_settings import UserSettings

class UploadQuery(BaseModel):
    path: str
    # new_name: str
    user_settings: UserSettings

    @model_validator(mode="before")
    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value