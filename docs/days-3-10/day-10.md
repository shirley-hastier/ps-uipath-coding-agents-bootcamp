# Day 10: Evals, Governance, and Deployment

**Focus:** Eval sets, guardrails, RBAC, publish/deploy/run, promotion checklist
**Checkpoint:** Present final readiness review

## Why this matters

This is demo day — the **demo ready** executive-tracking milestone (see
[Program Overview](../program-overview.md#executive-tracking-checkpoints))
and the culmination of the whole two weeks. Day 10 is about proving your
solution is ready to show, not just that it exists.

## Promotion checklist

Reuses and extends the
[Day 2 production-readiness checklist](../day-2/6-coded-agents-and-production-readiness.md#production-readiness-checklist):

- [ ] Package published **and** registered/visible where end users will
      actually access it (these are separate steps — confirmed more than
      once as a source of confusion across deliveries)
- [ ] Evaluation sets exist and cover the classes/paths that matter for
      your use case — not just the happy path
- [ ] Evaluator actually measures what you care about (recall the Day 1
      gotcha: a default evaluator scoring free-text rationale instead of
      just the classification label produces misleading scores)
- [ ] Guardrails configured for any tool that can take a consequential
      action
- [ ] Deployed to the correct org/tenant/folder — verify this directly,
      don't assume
- [ ] RBAC / access reviewed — who can run this, who can see its outputs,
      who approved the scopes it touches
- [ ] You can diagnose a failure by pasting its Orchestrator job URL into
      your coding agent (see [Day 2](../day-2/6-coded-agents-and-production-readiness.md#troubleshooting-a-live-failure))

## Preparing your final readiness review

Structure your Day 10 presentation around:

1. **The business problem** — stated in one or two sentences, not
   technology-first (this echoes the [Program Overview](../program-overview.md)'s
   opening guidance: the most successful participants started with a
   business problem, not a technology objective)
2. **What you built** — the agent(s)/automation(s)/app(s), and how they
   fit together
3. **Evidence it works** — evaluation results, a live or recorded demo run
4. **What's still open** — known limitations, anything marked
   `[Needs validation]` in your own build, and your path to closing those
   gaps
5. **What "production" requires next** — governance/RBAC sign-off,
   remaining integration work, ownership handoff

## A closing reminder

> "These agents are here to help you be more productive, but at the end,
> you are responsible for whatever is being produced."

That's true on Day 10 exactly as much as it was on Day 1 — the demo is
yours to stand behind, not the coding agent's.

## Checkpoint

- [ ] Every item in the promotion checklist above is checked or has an
      explicit, named reason it isn't
- [ ] Final readiness review presented, covering business problem, what
      was built, evidence, open items, and next steps toward production

## Office hours discussion prompts

1. What changed since yesterday?
2. What's blocked — anything that needs escalation before demo day?
3. What will you complete next?
