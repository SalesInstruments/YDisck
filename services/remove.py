import yadisk
from schemes.remove_scheme import RemoveQuery
from sqlalchemy.ext.asyncio import AsyncSession
from services.utils.get_storage_token import get_storage_token_ydisk

async def remove_file(remove_schema:RemoveQuery, 
                      db: AsyncSession):
    token = await get_storage_token_ydisk(token=remove_schema.user_settings.access_token,
                                          storage_name=remove_schema.user_settings.storage_name,
                                          db=db)
    y = yadisk.AsyncClient(token=token)

    await y.remove(remove_schema.path, permanently=True)