# Hands-On Lab: Build a Conversational Agent

## Business/technical context

Every recorded delivery built some form of conversational agent as the Day
2 anchor exercise — an assistant scoped to a narrow, real task (monitoring
Orchestrator activity, answering documentation questions, querying an
internal system). This lab is deliberately built around a **known rough
edge**: attaching a tool via a not-yet-fully-reliable MCP path. That's
included on purpose — recovering gracefully from a partial failure is a
skill you'll need constantly once you're past the bootcamp.

## Learning objective

Build a working UiPath **conversational agent**, scoped to a specific task,
and practice recovering when an attempted capability (an MCP-based tool)
doesn't work as expected.

## What participants will build

A conversational agent that can answer questions within a narrow, defined
scope — for example, an IT-team assistant for monitoring Orchestrator
activity (read-only), or a documentation assistant scoped to official
UiPath docs. Pick whichever maps closer to your own use case.

## Prerequisites

Completed Day 1's [Hands-On Lab](../day-1/4-hands-on-lab-sentiment-agent.md),
authenticated coding agent, and (if attempting the MCP path) admin rights
to create an External Application.

## Estimated duration

90 minutes, including troubleshooting time. Plan for the MCP-tool attempt
to consume 30-45 minutes before you decide whether to keep debugging it or
fall back — don't let it eat the whole session.

## Products & tools used

Your coding agent · UiPath Studio Web (Agent Builder — Conversational) ·
Integration Service (fallback tool path) · Orchestrator (Admin → External
Applications, Agents, Deploy)

## Demo

=== "Coach View"

    **Purpose**

    Model the exact sequence participants will follow: specific prompt →
    plan mode → clarifying questions → attempted tool creation → discover
    the tool wasn't actually created → recover with a fallback.

    **Key message**

    > "Say 'UiPath conversational agent' explicitly." A vague prompt has
    > previously produced a Python/pro-coded conversational agent embedded
    > in a pro-coded app instead of a native UiPath one — the same
    > agent-type ambiguity from Day 1, showing up again here.

    **What to show on screen**

    1. New coding session, Plan Mode on.
    2. A specific prompt naming the agent type, scope, read/write
       boundary, and deployment target (see the exercise prompt below).
    3. Let Plan Mode's clarifying questions play out.
    4. Approve, let it build — including its attempt to create a tool.
    5. When the "tool attachment" step reports done but doesn't actually
       work, name it out loud: "this is a known gap, not something you did
       wrong."
    6. Pivot live to the fallback (a documentation/web-search-only agent,
       or a custom Integration Service connector) and get a working demo.

    **Expected demo outcome**

    A deployed conversational agent that correctly answers in-scope
    questions and correctly **declines** out-of-scope requests (e.g., asks
    it to take an action, and it should say that's outside what it can do
    given its current tools).

    **Recovery guidance if the demo fails**

    This is the demo where "failure" is part of the lesson. If the MCP
    tool doesn't attach:

    1. Say so plainly — don't paper over it.
    2. Rebuild the same agent with only the built-in **web search** tool,
       scoped to official documentation.
    3. Show that a correctly-scoped agent still refuses out-of-scope asks
       gracefully — that's a success, not a consolation prize.

    **Transition into the participant exercise**

    "Now build your own — pick a real, narrow task, and expect at least one
    thing not to work exactly as planned."

