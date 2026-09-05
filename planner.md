# RoleReady Product Plan

## Current Completed State

RoleReady has a FastAPI backend and an editable Next.js dashboard. The starter covers profile, job-platform, and target-company configuration, plus a draft-to-review-to-approved application workflow. Applications are never submitted automatically.

An OpenAI-ready service boundary supports future resume extraction, job matching, and draft generation. Without an API key, it uses safe placeholder behavior. Local development authentication is scaffolded, Google OAuth configuration hooks are ready, and environment examples and setup documentation are included. Backend linting and tests, frontend linting, and the frontend production build are passing.

## Proposed Next Steps

1. Add resume and blueprint upload, then extract core skills, years of experience, preferred roles, locations, and work preferences into structured data.
2. Add an editable profile-review screen so imported values can be corrected and approved before use.
3. Make every configuration control fully functional, with saved data and clear enabled or disabled states for each action.
4. Implement the agents using verified profile and resume data for explainable job scoring, resume tailoring, and answer drafts, without invented claims.
5. Add persisted data and authentication: a database, secure user accounts, completed Google sign-in, and strict per-user data isolation.
6. Add live job-discovery integrations and practical employer and company controls.
7. Complete application preparation and human approval flows while retaining the no-auto-submit rule.
8. Finish testing, accessibility, audit trails, security and privacy review, and deployment.

## Decisions Needed

- Choose the first supported resume and blueprint file formats.
- Confirm which profile fields must be reviewed before agents can use them.
- Select the initial database, hosting environment, and sign-in policy.
- Prioritize the first job sources and target employers for live discovery.
- Define what approval records and draft history must be retained.

## Future Operational Steps

- Configure production credentials and OAuth redirect URLs outside source control.
- Establish data retention, deletion, backup, and account-recovery procedures.
- Review privacy and security controls before using real candidate data.
- Deploy staging first, complete an end-to-end acceptance review, then promote to production.
- Monitor service health, agent quality, costs, failed integrations, and approval activity after launch.
