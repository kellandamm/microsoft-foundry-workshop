# Agent

This folder contains the AI agent used in the workshop.

---

## Folder structure

```
agent/
├── README.md
├── config/
│   └── agent.yaml       ← agent name, instructions, model, tools
├── src/
│   └── main-agent.*     ← agent implementation (your language)
├── tools/
│   └── sample-tool.*    ← example tool implementation
└── tests/
    └── smoke-test.*     ← quick validation script
```

---

## Configuration

See `config/agent.yaml` for the agent definition. Key fields:

| Field | Description |
|---|---|
| `name` | Display name for the agent |
| `instructions` | System prompt / persona that guides agent behaviour |
| `model` | Reference to the model deployment in your Foundry project |
| `tools` | List of tool definitions the agent can call |

---

## Running locally

1. Ensure your `.env` (or equivalent) contains:
   - `FOUNDRY_PROJECT_CONNECTION`
   - `FOUNDRY_MODEL_DEPLOYMENT`
2. Install dependencies for your chosen language/SDK.
3. Run the entry point in `src/`.
4. Send a test message and verify the response.

```bash
# Example (Python)
python agent/src/main-agent.py

# Example (.NET)
dotnet run --project agent/src

# Example (Node.js)
node agent/src/main-agent.js
```

---

## Adding a tool

1. Create a new file in `agent/tools/`.
2. Implement the function that will be called (name, parameters, return value).
3. Register the tool in `agent/config/agent.yaml` under the `tools:` section.
4. Restart the agent and send a prompt that requires the tool.

---

## Testing

Run the smoke test after any change:

```bash
bash agent/tests/smoke-test.sh
# or
python agent/tests/smoke-test.py
```
