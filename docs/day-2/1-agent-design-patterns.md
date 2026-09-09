# Common Agent Design Patterns

*Roughly 15-20 minutes. This sets vocabulary for everything else today —
keep it grounded in the Day 1 agent participants already built.*


**What you'll take from this**

A shared vocabulary (inputs, instructions, context, tools, governance,
outputs) you'll use for the rest of today, and a simple test for
"should this be an agent or a robot?"

## The building blocks of a UiPath agent

| Block | What it is |
|---|---|
| **Inputs / Outputs** | Structured or unstructured data in, structured or unstructured data out |
| **Instructions** | The role, goals, and constraints you give the agent (its system prompt) |
| **Context** | Short- and long-term memory, plus grounding in enterprise data (see [Context Grounding](2-context-grounding.md)) |
| **Tools** | How the agent takes action — RPA workflows, APIs, connectors, other agents (see [Tools & Integrations](3-tools-and-integrations.md)) |
| **Governance** | Trust, transparency, guardrails, and audit trails around everything the agent does |

## Agent vs. robot: the decision rule

> "If it is very deterministic, rule-based, then robots or RPA could be the
> best option. But if it requires an end goal, or is non-deterministic, or
> requires reasoning or classification, then the agent will be the go-to."

In practice: a fixed sequence of steps with no judgment calls is a robot.
A task where the right next step depends on interpreting ambiguous input is
an agent.

## Model selection & token optimization

Every model you can choose in Agent Builder (Definition → Properties → 
model dropdown) has a cost/capability trade-off. Practical levers:

- Prefer a smaller/"mini" model unless quality genuinely requires more
- Cap **maximum tokens per response**
- Minimize what's in the context window — don't hand the agent more than it
  needs for the task
- For tool-heavy agents, watch for excessive back-and-forth tool calls —
  that's a token cost as much as a latency cost

There's also **Autopilot for UI automation** ("Screenplay"), a distinct
pattern from autonomous/conversational agents: you describe interactions in
natural language and can cap the number of allowed actions, for lightweight
UI-automation-by-description rather than a full agent build.

Continue to [Enterprise Data & Context Grounding](2-context-grounding.md).
