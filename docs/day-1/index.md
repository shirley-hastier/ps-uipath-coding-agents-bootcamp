# Day 1: Builder Foundations

## Business context

Attendees arrive with a business problem in mind but, in most cases, no
hands-on experience building end-to-end with a coding agent against the
UiPath platform. Day 1 exists to remove that gap fast: everyone should be
**building by midday**, not still configuring their laptop at 2pm.

## Learning objective

By the end of Day 1, every participant can:

- Explain, in one sentence, why coding agents change the automation
  development lifecycle (not just "AI writes code faster")
- Authenticate their coding agent to the correct UiPath organization and
  tenant, with UiPath skills installed and discoverable
- Write a prompt that reliably produces a **UiPath low-code agent** (not a
  generic Python/coded agent) from their coding agent of choice
- Build, deploy, and run at least one evaluation against a working agent

## What you'll build today

A **UiPath low-code sentiment-analysis agent**: built with your coding agent
of choice, deployed to the UiPath platform, and validated with at least one
evaluation set. This is deliberately a small, well-scoped build — the
point is to prove the end-to-end loop (build → deploy → evaluate → iterate)
works, before Day 2 layers on tools, MCP, and more complex patterns.

!!! note "Non-determinism is expected, not a bug"
    Every delivery of this lab has produced different results across
    participants from a similarly-worded prompt — different output schemas,
    different numbers of generated evaluation cases, different clarifying
    questions from Plan Mode. That's the coding agent being genuinely
    non-deterministic, and it's a deliberate teaching moment (see
    [Reflection](5-reflection-and-day-2-preview.md)), not something to "fix."

## Agenda

| # | Segment | Type |
|---|---|---|
| 00 | Welcome & Program Kickoff | Instruction |
| 01 | UiPath Vision: Agentic Business Orchestration | Instruction |
| 02 | Why Coding Agents Matter · From Coding Agents to Production Solutions | Instruction |
| 03 | [Environment Setup](2-environment-setup.md) | Exercise |
| 04 | [Prompting Coding Agents for Better Outcomes](3-prompting-coding-agents.md) | Instruction |
| 05 | [Hands-On Lab: Build a Low-Code Agent](4-hands-on-lab-sentiment-agent.md) | Exercise |
| 06 | [Reflection & Project Planning](5-reflection-and-day-2-preview.md) | Reflection |
| 07 | Day 2 Preview | Instruction |

!!! warning "Needs validation — timing"
    The deck frames Day 1 as a single day. Every recorded delivery
    (customer pilot and all three internal 101 runs) actually ran
    5–6.5 hours end-to-end, and the internal versions compress Day 1 **and**
    Day 2 content into one session. Confirm the real-time budget per segment
    with your coach before planning break schedules — plan for the setup and
    hands-on lab segments to run long.

## Preflight checklist (coach: confirm before Day 1 starts)

- [ ] Every attendee has a coding-agent license (Claude Code, Codex, Cursor,
      etc.) — UiPath does not provide these licenses
- [ ] Every attendee has Node.js and an IDE (VS Code, or UiPath Studio
      Desktop with the terminal panel) installed
- [ ] Training vs. customer environment decision is made and communicated
      (see [Program Overview](../program-overview.md#training-environment-vs-customer-environment))
- [ ] The org/tenant/authority URL for this cohort is confirmed and
      distributed
- [ ] Each attendee (or small team) has a named use case in mind
- [ ] GitHub access is available if you plan to have attendees push their
      build

## Products & tools used today

UiPath CLI (`uip`) · UiPath skills · a coding agent (Claude Code, Codex,
Cursor, or similar) · UiPath Studio Web (Agent Builder, Evaluators) ·
Orchestrator (deployment target) · optionally GitHub (source control)
