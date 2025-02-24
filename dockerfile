FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app/

RUN python manage.py migrate

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]