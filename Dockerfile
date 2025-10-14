# Dockerfile (Corrected)
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# System dependencies... (no changes here)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential cmake git curl libgomp1 && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY . .

# Python dependencies... (no changes here)
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -e .

# Securely run the script with credentials
RUN --mount=type=secret,id=gcp-credentials \
    export GOOGLE_APPLICATION_CREDENTIALS=/run/secrets/gcp-credentials && \
    python pipeline/training_pipeline.py

EXPOSE 5000

CMD ["python", "application.py"]