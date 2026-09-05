from fastapi import APIRouter

from app.schemas.jobs import DiscoveryRequest, JobOpportunity
from app.services.discovery import discover_jobs
from app.services.store import store

router = APIRouter()


@router.get("", response_model=list[JobOpportunity])
def list_jobs() -> list[JobOpportunity]:
    return store.jobs


@router.post("/discover", response_model=list[JobOpportunity])
def run_discovery(request: DiscoveryRequest) -> list[JobOpportunity]:
    jobs = discover_jobs(request)
    store.jobs = jobs
    return jobs

