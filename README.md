# FastAPI Feature-Based Application

This project is a FastAPI application built with a feature-based architecture and a pragmatic Clean Architecture approach.

## Architecture

The application is organized by features (`users`, `auth`, `blog`, `comments`) rather than by technical layers. Each feature is self-contained and follows this structure:

- `routes.py`: FastAPI endpoints. Contains no business logic. Delegates to services.
- `services.py`: Business logic and database interactions. Handles ORM models.
- `schemas.py`: Pydantic models for request/response validation.
- `models.py`: SQLAlchemy ORM models.
- `tests/`: Feature-specific tests.

### Core Module

Common functionality is located in `app/core/`:
- `config.py`: Environment configuration.
- `database.py`: Database connection and session management.
- `security.py`: Authentication utilities (JWT, password hashing).
- `dependencies.py`: FastAPI dependencies (e.g., `get_db`, `get_current_user`).

## Tech Stack

- **FastAPI**: Web framework.
- **Pydantic v2**: Data validation.
- **SQLAlchemy 2.0**: ORM (using modern `Mapped` syntax).
- **SQLite**: Database.
- **JWT**: Authentication.

## Installation

1. Install dependencies:
   ```bash
   pip install fastapi uvicorn sqlalchemy pydantic-settings python-jose[cryptography] passlib[bcrypt] python-multipart bcrypt==4.0.1 email-validator
   ```

2. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

3. Run tests:
   ```bash
   pytest
   ```
