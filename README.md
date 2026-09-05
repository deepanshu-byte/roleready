# RoleReady

RoleReady is a lightweight starter for a review-first job application assistant. It helps collect profile data, discover and score jobs, generate tailored resume/application drafts, and keep every submission behind an explicit human approval step.

## Structure

- `backend/` - FastAPI API with modular profile, platform, company, discovery, tailoring, draft, and approval services.
- `frontend/` - Next.js + TypeScript dashboard for configuration, job queue, tailored drafts, and final approval.
- `.env.example` - root reference for local configuration. Each app also has its own sample env file.

## Quick Start

Backend:

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools
python -m pip install -e ".[dev]"
cp .env.example .env
uvicorn app.main:app --reload --port 8000
```

The packaging-tool upgrade is required on Python installations that create virtual environments with an older `pip`; editable `pyproject.toml` installs require PEP 660 support.

Frontend:

```bash
cd frontend
npm install
cp .env.local.example .env.local
npm run dev
```

Open `http://localhost:3000`. The frontend expects the API at `NEXT_PUBLIC_API_BASE_URL`, defaulting to `http://localhost:8000`.

## Configuration

Do not commit real secrets. Use environment variables for all credentials and API keys.

Important backend variables:

- `ROLEREADY_ENV` - `local`, `staging`, or `production`.
- `ROLEREADY_CORS_ORIGINS` - comma-separated allowed frontend origins.
- `OPENAI_API_KEY` - optional. When absent, the agent layer returns safe placeholder outputs.
- `DEVELOPMENT_AUTH_USERNAME` and `DEVELOPMENT_AUTH_PASSWORD` - local credentials-based development scaffold.
- `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, `GOOGLE_REDIRECT_URI` - Google OAuth hooks.

## Approval Model

RoleReady intentionally does not implement automatic job submission. Applications move through:

1. `draft`
2. `review`
3. `approved`

The backend requires an explicit `POST /api/applications/{id}/approve` call before an application can become approved. Future platform integrations should keep submission as a separate, auditable action.

## Useful API Endpoints

- `GET /health` - service health.
- `GET /api/config` - public runtime configuration flags.
- `GET /api/profile` and `PUT /api/profile` - configurable user profile fields.
- `GET /api/jobs` and `POST /api/jobs/discover` - job queue and discovery placeholder.
- `POST /api/applications/drafts` - generate an application draft.
- `POST /api/applications/{id}/submit-for-review` - move draft to review.
- `POST /api/applications/{id}/approve` - explicit approval action.

## Verification

Run checks after installing dependencies:

```bash
cd backend && ruff check app && pytest
cd frontend && npm run lint && npm run build
```
