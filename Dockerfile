FROM python:3.13.7-slim

WORKDIR /app

COPY requirements-docker.txt .

RUN pip install --no-cache-dir -r requirements-docker.txt

COPY src ./src 

CMD ["python", "src/main.py"]



