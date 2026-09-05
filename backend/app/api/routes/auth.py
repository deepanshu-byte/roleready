from typing import Optional, Union

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from app.core.config import get_settings

router = APIRouter()


class LocalLoginRequest(BaseModel):
    username: str
    password: str


@router.post("/local/login")
def local_login(payload: LocalLoginRequest) -> dict[str, str]:
    settings = get_settings()
    if not settings.development_auth_username or not settings.development_auth_password:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Local development credentials are not configured.",
        )

    if (
        payload.username != settings.development_auth_username
        or payload.password != settings.development_auth_password
    ):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials.")

    return {"status": "ok", "mode": "development", "username": payload.username}


@router.get("/google/config")
def google_config() -> dict[str, Union[bool, Optional[str]]]:
    settings = get_settings()
    return {
        "configured": settings.google_oauth_configured,
        "client_id": settings.google_client_id,
        "redirect_uri": settings.google_redirect_uri,
    }
