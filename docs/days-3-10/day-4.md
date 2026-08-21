# Day 4: UiPath Skills and CLI Hygiene

**Focus:** `uip skills`, `uip tools`, auth, output formats, repeatable setup
**Checkpoint:** Confirm setup and skills visibility

## Why this matters

This is also the **MVP running** executive-tracking milestone (see
[Program Overview](../program-overview.md#executive-tracking-checkpoints)).
"Hygiene" here means: is your setup repeatable enough that you (or a
teammate) could tear it down and rebuild it without re-solving the same
auth or PATH problem you hit on Day 1?

## Self-paced exercise

1. **Re-verify your core commands** (same as
   [Day 1 Environment Setup](../day-1/2-environment-setup.md)):

   ```powershell
   uip --version
   uip --help
   uip login --authority {{ training_url }} --tenant "{{ training_tenant }}"
   ```

2. **Check `uip tools`.** Running `uip tools install` without naming a
   specific tool has been observed to throw a validation error — you must
   specify which tool. Get familiar with listing and installing tools
   explicitly rather than guessing at a bare command.

3. **Check `uip skills list`.** Confirm this returns the skills relevant
   to your use case (e.g., `uipath-rpa`, `uipath-platform`,
   `uipath-maestro-case`, `uipath-coded-apps`). If a skill you expect isn't
   there:

   ```powershell
   uip update
   ```

   An outdated CLI is the most common cause of "missing" skills across
   every delivery observed.

4. **Confirm output formats.** If your workflow involves scripting or
   CI-style automation around the CLI, check what output formats `uip`
   commands support (e.g., machine-readable vs. human-readable) so you're
   not parsing free text unnecessarily.

5. **Write down your setup as a repeatable checklist** — the exact
   commands, in order, that take a fresh machine to "ready to build." This
   is what makes setup something you (or a new team member) can redo in
   minutes, not an hour of half-remembered troubleshooting.

## Checkpoint

- [ ] `uip --version`, `uip --help`, and `uip login` (with explicit
      `--authority`/`--tenant`) all succeed
- [ ] `uip skills list` shows the skills your use case needs
- [ ] You have a written, repeatable setup checklist — not just tribal
      knowledge in your head
- [ ] Your MVP is running (this day's executive-tracking milestone)

## Troubleshooting

Reuses the same failure modes as
[Day 1 Environment Setup](../day-1/2-environment-setup.md#troubleshooting) —
if you're hitting something new, check there first.

## Office hours discussion prompts

1. What changed since yesterday?
2. Is your MVP actually running, or close? If not, what's the one thing
   blocking it?
3. What will you complete next?
