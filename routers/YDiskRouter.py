from fastapi import (APIRouter,
                     File, 
                     UploadFile, 
                     Body)

from database import db_dependency

from services.upload import upload_file
from services.listdir import get_listdir
from services.remove import remove_file
from services.rename import rename_file
from services.copy import copy_file

from schemes.list_dir_scheme import ListFilesQuery
from schemes.rename_scheme import RenameQuery
from schemes.remove_scheme import RemoveQuery
from schemes.upload_scheme import UploadQuery
from schemes.copy_scheme import CopyQuery


router = APIRouter(
    prefix="/YDisck",
    tags=["YDisck"]
) 

@router.post("/upload")
async def upload(db: db_dependency,
                 upload_scheme: UploadQuery = Body(...), 
                 file: UploadFile = File(...),
                 ):
    return await upload_file(upload_scheme,
                             db,
                             file)

@router.post("/copy")
async def copy(remove_scheme:CopyQuery, 
               db: db_dependency):
    return await copy_file(remove_scheme,
                           db)

@router.post("/")
async def listdir(list_dir_scheme: ListFilesQuery,
                  db: db_dependency):
    return await get_listdir(list_dir_scheme, 
                             db)

@router.delete("/delete")
async def remove(remove_scheme:RemoveQuery, 
                 db: db_dependency):
    return await remove_file(remove_scheme,
                             db)

@router.put("/rename")
async def rename(rename_scheme: RenameQuery,
                 db: db_dependency):
    return await rename_file(rename_scheme,
                             db)