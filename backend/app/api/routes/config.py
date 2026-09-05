from typing import Union

from fastapi import APIRouter

from app.core.config import get_settings

router = APIRouter()


@router.get("/config")
def read_config() -> dict[str, Union[bool, str]]:
    settings = get_settings()
    return {
        "environment": settings.environment,
        "openai_enabled": settings.openai_enabled,
        "google_oauth_configured": settings.google_oauth_configured,
    }
