# Day 5: Low-Code Agent Authoring

**Focus:** `agent.json`, inputs, outputs, prompts, tools, validation
**Checkpoint:** Add one input, one output, and validate

## Why this matters

Day 1 had your coding agent write `agent.json` for you. Day 5 is about
understanding it well enough to make a **deliberate, hand-guided change**
instead of only ever re-prompting from scratch.

## What's inside `agent.json`

This is the agent's definition — the file UiPath Studio Web's Agent
Builder reads and writes:

| Section | What it controls |
|---|---|
| **Settings** | Model choice and temperature. A temperature of 0 was traced live as the root cause of failed evaluations more than once — low temperature means highly consistent, less "creative" output, which is desirable for classification tasks but can trip up evaluators expecting some variance. |
| **`inputSchema`** | What comes in — e.g., raw text, plus optional context like a channel or product line |
| **`outputSchema`** | What comes out — a structured verdict (a label, a score, a confidence, a recommended action), not free-form prose |
| **Prompt (`messages`)** | The system message sets role and ground rules; the user message is a template referencing input fields (e.g. `{input.text}`) |

The coupling matters: change the schema, and the prompt template that
references it needs to change too. That's exactly why this file is meant
to be edited deliberately, not blindly regenerated every time.

## Self-paced exercise

1. **Open your Day 1 (or use-case) agent's `agent.json`** and read through
   each section above. Identify: what's the input schema, what's the
   output schema, what does the prompt template reference?

2. **Add one new input field.** For example, if your agent classifies
   free-text feedback, add an optional `channel` or `source` field to
   `inputSchema`.

3. **Add one new output field** that makes use of it — e.g., have the
   output include a `recommendedAction` derived partly from the new input.

4. **Update the prompt template** to reference the new input field, and
   make sure the system message still constrains the model correctly for
   the new output shape.

5. **Validate.** Run the agent's validation step, then a manual test run
   with the new input field populated, and confirm the new output field
   comes back sensibly.

## Checkpoint

- [ ] `agent.json` reviewed and understood section by section
- [ ] One new input field added
- [ ] One new output field added, derived from the new input
- [ ] Prompt template updated to match the new schema
- [ ] Validation run, and a manual test confirms the new fields work

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Evaluation scores dropped after your schema change | Evaluator is still checking the old schema/fields | Update or regenerate the evaluator to match the new output schema |
| New output field is inconsistent/unpredictable | Temperature setting, or an underspecified prompt for the new field | Check the agent's temperature under Settings; be as explicit about the new field's expected values as you were for the original ones |
| Agent ignores the new input field | Prompt template wasn't actually updated to reference it | Confirm the user message template includes a placeholder for the new field (e.g. `{input.newField}`) |

## Office hours discussion prompts

1. What changed since yesterday?
2. What's blocked?
3. What will you complete next?
