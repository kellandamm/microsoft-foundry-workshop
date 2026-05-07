# Workshop Checklist

Use this list to track your progress during the 2-hour workshop.

---

## Setup

- [ ] I can sign into Azure and access Microsoft Foundry.
- [ ] I created or selected an AI hub and project.
- [ ] I deployed the required models.
- [ ] I cloned the workshop repo and opened it in my IDE.
- [ ] I ran `scripts/bootstrap.*` with no errors.

---

## Agent — basics

- [ ] I reviewed `agent/config/agent.yaml`.
- [ ] I implemented a basic agent in `agent/src/`.
- [ ] I ran the agent locally.
- [ ] I sent at least one test message and saw a response.

---

## Agent — tools / grounding

- [ ] I implemented at least one tool in `agent/tools/`.
- [ ] I registered the tool in `agent/config/agent.yaml`.
- [ ] I confirmed the agent called the tool in a test run.

---

## Web app

- [ ] I configured `webapp/config/` with the agent endpoint and auth.
- [ ] I ran the web app locally.
- [ ] I sent messages from the browser and saw agent responses.

---

## Deployment

- [ ] I deployed resources using the templates in `infrastructure/`.
- [ ] I configured the hosted web app to call the hosted agent.
- [ ] I validated the end-to-end flow from a browser.

---

## Extras (time permitting)

- [ ] I enabled logging / tracing / basic evaluation.
- [ ] I experimented with a different scenario or prompt.
- [ ] I noted next steps for my own environment.
