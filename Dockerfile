FROM python:3.8.1-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY tabulate-form.py tabulate-form.py

ENTRYPOINT ["python3", "tabulate-form.py"]

