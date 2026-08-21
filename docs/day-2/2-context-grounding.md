# Enterprise Data & Context Grounding

*Roughly 15-20 minutes, instruction + short demo.*

=== "Coach View"

    **Purpose**

    Show participants how to ground an agent in real enterprise data —
    and, just as importantly, when grounding via RAG is the *wrong* choice.

    **Key message**

    Context grounding options depend on the use case: API workflows,
    Integration Service connectors, or IXP. Within Context Grounding
    itself, there's a real trade-off between response quality and speed —
    and RAG is not always the right tool, even the "advanced" kind.

    **What to show on screen**

    Orchestrator → create a **Storage Bucket** (native, or Azure/AWS-backed;
    point out the read-only and audit-logging toggles), then create an
    **Index** on top of it, then show the index (not the bucket) being
    attached to an agent as context.

    **Suggested narration**

    > "Start basic — do some prompts, see how it performs — and then move
    > to other options if you need to."

    **A real story worth telling verbatim:**

    > A customer needed an agent to look up SOP business rules from a
    > document. Even "advanced" RAG couldn't reliably extract them — the
    > document just wasn't structured for it. The fix wasn't a better RAG
    > setup; it was switching to a **deterministic decision-table (DMN)
    > approach** instead, specifically because "we always ensure that the
    > output was going to be correct — it's a deterministic approach to
    > validating business rules."

    **Likely questions & recommended answers**

    | Question | Answer |
    |---|---|
    | "When should I use Deep RAG instead of basic?" | Deep RAG gives better responses but is slower. Start basic, test with real prompts, only escalate if quality genuinely requires it. |
    | "My agent needs to follow a fixed set of business rules reliably — should I use RAG?" | Probably not, if the rules are the kind of thing that must be *exactly* right every time. Consider a deterministic decision table (DMN) instead — RAG is a retrieval mechanism, not a correctness guarantee. |

    **Transition into the next segment**

    "Grounding tells the agent what it knows. Now let's talk about how it
    takes action."

=== "Participant View"

    **What you'll observe**

    A live Storage Bucket + Index setup, and a real example of RAG failing
    on a business-rules use case — and what to do instead when that
    happens to you.

    **Why this matters**

    Your own use case almost certainly needs *some* form of grounding.
    Knowing the options — and their failure modes — up front saves you from
    building on the wrong one.

## Grounding options by use case

| Use case | Grounding option |
|---|---|
| Calling external systems for live data | API workflow or Integration Service connector |
| Documents, unstructured content | IXP (Intelligent Xtraction & Processing) |
| Enterprise knowledge/content search | Context Grounding (Storage Bucket + Index) |

## Setting up Context Grounding

1. Create a **Storage Bucket** in Orchestrator (native storage, or an
   Azure/AWS-backed bucket). Configure read-only access and audit logging
   if this is sensitive content.
2. Create an **Index** on top of the bucket.
3. Attach the **index** — not the bucket directly — to your agent as
   context.

## Basic vs. Deep (advanced) RAG

> "If you use Deep RAG, you will have greater responses... but it will also
> be slower."

Guidance: start with basic retrieval, test it against real prompts your
use case will actually see, and only move to Deep RAG if quality genuinely
requires it.

!!! warning "RAG is not a substitute for deterministic correctness"
    If your use case depends on getting business rules *exactly* right
    every time — not "usually right" — RAG grounding is the wrong tool,
    no matter how advanced. Use a deterministic mechanism instead, such as
    an Orchestrator **DMN (Decision Model Notation) business rules table**.
    This is a real lesson from a real customer engagement, not a
    hypothetical caution.

Continue to [Tool-Using Agents & Integrations](3-tools-and-integrations.md).
