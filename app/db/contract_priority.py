from app.db.models import Base
from decimal import Decimal
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Boolean, UniqueConstraint, ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .contract import Contract
    from .equipment import Equipment


class ContractPriority(Base):
    __tablename__ = "contract_priority"
    __table_args__ = (
        UniqueConstraint("id_contract","id_equipment",name="uq_contract_equipment"),
        {"comment": "Порядок распределения объемов по договорам (связка Many-to-Many)"}
    )

    id: Mapped[int] = mapped_column(primary_key=True, comment="Суррогатный ключ")
    priority : Mapped[int] = mapped_column(Integer, comment="Приоритет распределения")
    is_primary : Mapped[bool] = mapped_column(Boolean, default=False, comment="Признак основного договора")

    id_contract : Mapped[int] = mapped_column(ForeignKey("contract.id"), comment="Ссылка на Договор")
    id_equipment : Mapped[int] = mapped_column(ForeignKey("equipment.id"), comment="Ссылка на Оборудование")
   
    contract: Mapped["Contract"] = relationship(back_populates="contract_priorities")
    equipment: Mapped["Equipment"] = relationship(back_populates="contract_priorities")