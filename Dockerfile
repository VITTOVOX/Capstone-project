# Use a small Python base
FROM python:3.11-slim

# Prevent Python from writing .pyc files and buffering stdout
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# OS deps (build tools + libpq if you ever use Postgres later)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl netcat-traditional \
 && rm -rf /var/lib/apt/lists/*

# Create app folder
WORKDIR /app

# Install Python deps early to use Docker layer cache
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project
COPY . /app

# If your settings use env vars, you can set sensible defaults here
ENV DJANGO_SETTINGS_MODULE=mySite.settings \
    DJANGO_DEBUG=False \
    DJANGO_ALLOWED_HOSTS="*"

# Make our entrypoint executable
RUN chmod +x /app/entrypoint.sh

# Expose Django dev port
EXPOSE 8000

# Start via entrypoint (migrate then runserver). Swap to gunicorn later if you like.
ENTRYPOINT ["/app/entrypoint.sh"]