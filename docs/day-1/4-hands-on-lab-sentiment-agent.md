# Hands-On Lab: Build a Low-Code Agent

## Business/technical context

Every recorded delivery of this bootcamp — the customer pilot and all three
internal 101 sessions — used the same first build: a **sentiment analysis
agent**. It's a good first lab because it's small enough to build and
evaluate in under two hours, but touches the entire loop you'll reuse for
every later exercise: build → deploy → evaluate → iterate.

## Learning objective

Build, deploy, and evaluate a working UiPath low-code agent end to end,
using your coding agent of choice — and experience firsthand why prompt
specificity and Plan Mode matter.

## What participants will build

A UiPath **low-code agent** that classifies free-text input as positive,
negative, or neutral sentiment (with a confidence score), deployed to your
cohort's UiPath environment and validated with at least one evaluation set.

## Prerequisites

Completed [Environment Setup](2-environment-setup.md) — authenticated
coding agent, UiPath skills visible via `/uipath`.

## Estimated duration

90–120 minutes for the core build + deploy + evaluate loop. Add 30-plus
minutes if you attempt the GitHub-publish or Autopilot extension challenges
below.

## Products & tools used

Your coding agent (Claude Code / Codex / Cursor) · UiPath CLI (`uip`) ·
UiPath Studio Web (Agent Builder, Evaluators) · Orchestrator (deployment
target) · optionally GitHub

## Architecture overview

```text
You (prompt) → Coding Agent → UiPath low-code agent scaffold
                                      |
                                      v
                         agent.json (model, input/output schema, prompt)
                                      |
                                      v
                   uip CLI: init → validate → bundle → upload
                                      |
                                      v
                    Orchestrator / Studio Web (Agent Builder)
                                      |
                                      v
                          Evaluators (default + custom)
```

`agent.json` is the agent's definition — model settings, input/output
schema, and the prompt template. Your coding agent writes this file for
you; you rarely need to hand-edit it, but understanding what's in it makes
debugging much faster.

## Demo

=== "Coach View"

    **Purpose**

    Show the full loop once, live, before participants try it themselves —
    including a deliberately underspecified prompt, so they see Plan
    Mode's clarifying questions in action.

    **Key message**

    A vague prompt is not wrong, it's an opportunity — Plan Mode will
    surface the decisions you didn't make explicit. Watch it happen, then
    make your own prompt more specific when you build your own agent.

    **What to show on screen**

    1. Type a deliberately generic prompt: *"Build a UiPath sentiment
       analysis agent"* — no folder, no agent type, no output shape
       specified.
    2. Turn on Plan Mode. Let the clarifying questions play out live: input
       format, output shape (label only vs. label + confidence vs. label +
       confidence + rationale), whether to include evaluations, deployment
       target.
    3. Approve the plan, let it build.
    4. Deploy, then run one test input live and show the result in Studio
       Web.

    **Expected demo outcome**

    A published low-code agent with at least a default evaluator, one
    successful test run visible in Studio Web.

    **Questions to ask participants**

    - "What did Plan Mode ask you that it *didn't* ask your neighbor, for a
      similar prompt?"
    - "If you had specified the output schema up front, what would you have
      told it?"

    **Likely questions & recommended answers**

    | Question | Answer |
    |---|---|
    | "My agent didn't create evaluation sets automatically — is that broken?" | No — this varies by run. If missing, just ask: "create evaluation sets for this solution, covering every classification (positive/negative/neutral)." |
    | "My evaluation score is much lower than my neighbor's for what looks like the same agent" | Very likely the default evaluator is scoring more than the label (e.g., also grading free-text rationale text, which varies run to run). Edit the evaluator to check only the field that matters, or build a custom evaluator (Day 2 topic, but you can preview it here). |
    | "Studio Web still shows my agent as a draft, but the CLI said it published successfully" | Publishing a package to Orchestrator and creating/registering the project in Studio Web are two separate steps. Ask your agent to also upload/register it in Studio Web. |

    **Recovery guidance if the demo fails**

    Live demos of this exact lab have hit real, non-scripted failures —
    treat them as teaching moments rather than derailments:

    - **Wrong tenant deployed to** — re-authenticate with the explicit
      `--authority`/`--tenant` form and ask the agent to redeploy. This has
      happened live to the instructor, not just participants.
    - **"Assertion failed to execute" on an evaluation run** — the
      generated evaluation set is likely missing expected-output values.
      Export the evaluation set's JSON schema, hand it back to the agent
      with instructions to regenerate a fully-formed set including expected
      outputs, and re-import.
    - If nothing works on screen, fall back to narrating the architecture
      diagram above and let participants build ahead in parallel — don't
      block the whole room on one demo failure.

    **Transition into the participant exercise**

    "Now it's your turn — and this time, you'll write your own prompt, not
    copy mine."

=== "Participant View"

    **What you'll observe**

    The coach building the same kind of agent you're about to build, using
    a deliberately vague prompt so you can see what Plan Mode asks for.

    **What you'll reproduce**

    The same loop, but with your **own** prompt and your **own** choices at
    each clarifying question — this is intentional. Everyone should get a
    slightly different agent.

    **Why this matters**

    You'll reuse this exact loop (build → deploy → evaluate → iterate) for
    every remaining exercise in the bootcamp, including your real use case.
    Get comfortable with it now on a low-stakes example.

