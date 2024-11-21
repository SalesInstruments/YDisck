from pydantic import BaseModel
from schemas.token_scheme import Token

class RenameQuery(BaseModel):
    storage_name: str
    src_path: str
    new_name: str
    token: Token
