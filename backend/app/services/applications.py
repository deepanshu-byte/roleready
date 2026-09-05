from typing import Optional
from uuid import uuid4

from fastapi import HTTPException, status

from app.schemas.applications import ApplicationDraft, ApplicationDraftCreate, ApplicationState
from app.services.agents import get_agent_service
from app.services.store import store


def create_application_draft(payload: ApplicationDraftCreate) -> ApplicationDraft:
    job = next((candidate for candidate in store.jobs if candidate.id == payload.job_id), None)
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found.")

    draft_content = get_agent_service().generate_tailored_draft(
        profile=store.profile,
        job=job,
        resume_source=payload.resume_source,
    )
    application = ApplicationDraft(
        id=f"app-{uuid4().hex[:8]}",
        job_id=payload.job_id,
        tailored_resume=draft_content.tailored_resume,
        cover_note=draft_content.cover_note,
        reviewer_note=payload.reviewer_note,
    )
    store.applications.append(application)
    return application


def submit_for_review(application_id: str) -> ApplicationDraft:
    application = _find_application(application_id)
    if application.state != ApplicationState.DRAFT:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Only draft applications can be submitted for review.",
        )
    application.state = ApplicationState.REVIEW
    return application


def approve_application(application_id: str, approval_note: Optional[str]) -> ApplicationDraft:
    application = _find_application(application_id)
    if application.state != ApplicationState.REVIEW:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Only applications in review can be approved.",
        )
    application.state = ApplicationState.APPROVED
    application.approval_note = approval_note
    return application


def _find_application(application_id: str) -> ApplicationDraft:
    for application in store.applications:
        if application.id == application_id:
            return application
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Application not found.")
