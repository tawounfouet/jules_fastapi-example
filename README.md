# FastAPI Feature-Based Application

This project is a FastAPI application built with a feature-based architecture and a pragmatic Clean Architecture approach.

## Architecture

The application is organized by features (`users`, `auth`, `blog`, `comments`) at the root level:

- `routes.py`: FastAPI endpoints. Contains no business logic. Delegates to services.
- `services.py`: Business logic and database interactions. Handles ORM models.
- `schemas.py`: Pydantic models for request/response validation.
- `models.py`: SQLAlchemy ORM models.
- `tests/`: Feature-specific tests.

### Config Module

Common configuration and core utilities are located in `config/`:
- `settings.py`: Global application settings (environment variables).
- `database.py`: Database connection and session management.
- `security.py`: Authentication utilities (JWT, password hashing).
- `dependencies.py`: FastAPI dependencies (e.g., `get_db`, `get_current_user`).

## Tech Stack

- **FastAPI**: Web framework.
- **Pydantic v2**: Data validation.
- **SQLAlchemy 2.0**: ORM.
- **SQLite**: Database.
- **JWT**: Authentication.
- **Docker**: Containerization.

## Installation

### Local

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

3. Run tests:
   ```bash
   pytest
   ```

### Docker

1. Build the image:
   ```bash
   docker build -t fastapi-app .
   ```

2. Run the container:
   ```bash
   docker run -d -p 8000:8000 fastapi-app
   ```
