from fastapi import APIRouter

from app.api.routes import applications, auth, config, jobs, profile

api_router = APIRouter()
api_router.include_router(config.router, tags=["config"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(profile.router, prefix="/profile", tags=["profile"])
api_router.include_router(jobs.router, prefix="/jobs", tags=["jobs"])
api_router.include_router(applications.router, prefix="/applications", tags=["applications"])

