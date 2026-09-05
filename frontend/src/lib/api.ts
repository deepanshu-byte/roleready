const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000";

export type RuntimeConfig = {
  environment: string;
  openai_enabled: boolean;
  google_oauth_configured: boolean;
};

export async function getRuntimeConfig(): Promise<RuntimeConfig | null> {
  try {
    const response = await fetch(`${API_BASE_URL}/api/config`, { cache: "no-store" });
    if (!response.ok) {
      return null;
    }
    return response.json();
  } catch {
    return null;
  }
}

export { API_BASE_URL };

