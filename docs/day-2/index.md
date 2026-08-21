# Day 2: Enterprise Agent Patterns

## Business context

Day 1 proved the loop works on a small, self-contained agent. Day 2 asks a
harder question: what does it take to move from "a demo that works for me"
to something enterprise-shaped — grounded in real data, able to take
action through real systems, safe to hand off to a human when it should
be, and observable once it's live? Every recorded delivery ran this as a
mix of concept walkthroughs and live building, with real (sometimes
unresolved) failures along the way — that's preserved in this guide
deliberately, because those failures are exactly what you'll hit in your
own office-hours build.

## Learning objective

By the end of Day 2, every participant can:

- Explain the building blocks of a UiPath agent (inputs, instructions,
  context, tools, governance, outputs) and when to use an agent vs. a
  deterministic robot/RPA workflow
- Ground an agent in enterprise data via Context Grounding, and know when
  *not* to reach for RAG
- Give an agent a tool via an Integration Service connector, and explain
  what an MCP server is (and isn't, yet, reliably able to do end-to-end)
- Choose an appropriate human-in-the-loop pattern for a given escalation
  need
- Build a working conversational agent
- Explain what evaluations, guardrails, and deployment readiness mean for
  an agent-built solution

## What you'll build today

A **UiPath conversational agent**, scoped to a real (if narrow) task —
every delivery used some flavor of "an assistant that helps a team monitor
or find information about X." You'll also see, live, what happens when you
try to attach a not-yet-fully-working capability (an MCP-based tool) and
how to recover from that gracefully — this is one of the most useful
moments in the whole bootcamp precisely because it doesn't go perfectly.

## Agenda

| # | Segment | Type |
|---|---|---|
| 00 | Welcome & Day 1 Recap | Instruction |
| 01 | [Common Agent Design Patterns](1-agent-design-patterns.md) | Instruction |
| 02 | [Enterprise Data & Context Grounding](2-context-grounding.md) | Instruction + Demo |
| 03 | [Tool-Using Agents & Integrations](3-tools-and-integrations.md) | Instruction + Exercise |
| 04 | [Human-in-the-Loop & Escalation Design](4-hitl-and-escalation.md) | Instruction + Demo |
| 05 | [Hands-On Lab: Build a Conversational Agent](5-hands-on-lab-conversational-agent.md) | Exercise |
| 06 | [Coded Agents & Production Readiness](6-coded-agents-and-production-readiness.md) | Instruction + Demo |
| 07 | [Reflection & Office Hours Handoff](7-reflection-and-office-hours-handoff.md) | Reflection |

!!! warning "Needs validation — MCP servers are not fully reliable yet"
    Across two separate live deliveries, an agent's attempt to create and
    attach an **MCP-based tool** reported success but had not actually
    created the underlying MCP server ("it did a mock... it didn't
    actually create the tool"). Treat MCP tool creation as a
    **pre-GA capability with a known gap**, not a guaranteed path — the
    [Tools & Integrations](3-tools-and-integrations.md) and
    [Hands-On Lab](5-hands-on-lab-conversational-agent.md) pages give you
    the documented fallback (a custom Integration Service connector, or a
    tool-free/web-search-only agent) so a demo failure doesn't stall your
    whole session. Confirm current MCP reliability with your coach before
    building a lab plan that depends on it.

## Preflight checklist (coach)

- [ ] Day 1's low-code sentiment agent is still deployed and reachable —
      you'll reference "your agent" as a running example throughout
- [ ] Confirm whether this cohort will attempt the MCP-tool path or go
      straight to the documented fallback, given the reliability gap above
- [ ] Confirm admin/External Application creation rights for participants
      who'll build a custom Integration Service connector — several
      deliveries had participants blocked here without admin rights

## Products & tools used today

UiPath Studio Web (Agent Builder — Autonomous & Conversational) ·
Integration Service (Connectors, custom connector builder) · Context
Grounding (Storage Buckets, Indexes) · Orchestrator (Admin → External
Applications, Agents, Monitoring) · Action Center / Action Apps · Maestro
(BPMN process flow) · optionally an MCP server
