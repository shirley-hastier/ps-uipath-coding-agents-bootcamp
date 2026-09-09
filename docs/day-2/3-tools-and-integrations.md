# Tool-Using Agents & Integrations

*Roughly 30-45 minutes — this segment ran long in every delivery due to
real connector/auth troubleshooting. Budget accordingly.*


**What you'll build**

A custom Integration Service connector from an existing API's Swagger/
OpenAPI definition, published and attached to an agent as a tool.

**Why this matters**

This is the most reliable way today to connect an agent to a system
that doesn't have a pre-built UiPath connector — and you'll very likely
need it for your own use case.

## What is MCP?

Model Context Protocol (MCP) is an open standard for connecting agents to
external systems and tools. The analogy that landed best across
deliveries:

> "It's a JSON middleman — if you need a function that the AI can't do, the
> MCP server does it and feeds it back as JSON the AI can read."

You don't need to understand the implementation behind an MCP server — you
just need to know its capabilities, the same way you'd call a function
without knowing what's inside it.

**MCP server types**, viewed in Orchestrator's MCP Servers screen:

| Type | What it does |
|---|---|
| **UiPath (hosted)** | Exposes UiPath artifacts/capabilities as tools to external systems |
| **Coded** | Host your own MCP server (via the UiPath SDK) wrapping custom logic or an API call |
| **Command** | Bring an MCP server from an external package feed via a command |
| **Remote** | Tunnel connection to a remote/vendor MCP server |

!!! danger "Needs validation — MCP tool creation is not reliably working yet"
    In two separate live deliveries, an agent's plan included creating an
    MCP-based tool, reported the step as complete ("Agent Core is valid and
    ready... everything except the MCP tool attachment is done"), but had
    **not actually created the MCP server**. One instructor's diagnosis:
    "the skill is in development, and it's not there yet." A separate
    participant found a pre-existing, working MCP server ("IT Orchestrator
    Read Only") but even that failed with a permissions error on a shared
    folder. **Do not build your Day 2 hands-on lab plan assuming an
    agent-created MCP tool will just work** — have the fallback below
    ready.

## Hands-on: build a custom Integration Service connector

This is the reliable path for giving an agent a new tool today.

1. **Get the target API's Swagger/OpenAPI JSON.** Orchestrator's own API
   docs page is a safe example (needs admin rights to export). Confirm
   whether your target system is cloud-reachable — one live attempt to
   reach an **on-prem-only** internal API from a cloud connector failed
   with an HTTP 400; on-prem APIs generally need bots running on-prem to
   reach them.
2. **Integration Service → Connectors → Build your own connector.** Import
   the Swagger/OpenAPI JSON — either upload the file or paste its URL
   directly.
3. **Select which endpoints to expose.** Limit to read (`GET`) operations
   unless you specifically need write access — this is a security
   recommendation, not just a convenience.
4. **Configure authentication.** For UiPath Orchestrator specifically, you
   first need a **UiPath External Application** (Admin → External
   Applications) providing a client ID and scopes. Point secret values to
   an Orchestrator **Asset** rather than hardcoding them.
5. **Publish the connector.** This step is easy to miss and is the most
   common reason a connector doesn't show up later as a tool.
6. **Test the connection** directly in the Integration Service UI — expect
   an HTTP 200.
7. **Add it as a Tool** in Agent Builder: click "+" under Tools → search
   under **Activities** (not "Connections") by connector/activity name →
   select the specific operation you need.

### Checkpoint

- [ ] Connector is published (not just created)
- [ ] Test connection returns success
- [ ] Connector activity is selectable as a Tool in Agent Builder
- [ ] Agent successfully calls the tool and returns a real result for a
      test prompt

### Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Connector doesn't appear as a tool option | Not published | Publish the connector, then retry |
| Can't find the connector under "Connections" in the Tools panel | Wrong search location | Search under **Activities**, not Connections |
| HTTP 400 or connection failure to an internal API | Target system is on-prem, connector is cloud-hosted | Route through an on-prem-capable bot/robot instead of a direct cloud connector |
| Governance-policy warning referencing an "Automation Ops Integration Service Policy" | Org-level policy restricting the connector | Escalate to your platform admin / office hours — this wasn't resolved live in any delivery observed |
| Agent replies with stale/wrong context on a follow-up question (e.g., re-uses a prior folder name it wasn't asked about) | Conversational context carrying over incorrectly between turns | Be explicit in follow-up prompts rather than assuming the agent tracks scope correctly |

## A brief note on IXP as a tool

IXP (Intelligent Xtraction & Processing — Document Understanding,
Communications Mining, and Generative Extraction) can also be exposed to
an agent as a tool, the same way an Integration Service connector is. Full
hands-on IXP work is covered in
[Days 3–10, Day 9](../days-3-10/day-9.md) — the short version for
today: IXP gives you visibility into taxonomy, per-field confidence, and
validation state that you lose if you extract documents with a generic
LLM prompt instead.

Continue to [Human-in-the-Loop & Escalation Design](4-hitl-and-escalation.md).
