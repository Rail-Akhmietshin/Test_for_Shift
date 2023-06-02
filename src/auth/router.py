
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from .base_config import current_user
from .models import User

router = APIRouter(
    prefix="/employee",
    tags=["Employee"]
)


@router.post("/money")
async def information_of_salary(user: User = Depends(current_user)) -> JSONResponse:
    return JSONResponse(content={
        user.email: {
            "My current salary": user.salary,
            "Date of salary increase": user.date_salary_increase.strftime("%d.%m.%Y")
        }
    })
