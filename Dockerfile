FROM python:3.12-slim

# Prevent Python from writing pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=80

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir --timeout 120 --retries 5 -r requirements.txt

COPY . .

# Run as a non-root user
RUN useradd --create-home --shell /bin/bash appuser \
    && chown -R appuser:appuser /app
USER appuser

# CapRover routes traffic to the container's HTTP port (default 80)
EXPOSE 80

# Serve with gunicorn in production. Honors the PORT env var so CapRover
# (or any host) can override the listen port.
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${PORT} --workers 2 --timeout 60 run:app"]




