# Enterprise Data & Context Grounding

*Roughly 15-20 minutes, instruction + short demo.*


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
