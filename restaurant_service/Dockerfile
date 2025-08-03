FROM python:3.9-slim
WORKDIR /app

# Install build dependencies for psycopg2
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy shared module first (from root context)
COPY shared/ /app/shared/

# Copy and install service requirements
COPY restaurant_service/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy service code
COPY restaurant_service/app/ /app/app/

EXPOSE 8002
CMD ["sh", "-c", "python -m uvicorn app.main:app --host 0.0.0.0 --port $PORT"]