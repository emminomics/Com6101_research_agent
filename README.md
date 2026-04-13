# COM6104 Research Assistant

## Architecture Diagram

```mermaid
flowchart TD
    A[User Input (Query)] --> B[LLM Backbone (Reasoning & Planning)]
    B --> C[Tool 1: Paper Search]
    B --> D[Tool 2: PDF/Notes Summarizer]
    C --> E[Short-Term Memory (Conversation Buffer + Context Recall)]
    D --> E
    E --> F[Final Output (Digest + Citations)]
