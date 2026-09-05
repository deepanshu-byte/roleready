from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Union

from app.core.config import get_settings
from app.schemas.applications import TailoredResume
from app.schemas.jobs import JobOpportunity
from app.schemas.profile import UserProfile


@dataclass
class TailoredDraftResult:
    tailored_resume: TailoredResume
    cover_note: str


class AgentService(ABC):
    @abstractmethod
    def extract_resume(self, resume_source: str) -> dict[str, Union[str, list[str]]]:
        raise NotImplementedError

    @abstractmethod
    def score_job_match(self, profile: UserProfile, company: str, keywords: list[str]) -> int:
        raise NotImplementedError

    @abstractmethod
    def generate_tailored_draft(
        self,
        profile: UserProfile,
        job: JobOpportunity,
        resume_source: str,
    ) -> TailoredDraftResult:
        raise NotImplementedError


class PlaceholderAgentService(AgentService):
    def extract_resume(self, resume_source: str) -> dict[str, Union[str, list[str]]]:
        return {
            "summary": "OpenAI is not configured, so RoleReady preserved the supplied resume source.",
            "source_preview": resume_source[:240],
            "skills": ["Python", "TypeScript", "Product engineering"],
        }

    def score_job_match(self, profile: UserProfile, company: str, keywords: list[str]) -> int:
        priority = next(
            (target.priority for target in profile.target_companies if target.name == company),
            3,
        )
        keyword_bonus = min(len(keywords) * 4, 12)
        return min(62 + priority * 5 + keyword_bonus, 95)

    def generate_tailored_draft(
        self,
        profile: UserProfile,
        job: JobOpportunity,
        resume_source: str,
    ) -> TailoredDraftResult:
        extracted = self.extract_resume(resume_source)
        return TailoredDraftResult(
            tailored_resume=TailoredResume(
                summary=f"{profile.full_name} positioned for {job.title} at {job.company}.",
                highlighted_skills=list(extracted["skills"]),
                experience_bullets=[
                    f"Emphasize recent work aligned with {job.title.lower()} responsibilities.",
                    f"Connect {profile.headline.lower()} background to {job.company}'s role needs.",
                    "Keep all claims reviewable before approval or submission.",
                ],
            ),
            cover_note=(
                f"Draft note for {job.company}: highlight relevant product engineering impact, "
                "specific role fit, and availability. Review before use."
            ),
        )


class OpenAIAgentService(PlaceholderAgentService):
    """Interface boundary for future OpenAI SDK calls.

    The class currently inherits safe placeholder behavior so local development works
    without network access or secrets. Add SDK-backed implementations here once the
    project chooses persistence, tracing, and prompt evaluation patterns.
    """


def get_agent_service() -> AgentService:
    settings = get_settings()
    if settings.openai_enabled:
        return OpenAIAgentService()
    return PlaceholderAgentService()
