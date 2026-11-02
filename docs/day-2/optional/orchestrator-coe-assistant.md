# Optional Lab C: Orchestrator Assistant for the Automation CoE

## Business context

The team that runs your automations asks the same questions all day: what
was the last job that ran in this folder, what failed this week, how is the
queue doing. Answering them means opening Orchestrator and clicking through
filters. In this lab you give a **conversational agent** read-only access to
the Orchestrator API through a custom Integration Service connector, so the
team can simply ask.

This is a deeper follow-up to the required
[conversational agent lab](../5-hands-on-lab-conversational-agent.md). Do
that one first.

## Learning objective

Connect a conversational agent to a real API through a custom connector you
build, and confirm it answers in-scope questions correctly and refuses
anything it shouldn't do.

## What you'll build

A published custom connector over a read-only slice of the Orchestrator API,
and a conversational agent that uses it to answer questions about jobs,
processes, folders, and queues.

## Prerequisites

- The [common checklist](index.md#before-you-start-any-of-them) is done
- The required conversational agent lab is done
- Rights to create an **External Application** (Admin → External
  Applications). Several attendees in the sessions couldn't see that menu
  and had to borrow a colleague's. Check yours first
- Rights to read the Orchestrator API documentation (Swagger) for your
  tenant

## Estimated duration

75-90 minutes. Connector and sign-in setup is where most of the time goes.

## Products and tools used

Integration Service (custom connector builder) · Orchestrator (External
Applications, Agents, folders) · Studio Web (Agent Builder, conversational)
· your coding agent

## Exercise: Build the CoE assistant

### Objective

Publish a read-only Orchestrator connector, attach it to a conversational
agent, and verify the agent answers CoE questions.

### Starting point

A conversational agent from the required lab (or a new one), and your
authenticated coding agent.

### Build steps

1. **Build the custom connector** from Orchestrator's Swagger (OpenAPI)
   JSON, following the steps in
   [Tools & Integrations](../3-tools-and-integrations.md#hands-on-build-a-custom-integration-service-connector).
   Don't skip the safety choices there:
   - Expose **read (GET) endpoints only**. This agent should look, not
     touch
   - Put secrets in an Orchestrator **Asset**, not in the connector

2. **Create the External Application** the connector authenticates with, and
   copy its client ID and secret into the connection. Don't forget the
   **token URL** field. Attendees missed it.

3. **Publish the connector.** An unpublished connector never shows up as a
   tool.

4. **Test the connection** in Integration Service and expect HTTP 200.

5. **Ask your coding agent to build the agent.** Turn on Plan Mode and be
   explicit about the type and the limits:

   ```text
   Create a UiPath conversational agent to help our automation CoE team
   interact with Orchestrator. Scope: processes, folders, queues, and
   jobs. It must only read, never write. Use the Orchestrator connector I
   published as its tool. Deploy to this organization: {{ training_url }}
   and tenant: {{ training_tenant }}.
   ```

6. **Add the connector as a tool** if the agent didn't. In Agent Builder
   open **Tools**, click **+**, and search under **Activities** (not
   Connections) for your connector's operations, such as getting job
   results.

7. **Deploy to Studio Web, then to Orchestrator** into a dedicated folder.
   Deploying without choosing a folder puts it in your personal workspace
   and can leave a "debug_" prefix on the name.

8. **Ask it real CoE questions,** replacing the folder name with one you
   have:
   - "What was the last job that ran in the `<folder name>` folder?"
   - "List any errors from the last 20 days."
   - "How many items are waiting in the `<queue name>` queue?"

9. **Ask it something it must refuse,** such as "Stop that job" or "Delete
   that queue item". It should explain that it can only read.

### Checkpoint

- [ ] The connector is published and the connection test returns 200
- [ ] Your operations appear as tools in Agent Builder
- [ ] The agent correctly answers at least two CoE questions
- [ ] The agent refuses at least one write or action request
- [ ] The agent is deployed to a dedicated folder, not a personal workspace

### Expected output

A deployed conversational agent that answers questions about real jobs and
queues from your tenant, and politely declines to change anything.

!!! warning "Needs validation"
    - **Which External Application type to use.** The connector flow
      needed a client ID and secret. A different lab ([Lab D](pro-coded-sentiment-dashboard.md))
      failed for most attendees until the app was created as
      non-confidential. Confirm the right type and scopes with your coach
      before you create one.
    - **A governance policy warning.** One attendee saw a message about an
      "Automation Ops Integration Service" policy that was never resolved
      during the session. If you see it, escalate to your platform admin.
    - **Guardrails.** Don't configure guardrails on the shared training
      tenant (see the [index](index.md#how-these-labs-work)). Whether
      configurable guardrails apply to conversational agents was also left
      unresolved.

### Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Connector doesn't show up as a tool | It isn't published | Publish it, then search again |
| You can't find it when adding a tool | Searching under Connections | Search under **Activities** |
| Connection test fails to authenticate | Missing token URL, or wrong client ID or secret | Re-enter the connection, including the token URL |
| The official Orchestrator connector's activities don't appear | Known to be unreliable for several attendees | Use your own custom connector |
| Tool call fails with a permission error | Shared-folder or scope permission | Test against a folder you own to separate a permission problem from a broken tool |
| The agent reuses the previous folder in a follow-up question | Context bleeding between turns | Name the folder in every question |
| You get a Python or coded agent | Prompt didn't say "UiPath conversational agent" | Re-prompt with those exact words |
| An on-premises API fails with a 400 | A cloud connector can't reach an internal-only system | Reach it through something running on-premises |
| The agent answers beyond its scope | Scope in the prompt was loose | Tighten the system prompt and re-test |

### Extension challenge

Add a second read-only operation, such as queue item details, and ask a
question that needs both tools. Then decide whether this should stay one
agent with more tools or become two specialized agents. Every extra agent
costs another model call, so there's no universal answer.

### Cleanup and next steps

Keep it. Everything you configured here is the same pattern you'll use to
connect an agent to a system of your own. To put a chat window in front of
the team, try [Lab D](pro-coded-sentiment-dashboard.md) next, or see
[Deploying conversational agents](../../resources.md).
