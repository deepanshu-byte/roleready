from app.schemas.jobs import DiscoveryRequest, JobOpportunity
from app.services.agents import get_agent_service
from app.services.store import store


def discover_jobs(request: DiscoveryRequest) -> list[JobOpportunity]:
    targets = store.profile.target_companies if request.include_target_companies else []
    companies = targets[:3] or store.profile.target_companies[:2]
    if not companies:
        companies = []

    jobs = [
        JobOpportunity(
            id=f"job-{index + 1}",
            title=f"{request.seniority} {request.keywords[0].title()}",
            company=company.name,
            platform="Company career page",
            location=request.locations[0],
            url=company.career_url or "https://example.com/careers",
            match_score=get_agent_service().score_job_match(store.profile, company.name, request.keywords),
            rationale=f"Matches {store.profile.headline} with priority target company focus.",
        )
        for index, company in enumerate(companies)
    ]

    if not jobs:
        jobs.append(
            JobOpportunity(
                id="job-1",
                title=f"{request.seniority} {request.keywords[0].title()}",
                company="Example Company",
                platform="Manual import",
                location=request.locations[0],
                url="https://example.com/job",
                match_score=72,
                rationale="Placeholder role until platforms or target companies are configured.",
            )
        )
    return jobs

