from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from typing import Annotated

from config import (DB_HOST, 
                    DB_NAME, 
                    DB_PASS, 
                    DB_PORT, 
                    DB_USER)


URL_DATABASE = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# Создаем асинхронный движок
engine = create_async_engine(URL_DATABASE, echo=True)

# Создаем асинхронную фабрику сессий
AsyncSessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)

Base = declarative_base()

# Dependency для получения асинхронной сессии
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

db_dependency = Annotated[AsyncSession, Depends(get_db)]

# Асинхронная инициализация базы данных
async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
