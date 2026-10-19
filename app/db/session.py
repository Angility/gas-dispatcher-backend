from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.core.config import settings

# 1. Создаем асинхронный движок (Пул соединений)
# Он управляет долгоживущими сетевыми кабелями до СУБД в Docker
async_engine = create_async_engine(
    settings.async_database_url,
    echo=settings.DB_ECHO,  # Включаем логирование SQL-запросов в консоль для дебага
)

# 2. Создаем фабрику асинхронных сессий
# expire_on_commit=False защищает нас от просрочки объектов в асинхронной среде
async_session_factory = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


# 3. Функция-зависимость (Dependency Injection) для FastAPI
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Асинхронный генератор сессий базы данных.
    Каждый HTTP-запрос получает из фабрики свою изолированную сессию.
    """
    async with async_session_factory() as session:
        try:
            yield session
        finally:
            # Гарантированно закрываем сессию и возвращаем кабель в пул движка
            await session.close()
