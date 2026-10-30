from app.db.models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, ForeignKey, UniqueConstraint
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .grs import GRS
    from .equipment import Equipment

class Gate(Base):
    __tablename__ = "gate"
    __table_args__ = (UniqueConstraint("ais_code"), {"comment": "Выход ГРС"})

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
   
    ais_code: Mapped[str] = mapped_column(String(12), comment="АИС.Код")
    ais_del: Mapped[bool] = mapped_column(Boolean, default=False, comment="АИС.Пометка удаления")

    id_grs: Mapped[int] = mapped_column(ForeignKey("grs.id"), comment="Ссылка на ГРС")

    equipments: Mapped[list["Equipment"]] = relationship(back_populates="gate")
    grs: Mapped["GRS"] = relationship(back_populates="gates")
   