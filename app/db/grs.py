from app.db.models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, UniqueConstraint
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .gate import Gate

class GRS(Base):
    __tablename__ = "grs"
    __table_args__ = (UniqueConstraint("ais_code"), {"comment": "Газораспределительная станция"})

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))

    ais_del: Mapped[bool] = mapped_column(Boolean, default=False, comment="АИС.Пометка удаления")
    ais_code: Mapped[str] = mapped_column(String(12), comment="АИС.Код")

    gates: Mapped[list["Gate"]] = relationship(back_populates="grs")