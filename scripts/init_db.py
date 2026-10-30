# scripts/init_db.py
import asyncio
import sys
from pathlib import Path

# Добавляем корень проекта в PYTHONPATH, чтобы импорты работали
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.db.session import async_engine
from app.db.models import Base


async def create_tables():
    """Создает все таблицы в базе данных."""
    print("🔌 Подключение к базе данных...")
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Все 13 таблиц успешно созданы!")


async def drop_tables():
    """⚠️ ОПАСНО: Удаляет все таблицы. Использовать только для сброса."""
    print("⚠️  УДАЛЕНИЕ ВСЕХ ТАБЛИЦ...")
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    print("🗑  Все таблицы удалены.")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--drop":
        asyncio.run(drop_tables())
    else:
        asyncio.run(create_tables())