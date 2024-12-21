import yadisk
from schemes.copy_scheme import CopyQuery
from sqlalchemy.ext.asyncio import AsyncSession
from services.utils.get_storage_token import get_storage_token_ydisk

async def copy_file(rename_schema: CopyQuery, 
                    db: AsyncSession):
    token = await get_storage_token_ydisk(token=rename_schema.user_settings.access_token,
                                          storage_name=rename_schema.user_settings.storage_name,
                                          db=db)

    y = yadisk.AsyncClient(token=token)
    
    await y.copy(rename_schema.src_path, rename_schema.dst_path)