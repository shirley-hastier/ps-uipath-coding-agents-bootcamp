# Optional Lab A: IXP Invoice Processing

## Business context

A large share of real automation use cases start with documents. You could
paste an invoice into a chat and ask a model to "pull out the fields", but
you'd lose what IXP (Intelligent Xtraction & Processing) gives you: a
taxonomy you control, a confidence score for every field, and a validation
step for the cases that need a human. This lab has your coding agent build
that IXP project for you.

## Learning objective

Build an IXP project that extracts a defined set of fields from invoices
from several different vendors, then review its confidence and tighten one
field.

## What you'll build

A published IXP project with a taxonomy for invoice fields, tested on a
small set of mixed-vendor invoices.

## Prerequisites

- The [common checklist](index.md#before-you-start-any-of-them) is done
- Three to five **non-sensitive** sample invoices, ideally from different
  vendors and layouts (PDF or image). Don't use real customer data
- A short list of the fields you want. Deciding this is your job, not the
  agent's. In a real project it comes from the process owner or subject
  matter expert

## Estimated duration

60-75 minutes. In the delivery session the build itself took under 20
minutes. The rest is reviewing results and fixing fields.

## Products and tools used

Your coding agent · UiPath CLI and the IXP skill · IXP · Orchestrator

## Exercise: Build an invoice extraction project

### Objective

Get a published IXP project that extracts your chosen fields from invoices
with different layouts, and review how confident it is.

### Starting point

An authenticated coding agent with UiPath skills installed, and your sample
invoices in a local folder.

### Build steps

1. **Confirm you're signed in to the right place** with `uip login`, or
   state the organization and tenant in your prompt. A coding agent that
   isn't logged in can deploy to the wrong organization.

2. **Decide your field list.** A good starting set from the delivery
   session:
   - Invoice number
   - Item number and description
   - Quantity and unit
   - Bill-to or remit-to party
   - Total
   - Taxes
   - Reference number
   - Invoice line items

3. **Turn on Plan Mode,** then write your prompt. Be specific about the
   fields. Don't just say "extract the data". Say "IXP project", and attach
   the invoices:

   ```text
   Create an IXP project to extract the following fields from the attached
   invoices: invoice number, item number, description, quantity, unit,
   remit-to party, total, taxes, reference number, and invoice line items.
   Deploy the solution to this organization: {{ training_url }} and this
   tenant: {{ training_tenant }}.
   ```

4. **Attach your invoices.** If you forget, the agent stops and tells you it
   can't see any invoice files, because it needs them to build the taxonomy
   and test extraction before deploying. Attach them and let it continue.

5. **Let it build, train, and publish.** If the agent says the IXP tool
   isn't installed, let it install it. That adds a few minutes.

6. **Open the project in IXP** and review each field: the taxonomy, the
   extracted value, and the **confidence** for every field. In the delivery
   session the overall confidence came back around 96-97%.

7. **Find one field that captured too much.** A common one is a quantity
   field that also grabbed its unit ("EA") or a reference number that picked
   up an amount.

8. **Fix it in the taxonomy, not by retraining.** Open the field in
   **Manage Taxonomy** and tighten its description (for example "the
   number only, without the unit of measure"). You can edit it yourself, or
   ask your coding agent to do it. Editing it yourself is usually quicker.

9. **Re-run on the same invoices** and confirm the field now comes back
   clean.

### Checkpoint

- [ ] The IXP project is built and published, and you can open it in IXP
- [ ] Your fields were extracted from invoices from more than one vendor
- [ ] You reviewed per-field confidence and can say which field was weakest
- [ ] You fixed at least one field by editing its taxonomy description

### Expected output

A published IXP project, a taxonomy of your fields, and extraction results
with a confidence for each field. Your exact fields and percentages will
differ from other attendees'.

!!! warning "Needs validation"
    The prompt above is reconstructed from dictation during the session, so
    its exact wording wasn't captured verbatim. Whether the IXP skill can
    also do the annotation and validation steps for you was not confirmed.
    In one session the skill wasn't available because the CLI was
    outdated. Run `uip update` and re-check `/uipath` before blaming your
    prompt.

### Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Agent says it doesn't see any invoice files | You forgot to attach them | Attach the invoices and let it continue |
| Agent says it can't find an IXP skill or tool | Your CLI is outdated | Run `uip update`, restart your coding agent, and check `/uipath` |
| Agent says the IXP tool isn't installed | The tool is installed on demand | Approve the install and wait a few minutes |
| Build looks fine but the project isn't where you expect | Deployed to the wrong organization or tenant | Check what `uip login` echoed back, and redeploy to the right one |
| A field includes extra text (a unit, a currency) | The taxonomy description is too loose | Tighten that field's description in Manage Taxonomy, then re-run |
| Fields come back empty for one vendor | That layout wasn't in your samples | Add invoices that cover the missing layout |
| IXP projects are missing or creation fails with a permission error | Tenant-level IXP access or entitlement | Ask your coach to confirm IXP is enabled for your tenant |

### Extension challenge

Ask your coding agent to build an RPA process that calls your published IXP
model and pushes the extracted values to an Orchestrator queue. One
attendee attempted this during the delivery session and hit a usage limit
before finishing, so treat it as unproven and expect to troubleshoot.

### Cleanup and next steps

Keep the project. If invoices are part of your own use case, **Day 9** of
[office hours](../../days-3-10/day-9.md) builds on this: confidence
thresholds, validation, and a document-to-action flow.
