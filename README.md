# COM6104 Research Assistant

## Architecture Diagram

```mermaid
flowchart TD
    A[User Input (Query)] --> B[LLM Backend]
    B --> C[Tool: Paper Search]
    B --> D[Tool: PDF Summarizer]
    C --> E[Results: Papers Found]
    D --> F[Results: PDF Summary]
    E --> G[Memory Buffer]
    F --> G[Memory Buffer]
    G --> H[Agent Response to User]
```
