"""Dependency injection for FastAPI routes."""

from typing import Generator

from app.core.config import get_settings


def get_settings_dependency():
    """Dependency to get application settings."""
    return get_settings()


# Example database dependency (for future use)
# def get_db() -> Generator:
#     """Get database session."""
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# Example authentication dependency (for future use)
# def get_current_user(token: str = Depends(oauth2_scheme)):
#     """Get current authenticated user."""
#     # Implementation here
#     pass