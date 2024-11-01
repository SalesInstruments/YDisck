from fastapi import (APIRouter,
                     File, 
                     UploadFile)


from services.upload import upload_file
from services.listdir import get_listdir
from services.delite import delite_file


router = APIRouter(
    prefix="/YDisck",
    tags=["YDisck"]
) 

@router.post("/")
async def upload(path: str, file: UploadFile = File(...)):
    return await upload_file(path, file)

@router.get("/")
async def listdir(path: str, limit: int = 20, offset: int = 0):
    return await get_listdir(path, limit, offset)

@router.delete("/")
async def delete(path: str):
    return await delite_file(path)