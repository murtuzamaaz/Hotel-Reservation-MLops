FROM python:slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies required for pyarrow and other native builds
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    git \
    curl \
    libgomp1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .

# Upgrade pip and install project dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -e .

# Run your training pipeline
RUN python pipeline/training_pipeline.py

EXPOSE 5000

CMD ["python", "application.py"]
