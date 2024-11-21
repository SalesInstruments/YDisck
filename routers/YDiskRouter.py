from fastapi import (APIRouter,
                     File, 
                     UploadFile)

from database import db_dependency

from services.upload import upload_file
from services.listdir import get_listdir
from services.remove import remove_file
from services.rename import rename_file

from schemas.list_dir_scheme import ListFilesQuery
from schemas.rename_schema import RenameQuery


router = APIRouter(
    prefix="/YDisck",
    tags=["YDisck"]
) 

@router.post("/upload")
async def upload(path: str, 
                 file: UploadFile = File(...)):
    return await upload_file(path, 
                             file)

@router.post("/")
async def listdir(list_dir_scheme: ListFilesQuery,
                  db: db_dependency):
    return await get_listdir(list_dir_scheme, 
                             db)

@router.delete("/delete")
async def remove(path: str):
    return await remove_file(path)

@router.put("/rename")
async def rename(rename_schema: RenameQuery,
                      db: db_dependency):
    return await rename_file(rename_schema,
                             db)