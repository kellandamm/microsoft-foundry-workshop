# Setup

Follow these steps before or at the start of the workshop.

---

## 1. Azure and Foundry access

1. Sign in to the [Azure portal](https://portal.azure.com).
2. Ensure you have:
   - An active Azure subscription.
   - Access to Microsoft Foundry and permission to create an AI hub and project.
3. Navigate to [Microsoft Foundry](https://ai.azure.com) and verify you can:
   - Create an AI hub.
   - Create an AI project inside the hub.

---

## 2. Create a workshop project

During the workshop you will:

1. Create a new AI hub for the workshop (or reuse an existing sandbox hub).
2. Create a new AI project in that hub.
3. Deploy the required models for:
   - Chat / completions.
   - Embeddings (optional, if you enable grounding / RAG later).

Record these values for use throughout the labs:

| Setting | Your value |
|---|---|
| Hub name | |
| Project name | |
| Project connection string / endpoint | |
| Primary model deployment name | |

---

## 3. Local environment

Install:

- Git
- A code editor (VS Code recommended)
- A runtime / framework of your choice for:
  - The agent (e.g., Python, .NET, Node.js)
  - The web app (SPA, server-rendered, or simple server)

Clone the repo:

```bash
git clone https://github.com/kellandamm/microsoft-foundry-workshop.git
cd microsoft-foundry-workshop
```

---

## 4. Environment configuration

Create a `.env` (or equivalent) in the root, `agent/`, and `webapp/` folders as needed.

Minimum variables to plan for:

| Variable | Description |
|---|---|
| `FOUNDRY_PROJECT_CONNECTION` | Connection string or project endpoint |
| `FOUNDRY_MODEL_DEPLOYMENT` | Name of the model deployment used by the agent |
| `AGENT_ENDPOINT_URL` | URL where the agent is hosted (local during early labs) |
| `AGENT_AUTH_INFO` | Key, token, or identity details (if required) |

> **Never commit `.env` files.** Add them to `.gitignore`.

---

## 5. Quick verification

Run the bootstrap script for your platform:

```bash
# bash / macOS / Linux / WSL
bash scripts/bootstrap.sh

# PowerShell / Windows
.\scripts\bootstrap.ps1
```

The script checks prerequisites and prints your environment summary. Fix any issues before the workshop begins.
