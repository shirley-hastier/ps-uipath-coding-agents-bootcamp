# 1. Installing the CLI and Skills

## Install the `uip` CLI

```bash
npm install --save-dev @uipath/cli
```

## Install UiPath skills for your coding agent

```bash
npx uip skills install --agent claude --local
```

!!! note
    Skills are installed per coding agent. If you use more than one agent
    (Claude Code, Codex, Cursor, etc.), install the skill set separately for
    each.

## Verify the install

```bash
npx uip --version
```

You should see a version number printed with no errors. If you hit an
authentication prompt, log in with:

```bash
npx uip auth login
```
