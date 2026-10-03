"use strict";
globalThis.StudyPlanAPI = {
  async generate(body) {
    const options = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    };
    for (let attempt = 0; attempt < 2; attempt++) {
      let response;
      try {
        response = await fetch("/api/plan/generate", options);
      } catch (error) {
        if (!(error instanceof TypeError)) throw error;
        if (attempt) throw new Error("PLAN_CONNECTION_INTERRUPTED");
      }
      if (response?.ok) return response.json();
      const error = response ? await response.json().catch(() => null) : null;
      // A proxy/connection interruption has no application error detail.
      // Retry it once; explicit validation, provider and budget errors remain visible.
      if (
        attempt ||
        (response &&
          (![502, 503, 504].includes(response.status) || error?.detail))
      )
        throw new Error(error?.detail || "PLAN_CONNECTION_INTERRUPTED");
      await new Promise((resolve) => setTimeout(resolve, 2000));
    }
  },
};
