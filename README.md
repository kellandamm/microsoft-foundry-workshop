# Microsoft Foundry Agent + Chat Workshop

This repo contains a 2-hour, hands-on workshop where you build an AI agent using Microsoft Foundry and connect it to a simple chat web application.

## What you'll build

- A prompt-driven agent hosted in Microsoft Foundry.
- At least one tool / grounding capability (API or data).
- A basic chat web UI that calls the agent endpoint.
- An end-to-end, cloud-hosted deployment you can extend after the workshop.

## Who this is for

- Developers and architects who want a practical intro to Microsoft Foundry and the Agent Service.
- Hands-on technical sellers and solution engineers.
- Cloud and AI platform teams evaluating agent-based patterns.

## Prerequisites

- An Azure subscription with access to Microsoft Foundry.
- Permission to create an AI hub and project in your tenant.
- Git and a code editor (VS Code or similar).
- Ability to run a web app and agent locally (language/framework of your choice).
- Basic familiarity with REST APIs and environment variables.

See [SETUP.md](./SETUP.md) for details.

## Workshop flow (2 hours)

1. Intro and scenario.
2. Environment and Foundry project setup.
3. Build and run a basic agent.
4. Add tools / grounding.
5. Wire up the chat web app.
6. Deploy end-to-end.
7. Hardening, observability, and next steps.

See [WORKSHOP-AGENDA.md](./WORKSHOP-AGENDA.md) for the detailed agenda.

## Repository structure

```
microsoft-foundry-workshop/
├── README.md
├── WORKSHOP-AGENDA.md
├── SETUP.md
├── CHECKLIST.md
├── docs/
│   ├── overview.md
│   ├── architecture.md
│   └── lab-guide.md
├── agent/
│   ├── README.md
│   ├── config/
│   │   └── agent.yaml
│   ├── src/
│   ├── tools/
│   └── tests/
├── webapp/
│   ├── README.md
│   ├── src/
│   └── config/
├── infrastructure/
│   ├── README.md
│   ├── main-template.json
│   └── parameters.workshop.json
├── scripts/
│   ├── bootstrap.sh
│   └── bootstrap.ps1
└── assets/
    ├── diagrams/
    └── sample-data/
```

## Getting started

1. Complete the steps in [SETUP.md](./SETUP.md).
2. Follow the time-boxed sections in [WORKSHOP-AGENDA.md](./WORKSHOP-AGENDA.md).
3. Use [CHECKLIST.md](./CHECKLIST.md) to track your progress.

> **Facilitator note:** See `docs/lab-guide.md` for delivery tips and timings.
