# 1. Python 3.10 image dan foydalanamiz
FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app/

RUN python manage.py migrate

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]