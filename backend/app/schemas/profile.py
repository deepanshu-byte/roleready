from typing import Optional

from pydantic import BaseModel, Field


class ProfileField(BaseModel):
    key: str
    label: str
    value: str = ""
    required: bool = False


class JobPlatform(BaseModel):
    name: str
    enabled: bool = True
    search_url: Optional[str] = None
    notes: str = ""


class TargetCompany(BaseModel):
    name: str
    priority: int = Field(default=3, ge=1, le=5)
    career_url: Optional[str] = None
    notes: str = ""


class UserProfile(BaseModel):
    full_name: str = "Deepanshu Pandey"
    email: str = "candidate@example.com"
    headline: str = "Product-minded software engineer"
    location: str = "Remote"
    profile_fields: list[ProfileField] = Field(
        default_factory=lambda: [
            ProfileField(key="years_experience", label="Years of experience", value="5"),
            ProfileField(key="core_stack", label="Core stack", value="Python, TypeScript, React"),
            ProfileField(key="work_authorization", label="Work authorization", value="Needs review"),
        ]
    )
    job_platforms: list[JobPlatform] = Field(
        default_factory=lambda: [
            JobPlatform(name="LinkedIn", search_url="https://www.linkedin.com/jobs/"),
            JobPlatform(name="Wellfound", search_url="https://wellfound.com/jobs"),
            JobPlatform(name="Company career pages", notes="Manual review-first discovery"),
        ]
    )
    target_companies: list[TargetCompany] = Field(
        default_factory=lambda: [
            TargetCompany(name="OpenAI", priority=5, career_url="https://openai.com/careers"),
            TargetCompany(name="Stripe", priority=4, career_url="https://stripe.com/jobs"),
            TargetCompany(name="Ramp", priority=4, career_url="https://ramp.com/careers"),
        ]
    )
