from app.db.models import Base
from decimal import Decimal
from datetime import date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Numeric, UniqueConstraint, Date, ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .equipment import Equipment
    from .contract import Contract
    from .daily_ledger import DailyLedger

class AllocatedPlan(Base):
    __tablename__ = "allocated_plan"
    __table_args__ = (
        UniqueConstraint("id_equipment","id_contract","period",name="uq_equipment_contract_period"),
        {"comment": "Плановый объем потребления газа за период (связка Many-to-Many)"}
    )

    id: Mapped[int] = mapped_column(primary_key=True, comment="Суррогатный ключ")
    period: Mapped[date] = mapped_column(Date, comment="Сутки")
    planned_volume: Mapped[Decimal] = mapped_column(Numeric(precision=12, scale=3), comment="Плановый объем")

    id_equipment : Mapped[int] = mapped_column(ForeignKey("equipment.id"), comment="Ссылка на Оборудование")
    id_contract : Mapped[int] = mapped_column(ForeignKey("contract.id"), comment="Ссылка на Договор")

    equipment: Mapped["Equipment"] = relationship(back_populates="allocated_plans")
    contract: Mapped["Contract"] = relationship(back_populates="allocated_plans")
    daily_ledger: Mapped["DailyLedger"] = relationship(back_populates="allocated_plan")