## Exercise: Build, Deploy, and Evaluate Your Sentiment Agent

### Objective

Build your own UiPath low-code sentiment-analysis agent, deploy it, and get
at least one passing evaluation run.

### Starting point

An authenticated coding agent with UiPath skills installed (from
[Environment Setup](2-environment-setup.md)). Nothing built yet.

### Build steps

1. **Confirm you're authenticated to the right environment** before you
   start building — check the org/tenant echoed back by `uip login`. More
   than one delivery has had a participant (and once, the instructor)
   accidentally deploy to the wrong tenant because this wasn't checked
   first.

2. **Write your own prompt.** Don't copy the coach's example verbatim —
   practice being specific. At minimum, state:
   - That you want a **UiPath low-code agent** (not a coded/Python agent)
   - What it should classify (e.g., free-text customer feedback, support
     tickets, social media comments — your choice)
   - Whether you already know your deployment folder/target (if so, say so
     up front — it saves the agent from spending tokens figuring it out)

   Example starting point (make it your own):

   ```text
   Build a UiPath low-code agent that classifies the sentiment of free-text
   customer feedback as positive, negative, or neutral, with a confidence
   score. Use plan mode first.
   ```

3. **Work through Plan Mode's clarifying questions.** Expect to be asked
   about input format, output shape, whether to include a confidence score,
   and whether to generate evaluation sets. Answer based on what you
   actually want — there's no single right answer.

4. **Approve the plan and let it build.** Do not blanket-approve a "bypass
   all permissions" option if offered — review what's being requested.

5. **Deploy.** If your agent doesn't ask where to deploy, tell it
   explicitly: your org, tenant, and (if you have one) target folder.

6. **Run a test.** Give it a piece of text with an obvious sentiment (e.g.,
   a clearly negative complaint) and confirm the output makes sense.

7. **Check for evaluation sets.** If none were created automatically, ask
   explicitly: *"create evaluation sets for this agent, covering positive,
   negative, and neutral classifications."*

8. **Run the evaluation** from Studio Web and check the score.

### Checkpoint

- [ ] Agent is visible and published in Studio Web (not stuck in draft)
- [ ] At least one manual test run returns a sensible classification
- [ ] At least one evaluation set exists, covering all three sentiment
      classes
- [ ] You've run the evaluation at least once and reviewed the score

### Expected output

A published low-code agent in Studio Web, one or more evaluation sets
attached, and at least one evaluation run with a visible score. Your exact
output schema, evaluator count, and score will likely differ from your
neighbor's — that's expected.

### Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Agent built but shows as "draft" in Studio Web despite CLI reporting success | Publishing to Orchestrator and registering in Studio Web are separate steps | Ask the agent to also upload/register the solution in Studio Web |
| No evaluation sets were generated | Not every run auto-generates them | Prompt explicitly: "create evaluation sets covering every classification" |
| Evaluation run fails with "assertion failed to execute" | Generated evaluation set is missing expected-output values | Export the eval set's JSON schema, ask the agent to regenerate a complete set including expected outputs, re-import |
| Evaluation score is surprisingly low compared to peers | Default evaluator may be scoring more fields than just the classification label (e.g., free-text rationale) | Edit the evaluator to check only the field(s) that matter, or note this for the custom-evaluator topic on Day 2 |
| "Cannot find a resource" type error referencing a data source | Some direct data-source-as-tool integrations are still in preview and can be unreliable | Use a small RPA/API tool to fetch the data and pass it in as an input instead of direct access, or (for small, rarely-changing reference data) paste it directly into the system prompt |
| Deployed, but can't find the agent afterward | Deployed to the wrong org/tenant, or into a shared folder you don't have visibility into | Re-check `uip login`'s echoed org/tenant; redeploy to your own workspace/folder if it landed in a shared one |
| Got a Python/coded agent instead of a low-code agent | Prompt didn't specify agent type | Re-prompt explicitly asking for a "UiPath low-code agent" |

### Extension challenge

Pick one, time permitting:

- **Autopilot path.** Build the *same* kind of sentiment agent a second
  way: inside Studio Web, use **Autopilot** (Create New → Agent →
  Autonomous) and type your agent description directly into the generation
  box, instead of going through your external coding agent. Compare the
  result — schema choices, generated evaluators — against your first build.
- **Push to GitHub.** Ask your coding agent to push the solution to a new
  GitHub repository. Notice what it generates alongside your code (an
  `AGENTS.md`/similar file documenting the solution and which skills were
  used) — this is exactly the kind of context file that makes it easier
  for a teammate (or you, after time away) to pick the project back up.
- **Custom evaluator preview.** If your default evaluator's score doesn't
  reflect what you actually care about, ask your coding agent to draft a
  custom evaluator, telling it specifically what the default evaluator got
  wrong (e.g., "it's scoring the rationale text, I only care about the
  sentiment label"). Full custom-evaluator design is a Day 2 topic — this
  is a preview.

### Cleanup / next steps

Leave your agent deployed — you'll build on this pattern later in the
bootcamp. Continue to
[Reflection & Day 2 Preview](5-reflection-and-day-2-preview.md).
