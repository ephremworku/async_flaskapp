# Flask Application with Celery Worker

This repository contains a Flask application for handling asynchronous tasks using Celery and Redis. The application is structured using clean architecture principles for better organization and maintainability.

## Project Structure

The project is organized into two main directories:

- **flask_app**: Contains the Flask application code.
- **celery_worker**: Contains the Celery worker code.

### Flask Application (`flask_app`)

The Flask application follows a clean architecture approach:

- **app/controllers**: Contains route handlers for the Flask application.
- **app/entities**: Contains domain entities or models.
- **app/templates**: Contains HTML templates for rendering views (if applicable).
- **app/usecases**: Contains business logic or use cases.
- **app/__init__.py**: Initializes the Flask application.
- **app/initialize.py**: Contains initialization logic.
- **app/main.py**: Entry point for the Flask application.

### Celery Worker (`celery_worker`)

The Celery worker code also follows a clean architecture:

- **worker/entities**: Contains entities or models specific to Celery tasks.
- **worker/repositories**: Contains database access or external service interaction logic.
- **worker/usecases**: Contains business logic or use cases specific to Celery tasks.
- **worker/__init__.py**: Initializes the Celery worker.
- **worker/initialize.py**: Contains initialization logic.
- **worker/tasks.py**: Contains Celery task definitions.

## Running the Applications

### Flask Application

To run the Flask application, use the following command:

```sh  
uvicorn main:asgi_app --host 0.0.0.0 --port 8000
```
This command starts the Flask application, making it accessible on port 8000.

## Celery Worker

To run the Celery worker, use the following command:

```sh  
celery -A worker.tasks worker --loglevel=info
```
## Dependencies

The project requires the following dependencies:

- Python 3.x
- Flask
- Celery
- Redis

## Getting Started

To get started with the project, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Configure any environment variables required for your setup.
4. Run the Flask application and Celery worker as described above.
 ## To Run the application using docker Container
 after clonning the repository and going to the directory of assync_flaskapp
 ```sh  
 sudo docker-compose up -d
 ```
 and the application will start up and running and at:
 ```sh  
 http://localhost/
 ```
 you will see the form to fill out and submit