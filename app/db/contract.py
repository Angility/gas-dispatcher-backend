from app.db.models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .consumer import Consumer
    from .contract_allocation import ContractAllocation

class Contract(Base):
    __tablename__ = "contract"
    __table_args__ = {"comment": "Договор поставки газа"}

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(40))

    ais_code: Mapped[str] = mapped_column(String(12), comment="АИС.Код")
    ais_deleted: Mapped[bool] = mapped_column(Boolean, default=False, comment="АИС.Пометка удаления")

    consumer : Mapped["Consumer"] = relationship(back_pipulates="consumer")
    contract_allocation : Mapped[list["ContractAllocation"]] = relationship(back_pipulates="contract_allocation")