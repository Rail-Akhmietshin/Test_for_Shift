from faker import Faker
import datetime
from random import randint as random_number


def get_user():
    faker = Faker()
    return {
        "email": faker.email(),
        "password": "string",
        "is_active": bool(random_number(0, 1)),
        "is_superuser": bool(random_number(0, 1)),
        "is_verified": bool(random_number(0, 1)),
        "salary": random_number(0, 1000000),
        "date_salary_increase": datetime.datetime.now().date().strftime("%Y-%m-%d")
    }

