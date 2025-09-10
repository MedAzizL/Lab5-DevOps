FROM python:3.10-slim

WORKDIR /app

# Install system dependencies for Postgres client
RUN apt-get update && apt-get install -y build-essential libpq-dev postgresql-client && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code and manage.py
COPY app/ ./app
COPY manage.py .

# Expose Flask port
EXPOSE 5000

CMD ["sh", "-c", "\
    echo 'Waiting for Postgres...' && \
    while ! pg_isready -h db -p 5432; do sleep 1; done && \
    echo 'Checking migrations...' && \
    if [ ! -d migrations ]; then \
        echo 'Initializing migrations...' && \
        flask db init && \
        flask db migrate -m 'initial migration'; \
    fi && \
    echo 'Upgrading database...' && \
    flask db upgrade && \
    echo 'Starting Flask server...' && \
    python manage.py runserver --host 0.0.0.0 --port 5000 \
"]