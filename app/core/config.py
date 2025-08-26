"""Application configuration settings."""

import os
from functools import lru_cache
from typing import List

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Application settings."""
    
    # Project Information
    PROJECT_NAME: str = "Vibe Coding Extended API"
    DESCRIPTION: str = "Extended version of vibe-coding with FastAPI backend and good vibes! ✨"
    VERSION: str = "1.0.0"
    
    # Environment
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    DEBUG: bool = os.getenv("DEBUG", "true").lower() == "true"
    
    # API Configuration
    API_V1_STR: str = "/api/v1"
    
    # CORS
    ALLOWED_HOSTS: List[str] = [
        "http://localhost:3000",
        "http://localhost:8000",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:8000",
    ]
    
    # Database (for future use)
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./vibe_coding.db")
    
    # Security (for future use)
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # External APIs (for future use)
    EXTERNAL_API_KEY: str = os.getenv("EXTERNAL_API_KEY", "")
    
    class Config:
        """Pydantic config."""
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()