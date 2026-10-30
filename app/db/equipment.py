from app.db.models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Boolean, UniqueConstraint
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .contract_priority import ContractPriority
    from .allocated_plan import AllocatedPlan
    from .gate import Gate
    from .consumer import Consumer


class Equipment(Base):
    __tablename__ = "equipment"
    __table_args__ = (UniqueConstraint("ais_code"), {"comment": "Объект СТМ (Оборудование)"})

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))

    ais_code: Mapped[str] = mapped_column(String(12), comment="АИС.Код")
    ais_del: Mapped[bool] = mapped_column(Boolean, default=False, comment="АИС.Пометка удаления")

    id_gate: Mapped[int] = mapped_column(ForeignKey("gate.id"), comment="Ссылка на Выход ГРС")
    id_consumer: Mapped[int] = mapped_column(ForeignKey("consumer.id"), comment="Ссылка на потребителя")

    allocated_plans: Mapped[list["AllocatedPlan"]] = relationship(back_populates="equipment")
    contract_priorities: Mapped[list["ContractPriority"]] = relationship(back_populates="equipment")
    gate: Mapped["Gate"] = relationship(back_populates="equipments")
    consumer: Mapped["Consumer"] = relationship(back_populates="equipments")
