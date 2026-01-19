# Setup Guide

## Prerequisites

- Python 3.11+
- Docker & Docker Compose

## Environment Configuration

Copy the example environment file:

```bash
cp .env.example .env
```

Adjust the values in `.env` if necessary.

## Running Locally (SQLite)

For quick development without external dependencies (except Redis/Minio if you use those features, though the app will try to run without them if not available or configured), you can run the app directly.

**Note**: To use the full features (Redis blacklist, S3 upload), you need those services running. You can run just those services via docker:

```bash
docker-compose up -d redis minio
```

Then run the app:

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

The app will use SQLite (`sql_app.db`) by default when running locally.

## Running with Docker (PostgreSQL)

To run the full stack including PostgreSQL:

1. Build and start containers:
   ```bash
   docker-compose up -d --build
   ```

2. Access the application at `http://localhost:8000`.

3. API Documentation (Swagger UI) is available at `http://localhost:8000/docs`.

4. Adminer (Database UI) is available at `http://localhost:8080`.
   - System: PostgreSQL
   - Server: db
   - Username: postgres
   - Password: postgres
   - Database: app_db

5. Minio Console is available at `http://localhost:9001`.
   - User: minioadmin
   - Password: minioadmin
