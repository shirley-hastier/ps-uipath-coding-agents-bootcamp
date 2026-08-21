# Day 8: Conversational Agents

**Focus:** Multi-turn flows, context, fallback, escalation, transcript tests
**Checkpoint:** Write 3 transcript-style tests

## Why this matters

This is also the **evaluation completed** executive-tracking milestone
(see [Program Overview](../program-overview.md#executive-tracking-checkpoints)).
Day 2's [conversational agent lab](../day-2/5-hands-on-lab-conversational-agent.md)
proved your agent answers correctly within scope. Day 8 is about proving
it consistently — including the cases where it should say "I can't do
that," not just the cases where it succeeds.

## A real example worth reusing as a template

From a live Day 2 delivery: a conversational agent scoped to
Orchestrator-monitoring (read-only) correctly answered "How can I set up
an unattended robot environment?" citing documentation sources, and then
correctly **refused** the follow-up "Can you enable that for me?" —
because that would require write access it didn't have. That refusal is
just as much a passing test as the correct answer.

## Self-paced exercise: write 3 transcript-style tests

A transcript-style test is a short, realistic multi-turn exchange with an
expected outcome — not just a single input/output pair. Write 3, covering
different categories:

1. **A correct in-scope answer**, including a follow-up question that
   depends on context from the first turn (tests multi-turn context
   handling, not just single-shot Q&A).
2. **A correct refusal** — a request the agent should decline given its
   scope/permissions, and what it should say instead of just failing
   silently or hallucinating an answer.
3. **A context-tracking edge case** — a scenario designed to catch the
   real failure mode observed live, where an agent incorrectly carried
   over scope from an earlier turn (e.g., assumed a specific folder or
   system from a previous question instead of asking for clarification).

Template:

```text
Test: <name>
Turn 1 (user): <message>
Expected: <what the agent should say/do>
Turn 2 (user): <follow-up message>
Expected: <what the agent should say/do, given Turn 1's context>
Pass/Fail: <run it, record what actually happened>
```

## Fallback behavior to test explicitly

- What happens when a tool call fails (not just when the agent decides to
  refuse)? Does it say so plainly, or does it guess?
- What happens when a question is ambiguous — does it ask a clarifying
  question, or assume a scope it shouldn't?

## Checkpoint

- [ ] 3 transcript-style tests written, covering: correct in-scope answer,
      correct refusal, and a context-tracking edge case
- [ ] All 3 have actually been run against your deployed agent, with
      pass/fail recorded
- [ ] Any failing test has a follow-up action (prompt/schema/guardrail fix)
      identified

## Office hours discussion prompts

1. What changed since yesterday?
2. What's blocked?
3. What will you complete next?
