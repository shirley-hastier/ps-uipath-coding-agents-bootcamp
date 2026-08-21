# Program Overview

## What this is

A **build accelerator**, not a lecture series. The first two days create
momentum; the following eight days remove blockers and harden each
attendee's use case.

| | |
|---|---|
| **Goal** | Enable each attendee to build one real coding-agent use case, reducing time-to-first-value by removing setup and access friction |
| **Audience** | Builders and technical practitioners with a business use case to implement; executive interest in measurable outcomes |
| **Format** | 2 days instructor-led + 8 days office hours & checkpoints |
| **Delivery** | Online, with security and environment readiness handled up front |
| **Outcome** | Each attendee builds and demos at least one coding-agent use case |

## Two-week delivery flow

| When | Session | Purpose |
|---|---|---|
| Day 1 | Foundations, setup, skills, CLI, coding-agent prompting, first build | Get everyone to a first working agent |
| Day 2 | Implementation patterns, agent tools, MCP servers, conversational agents, external agents, DU/IXP, evals, governance | Extend and stabilize the build path |
| Days 3–10 | Daily office hours + checkpoints | Remove blockers, refine use cases, track progress |

### Executive tracking checkpoints

| Day | Milestone |
|---|---|
| 2 | Use case selected |
| 4 | MVP running |
| 8 | Evaluation completed |
| 10 | Demo ready |

## The most successful participants...

...start with a **business problem, not a technology objective**. Select a
problem from your current workload before Day 1, and use the two weeks to
build a solution for it — not a generic tech demo.

Think about:

- Repetitive tasks that consume valuable time
- Manual research, analysis, or documentation tasks
- Integration challenges between systems and teams
- Opportunities to accelerate software development with AI-assisted coding

## Attendee prerequisites

Confirm all of these **before** Day 1:

- [ ] Coding-agent license assigned (UiPath does not provide third-party
      coding-agent licenses — Claude, Codex, Cursor, etc. are the
      customer's/attendee's responsibility)
- [ ] Developer IDE installed (e.g., VS Code)
- [ ] Access to the target UiPath environment (see below)
- [ ] A named use case, per attendee or small team
- [ ] Version control set up (GitHub)

## Training environment vs. customer environment

!!! warning "Needs validation"
    This decision must be made and communicated **before** Day 1 — it drives
    access, security approvals, and how quickly participants can start
    building. Confirm which path this cohort is using and update the
    `training_url` / `training_tenant` values in `main.py` accordingly.

| Option | Best use | Benefits | Trade-offs |
|---|---|---|---|
| **Training environment** | Fast start and controlled labs | Avoids security delays; standardizes setup | May need to be reproduced later in customer systems |
| **Customer environment** | Closer to production reality | Uses real integrations, permissions, and constraints | Security and access reviews can slow onboarding and put the timeline at risk |

Recommended launch sequence: confirm licensing and IDE readiness first,
choose the environment path second, then lock the use-case intake and
security approvals in parallel.

## Learning design principle

Teach what attendees need immediately to move **their own** use case
forward. Every conceptual segment is followed by a lab, a checkpoint, or a
decision — participants should be building by midday on Day 1.

| Day | Focus |
|---|---|
| Day 1 | Foundations and setup · UiPath skills and the `uip` CLI · Prompting, first build, first debug |
| Day 2 | Patterns and resources · MCP servers and external agents · Evaluations, governance, deploy |
