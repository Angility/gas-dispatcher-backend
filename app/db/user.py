from app.db.models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, ForeignKey, UniqueConstraint
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .role import Role
    from .comment import Comment

class User(Base):
    __tablename__ = "user"
    __table_args__ = {"comment": "Пользователи"}
  

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))   
    login: Mapped[str] = mapped_column(String(50), unique=True, comment="Логин")
    email: Mapped[str] = mapped_column(String(100), unique=True, comment="Электронная почта (для восстановления пароля)")
    password_hash: Mapped[str] = mapped_column(String(255), comment="Хеш пароля")
    salt: Mapped[str] = mapped_column(String(12), comment="Соль для хеша")
    is_blocked: Mapped[bool] = mapped_column(Boolean, default=False, comment="Пользователь заблокирован")

    id_role: Mapped[int] = mapped_column(ForeignKey("role.id"), comment="Ссылка на Роль")

    comments: Mapped[list["Comment"]] = relationship(back_populates="user")
    role: Mapped["Role"] = relationship(back_populates="users")
   