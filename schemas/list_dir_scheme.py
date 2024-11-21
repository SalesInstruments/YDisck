from typing import Optional, List, Dict
from pydantic import BaseModel
from datetime import datetime
from schemas.token_scheme import Token

# class CommentIDs(BaseModel):
#     private_resource: str
#     public_resource: str

class FileItem(BaseModel):
    size: Optional[int]
    name: str
    type: str

class ListFiles(BaseModel):
    path: str
    limit: int
    offset: int
    items: List[FileItem]
    # path: str
    # total: int

# class Embedded(BaseModel):
#     name: str
#     exif: Dict[str, str]  # Замените на более точный тип, если известен
#     resource_id: str
#     created: datetime
#     modified: datetime
#     path: str
#     type: str
#     revision: int
    # _embedded: EmbeddedList  # Включаем вложенный объект

class ListFilesQuery(BaseModel):
    storage_name: str
    path: str
    limit: int = 20
    offset: int = 0
    token: Token