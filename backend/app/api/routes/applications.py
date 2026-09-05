from fastapi import APIRouter, HTTPException, status

from app.schemas.applications import (
    ApplicationDraft,
    ApplicationDraftCreate,
    ApplicationState,
    ApprovalRequest,
)
from app.services.applications import (
    approve_application,
    create_application_draft,
    submit_for_review,
)
from app.services.store import store

router = APIRouter()


@router.get("", response_model=list[ApplicationDraft])
def list_applications() -> list[ApplicationDraft]:
    return store.applications


@router.post("/drafts", response_model=ApplicationDraft, status_code=status.HTTP_201_CREATED)
def create_draft(payload: ApplicationDraftCreate) -> ApplicationDraft:
    return create_application_draft(payload)


@router.post("/{application_id}/submit-for-review", response_model=ApplicationDraft)
def review(application_id: str) -> ApplicationDraft:
    return submit_for_review(application_id)


@router.post("/{application_id}/approve", response_model=ApplicationDraft)
def approve(application_id: str, payload: ApprovalRequest) -> ApplicationDraft:
    if not payload.confirmed:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Approval requires confirmed=true.",
        )
    return approve_application(application_id, payload.reviewer_note)


@router.post("/{application_id}/mark-draft", response_model=ApplicationDraft)
def move_back_to_draft(application_id: str) -> ApplicationDraft:
    for application in store.applications:
        if application.id == application_id:
            application.state = ApplicationState.DRAFT
            return application
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Application not found.")
