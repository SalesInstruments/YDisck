import yadisk
import aiohttp
import asyncio

from services.utils.aio_requests.get import get
from schemas.list_dir_scheme import FileItem, ListFiles

async def get_listdir(path: str, limit: int = 20, offset: int = 0):

    y = yadisk.AsyncClient(token="y0_AgAAAAA2bkLJAAyZhgAAAAEUUNqgAABEIQCFPARHka_SA_Yc4rWJuWVhpQ")

    items = [
        FileItem(
            name=i.name,
            size=i.size,
            type=i.type
        ) 
        async for i in y.listdir(f"{path}", limit=limit, offset=offset)
    ]

    return ListFiles(path=path,
                     limit=limit,
                     offset=offset, 
                     items=items)