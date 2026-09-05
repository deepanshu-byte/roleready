from pydantic import BaseModel, Field


class DiscoveryRequest(BaseModel):
    keywords: list[str] = Field(default_factory=lambda: ["software engineer", "full stack"])
    locations: list[str] = Field(default_factory=lambda: ["Remote", "United States"])
    seniority: str = "Mid-Senior"
    include_target_companies: bool = True


class JobOpportunity(BaseModel):
    id: str
    title: str
    company: str
    platform: str
    location: str
    url: str
    match_score: int = Field(ge=0, le=100)
    status: str = "new"
    rationale: str

