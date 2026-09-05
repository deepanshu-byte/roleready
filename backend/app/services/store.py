from pydantic import BaseModel, Field

from app.schemas.applications import ApplicationDraft
from app.schemas.jobs import JobOpportunity
from app.schemas.profile import UserProfile


class InMemoryStore(BaseModel):
    profile: UserProfile = Field(default_factory=UserProfile)
    jobs: list[JobOpportunity] = Field(default_factory=list)
    applications: list[ApplicationDraft] = Field(default_factory=list)


store = InMemoryStore()

