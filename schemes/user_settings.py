from pydantic import BaseModel

class UserSettings(BaseModel):
    storage_name: str
    access_token: str