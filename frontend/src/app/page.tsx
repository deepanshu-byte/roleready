import {
  BriefcaseBusiness,
  Building2,
  CheckCircle2,
  CircleAlert,
  FileText,
  KeyRound,
  Send,
  Settings2,
  Sparkles,
  UserRound
} from "lucide-react";

import { API_BASE_URL, getRuntimeConfig } from "@/lib/api";

const profileFields = [
  ["Years of experience", "5"],
  ["Core stack", "Python, TypeScript, React"],
  ["Work authorization", "Needs review"],
  ["Preferred role", "Full-stack product engineer"]
];

const platforms = [
  ["LinkedIn", "Enabled", "Manual review import"],
  ["Wellfound", "Enabled", "Startup-focused queue"],
  ["Company pages", "Enabled", "Target-company discovery"]
];

const companies = [
  ["OpenAI", "Priority 5", "AI product engineering"],
  ["Stripe", "Priority 4", "Developer platforms"],
  ["Ramp", "Priority 4", "Finance automation"]
];

const jobs = [
  ["Senior Full Stack Engineer", "OpenAI", "92", "review fit"],
  ["Product Engineer", "Stripe", "88", "draft resume"],
  ["Platform Engineer", "Ramp", "83", "new"]
];

export default async function Dashboard() {
  const config = await getRuntimeConfig();

  return (
    <main className="min-h-screen bg-[#f7f5f0] text-[#22231f]">
      <section className="border-b border-[#ded8cb] bg-[#fdfcf8]">
        <div className="mx-auto flex max-w-7xl flex-col gap-8 px-5 py-7 md:px-8 lg:flex-row lg:items-center lg:justify-between">
          <div>
            <div className="mb-4 inline-flex items-center gap-2 rounded-full border border-[#d8d0c1] bg-white px-3 py-1 text-sm text-[#686154]">
              <Sparkles size={16} aria-hidden />
              Review-first application workspace
            </div>
            <h1 className="max-w-3xl text-4xl font-semibold tracking-normal md:text-6xl">
              RoleReady
            </h1>
            <p className="mt-4 max-w-2xl text-lg leading-8 text-[#5d5a52]">
              Configure your profile, score target roles, generate tailored drafts, and approve
              every application before anything leaves the workspace.
            </p>
          </div>
          <div className="grid min-w-[280px] gap-3 rounded-lg border border-[#ded8cb] bg-white p-4 shadow-sm">
            <StatusRow
              label="API"
              value={config ? `Connected to ${config.environment}` : "Using dashboard mock data"}
              healthy={Boolean(config)}
            />
            <StatusRow
              label="OpenAI"
              value={config?.openai_enabled ? "Configured" : "Placeholder agents active"}
              healthy={Boolean(config?.openai_enabled)}
            />
            <StatusRow
              label="Google OAuth"
              value={config?.google_oauth_configured ? "Configured" : "Awaiting env vars"}
              healthy={Boolean(config?.google_oauth_configured)}
            />
          </div>
        </div>
      </section>

      <section className="mx-auto grid max-w-7xl gap-5 px-5 py-6 md:px-8 lg:grid-cols-[1.05fr_0.95fr]">
        <Panel icon={<UserRound size={19} />} title="Profile Fields" action="Edit profile">
          <div className="grid gap-3 sm:grid-cols-2">
            {profileFields.map(([label, value]) => (
              <label className="grid gap-2" key={label}>
                <span className="text-sm font-medium text-[#686154]">{label}</span>
                <input className="input" defaultValue={value} />
              </label>
            ))}
          </div>
        </Panel>

        <Panel icon={<KeyRound size={19} />} title="Auth & API Hooks" action="Check setup">
          <div className="grid gap-3 text-sm">
            <ConfigLine label="Backend base URL" value={API_BASE_URL} />
            <ConfigLine label="Local credentials" value="DEVELOPMENT_AUTH_USERNAME / PASSWORD" />
            <ConfigLine label="Google OAuth" value="GOOGLE_CLIENT_ID / GOOGLE_CLIENT_SECRET" />
          </div>
        </Panel>

        <Panel icon={<BriefcaseBusiness size={19} />} title="Job Platforms" action="Add platform">
          <div className="grid gap-3">
            {platforms.map(([name, state, note]) => (
              <Row key={name} title={name} meta={note} badge={state} />
            ))}
          </div>
        </Panel>

        <Panel icon={<Building2 size={19} />} title="Target Companies" action="Add company">
          <div className="grid gap-3">
            {companies.map(([name, priority, note]) => (
              <Row key={name} title={name} meta={note} badge={priority} />
            ))}
          </div>
        </Panel>
      </section>

      <section className="mx-auto grid max-w-7xl gap-5 px-5 pb-8 md:px-8 lg:grid-cols-[0.9fr_1.1fr]">
        <Panel icon={<Settings2 size={19} />} title="Job Queue" action="Discover jobs">
          <div className="grid gap-3">
            {jobs.map(([role, company, score, state]) => (
              <div className="rounded-lg border border-[#ddd6c8] bg-white p-4" key={`${role}-${company}`}>
                <div className="flex items-start justify-between gap-3">
                  <div>
                    <h3 className="font-semibold">{role}</h3>
                    <p className="mt-1 text-sm text-[#686154]">{company}</p>
                  </div>
                  <span className="rounded-full bg-[#184d47] px-3 py-1 text-sm font-semibold text-white">
                    {score}%
                  </span>
                </div>
                <div className="mt-4 flex items-center justify-between">
                  <span className="text-sm capitalize text-[#686154]">{state}</span>
                  <button className="icon-button" aria-label={`Create draft for ${role}`}>
                    <FileText size={17} />
                  </button>
                </div>
              </div>
            ))}
          </div>
        </Panel>

        <Panel icon={<FileText size={19} />} title="Tailored Draft & Approval" action="Submit review">
          <div className="grid gap-4">
            <div className="rounded-lg border border-[#ddd6c8] bg-[#fbfaf5] p-4">
              <div className="mb-3 flex items-center gap-2 text-sm font-semibold text-[#184d47]">
                <Sparkles size={16} />
                Tailored resume draft
              </div>
              <textarea
                className="textarea min-h-40"
                defaultValue={
                  "Summary: Product-minded software engineer positioned for Senior Full Stack Engineer.\n\nBullets:\n- Emphasize Python, TypeScript, and React delivery.\n- Connect product judgment to AI workflow tooling.\n- Keep all claims reviewable before final approval."
                }
              />
            </div>
            <div className="rounded-lg border border-[#d7cab1] bg-[#fff8e8] p-4">
              <div className="mb-3 flex items-center gap-2 font-semibold text-[#7a4d00]">
                <CircleAlert size={18} />
                Approval gate
              </div>
              <p className="text-sm leading-6 text-[#63543a]">
                Automatic submission is intentionally absent. Move a draft to review, inspect the
                content, then approve explicitly when it is ready.
              </p>
              <div className="mt-4 flex flex-wrap gap-3">
                <button className="primary-button">
                  <Send size={17} />
                  Submit for review
                </button>
                <button className="secondary-button">
                  <CheckCircle2 size={17} />
                  Approve draft
                </button>
              </div>
            </div>
          </div>
        </Panel>
      </section>
    </main>
  );
}

