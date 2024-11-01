from fastapi import (UploadFile)
import yadisk
from io import BytesIO
from services.utils.aio_requests.get import get

async def upload_file(path: str, file: UploadFile):
    print(file.filename)
    y = yadisk.AsyncClient(token="y0_AgAAAAA2bkLJAAyZhgAAAAEUUNqgAABEIQCFPARHka_SA_Yc4rWJuWVhpQ")

    # Асинхронно читаем файл как байты
    file_bytes = await file.read()

    byte_stream = BytesIO(file_bytes)
    
    await y.upload(byte_stream, f"{path}{file.filename}")


