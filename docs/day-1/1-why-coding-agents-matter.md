# UiPath Vision & Why Coding Agents Matter

*Segments 00–02 of Day 1. Roughly 20-25 minutes of instruction — this is
scene-setting, not hands-on. Keep it moving; the goal is context for the
build that follows, not platform mastery.*


**What you'll observe**

A short tour of the UiPath platform's four pillars and where coding
agents fit in the overall development experience — this is context,
not something you'll build yet.

**Why this matters**

Every exercise for the next two weeks maps back to one of these layers.
Knowing the vocabulary now (Agentic Automation vs. Business
Orchestration, builder toolchain vs. agentic automation stack) will
save you time later when a coach says "that's a tool-layer problem" or
"that belongs in orchestration."

## The four pillars

| Pillar | What it does |
|---|---|
| **Agentic Automation** | The execution layer — agents, automations, APIs, document intelligence, connectors, and people combine to execute business tasks and decisions |
| **Business Orchestration** | The coordination layer — Maestro, Case Management, and human-in-the-loop experiences ensure the right work happens at the right time with the right participants |
| **Agentic Testing** | Validates that applications, automations, and agents perform reliably before reaching production |
| **Industry & Department Solutions** | Production-ready, industry-specific solutions built on top of the other three pillars |

This bootcamp focuses on the first two.

## Why coding agents matter

Per the 2025 Stack Overflow Developer Survey (cited in the master deck):

- **70%** of developers now use or plan to use AI coding tools
- **84%** of agent users agree agents have reduced time on specific
  development tasks; 69% agree they've increased productivity
- **66%** are frustrated with AI solutions that are "almost, but not quite
  right" — 45% specifically with debugging AI-generated code

Every delivery of this bootcamp has echoed that last stat back in the room:
coding agents accelerate the parts of the job builders already do —
learning APIs, writing boilerplate, debugging, integrations, tests,
prototypes — but they don't remove the need for a builder who knows what
"correct" looks like.

## From Coding Agents to Production Solutions

The mental model to carry through the rest of the bootcamp:

```text
Builder Toolchain              Agentic Automation Stack           Enterprise Landscape
(Claude Code, Codex, Cursor,    UX → Reasoning → Capability →      Salesforce, SAP, Workday,
 IDE, uip CLI, UiPath skills)   Data → AI/Models → Operations      ServiceNow, custom apps...
        |                       (all governed by AI Trust Layer)          |
        +---------- accelerates how you build ---------------------------+
```

Coding agents help you **build** solutions faster. The UiPath platform
provides the capabilities to **run** them reliably, securely, and at scale
in production. Keep that distinction — it comes up again on Day 2 when we
talk about evaluations, guardrails, and governance.
