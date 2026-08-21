# Exercise: Environment Setup

**Estimated duration:** 30–75 minutes. Every recorded delivery has run long
here — at least one attendee typically hits a PATH, permissions, or
tenant-auth issue. Budget for it rather than treating it as an exception.

## Objective

Get your coding agent authenticated to the correct UiPath organization and
tenant, with UiPath skills installed and discoverable, so you're ready to
build.

## Starting point

You should already have, per the [preflight checklist](index.md#preflight-checklist-coach-confirm-before-day-1-starts):

- Node.js installed
- A coding agent installed (Claude Code, Codex, Cursor, or similar)
- An IDE or terminal you're comfortable in

## Build steps

### 1. Choose your terminal / IDE

All of the following are valid — pick whichever you're most comfortable in:

- PowerShell or Command Prompt
- VS Code, with the Claude Code / Codex extension installed (Extensions
  panel → search the extension name → Install)
- UiPath Studio Desktop's built-in terminal panel

!!! warning "Needs validation — Studio Desktop version"
    The terminal panel requires a relatively recent Studio Desktop release
    (one delivery specifically warned that the **LTS** channel is too old —
    you need the **STS** channel). The exact minimum build number was
    unclear across sources — confirm the current minimum with your coach
    rather than guessing from a version number.
- The standalone coding-agent desktop app (search for "Claude" or "Codex"
  in your OS's app search)

Windows users: on a locked-down/IT-managed machine, a global npm install
(`-g`) may be blocked by policy. If so, use `npx` instead of a global
install (see step 3), or install locally into a project folder.

### 2. Verify your prerequisites

Run each of these and confirm you get a real version number back, not a
"not recognized" error:

```powershell
git --version
node -v
npm --version
uip --version
uip --help
```

If `node -v` fails, Node.js isn't installed — install it from
[nodejs.org](https://nodejs.org) (LTS) before continuing.

If `uip --version` fails, install the UiPath CLI:

```powershell
npm -g install @uipath/cli
```

!!! warning "Needs validation — CLI is pre-GA and evolving"
    This exact command is what the master deck documents. However, every
    live delivery observed a **different**, more interactive install/skills
    flow (see step 3) — a sign the CLI's install and skills UX changed
    between sessions. Run `uip --help` on the day to confirm current syntax
    rather than trusting either source blindly. This is expected: the
    product is explicitly pre-GA, and feedback from cohorts like this one is
    part of what improves it.

### 3. Install UiPath skills

The documented path (master deck), for Claude Code:

```powershell
claude plugin marketplace add https://github.com/UiPath/skills
claude plugin install uipath@uipath-marketplace
```

*Using Codex, Cursor, or another coding agent? Replace `claude` with your
agent's equivalent command.*

In practice, multiple deliveries instead walked through an **interactive**
skills installer: run the install/skills command, then use arrow keys +
<kbd>Space</kbd> to select which agent(s) to install skills for, then
<kbd>Enter</kbd> to confirm. If your coach's demo looks like that instead of
the two commands above, follow along with what's on screen — both are
installing the same UiPath skills, just via different CLI UX.

### 4. Authenticate

Default login (targets UiPath Cloud):

```powershell
uip login
```

If this cohort is using a non-default environment (a staging org, or a
specific tenant), use the explicit form instead:

```powershell
uip login --authority {{ training_url }} --tenant "{{ training_tenant }}"
```

Confirm the org and tenant name **echoed back** by the CLI after login
before doing anything else. Every delivery of this bootcamp has had at
least one attendee accidentally build or deploy against the wrong
tenant/org because of a login mismatch — it's cheap to check now and
expensive to discover after a deploy.

!!! danger "Common mistake: wrong tenant"
    In one delivery, the instructor's own agent was deployed to the wrong
    tenant because of a login mix-up, and had to be re-authenticated and
    re-deployed. In another, a participant's login failed silently because
    they typed the tenant name with a small typo (missing a trailing "s").
    Tenant names must match **exactly**.

### 5. Verify skills are visible to your coding agent

From inside your coding agent's chat, type:

```text
/uipath
```

This should list the installed UiPath skill commands. If it doesn't show
anything, or your agent says it doesn't have access to a skill you expect,
try:

```powershell
uip update
```

An outdated CLI is the most common cause of "missing" skills across every
delivery observed.

## Checkpoint

Before moving on, confirm:

- [ ] `uip --version` and `uip --help` both return valid output
- [ ] `uip login` (or the explicit `--authority`/`--tenant` form) succeeds,
      and the echoed-back org/tenant is the one you expect
- [ ] `/uipath` inside your coding agent lists UiPath skills

## Expected output

A terminal session where all prerequisite commands succeed, and your coding
agent can list UiPath skills when asked. You have not built anything yet —
this is purely readiness.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `node`/`npm` "not recognized" | Node.js not installed, or not on PATH | Install Node.js LTS from nodejs.org; restart your terminal |
| Coding agent binary (e.g. `claude --version`) "not recognized" after install | Install location isn't on your PATH environment variable | Windows: System Properties → Advanced → Environment Variables → edit the **`Path`** *System* variable → add the folder from the agent's install output → restart your terminal. Or, open the agent's desktop app and ask it to add itself to PATH for you. |
| Global npm install fails / blocked | IT policy blocks global installs on this machine | Use `npx uip <command>` instead of a global install, or install locally into a project folder and reference it explicitly in your IDE's settings |
| `uip login` succeeds but agent seems to hit the wrong org | Default `uip login` targets UiPath Cloud, not this cohort's environment | Re-run with explicit `--authority` and `--tenant` flags; confirm the echoed-back org/tenant |
| Skill install "not recognized" or fails | Coding agent app itself isn't installed yet, or CLI is outdated | Confirm the coding agent app runs first (`claude --version` etc.), then re-run skills install; try `uip update` |
| Agent says it doesn't have access to a skill you expect | Outdated UiPath CLI | `uip update`, then re-check with `/uipath` |
| Everything installed, but the coding agent still can't find the `uip` CLI | The agent's working environment doesn't see your global install (common in IDE-embedded terminals) | Add a project-level rule/config pointing at the CLI's install path, or install the CLI locally into the project instead of globally |

## Cleanup / next steps

None needed — this exercise only sets up tooling. Continue to
[Prompting Coding Agents for Better Outcomes](3-prompting-coding-agents.md).
