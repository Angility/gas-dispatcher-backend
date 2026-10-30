from app.db.models import Base
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, ForeignKey, UniqueConstraint
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .daily_ledger import DailyLedger
    from .user import User

class Comment(Base):
    __tablename__ = "comment"
    __table_args__ = {"comment": "Комментарии пользователей"}

    id: Mapped[int] = mapped_column(primary_key=True, comment="Суррогатный ключ")
    timestamp: Mapped[datetime] = mapped_column(DateTime, server_default="now()", comment="Момент времени")
    text: Mapped[str] = mapped_column(String(300), comment="Текст")
    
    id_user: Mapped[int] = mapped_column(ForeignKey("user.id"), comment="Ссылка на Пользователя")
    id_daily_ledger: Mapped[int] = mapped_column(ForeignKey("daily_ledger.id"), comment="Ссылка на строку журнала")
 
    user: Mapped["User"] = relationship(back_populates="comments")
    daily_ledger: Mapped["DailyLedger"] = relationship(back_populates="comments")