# Reference Architecture

## High-level flow

```
User (Browser)
    │
    ▼
Chat Web App  ──────────────────────────────────────────┐
(webapp/src/)                                           │
    │  HTTPS + auth                                     │
    ▼                                                   │
Agent Endpoint                                          │
(Microsoft Foundry Agent Service)                       │
    │                                                   │
    ├──► Tool calls (agent/tools/)                      │
    │       e.g. REST API, data lookup, calculation     │
    │                                                   │
    └──► Grounding / retrieval (optional)               │
            e.g. Foundry IQ, Azure AI Search            │
    │                                                   │
    ▼                                                   │
Model Deployment                                        │
(chat / completions)                                    │
    │                                                   │
    ▼                                                   │
Response  ──────────────────────────────────────────────┘
    │
    ▼
User (Browser)
```

---

## Key components

| Component | Role | Workshop folder |
|---|---|---|
| **Chat web app** | Browser UI + backend that brokers calls to the agent | `webapp/` |
| **Agent** | Hosted in Foundry; configured with instructions, model, tools | `agent/` |
| **Tools** | Optional external actions or lookups the agent can invoke | `agent/tools/` |
| **Grounding data** | Optional knowledge base for retrieval-augmented responses | `assets/sample-data/` |
| **Infrastructure** | Templates to provision hosting, identity, networking | `infrastructure/` |

---

## Design principles

- **Stack-agnostic** — the pattern works in Python, .NET, Node.js, or any language with an HTTP client.
- **Separation of concerns** — the web app does not contain business logic; it delegates all reasoning to the agent.
- **Secure by default** — use managed identity or short-lived tokens; avoid long-lived keys in code.
- **Observable** — instrument the agent and web app for tracing from the start, not as an afterthought.

---

## Reference architectures

- [Basic Microsoft Foundry Chat](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/basic-microsoft-foundry-chat)
- [Baseline Microsoft Foundry Chat](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/baseline-microsoft-foundry-chat)
