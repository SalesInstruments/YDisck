from pydantic import BaseModel
from schemes.user_settings import UserSettings

class RemoveQuery(BaseModel):
    path: str
    user_settings: UserSettings