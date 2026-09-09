# Human-in-the-Loop & Escalation Design

*Roughly 15-20 minutes, instruction + short demo.*


**What you'll take from this**

Three concrete escalation patterns to choose from for your own use
case, instead of defaulting to "add a review step" without thinking
through who's reviewing and how.

## Three HITL implementation options

| Option | When to use it |
|---|---|
| **Agent's built-in escalation point** | Triggers only when a specific condition is met — not on every run. Good default when escalation is the exception, not the norm. |
| **Custom app / Action Center (Action App)** | A human-facing review UI presenting the agent's reasoning plus supporting documents, with accept/reject/edit options. Use when you expect a meaningful *volume* of pending reviews that need to be tracked and assigned across a team. |
| **Conversational agent as the human-facing UI** | The human interacts with the agent directly in natural language; the conversation itself is the human-in-the-loop mechanism. |

## Action App vs. App

- A plain **App** is a standalone deployed application with no built-in
  queue or assignment layer.
- An **Action App** surfaces in **Action Center**, so pending
  human-in-the-loop tasks can be tracked and assigned across a team at
  volume — think "hundreds of requests popping up," not one-off reviews.

## Escalation in Maestro

Model human-in-the-loop directly in a BPMN process flow using a
**User Task** node, with a descriptive comment on what the human is meant
to do (e.g., "validate invoice data" or "claim officer verification"). This
is also how Case Management stages block on human review before
progressing (e.g., pulling documents from multiple systems in parallel,
then blocking on a review stage until a human signs off).

## Guardrails, briefly

Guardrails are configured at the **tool** level: choose enforcement timing
(pre-call, post-call, or both), the action on trigger (escalate / block /
log), and severity. Example: a web-search tool with a URL allow-list or
deny-list.

!!! warning "Needs validation — guardrails for conversational agents"
    Guardrail configuration was confirmed working for **autonomous**
    agents in a live demo. Whether the same configurable guardrails are
    available for **conversational** agents was left explicitly
    unresolved in that same session — confirm current state with your
    coach before promising it to a customer.

One live example worth knowing about: a conversational agent refused a
question containing an inappropriate value in a "Medical Alert" field,
citing HIPAA — **without any guardrail having been explicitly
configured**. Some safety behavior is built into the underlying model
itself, separate from anything you configure.

Continue to
[Hands-On Lab: Build a Conversational Agent](5-hands-on-lab-conversational-agent.md).
