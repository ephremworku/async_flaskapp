# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y nginx

# Copy the requirements file into the container
COPY ./app/requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

ENV CELERY_BROKER_URL redis://redis:6379/0
ENV CELERY_RESULT_BACKEND redis://redis:6379/0
ENV C_FORCE_ROOT true
# Copy the Flask application code into the container
COPY ./app .

# Expose the port that Uvicorn will listen on
EXPOSE 8000

# Run Uvicorn when the container launches
CMD ["uvicorn", "main:asgi_app", "--host", "0.0.0.0", "--port", "8000"]
