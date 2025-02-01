from pydantic import BaseSettings

class Settings(BaseSettings):
    # CORS settings
    allow_origins: list[str] = ["*"]  # Update with your frontend URL in production
    allow_credentials: bool = True
    allow_methods: list[str] = ["*"]
    allow_headers: list[str] = ["*"]

    # Logging settings
    log_level: str = "INFO"

    class Config:
        env_file = ".env"

settings = Settings()
