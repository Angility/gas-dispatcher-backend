# scripts/seed_db.py
import asyncio
from datetime import date, timedelta
from decimal import Decimal

from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import async_session_factory
from app.db import (
    Role, User, GRS, Gate, Consumer, Equipment,
    Contract, ContractPriority, AllocatedPlan, DailyLedger
)


async def seed_database():
    """Заполняет БД тестовыми данными."""
    print("🌱 Начинаем заполнение БД тестовыми данными...")
    
    async with async_session_factory() as session:
        # 1. Создаем роль и пользователя
        role = Role(name="admin", description="Администратор системы")
        session.add(role)
        await session.flush()  # Получаем ID роли
        
        user = User(
            name="Тестовый Диспетчер",
            login="dispatcher",
            email="test@example.com",
            password_hash="fake_hash_for_seed",
            salt="fake_salt",
            id_role=role.id
        )
        session.add(user)
        
        # 2. Создаем ГРС и выход
        grs = GRS(name="ГРС Северная", ais_code="GRS001")
        session.add(grs)
        await session.flush()
        
        gate = Gate(name="Выход №1", ais_code="GATE001", id_grs=grs.id)
        session.add(gate)
        await session.flush()
        
        # 3. Создаем потребителя
        consumer = Consumer(name="ООО ТестГаз", ais_code="CONS001")
        session.add(consumer)
        await session.flush()
        
        # 4. Создаем оборудование
        equipment = Equipment(
            name="Узел учета №1", 
            ais_code="EQ001", 
            id_gate=gate.id, 
            id_consumer=consumer.id
        )
        session.add(equipment)
        await session.flush()
        
        # 5. Создаем два договора для этого потребителя
        contract_primary = Contract(name="ДОГ-2026-001", ais_code="CTR001", id_consumer=consumer.id)
        contract_secondary = Contract(name="ДОГ-2026-002", ais_code="CTR002", id_consumer=consumer.id)
        session.add_all([contract_primary, contract_secondary])
        await session.flush()
        
        # 6. Настраиваем приоритеты договоров для оборудования
        priority1 = ContractPriority(
            id_equipment=equipment.id, 
            id_contract=contract_primary.id, 
            is_primary=True, 
            priority=0
        )
        priority2 = ContractPriority(
            id_equipment=equipment.id, 
            id_contract=contract_secondary.id, 
            is_primary=False, 
            priority=1
        )
        session.add_all([priority1, priority2])
        
        # 7. Создаем планы на 5 дней
        today = date.today()
        for i in range(5):
            day = today + timedelta(days=i)
            
            plan_main = AllocatedPlan(
                period=day,
                id_equipment=equipment.id,
                id_contract=contract_primary.id,
                planned_volume=Decimal("100.000")
            )

            if i == 0:
                main_plan_today = plan_main


            plan_sec = AllocatedPlan(
                period=day,
                id_equipment=equipment.id,
                id_contract=contract_secondary.id,
                planned_volume=Decimal("50.000")
            )
            session.add_all([plan_main, plan_sec])

        await session.flush() 
        
        # 8. Вносим факт за сегодня (для проверки распределения)
        ledger_entry = DailyLedger(
            id_allocated_plan=main_plan_today.id,
            actual_volume=Decimal("120.000")
        )
        session.add(ledger_entry)
        
        # Сохраняем всё
        await session.commit()
        print("✅ База данных успешно заполнена!")
        print(f"   - ГРС: {grs.name}")
        print(f"   - Оборудование: {equipment.name}")
        print(f"   - Договоров: 2 (Основной + Дополнительный)")
        print(f"   - Планов создано: 10 (на 5 дней)")
        print(f"   - Факт внесен за: {today}")


if __name__ == "__main__":
    try:
        asyncio.run(seed_database())
    except Exception as e:
        print(f"❌ Ошибка при заполнении БД: {e}")
        import traceback
        traceback.print_exc()