# FastAPI Feature-Based Application

This project is a FastAPI application built with a feature-based architecture and a pragmatic Clean Architecture approach.

## Documentation

- [Architecture Overview](docs/architecture.md)
- [Setup & Installation](docs/setup.md)

## Features

- **Users**: Register, list, upload avatar (S3/Minio).
- **Auth**: JWT Login, Logout (Redis blacklist).
- **Blog**: Create and list posts.
- **Comments**: Comment on posts.

## Quick Start

### Docker (Recommended)

```bash
cp .env.example .env
docker-compose up -d --build
```

Visit `http://localhost:8000/docs`.

### Local Development

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```
