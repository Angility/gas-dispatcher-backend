from app.db.models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .contract import Contract

class ContractAllocation(Base):
    __tablename__ = "contract_allocation"
    __table_args__ = {"comment": "Детализация поставки"}

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(40))

    ais_code: Mapped[str] = mapped_column(String(12), comment="АИС.Код")
    ais_deleted: Mapped[bool] = mapped_column(Boolean, default=False, comment="АИС.Пометка удаления")

    contract : Mapped["Contract"] = relationship(back_pipulates="contract")