FROM python:3.11

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && apt-get install -y netcat alembic gunicorn
RUN curl -sSL https://install.python-poetry.org | python3 -

RUN mkdir /Shift

WORKDIR /Shift

COPY pyproject.toml .
COPY poetry.lock .

RUN pip3 install poetry

RUN poetry config virtualenvs.create false \
  && poetry install --no-dev --no-interaction --no-ansi

COPY . /Shift

ENV PYTHONPATH=/Shift

RUN chmod a+x *.sh

ENTRYPOINT ["/Shift/app.sh"]