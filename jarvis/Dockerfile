FROM python:3.12-slim

# Prevent Python from creating .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Enable unbuffered Python output
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# System dependencies for PyAudio and audio support
RUN apt-get update && apt-get install -y \
    portaudio19-dev \
    python3-pyaudio \
    gcc \
    libasound2-dev \
    espeak \
    espeak-ng \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better Docker layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install  --default-timeout=100 --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Start assistant
CMD ["python", "main.py"]
