# Coded Agents & Production Readiness

*Roughly 20-30 minutes, instruction + demo. This closes out the concept
material before wrap-up.*


**What you'll take from this**

When to reach for a coded agent instead of low-code, what "production
ready" checks for beyond "it built successfully," and a troubleshooting
pattern (paste the job URL) you'll use constantly in office hours.

## Coded agents, briefly

For teams with a software-engineering background needing more
sophistication than low-code allows: build on open frameworks (e.g.
LangGraph), then publish back into the UiPath platform to reuse RPA
workflows, APIs, and IXP the same way a low-code agent would. This gets you
graph-based orchestration (states, edges, transitions), memory/checkpoints,
and interrupt nodes for human-in-the-loop flows, while still going through
UiPath's governed package → process → job lifecycle and AI Trust Layer for
LLM calls.

!!! note
    A full LangGraph/LangChain integration walkthrough exists as an
    appendix example in the master deck, referenced but not built live in
    any delivery observed for this guide. Treat it as a pointer for
    self-study or an office-hours topic, not something to attempt cold in
    the Day 2 session.

## Evaluations and guardrails: what "good" looks like

Some deliveries observed an agent's Plan Mode automatically including
**guardrails** and **10 auto-generated evaluation scenarios** in a single
build pass, without being asked — a sign the underlying skill improves over
time. Don't assume this happens by default, though: if your build doesn't
include evaluation coverage, ask explicitly, the same way you did on Day 1.

## Production readiness checklist

Before you call something "done":

- [ ] Package published **and** registered/visible where end users will
      actually access it (Studio Web / Orchestrator / the target app) —
      these are separate steps
- [ ] Evaluation sets exist and cover the classes/paths that matter for
      this use case
- [ ] Guardrails configured for any tool that can take a consequential
      action
- [ ] Deployed to the correct org/tenant/folder (not a personal workspace
      by accident)
- [ ] You can diagnose a failure by pasting its Orchestrator job URL into
      your coding agent and getting a real root-cause answer

## Troubleshooting a live failure

1. Find the failed job in Orchestrator → Monitoring.
2. Copy its URL.
3. Paste the URL into your coding agent and ask it to diagnose the
   failure — no manual log download/attach required; the agent can pull
   job/log context directly from the URL.
4. Treat the returned root cause as a starting hypothesis, not gospel —
   verify against what you know about the process before acting on it.

## A grounding reminder

> "These agents are here to help you be more productive, but at the end,
> you are responsible for whatever is being produced."

Continue to [Reflection & Office Hours Handoff](7-reflection-and-office-hours-handoff.md).
