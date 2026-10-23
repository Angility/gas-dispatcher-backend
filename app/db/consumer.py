from app.db.models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .equipment import Equipment
    from .contract import Contract

class Consumer(Base):
    __tablename__ = "consumer"
    __table_args__ = {"comment": "Потребитель газа"}

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(40))
    ais_code: Mapped[str] = mapped_column(String(12), comment="АИС.Код")
    ais_deleted: Mapped[bool] = mapped_column(Boolean, default=False, comment="АИС.Пометка удаления")

    equipments: Mapped[list["Equipment"]] = relationship(back_populates="consumer")
    contracts: Mapped[list["Contract"]] = relationship(back_populates="contract")  