from app.db.models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, UniqueConstraint
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .equipment import Equipment
    from .contract import Contract

class Consumer(Base):
    __tablename__ = "consumer"
    __table_args__ = (UniqueConstraint("ais_code"), {"comment": "Потребитель газа"})

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))   
   
    ais_del: Mapped[bool] = mapped_column(Boolean, default=False, comment="АИС.Пометка удаления")
    ais_code: Mapped[str] = mapped_column(String(12), comment="АИС.Код")

    equipments: Mapped[list["Equipment"]] = relationship(back_populates="consumer")
    contracts: Mapped[list["Contract"]] = relationship(back_populates="consumer")  