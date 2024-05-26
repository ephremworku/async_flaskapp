# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /celery_worker

# Install system dependencies
RUN apt-get update && apt-get install -y redis-server

ENV CELERY_BROKER_URL redis://redis:6379/0
ENV CELERY_RESULT_BACKEND redis://redis:6379/0

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Celery worker code into the container
COPY . .

# Run the Celery worker when the container launches
CMD ["celery", "-A", "worker.tasks", "worker", "--loglevel=info"]
