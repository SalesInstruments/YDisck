from services.utils.check_token import check_token
from models.StoragesModel import YDiskStoragesModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

async def get_storage_token_ydisk(token:str, storage_name:str, db: AsyncSession):
    response = await check_token(token)
    user_id = response["id"]

    # Запрос через ORM
    query = (
        select(YDiskStoragesModel)
        .where(
            YDiskStoragesModel.user_id == user_id,
            YDiskStoragesModel.storage_name == storage_name,
        )
    )

    # Выполнение запроса
    result = await db.execute(query)
    storage = result.scalars().first()  # Получаем первый результат или None

    return storage.yid_key