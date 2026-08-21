# Day 3: Prompting Coding Agents for UiPath

**Focus:** Outcome prompts, constraints, review loops, acceptance criteria
**Checkpoint:** Rewrite 3 vague asks into build-ready prompts

## Why this matters

By Day 2's end, your use case is selected. Day 3 is about turning "I want
to automate X" into prompts specific enough that your coding agent builds
the *right* thing on the first or second pass, not the fifth. This
reinforces [Day 1's prompting techniques](../day-1/3-prompting-coding-agents.md)
against your own real use case instead of a training example.

## Self-paced exercise

1. **Write down 3 vague asks** you'd naturally make about your use case —
   the kind of one-liner you'd say to a human colleague. Examples of
   "vague" from what real cohorts actually wrote before revising:
   - "Build an agent for this."
   - "Make it work."
   - "Fix the case demo."

2. **For each one, rewrite it as a build-ready prompt** that answers:
   - **Outcome** — the concrete result you want
   - **Where** — folder, project, tenant, or file
   - **Which UiPath area** — RPA, low-code agent, conversational agent,
     Maestro, coded app, SDK (say the exact type — this is the single most
     repeated lesson from every Day 1/2 delivery: an underspecified agent
     type produces the wrong kind of agent)
   - **Constraints** — what must not change, what must not run without
     approval
   - **Verification** — how you'll know it worked (validate, build, pack,
     run an evaluation)

   Example transformation:

   | Vague | Build-ready |
   |---|---|
   | "Make the case demo work." | "Studio Web shows 'Case has no valid terminal exit' for my Case Management demo. Inspect the case model, add a valid terminal exit rule on the final stage, validate, pack, and upload. Report the validation result and Designer URL." |

3. **Run all 3 rewritten prompts** against your actual use case (or the
   relevant part of it) and compare the result to what you expected.

4. **Set up a review loop.** After each build: verify → note what's
   wrong → refine the prompt → rebuild. Expect 2-3 iterations before a
   result is genuinely good, not just "technically runs."

## Checkpoint

- [ ] 3 vague asks rewritten into build-ready prompts, each naming outcome,
      location, UiPath area, constraints, and verification
- [ ] Each rewritten prompt has actually been run once against your use
      case
- [ ] You can point to one concrete difference in output quality between
      the vague version and the build-ready version

## Office hours discussion prompts

1. What changed since yesterday?
2. What's blocked — is it a prompting problem, or something else (auth,
   permissions, a missing skill)?
3. What will you complete next?
