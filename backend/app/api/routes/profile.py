from fastapi import APIRouter

from app.schemas.profile import UserProfile
from app.services.store import store

router = APIRouter()


@router.get("", response_model=UserProfile)
def get_profile() -> UserProfile:
    return store.profile


@router.put("", response_model=UserProfile)
def update_profile(profile: UserProfile) -> UserProfile:
    store.profile = profile
    return store.profile