=== "Participant View"

    **What you'll observe**

    A live build that includes a real failure (an MCP-tool attachment that
    silently didn't work) and a live recovery.

    **What you'll reproduce**

    The same pattern with your own scope: specific prompt, plan mode,
    attempt a tool, verify it actually works (don't trust a "done" status
    message alone), fall back if it doesn't.

## Exercise: Build Your Conversational Agent

### Objective

Build, deploy, and verify a conversational agent scoped to a specific,
narrow task.

### Starting point

An authenticated coding agent, Day 1's agent still deployed as a reference
point.

### Build steps

1. **Start a new session and turn on Plan Mode** — you're likely
   underspecified on the details, which is exactly when Plan Mode earns
   its keep.

2. **Write a specific prompt.** At minimum, state:
   - That you want a **UiPath conversational agent** (say those exact
     words)
   - Its scope (what it should help with, and what it explicitly should
     **not** do — e.g., "read only, never write")
   - Deployment target (your org/tenant)

   Example starting point (adapt to your own use case):

   ```text
   Create a UiPath conversational agent to assist the IT team with
   Orchestrator automation monitoring. Scope: processes, folders, queues,
   jobs. It should only read, never write. Deploy to this organization:
   {{ training_url }}.
   ```

3. **Work through Plan Mode's clarifying questions** — expect to be asked
   which resource types to include, what to name the agent/project, and
   which deployment channel to target (Orchestrator, with access via
   UiPath Assistant, Studio Web chat, Teams, or embedded in a pro-coded
   app).

4. **Approve the plan and let it build.** If your plan includes creating a
   new tool (an MCP server, or an Integration Service connector), pay
   attention to how it's built — this is the step most likely to need a
   recovery move.

5. **Verify the tool was actually created — don't trust a status message
   alone.** Check the tool in Orchestrator/Integration Service directly.
   If your plan involved an MCP-based tool and it reports "done" but you
   can't find an actual MCP server: that's the known gap (see
   [Tools & Integrations](3-tools-and-integrations.md)). Don't keep
   retrying the same prompt.

6. **If the tool didn't actually get created, recover:**
   - Rebuild with only the agent's **built-in web search tool**, scoped to
     a specific source (e.g., official UiPath documentation), **or**
   - Build a [custom Integration Service connector](3-tools-and-integrations.md#hands-on-build-a-custom-integration-service-connector)
     for the specific API call you need, and attach that instead.

7. **Deploy** to Studio Web, then to Orchestrator (UiPath → Agents →
   Deploy Agents).

8. **Test both in-scope and out-of-scope questions.** Confirm the agent
   answers correctly within scope, and **declines appropriately** when
   asked to do something outside its tools/permissions (e.g., asked to
   take an action it only has read access for).

### Checkpoint

- [ ] Agent is deployed and reachable (Studio Web chat, or your chosen
      deployment channel)
- [ ] At least one in-scope question gets a correct, sourced answer
- [ ] At least one out-of-scope/action request is correctly declined
- [ ] If a planned tool didn't actually get created, you've verified that
      directly (not just trusted a status message) and have a working
      fallback deployed instead

### Expected output

A deployed conversational agent, verified working within its stated scope,
with a documented fallback if your first tool-attachment attempt didn't
pan out.

### Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Agent reports a tool/MCP server was created, but you can't find it in Orchestrator | Known pre-GA gap — the build step can silently not complete | Verify directly in Orchestrator/Integration Service; don't retry the same prompt — switch to the documented fallback |
| A tool call fails with a permissions error even though the tool exists | Likely a shared-folder/scope permission issue, not a broken tool | Test against your own personal workspace/folder instead of a shared one to isolate the cause |
| Got a Python/coded conversational agent instead of a native UiPath one | Prompt didn't specify agent type explicitly | Re-prompt, explicitly asking for a "UiPath conversational agent" |
| Deployed agent shows a "debug\_" prefix or lands somewhere unexpected | Deployed without first creating/selecting a dedicated Orchestrator folder | Create/select a target folder before deploying, the same way you would for a classic RPA package/process |
| Agent carries over context incorrectly between conversational turns (e.g., assumes a folder/scope from a previous question) | Conversational context bleeding across turns | Be explicit about scope in every follow-up question rather than assuming context tracking is correct |

### Extension challenge

If your first build used the web-search fallback, go back and attempt the
custom Integration Service connector path for a real API relevant to your
own use case — this is closer to what you'll actually need for your Day
10 demo.

### Cleanup / next steps

Leave the agent deployed. Continue to
[Coded Agents & Production Readiness](6-coded-agents-and-production-readiness.md).
