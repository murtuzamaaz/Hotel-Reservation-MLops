FROM python:slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONNUNBUFFERED=1


WORKDIR /APP

RUN apt-get update && apt-get-install -y --no-install-recommends \
    libgomp \
    && apt-get-clean \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install -no-cache-dir -e .

RUN python pipeline/training_pipeline.py

EXPOSE 5000

COPY . .

CMD [ "python" , "application.py"]
