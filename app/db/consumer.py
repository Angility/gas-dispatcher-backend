from app.db.models import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean

class Consumer(Base):
    __tablename__ = "consumer"
    __table_args__ = {"comment": "Потребитель"}

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(40))
    ais_code: Mapped[str] = mapped_column(String(12), comment="АИС.Код")
    ais_deleted: Mapped[bool] = mapped_column(Boolean, default=False, comment="АИС.Пометка_удаления")
