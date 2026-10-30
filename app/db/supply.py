from app.db.models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, UniqueConstraint
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .allocated_supply import AllocatedSupply

class Supply(Base):
    __tablename__ = "supply"
    __table_args__ = (UniqueConstraint("ais_code"), {"comment": "Поставка"})

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(40))

    ais_del: Mapped[bool] = mapped_column(Boolean, default=False, comment="АИС.Пометка удаления")
    ais_code: Mapped[str] = mapped_column(String(12), comment="АИС.Код")

    allocated_supply : Mapped[list["AllocatedSupply"]] = relationship(back_populates="supply")