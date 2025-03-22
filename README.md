# Blog API with FastAPI, SQLite, and JWT Authentication

This project is a robust REST API built using FastAPI, SQLite, and JWT authentication. It is containerized with Docker for seamless deployment and local development.

## Features
- User authentication using JWT (JSON Web Token)
- CRUD operations for blog posts
- SQLite as the database
- Docker support for containerized deployment

## Prerequisites
Ensure you have the following installed:
- [Python 3.10+](https://www.python.org/downloads/)
- [Docker](https://docs.docker.com/get-docker/)

## Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/your-repo/blog-fastapi.git
   cd blog-post-project
   ```

2. **Create a Virtual Environment** (optional but recommended)
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```sh
   pip3 install -r requirements.txt
   ```

## Running the API Locally

1. **Setup Database Connection**

2. **Run the FastAPI Server**
   ```sh
   uvicorn main:app --reload
   ```

The API will be available at `http://127.0.0.1:8000`.

## Running the API with Docker

1. **Build the Docker Image**
   ```sh
   docker build -t fastapi-blog .
   ```

2. **Run the Docker Container**
   ```sh
   docker run -dp 8000:8000 fastapi-blog
   ```

The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

### Authentication
- **Login:** `POST /login` - Authenticate a user and receive a JWT token.

### User Management
- **Create a user:** `POST /user` - Register a new user.
- **Get user by ID:** `GET /user/{id}` - Retrieve a user by ID.

### Blog Management
- **Create a blog:** `POST /blog/` - Create a new blog post.
- **Get all blogs:** `GET /blog/` - Retrieve all blog posts.
- **Get blog by ID:** `GET /blog/{id}` - Retrieve a blog post by ID.
- **Update a blog:** `PUT /blog/{id}` - Update a blog post.
- **Delete a blog:** `DELETE /blog/{id}` - Delete a blog post.

## Testing the API

### Using API Docs
FastAPI provides an interactive API documentation available at:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

To test the API, navigate to these URLs in your browser and use the interactive interface to send requests.

### Using Postman or curl
You can use [Postman](https://www.postman.com/) or `curl` to test the endpoints.

Example using `curl`:
```sh
curl -X POST "http://127.0.0.1:8000/login" -H "Content-Type: application/json" -d '{"username": "test", "password": "password"}'
```
### Future Enhancements
- Deploy to AWS using services like ECS, Lambda, or EC2
- Use PostgreSQL instead of SQLite for production
- Implement rate limiting and logging
---
Happy coding! 🚀


