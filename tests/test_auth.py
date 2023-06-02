from httpx import AsyncClient

import urllib.parse

from tests.generators.user_builder import get_user

user = get_user()


async def test_register(ac: AsyncClient):
    response = await ac.post("/auth/register", json=user)
    assert response.status_code == 201


async def test_get_info_of_user(ac: AsyncClient):
    user_params = urllib.parse.urlencode({
        "username": user["email"],
        "password": user["password"],
    })
    login_response = await ac.post(
        url="/auth/jwt/login",
        content=user_params,
        headers={
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    )
    assert login_response.status_code == 204, "Incorrect user login or password"

    info_of_salary = await ac.post("/employee/money", cookies=dict(login_response.cookies))
    assert user["email"] in info_of_salary.json().keys(), "Incorrect user information"
