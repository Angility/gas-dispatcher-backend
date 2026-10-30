from app.db.models import Base
from decimal import Decimal
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Numeric, UniqueConstraint, ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .supply import Supply
    from .contract import Contract

class AllocatedSupply(Base):
    __tablename__ = "allocated_supply"
    __table_args__ = (
        UniqueConstraint("id_supply","id_contract",name="uq_supply_contract"),
        {"comment": "Распределение поставок по договорам (связка Many-to-Many)"}
    )

    id: Mapped[int] = mapped_column(primary_key=True, comment="Суррогатный ключ")
    allocation_ratio: Mapped[Decimal] = mapped_column(Numeric(precision=12, scale=3), comment="Пропорция распределения (0.000 - 1.000)")

    id_supply : Mapped[int] = mapped_column(ForeignKey("supply.id"), comment="Ссылка на Поставку")
    id_contract : Mapped[int] = mapped_column(ForeignKey("contract.id"), comment="Ссылка на Договор")

    supply: Mapped["Supply"] = relationship(back_populates="allocated_supply")
    contract: Mapped["Contract"] = relationship(back_populates="allocated_supply")