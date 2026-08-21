# Day 9: IXP / Document Understanding Intake

**Focus:** Extraction, confidence, validation, document-to-action workflow
**Checkpoint:** Design extraction and validation flow

## Why this matters

If your use case involves documents — invoices, forms, contracts, tickets
— IXP (Intelligent Xtraction & Processing) is almost certainly a better
fit than asking a generic LLM prompt to "read this PDF and pull out the
fields." IXP gives you per-field confidence scores, a validation/annotation
workflow, and a taxonomy you control — visibility you lose with a
generic extraction prompt.

## The three IXP capabilities

| Capability | Best for |
|---|---|
| **Communications Mining** | Understanding conversations at scale — email, chat, tickets |
| **Document Understanding (classic)** | Semi-structured documents with a fairly consistent layout (e.g., invoices, POs) — annotation-based |
| **Generative Extraction** | Complex or highly variable documents, where you describe each field in natural language instead of visually annotating a fixed template |

## Hands-on: Document Understanding (annotation-based)

1. **Create/open an IXP project**, choose "structured and semi-structured"
   (this routes to Document Understanding).
2. **Upload sample documents.** Auto-classification runs automatically —
   the system will group similar documents (e.g., "these look like
   invoices"). Aim for enough samples to cover real variation; a handful
   of near-identical documents from one vendor won't tell you much about
   how the model generalizes.
3. **Annotate.** Open each document, review the auto-identified fields,
   confirm or correct them.
4. **Add a custom field** if the out-of-box taxonomy doesn't cover
   something you need: open the taxonomy editor → "Add Field" → name and
   type (exact text vs. an ID vs. other types) → save → return to
   annotate and manually tag the new field in each sample document (it
   won't show as confirmed until you do).
5. **Handle line-item/table fields carefully.** These are a common source
   of misclassification (e.g., a fee amount lumped into the wrong
   category) — expect to manually reassign mis-tagged line items to the
   correct taxonomy category.
6. **Review the project/health score** — per-field accuracy plus
   recommendations (e.g., "add more samples" if variation is high).
7. **Publish** a named version. It then becomes selectable from a dropdown
   inside an RPA workflow's "Extract Data" activity — no separate
   integration step needed.

## Hands-on: Generative Extraction (for more variable documents)

Distinguished from classic DU by using natural-language field
**instructions** instead of purely visual annotation:

1. Define each field by describing what to extract in plain language
   (e.g., "extract the line-item tax rate").
2. Choose field type: **exact text** (literally present in the document)
   vs. **inferred** (a value derived from context, not literally written —
   e.g., a yes/no judgment).
3. Test against a deliberately mixed set of document formats/vendors to
   check the extraction genuinely generalizes, rather than only working on
   the format you tested with.
4. If a field captures unwanted extra content (e.g., a quantity field that
   bundles in a unit abbreviation), **update the field's taxonomy
   description** rather than trying to "retrain" — Generative Extraction
   is driven by the instruction text, so refining that text is the fix.

## Using IXP as an agent tool

The same IXP project can be exposed to an agent as a tool, the same way an
Integration Service connector is (see
[Day 2: Tools & Integrations](../day-2/3-tools-and-integrations.md#a-brief-note-on-ixp-as-a-tool)) —
useful when your document-to-action workflow needs an agent to reason
about what to do *after* extraction (route it, flag it for review,
trigger a downstream process), not just extract the fields.

## Self-paced exercise: design your extraction and validation flow

For your own document-driven use case, write down:

1. **Which capability fits** — DU (fairly consistent layout) or Generative
   Extraction (high variability)?
2. **The field list**, and for each: exact text or inferred?
3. **The confidence threshold** below which a document should route to a
   human for validation, rather than proceeding automatically
4. **The document-to-action step** — what happens after extraction:
   straight-through processing, an agent decision, or a human review task?

## Checkpoint

- [ ] Extraction capability chosen (DU vs. Generative Extraction) with a
      stated reason
- [ ] Field list defined, with type (exact/inferred) for each
- [ ] A confidence threshold defined for routing to human validation
- [ ] The document-to-action step is designed, not left as "figure it out
      later"

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Line-item/table fields misclassified | OCR grouped values incorrectly | Manually reassign to the correct taxonomy category; consider more diverse training samples |
| A field captures extra unwanted text | Taxonomy field description is too broad (Generative Extraction) | Refine the field's natural-language description rather than trying to "retrain" |
| Health score flags high variation | Not enough diverse samples | Add more samples covering the real range of formats/vendors you'll see in production |

## Office hours discussion prompts

1. What changed since yesterday?
2. What's blocked?
3. What will you complete next?