function Panel({
  icon,
  title,
  action,
  children
}: Readonly<{
  icon: React.ReactNode;
  title: string;
  action: string;
  children: React.ReactNode;
}>) {
  return (
    <section className="rounded-lg border border-[#ded8cb] bg-[#fdfcf8] p-5 shadow-sm">
      <div className="mb-5 flex items-center justify-between gap-3">
        <div className="flex items-center gap-2">
          <span className="grid size-9 place-items-center rounded-lg bg-[#184d47] text-white">{icon}</span>
          <h2 className="text-lg font-semibold">{title}</h2>
        </div>
        <button className="small-button">{action}</button>
      </div>
      {children}
    </section>
  );
}

function StatusRow({ label, value, healthy }: Readonly<{ label: string; value: string; healthy: boolean }>) {
  return (
    <div className="flex items-center justify-between gap-4">
      <span className="text-sm font-medium text-[#686154]">{label}</span>
      <span className={healthy ? "status-ok" : "status-wait"}>{value}</span>
    </div>
  );
}

function ConfigLine({ label, value }: Readonly<{ label: string; value: string }>) {
  return (
    <div className="rounded-lg border border-[#ddd6c8] bg-white p-3">
      <div className="text-xs font-semibold uppercase text-[#777065]">{label}</div>
      <div className="mt-1 break-words text-[#22231f]">{value}</div>
    </div>
  );
}

function Row({ title, meta, badge }: Readonly<{ title: string; meta: string; badge: string }>) {
  return (
    <div className="flex items-center justify-between gap-3 rounded-lg border border-[#ddd6c8] bg-white p-4">
      <div>
        <h3 className="font-semibold">{title}</h3>
        <p className="mt-1 text-sm text-[#686154]">{meta}</p>
      </div>
      <span className="shrink-0 rounded-full bg-[#e7efe4] px-3 py-1 text-sm font-semibold text-[#24533b]">
        {badge}
      </span>
    </div>
  );
}

