# Optional Lab D: Pro-Coded Dashboard for Your Sentiment Agent

## Business context

On Day 1 you built an agent that classifies sentiment. A manager who wants
to *see* what it's doing isn't going to read job logs. They want a
dashboard: how many runs, how many positive, negative, or neutral, and a
way to filter to the negative ones and dig in. A pro-coded app is how you
build that view, and your coding agent can build it from a description.

## Learning objective

Build a pro-coded app that reads your Day 1 agent's job history, then
refine it by describing changes in plain language the way a real customer
would ask for them.

## What you'll build

A web dashboard that shows your sentiment agent's runs with sentiment and
confidence for each, first on `localhost`, and optionally deployed to the
platform.

## Prerequisites

- The [common checklist](index.md#before-you-start-any-of-them) is done
- Your Day 1 sentiment agent is deployed **and has run several times** with
  different text (positive, negative, neutral). A dashboard has nothing to
  chart without job history
- Node.js and the Coded Apps skill available to your coding agent
- Rights to create an **External Application** (Admin → External
  Applications)
- The "Build Your First Coded App" chapter of the
  [UiPath for Coding Agents Deep Dive](https://academy.uipath.com/courses/uipath-for-coding-agents-deep-dive)
  Academy course open for reference

## Estimated duration

60-90 minutes. Authentication setup is the part most likely to take longer
than planned.

## Products and tools used

Your coding agent · Coded Apps skill and the UiPath TypeScript SDK ·
Orchestrator (jobs, Apps) · External Applications · optionally Data Fabric

## Exercise: Build the dashboard

### Objective

Get a working dashboard of your agent's runs, then improve it in two or
three rounds of plain-language changes.

### Starting point

The deployed Day 1 sentiment agent, with at least five or six job runs.

### Build steps

1. **Generate job history first.** Run your agent several times with clearly
   positive, clearly negative, and neutral text. Confirm the jobs appear in
   Orchestrator.

2. **Create the External Application** (Admin → External Applications):
   - Create it as **non-confidential**. A confidential app caused a sign-in
     failure for nearly everyone in one session
   - Set the redirect URL to `localhost` with the **same port** your app
     will run on. A port mismatch looks exactly like a sign-in bug
   - Grant only the scopes the dashboard needs to read jobs

3. **Keep configuration out of your prompt.** Put the organization, tenant,
   client ID and URL in a `.env` file the app reads. Hardcoding them in the
   prompt is fine for a demo and a bad habit for anything real.

4. **Turn on Plan Mode,** then ask for the dashboard. Open the Academy guide
   and use its prompt structure for the connection details. Describe what you
   want to see:

   ```text
   Create a UiPath coded app that shows a dashboard of my sentiment analysis
   agent's job history from Orchestrator. Show each run with its sentiment
   and confidence, a count of how many were positive, negative and neutral,
   and a filter so I can view only the negative ones. Use the Coded Apps
   skill and the UiPath TypeScript SDK. Read my settings from the .env file.
   ```

5. **Choose "Coded app"** when asked. Don't choose "Action app". That's a
   different thing, used for human review tasks.

6. **Approve the SDK use** when the agent asks, and let it build. This takes
   a few minutes.

7. **Run it locally** and sign in. If you see zeros or default values, tell
   the agent: "It has no data. Pull the information from the sentiment
   agent's jobs in Orchestrator," and check the process name matches yours.

8. **Refine it, one change per prompt.** Treat yourself as the developer on a
   customer's change request. These came up in the delivery session:
   - Confidence shows as `1.0%` when it should be `98%`:
     "The confidence is displaying 1.0% instead of 98%. Fix that."
   - Colors: "Show confidence above 50% in green and below 50% in red."
   - "Color the sentiment column the same way: positive, neutral, negative."

9. **Re-test with one positive and one negative run** after each change.

10. **Optional: deploy it to the platform.** Ask the agent to build and
    deploy the app to the cloud rather than leave it on `localhost`. It then
    shows up in Orchestrator under your folder's **Apps**.

### Checkpoint

- [ ] The dashboard loads and signs in
- [ ] It shows real runs from your Day 1 agent, with sentiment and
      confidence
- [ ] You applied at least two plain-language refinements and verified each
- [ ] Your client ID and tenant are in `.env`, not hardcoded in your code

### Expected output

A dashboard where you can see run counts by sentiment and filter to the
negative ones, running on `localhost` and optionally on the platform.

!!! warning "Needs validation"
    The exact starting prompt in the Academy guide was pasted from a
    document during the session and never read aloud, so the one above is a
    reasonable description, not the official text. Required scopes weren't
    confirmed either. Use the Academy guide and your coach for both. Cloud
    deployment was only mentioned in passing and not completed on screen, and
    the guide notes the CLI's pack and publish commands are much faster than
    having the agent do it.

### Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Sign-in loops or fails | External app was created as confidential | Create a new **non-confidential** app and give the agent the new app ID |
| Sign-in works on one port, fails on another | Redirect URL port doesn't match the port the app runs on | Make them identical |
| "Application doesn't have this scope" or an entity error | App scopes don't include what the dashboard reads | Add the missing scope, or check the data lives where you think it does |
| Others can't read your Data Fabric entity | Entity was created in a Shared folder | Recreate it in your own workspace |
| Dashboard shows zeros or defaults | No job history, or it's looking at the wrong process | Run the agent more, tell the agent to read the jobs, and check the process name |
| Agent asks "Coded app or Action app?" | Normal prompt | Pick **Coded app** |
| Agent asks for scopes or a client ID you don't remember | Created outside this session | Look them up on the External Application page |
| App won't start, or the CLI isn't found | Wrong terminal or PATH | Try another terminal and re-check `uip --version` |
| Confidence appears as 1.0% | Value is 0-1 but displayed as a percent | Describe the bug and the correct value to the agent |

### Extension challenge

Add a small conversational agent to the page so a user can ask "show me the
most negative run today". A customer proof of concept did exactly this with
a knowledge base. Treat the embedding steps (iframe, or the TypeScript SDK)
as unproven here and check
[Deploying conversational agents](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/conversational-agents-deployment).

### Cleanup and next steps

Keep the app and its `.env` out of any shared repository, since the `.env`
holds your tenant details. If dashboards are in your use case, this is the
same pattern you'd use for your Day 10 demo.
