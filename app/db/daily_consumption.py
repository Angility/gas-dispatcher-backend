from app.db.models import Base
from datetime import date
from decimal import Decimal
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, Numeric, Date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .contract import Contract
    from .equipment import Equipment

class DailyConsumption(Base):
    __tablename__ = "contract_allocation"
    __table_args__ = {"comment": "Детализация поставки"}

    id: Mapped[int] = mapped_column(primary_key=True)
    consumption_date: Mapped[date] = mapped_column(Date, comment="Сутки")
    
    planned_volume: Mapped[Decimal] = mapped_column(Numeric(precision=12, scale=3), comment="Плановый объем")
    actual_volume: Mapped[Decimal] = mapped_column(Numeric(precision=12, scale=3), comment="Фактический объем")

    equipments: Mapped[list["Equipment"]] = relationship(back_populates="equipment")
#    contract : Mapped[list["Contract"]] = relationship(back_pipulates="contract")