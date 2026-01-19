# Architecture

The application follows a **feature-based architecture** combined with principles of **Clean Architecture**. This ensures scalability, maintainability, and clear separation of concerns.

## Directory Structure

The project is organized by features at the root level. Each feature (domain) is self-contained.

```
.
├── auth/           # Authentication feature
├── blog/           # Blog posts feature
├── comments/       # Comments feature
├── config/         # Global configuration and core utilities
├── users/          # Users management feature
├── main.py         # Application entry point
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## Feature Structure

Each feature folder (e.g., `users/`) typically contains:

- `routes.py`: Defines the API endpoints (Controllers). Responsible for parsing requests and calling services.
- `services.py`: Contains business logic (Use Cases). Handles data processing and interacts with the database/ORM.
- `schemas.py`: Pydantic models (DTOs) for data validation and serialization.
- `models.py`: SQLAlchemy ORM models (Entities) representing database tables.
- `tests/`: Unit and integration tests for the feature.

## Core/Config Layer

The `config/` directory contains shared infrastructure code:

- `settings.py`: Application configuration using Pydantic Settings.
- `database.py`: Database connection setup (SQLAlchemy).
- `dependencies.py`: FastAPI dependency injection providers (e.g., current user, db session).
- `security.py`: Security utilities (hashing, JWT).
- `redis_client.py`: Redis client configuration.
- `storage.py`: S3/Minio client configuration.

## External Services

The application integrates with:

- **PostgreSQL**: Primary relational database.
- **Redis**: Used for token blacklisting (logout) and potentially caching.
- **Minio (S3)**: Object storage for file uploads (e.g., user avatars).

## Data Flow

Request -> `routes.py` -> `services.py` -> `models.py`/`database` -> Response
