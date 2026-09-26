FROM python:3.12-slim

WORKDIR /app

# Install PostgreSQL driver
RUN pip install --no-cache-dir psycopg2-binary

COPY app.py .

CMD ["python", "app.py"]