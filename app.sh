#!/bin/bash

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  echo "Waiting for postgres..."
  sleep 1;
done

echo "PostgreSQL started"

alembic upgrade head

gunicorn src.main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000