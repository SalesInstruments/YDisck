import yadisk

from services.utils.get_storage_token import get_storage_token_ydisk
from schemas.list_dir_scheme import FileItem, ListFiles
from schemas.list_dir_scheme import ListFilesQuery

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

async def get_listdir(list_dir_scheme: ListFilesQuery, 
                      db: AsyncSession):
    
    token = await get_storage_token_ydisk(token=list_dir_scheme.token.access_token,
                                          storage_name=list_dir_scheme.storage_name,
                                          db=db)
    y = yadisk.AsyncClient(token=token)

    data = y.listdir(f"{list_dir_scheme.path}", 
                     limit=list_dir_scheme.limit, 
                     offset=list_dir_scheme.offset)

    print()

    items = [
        FileItem(
            name=i.name,
            size=i.size,
            type=i.type
        ) 
        async for i in data
    ]

    return ListFiles(path=list_dir_scheme.path,
                     limit=list_dir_scheme.limit,
                     offset=list_dir_scheme.offset, 
                     items=items)