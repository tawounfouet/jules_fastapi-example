from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Feature Based"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "changethis"  # Should be changed in production
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DATABASE_URL: str = "sqlite:///./sql_app.db"

    model_config = SettingsConfigDict(case_sensitive=True)

settings = Settings()
