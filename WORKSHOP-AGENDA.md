# Workshop Agenda (2 hours)

This agenda is optimized for a 2-hour delivery with short, focused lab segments.

## High-level schedule

| Time | Section |
|---|---|
| 0:00–0:10 | Intro and scenario |
| 0:10–0:25 | Environment and Foundry project setup |
| 0:25–0:45 | Build and run a basic agent |
| 0:45–1:05 | Add tools / grounding |
| 1:05–1:25 | Wire up the chat web app |
| 1:25–1:45 | Deploy end-to-end |
| 1:45–2:00 | Hardening, observability, wrap-up |

---

## 0:00–0:10 — Intro and scenario

- Slides: Why Microsoft Foundry, agent basics, and target architecture.
- Walk through `docs/overview.md` and `docs/architecture.md`.
- Demo the final chat experience briefly so participants know where they're headed.

**Outcome:** Everyone understands the scenario and the end state.

---

## 0:10–0:25 — Environment and project setup

- Create or open a Foundry AI hub and project.
- Confirm model deployments required for the workshop.
- Clone this repo and open it in your IDE.
- Validate environment using `scripts/bootstrap.*`.

**Outcome:** Everyone can connect to the Foundry project and run basic commands.

---

## 0:25–0:45 — Build and run a basic agent

- Review `agent/config/agent.yaml` (instructions, model, basic settings).
- Implement a simple agent in `agent/src/` that echoes and reformats user requests.
- Run locally, send a test message, and inspect the response.

**Outcome:** A working agent that responds to simple prompts.

---

## 0:45–1:05 — Add tools / grounding

- Introduce tools and grounding concepts.
- Implement one tool in `agent/tools/` (e.g., a calculation or data lookup).
- Register the tool in `agent/config/agent.yaml`.
- Run a test that forces the agent to use the tool.

**Outcome:** Agent can call at least one tool and include its result in replies.

---

## 1:05–1:25 — Wire up the chat web app

- Open `webapp/src/` and review the chat UI skeleton.
- Configure the app to call the agent endpoint.
- Run the web app locally and send messages via the browser.

**Outcome:** End-to-end chat from browser → web app → agent → response.

---

## 1:25–1:45 — Deploy end-to-end

- Use templates in `infrastructure/` to deploy agent + web app.
- Configure app settings to point to the hosted agent.
- Validate connectivity and show a live demo.

**Outcome:** Cloud-hosted chat experience that participants can share.

---

## 1:45–2:00 — Hardening, observability, wrap-up

- Discuss auth, network controls, logging, cost and safety controls.
- Show where to enable tracing and evaluation.
- Summarize next steps and share links to official docs and reference repos.

**Outcome:** Participants leave with a working app and a clear path to production.

---

## Repo ↔ Agenda mapping

| Agenda block | Folder / files touched |
|---|---|
| Intro & scenario | `README.md`, `docs/overview.md`, `docs/architecture.md` |
| Env & project setup | `SETUP.md`, `infrastructure/`, `scripts/bootstrap.*` |
| Basic agent | `agent/config/`, `agent/src/`, `agent/README.md` |
| Tools / grounding | `agent/tools/`, `assets/sample-data/`, `agent/config/` |
| Chat web app | `webapp/src/`, `webapp/config/`, `webapp/README.md` |
| Deploy end-to-end | `infrastructure/`, `scripts/`, `webapp/config/` |
| Hardening & wrap-up | `docs/lab-guide.md`, `CHECKLIST.md` |
