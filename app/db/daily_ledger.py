from app.db.models import Base
from datetime import date
from decimal import Decimal
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Numeric, ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .allocated_plan import AllocatedPlan
    from .comment import Comment
    
class DailyLedger(Base):
    __tablename__ = "daily_ledger"
    __table_args__ = {"comment": "Суточное потребление"}

    id: Mapped[int] = mapped_column(primary_key=True)
    actual_volume: Mapped[Decimal] = mapped_column(Numeric(precision=12, scale=3), nullable=True, comment="Фактический объем")
    
    id_allocated_plan: Mapped[int] = mapped_column(ForeignKey("allocated_plan.id"), unique=True, comment="Ссылка на Плановый объем")
   
    allocated_plan: Mapped["AllocatedPlan"] = relationship(back_populates="daily_ledger")
    comments: Mapped[list["Comment"]] = relationship(back_populates="daily_ledger")

    