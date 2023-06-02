from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import MetaData, String, Integer, Date
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base, metadata


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "app_user"

    metadata = metadata

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    salary: Mapped[int] = mapped_column(Integer, nullable=False)
    date_salary_increase: Mapped[datetime.date] = mapped_column(Date)

