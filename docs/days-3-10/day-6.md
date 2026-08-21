# Day 6: MCP Server Patterns

**Focus:** UiPath MCP, external MCP, tool contracts, security review
**Checkpoint:** Create a tool catalog

## Why this matters

Day 2 introduced MCP servers conceptually and flagged a real limitation:
agent-driven MCP tool creation has been observed to silently not complete
in more than one live delivery (see
[Day 2: Tools & Integrations](../day-2/3-tools-and-integrations.md#what-is-mcp)).
Day 6 goes deeper on the pattern and, critically, on the **security review**
angle that Day 2 didn't have time to fully resolve.

## Recap: MCP server types

| Type | What it does |
|---|---|
| **UiPath (hosted)** | Exposes UiPath artifacts/capabilities as tools to external systems |
| **Coded** | Host your own MCP server (via the UiPath SDK) wrapping custom logic or an API call |
| **Command** | Bring an MCP server from an external package feed via a command |
| **Remote** | Tunnel connection to a remote/vendor MCP server |

## Security review

A real question raised live and worth working through for your own use
case: for MCP the same way as for a traditional API, **you can scope
exactly which tools/functions are exposed** per MCP server — this is your
main lever for keeping an MCP integration safe. Concretely:

- Limit exposed functions to what the agent genuinely needs (read-only
  where possible, the same guidance as the [custom Integration Service
  connector exercise](../day-2/3-tools-and-integrations.md#hands-on-build-a-custom-integration-service-connector))
- Check your organization's compliance/security guidelines for AI tool
  access before connecting an MCP server to a production system
- If you're unsure, escalate to your security team or platform admin
  rather than guessing — this was explicitly the answer given the one time
  this was asked live

## Self-paced exercise: build a tool catalog

1. **List every tool your use case's agent(s) will plausibly need** —
   read operations, write operations, and anything cross-system.
2. **For each tool, record:**
   - What it does (in plain language — this doubles as the tool
     description the agent will reason from)
   - Read or write?
   - Which system it touches
   - How it's implemented (Integration Service connector, MCP server,
     RPA workflow, another agent)
   - Who approved it for this scope (you, a security reviewer, no one yet)
3. **Flag anything write-capable or cross-system** for an explicit security
   review before it goes live in your build.
4. **If you attempt an MCP-based tool**, verify it was actually created
   (check the Orchestrator MCP Servers screen directly) — don't trust a
   coding agent's "done" status alone, per the Day 2 gotcha.

## Checkpoint

- [ ] Tool catalog written for your use case: name, description,
      read/write, system, implementation, review status
- [ ] Every write-capable or cross-system tool has an explicit
      review status recorded (not left blank)
- [ ] If an MCP-based tool was attempted, its existence was verified
      directly, not just assumed from a status message

## Office hours discussion prompts

1. What changed since yesterday?
2. What's blocked — did you hit the MCP tool-creation gap from Day 2?
3. What will you complete next?
