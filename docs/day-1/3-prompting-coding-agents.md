# Prompting Coding Agents for Better Outcomes

*Roughly 15-20 minutes of instruction before the hands-on lab. This is the
last stop before building — keep the examples concrete.*

=== "Coach View"

    **Purpose**

    Give participants a repeatable prompting loop and a short list of
    habits that prevent the most common failure mode: an underspecified
    prompt producing something that technically runs but isn't what the
    business needed (or isn't even the right *kind* of agent).

    **Key message**

    Coding agents are non-deterministic. The fix isn't a "magic prompt" —
    it's a loop (explore, plan, code, verify, run, commit) and a habit of
    being specific about the one or two things that actually matter for
    this task.

    **What to emphasize**

    - **"Low-code UiPath agent" vs. a generic coded agent.** This is the
      single most repeated warning across every delivery of this bootcamp:
      if your prompt just says "build an agent," some participants — and
      at least one real customer — have ended up with a Python/coded agent
      instead of a UiPath low-code agent. Say the words "UiPath low-code
      agent" explicitly.
    - Plan Mode is not mandatory overhead — it's most valuable when you're
      *not* already sure exactly what you want. If you can fully describe
      the outcome up front, skip it and let the agent ask permission for
      specific actions as it goes.
    - Iteration is expected. "More than 90% would not be good enough" on a
      first pass is a normal outcome, not a failure.

    **Suggested narration**

    > "Garbage in, garbage out is a well-known phrase in software — it
    > applies here too. The more content and context you provide, the
    > better the result, and it also helps with token efficiency — the
    > agent spends fewer tokens exploring things you could have just told
    > it."

    **Likely questions & recommended answers**

    | Question | Answer |
    |---|---|
    | "Why did Plan Mode ask me something totally different from what it asked my neighbor, for the same prompt?" | Expected — coding agents are non-deterministic. Different clarifying questions from an identical prompt is normal, not a bug. |
    | "Should I always turn Plan Mode on?" | No. It's most useful when you're underspecified or exploring; if you already know exactly what you want, describing it fully in the prompt is often faster. |
    | "Do slash commands like `/clear` work the same in every coding agent?" | The core commands are conceptually similar across tools, but exact syntax varies. Verify with your specific agent. |

    **Transition into the hands-on lab**

    "Let's put this into practice — you're going to build a real agent in
    the next segment, and you'll pick the prompt yourself."

=== "Participant View"

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
