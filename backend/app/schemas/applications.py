from enum import Enum
from typing import Optional

from pydantic import BaseModel


class ApplicationState(str, Enum):
    DRAFT = "draft"
    REVIEW = "review"
    APPROVED = "approved"


class ApplicationDraftCreate(BaseModel):
    job_id: str
    resume_source: str = "base resume placeholder"
    reviewer_note: Optional[str] = None


class TailoredResume(BaseModel):
    summary: str
    highlighted_skills: list[str]
    experience_bullets: list[str]


class ApplicationDraft(BaseModel):
    id: str
    job_id: str
    state: ApplicationState = ApplicationState.DRAFT
    tailored_resume: TailoredResume
    cover_note: str
    reviewer_note: Optional[str] = None
    approval_note: Optional[str] = None


class ApprovalRequest(BaseModel):
    confirmed: bool = False
    reviewer_note: Optional[str] = None
