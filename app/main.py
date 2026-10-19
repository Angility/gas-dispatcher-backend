from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db

# Инициализируем наше веб-приложение
app = FastAPI(title="Gas Dispatcher Backend")


@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check(db: AsyncSession = Depends(get_db)):
    """Асинхронный эндпоинт для проверки здоровья бэкенда и связи с PostgreSQL"""
    try:
        # Отправляем в базу легкий асинхронный запрос "SELECT 1"
        # Ключевое слово await обязательно при работе с сетью!
        await db.execute(text("SELECT 1"))
        
        # Если база ответила, возвращаем успешный статус
        return {"status": "ok", "db": "connected"}
        
    except Exception as e:
        # Если контейнер Postgres упал, сеть моргнула или пароль не подошел — 
        # перехватываем ошибку и выбрасываем строгий HTTP-статус 500
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "status": "error",
                "db": "disconnected",
                "message": str(e)
            }
        )
