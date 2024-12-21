from pydantic import BaseModel
from schemes.user_settings import UserSettings

class CopyQuery(BaseModel):
    src_path: str
    dst_path: str
    user_settings: UserSettings
