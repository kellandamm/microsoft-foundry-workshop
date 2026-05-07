# Lab Guide (Facilitator)

This guide aligns with `WORKSHOP-AGENDA.md` and adds facilitation tips, checkpoints, and fallback paths.

---

## General tips

- Pre-provision the Foundry hub and project before the session to save 5–10 minutes.
- Share your `.env.example` template in advance so participants can fill in values before the workshop.
- Have a working reference solution in a separate branch (`solution/`) as a fallback for blocked participants.
- Keep each lab segment time-boxed; use the fallback branch if anyone falls more than one section behind.

---

## Lab 1 — Agent basics (0:25–0:45)

**Files:** `agent/config/agent.yaml`, `agent/src/`

**Goal:** Run an agent locally and send a test message.

**Steps:**
1. Walk through `agent/config/agent.yaml` — explain each field.
2. Implement or show the starter code in `agent/src/`.
3. Run the agent and send a test message.

**Checkpoint:** Everyone sees a non-trivial agent response in their terminal.

**Fallback:** Provide a working agent config and src file from the `solution/` branch.

---

## Lab 2 — Tools / grounding (0:45–1:05)

**Files:** `agent/tools/`, `agent/config/agent.yaml`

**Goal:** Implement and call a simple tool.

**Steps:**
1. Explain what a tool definition looks like (name, description, parameters, handler).
2. Add a sample tool from `agent/tools/`.
3. Register it in `agent/config/agent.yaml`.
4. Send a prompt that forces a tool call; inspect the tool call + result in the response.

**Checkpoint:** Participants can show a response that includes visible tool output.

**Fallback:** Use the pre-built tool in `agent/tools/sample-tool.*` from the `solution/` branch.

---

## Lab 3 — Chat web app (1:05–1:25)

**Files:** `webapp/src/`, `webapp/config/`

**Goal:** Send messages from the browser to the agent.

**Steps:**
1. Review the chat UI skeleton in `webapp/src/`.
2. Configure `webapp/config/` with agent endpoint and auth.
3. Start the dev server and open in browser.
4. Send a message and confirm the response renders.

**Checkpoint:** End-to-end chat working locally for every participant.

**Fallback:** Use the reference web app from the `solution/` branch.

---

## Lab 4 — Deploy (1:25–1:45)

**Files:** `infrastructure/`, `scripts/`

**Goal:** Deploy to the cloud and update configuration.

**Steps:**
1. Run the deployment template from `infrastructure/`.
2. Update `webapp/config/` with the hosted agent endpoint.
3. Redeploy or restart the web app.
4. Open the hosted URL and validate end-to-end.

**Checkpoint:** Hosted URL working for at least one participant (demo from facilitator if time is short).

---

## Fallback path summary

If time is running short, prioritize Labs 1 and 3 (agent basics + web app). Labs 2 and 4 can be completed independently after the workshop using `CHECKLIST.md`.
