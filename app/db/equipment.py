from app.db.models import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey, Boolean

class Equipment(Base):
    __tablename__ = "equipment"   
    __table_args__ = {"comment": "Объект СТМ (Оборудование)"}

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(40))
    gate: Mapped[str] = mapped_column(String(20))
   
    id_grs: Mapped[int] = mapped_column(ForeignKey("grs.id"), comment="Ссылка на ГРС")
    id_consumer: Mapped[int] = mapped_column(ForeignKey("consumer.id"), comment="Ссылка на потребителя")
    
    ais_code: Mapped[str] = mapped_column(String(12), comment="АИС.Код")
    ais_deleted: Mapped[bool] = mapped_column(Boolean, default=False, comment="АИС.Пометка_удаления")
 