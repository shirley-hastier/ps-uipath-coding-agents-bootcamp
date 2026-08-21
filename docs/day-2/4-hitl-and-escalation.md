# Human-in-the-Loop & Escalation Design

*Roughly 15-20 minutes, instruction + short demo.*

=== "Coach View"

    **Purpose**

    Give participants a concrete menu of HITL patterns, rather than a
    single generic "add a human review step" answer.

    **Key message**

    Escalation isn't one feature — it's a design decision with at least
    three viable implementations, chosen based on who the human is and how
    they'll interact with the work.

    **What to show on screen**

    An agent's built-in escalation configuration; a Maestro BPMN flow with
    a **User Task** node added; the difference between a plain **App** and
    an **Action App**.

    **Suggested narration**

    > "If we give an agent too much freedom, and it does something it
    > shouldn't, that's a problem. Pay close attention to authorization
    > prompts — if the action matches your intent, allow it; otherwise,
    > deny or redirect it."

    **Likely questions & recommended answers**

    | Question | Answer |
    |---|---|
    | "What's the difference between an App and an Action App?" | A regular App is a standalone deployed application. An **Action App** surfaces in **Action Center**, so a large volume of pending human-in-the-loop tasks can be tracked, assigned, and worked across a team — needed once you have more than a handful of ad-hoc approvals. |
    | "Is there a dedicated 'escalation' node in Maestro?" | Not a specifically-named one — you get this behavior via a **User Task** node in the BPMN flow. |
    | "Do conversational agents need human-in-the-loop too?" | Rarely, based on what's been observed — a conversational agent's natural human-facing turn-taking often *is* the human-in-the-loop mechanism. It's still an option if you need it, just less commonly reached for. |

    **Transition into the hands-on lab**

    "You've now seen inputs, context, tools, and escalation options — let's
    put them together and build a conversational agent."

=== "Participant View"

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
