from app.db.models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, UniqueConstraint
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User

class Role(Base):
    __tablename__ = "role"
    __table_args__ = (UniqueConstraint("name"), {"comment": "Роли пользователей"})

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(1000))

    users: Mapped[list["User"]] = relationship(back_populates="role")