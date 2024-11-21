from pydantic import BaseModel
from schemes.user_settings import UserSettings

class RenameQuery(BaseModel):
    src_path: str
    new_name: str
    user_settings: UserSettings
