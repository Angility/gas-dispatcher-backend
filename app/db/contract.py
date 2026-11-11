from app.db.models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, ForeignKey, UniqueConstraint
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .consumer import Consumer
    from .allocated_supply import AllocatedSupply
    from .contract_priority import ContractPriority
    from .allocated_plan import AllocatedPlan


class Contract(Base):
    __tablename__ = "contract"
    __table_args__ = (UniqueConstraint("ais_code"), {"comment": "Договор поставки газа"})

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
   
    ais_code: Mapped[str] = mapped_column(String(12), comment="АИС.Код")
    ais_del: Mapped[bool] = mapped_column(Boolean, default=False, comment="АИС.Пометка удаления")
    
    id_consumer: Mapped[int] = mapped_column(ForeignKey("consumer.id"),comment="Ссылка на потребителя")

    allocated_supply : Mapped[list["AllocatedSupply"]] = relationship(back_populates="contract")
    contract_priorities : Mapped[list["ContractPriority"]] = relationship(back_populates="contract")
    consumer : Mapped["Consumer"] = relationship(back_populates="contracts")
    allocated_plans: Mapped[list["AllocatedPlan"]] = relationship(back_populates="contract")