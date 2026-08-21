# Day 7: External and Coded Agents

**Focus:** Coded agents, external agents, handoff contracts, Maestro orchestration
**Checkpoint:** Define one external-agent contract

## Why this matters

Not every part of your solution needs to be a single agent doing
everything. Day 7 is about explicitly designing the **handoff** — what one
agent (or robot, or human) passes to another, and what it expects back —
rather than letting that boundary stay implicit and fragile.

## When to reach for a coded agent

Recap from [Day 2](../day-2/6-coded-agents-and-production-readiness.md#coded-agents-briefly):
coded agents are for teams with software-engineering depth who need more
control than low-code allows — open frameworks (e.g. LangGraph),
graph-based orchestration with explicit states/edges, memory/checkpoints,
and interrupt nodes for human-in-the-loop — while still publishing back
into UiPath's governed package → process → job lifecycle.

## Multi-agent design: manager/specialist pattern

From Day 2's design-patterns discussion: think of a manager agent
delegating to specialist agents the way a manager delegates to team
members with focused expertise, rather than one agent trying to do
everything. The trade-off is real: **every extra agent is an extra LLM
call**. Only split into multiple agents when a single agent with more
tools genuinely can't do the job cleanly — there's no universal rule here,
it's a solution-design judgment call for your specific case.

## Maestro orchestration, briefly

Maestro is where you integrate agents, RPA, APIs, and IXP end-to-end using
BPMN concepts (events, tasks, gateways for parallel/exclusive paths), all
on top of the AI Trust and Governance foundation. A **User Task** node is
how you model a human-in-the-loop handoff inside a BPMN flow (see
[Day 2: HITL & Escalation](../day-2/4-hitl-and-escalation.md#escalation-in-maestro)).

## Self-paced exercise: define one external-agent contract

Pick one boundary in your use case where an agent hands off to something
else (another agent, a robot, an external system, or a human), and write
down:

1. **What triggers the handoff** — the specific condition, not "when it's
   ready"
2. **What's passed across the boundary** — the exact fields/schema, the
   same discipline as an `agent.json` input/output schema
3. **What the receiving side is expected to do with it**
4. **What comes back** — the response contract, including failure/error
   shape, not just the happy path
5. **Who owns each side** — which agent, robot, or team is responsible for
   each half of the contract

Example shape (adapt to your use case):

```text
Trigger: sentiment classification returns "negative" with confidence > 0.8
Passes: { customerId, feedbackText, sentimentScore, category }
Receiving side: escalation agent / Action Center review task
Expected response: { reviewDecision: "approved" | "escalate" | "reject",
                      reviewerNotes }
Owner (sending): sentiment-analysis agent
Owner (receiving): human reviewer via Action App
```

## Checkpoint

- [ ] One external-agent (or agent-to-robot, or agent-to-human) contract
      is written down explicitly — trigger, payload, expected response,
      ownership on both sides
- [ ] The contract's failure/error path is defined, not just the happy
      path

## Office hours discussion prompts

1. What changed since yesterday?
2. What's blocked?
3. What will you complete next?
