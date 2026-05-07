# Workshop Overview

This workshop introduces Microsoft Foundry for building and hosting AI agents, then connects those agents to a simple chat web application.

---

## Learning objectives

By the end of this workshop you will be able to:

- Explain when to use agents vs simple chat completions.
- Create and configure an agent in a Foundry project.
- Attach tools and grounding capabilities to an agent.
- Connect a web application to an agent endpoint.
- Deploy an end-to-end solution you can extend after the workshop.

---

## Scenario

Choose a simple business scenario (for example: internal helpdesk, FAQ assistant, or sales assistant). Throughout the labs, you will adapt the agent instructions and tools to fit that scenario.

---

## Key Microsoft Foundry concepts

| Concept | Description |
|---|---|
| **AI Hub** | Top-level resource that groups projects, compute, and shared connections. |
| **AI Project** | Isolated workspace inside a hub; where you deploy models and agents. |
| **Foundry Agent Service** | Managed service for hosting, running, and scaling agents. |
| **Tools** | Functions or APIs an agent can call to take action or retrieve data. |
| **Grounding / IQ** | Connecting the agent to your own data for retrieval-augmented responses. |
| **Model Deployment** | A specific model version deployed in your project, referenced by the agent. |

---

## What you will touch in this workshop

1. Foundry portal (hub + project creation, model deployment).
2. Agent configuration (instructions, model reference, tools).
3. Agent SDK / API (run the agent programmatically in your language of choice).
4. A chat web app (calls the agent endpoint, renders conversation UI).
5. Deployment templates (provision hosting infrastructure).
