from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(String(255))