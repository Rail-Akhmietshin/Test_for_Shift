from datetime import datetime, timedelta
import datetime as head_datetime
from typing import Optional

from fastapi_users import schemas, models
from pydantic import EmailStr


class UserRead(schemas.BaseUser[int]):
    id: models.ID
    email: EmailStr
    salary: int
    date_salary_increase: Optional[head_datetime.date]
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    email: EmailStr
    password: str
    salary: int
    date_salary_increase: Optional[head_datetime.date] = datetime.now().date() + timedelta(days=6)
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserUpdate(schemas.BaseUserUpdate):
    password: Optional[str]
    email: Optional[EmailStr]
    salary: Optional[int]
    date_salary_increase: Optional[head_datetime.date] = datetime.now().date() + timedelta(days=6)
    is_active: Optional[bool]
    is_superuser: Optional[bool]
    is_verified: Optional[bool]
