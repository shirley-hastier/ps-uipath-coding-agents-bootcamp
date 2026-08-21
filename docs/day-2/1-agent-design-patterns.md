# Common Agent Design Patterns

*Roughly 15-20 minutes. This sets vocabulary for everything else today —
keep it grounded in the Day 1 agent participants already built.*

=== "Coach View"

    **Purpose**

    Give participants a mental model for what's actually inside a UiPath
    agent, and a clear decision rule for when to reach for an agent versus
    a deterministic robot.

    **Key message**

    An agent is inputs + instructions + context + tools + governance,
    producing outputs — and every one of those pieces is a design decision,
    not a default you accept. Point back at yesterday's `agent.json` to
    make this concrete.

    **What to show on screen**

    Agent Builder → Definition → Properties, showing the model dropdown and
    "maximum tokens per response" setting — this is a natural jumping-off
    point for the token-optimization discussion below.

    **Suggested narration**

    > "If it is very deterministic and rule-based, a robot or RPA workflow
    > is the best option. If it requires reasoning, classification, or
    > working toward an end goal with non-deterministic paths, that's where
    > an agent is the right tool."

    **Questions to ask participants**

    - "Think about your own use case — is the core decision deterministic,
      or does it need judgment? Robot, or agent?"

    **Likely questions & recommended answers**

    | Question | Answer |
    |---|---|
    | "Does a bigger/more expensive model always give better results?" | Not necessarily, and it costs more in AI units/tokens. Start with a smaller model, cap max tokens per response, and only upgrade if quality genuinely requires it. One real MCP-based agent burned excessive tokens on unnecessary back-and-forth calls due to poor optimization — this is a real cost lever, not a theoretical one. |
    | "Why do we care about traceability/logs so much?" | Because agents are non-deterministic — the same prompt can produce different plans for different people, or even the same person on different runs. Logs are how you debug that after the fact. |

    **Transition into the next segment**

    "Every agent needs to reason with the right information — let's talk
    about how you ground it in your enterprise's actual data."

=== "Participant View"

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
