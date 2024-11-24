from fastapi import (UploadFile)
from sqlalchemy.ext.asyncio import AsyncSession
import yadisk
from io import BytesIO
from services.utils.get_storage_token import get_storage_token_ydisk

from schemes.upload_scheme import UploadQuery

async def upload_file(upload_scheme: UploadQuery,
                      db: AsyncSession, 
                      file: UploadFile):
    print(f"{upload_scheme.path}{file.filename}")

    token = await get_storage_token_ydisk(token=upload_scheme.user_settings.access_token,
                                          storage_name=upload_scheme.user_settings.storage_name,
                                          db=db)

    y = yadisk.AsyncClient(token=token)

    # Асинхронно читаем файл как байты
    file_bytes = await file.read()

    byte_stream = BytesIO(file_bytes)
    
    await y.upload(byte_stream, f"{upload_scheme.path}{file.filename}")


