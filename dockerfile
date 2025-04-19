FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN python get-pip.py

RUN pip install --no-cache-dir -r requirements.txt
ENV PYTHONPATH=/app


CMD ["python", "run.py"]

