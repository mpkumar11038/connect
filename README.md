# Connect - Django REST Framework Social Networking API

This project, Connect, provides a social networking API built with Django REST Framework. It allows users to search for other users, send/manage friend requests, and view their friend list. The project is containerized using Docker for easy deployment.

## Features
- User signup with email (no verification required).
- User login with email and password (case-insensitive).
- Search for users by email or name (paginated results).
- Send friend requests to other users.
- Accept/reject friend requests.
- View list of friends and pending friend requests.
- Rate limiting for sending friend requests (max 3 per minute).

## Prerequisites
   
- Docker installed: https://www.docker.com/

## Setting Up

- Clone the repository:
   
   ```bash
   git clone https://<your_repository_url>
   ```

- Navigate to the project directory:
   ```bash
   cd connect

- Build Docker images:
   ```bash
   docker-compose build
   ```

- Run the development environment:
   ```bash
   docker-compose up -d
   ```

This will start the Django application and database service in Docker containers.

## Using the API
By default, the API will be accessible at http://localhost:8000/ in your browser. You'll need to use tools like Postman
or curl to interact with the API endpoints.

## Authentication:

The API requires authentication for most functionalities. Use the login endpoint to obtain a JWT token for subsequent requests.

Refer to the Postman collection (provided in a separate file) for detailed API endpoint examples.
