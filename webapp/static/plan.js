(function (root) {
  "use strict";
  const ready = (step, checks, plan) =>
    step.checklist.length > 0 &&
    step.checklist.every((_, i) => checks[`${step.id}:${i}`] === true) &&
    (!step.choices ||
      step.choices.some((c) => c.id === plan.choices?.[step.id]));
  const validated = (step, checks, plan) =>
    !!plan.confirmed?.[step.id] && ready(step, checks, plan);
  const frontier = (journey, checks, plan) => {
    const first = journey.steps.findIndex((s) => !validated(s, checks, plan));
    return first < 0 ? journey.steps.length : first;
  };
  const reopen = (journey, index, plan) => {
    for (const step of journey.steps.slice(index))
      delete plan.confirmed?.[step.id];
  };
  const confirm = (journey, index, checks, plan) => {
    if (
      index < 0 ||
      index >= journey.steps.length ||
      index > frontier(journey, checks, plan) ||
      !ready(journey.steps[index], checks, plan)
    )
      return false;
    plan.confirmed ??= {};
    plan.confirmed[journey.steps[index].id] = new Date().toISOString();
    return true;
  };
  const api = { ready, validated, frontier, reopen, confirm };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.StudyPlan = api;
})(globalThis);
