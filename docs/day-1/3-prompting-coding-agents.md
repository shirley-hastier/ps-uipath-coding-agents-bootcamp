# Prompting Coding Agents for Better Outcomes

*Roughly 15-20 minutes of instruction before the hands-on lab. This is the
last stop before building — keep the examples concrete.*


**What you'll take into the lab**

A short checklist of habits, not a script to memorize. You'll apply
these directly in the next exercise.

## The core workflow

```text
Explore → Plan → Code → Verify → Run → Commit
```

| Step | Example instruction |
|---|---|
| 1. Explore | "Read the existing solution and related files, don't write code yet" |
| 2. Plan | "Use plan mode first — think through the design before building" |
| 3. Code | "Implement the plan and verify it works" |
| 4. Verify | "Run all evaluations, look through what was generated" |
| 5. Run | "Run it end-to-end to make sure it actually works" |
| 6. Commit | "Commit changes with a descriptive message" (requires being authenticated where you're committing to) |

## Top 5 practices

1. **Be specific, not vague.** "Build a UiPath low-code sentiment analysis
   agent that classifies free-text customer feedback" beats "build an
   agent." Say the deployment target, the agent type (low-code vs. coded vs.
   conversational), and any constraints up front if you already know them.
2. **Use Plan Mode when you're not fully sure.** Toggle it via your agent's
   mode selector, or your keyboard's mode-switch shortcut (varies by tool —
   confirm yours), or just say "use plan mode first" in the prompt.
3. **Iterate 2–3 times.** The first version is rarely right. Treat that as
   normal, not a signal something is broken.
4. **Clear context between unrelated tasks.** Use your agent's session-reset
   command (e.g. `/clear`) so unrelated work doesn't bleed into your next
   prompt — or open a separate terminal/session for parallel, unrelated
   work.
5. **Say what must not change.** If you have an existing project, be
   explicit about scope: which files, which folder, which behavior must
   stay untouched.

## A recurring, concrete warning

> "If you're not specific enough and you just say, hey, build an agent, you
> may find some of you will be creating a coded agent instead of a low-code
> agent." — instructor, private-preview delivery

This has happened with a real customer, not just in training. When your
goal is a **UiPath low-code agent**, say those words.

## Power tips

- Give your agent a project-level context file (an `AGENTS.md`/`CLAUDE.md`
  style file) so it reads project-specific conventions automatically
  without you repeating them every session.
- Escalation/authorization prompts: never blanket-approve "bypass
  permissions" options — review what's being requested. This was called
  out explicitly as a security risk in more than one delivery.
- If your agent starts doing something you didn't intend, interrupt it
  immediately (most tools bind this to <kbd>Esc</kbd>) rather than letting
  it keep going and cleaning up after.
- Paste real error messages directly into your prompt rather than
  paraphrasing them — "I'm getting this error in Orchestrator, help me fix
  it" works better with the actual error text attached.
- For secrets (org, tenant, client IDs, tokens): use environment variables
  or a `.env` file, never hardcode them into a prompt or into checked-in
  code.

Now put this into practice — continue to
[Hands-On Lab: Build Your First Agent](4-hands-on-lab-sentiment-agent.md).
