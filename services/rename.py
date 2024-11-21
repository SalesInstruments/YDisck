import yadisk
from schemas.rename_schema import RenameQuery
from sqlalchemy.ext.asyncio import AsyncSession
from services.utils.get_storage_token import get_storage_token_ydisk

async def rename_file(rename_schema: RenameQuery, 
                      db: AsyncSession):
    token = await get_storage_token_ydisk(token=rename_schema.token.access_token,
                                          storage_name=rename_schema.storage_name,
                                          db=db)

    y = yadisk.AsyncClient(token=token)
    
    await y.rename(rename_schema.src_path, rename_schema.new_name)