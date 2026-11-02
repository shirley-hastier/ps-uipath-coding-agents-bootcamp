# Optional Hands-On Labs

Finished the required [conversational agent lab](../5-hands-on-lab-conversational-agent.md)
with time to spare? These four optional labs reuse what you've already
built and set up on Day 1 and Day 2. They're not required and they don't
depend on each other, so **pick one or two** that sit closest to your own
use case rather than trying to do all four.

## The four labs

| Lab | You'll build | Good fit if your use case... | Time |
|---|---|---|---|
| [A. IXP invoice processing](ixp-invoice-processing.md) | An IXP project that extracts fields from invoices | Starts with documents (invoices, forms, statements) | 60-75 min |
| [B. UI automation on UiBank](uibank-ui-automation.md) | An RPA workflow that submits a loan application on a web app | Touches an application that has no API | About 60 min |
| [C. Orchestrator CoE assistant](orchestrator-coe-assistant.md) | A conversational agent that answers questions about jobs and queues | Needs an agent to read from a system through a connector | 75-90 min |
| [D. Sentiment dashboard](pro-coded-sentiment-dashboard.md) | A pro-coded app that charts your Day 1 sentiment agent's runs | Needs a custom UI or reporting view on top of an agent | 60-90 min |

## Before you start any of them

- [ ] You're signed in with `uip login` to the right organization and
      tenant (see [Environment Setup](../../day-1/2-environment-setup.md)),
      and the echoed-back org and tenant are the ones you expect
- [ ] Your CLI is current (`uip update`), because several skills only
      appear on a recent CLI
- [ ] You can see the UiPath skills in your coding agent (`/uipath`)
- [ ] Your Day 1 [sentiment agent](../../day-1/4-hands-on-lab-sentiment-agent.md)
      is still deployed (required for lab D, and a useful reference for
      the others)

## How these labs work

Each lab follows the same loop you used on Day 1: write a specific prompt,
let Plan Mode ask its clarifying questions, build, **verify the result
yourself**, and iterate two or three times. Expect your result to differ
from your neighbor's. That's the coding agent being non-deterministic, not
a mistake.

!!! warning "Needs validation"
    These labs come from what attendees built during the delivery
    sessions, and several steps were never completed cleanly on screen.
    Wherever a prompt, flag, or setting wasn't confirmed, the lab says so.
    If something doesn't match what you see, trust your screen and ask
    your coach.

!!! warning "Needs validation: shared training tenant"
    On the shared staging training tenant, agents that declare a guardrail
    were observed to fault on every run, and agent evaluation runs were
    observed to fail. Both were noticed in August, so check with your
    coach whether they still apply. Until then, don't add guardrails to
    agents you build for these labs, and don't rely on evaluation scores
    there.

## Products and tools used across the labs

UiPath CLI (`uip`) and skills · your coding agent · Studio Web (Agent
Builder) · Studio Desktop (lab B) · IXP (lab A) · Integration Service
(lab C) · Orchestrator (all) · Coded Apps (lab D)
