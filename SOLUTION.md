# Solution Branch

This branch (`solution`) contains the completed, working version of the workshop.
Use it as a reference if you get stuck, or as a facilitator fallback during labs.

## What's different from `main`

| Area | `main` (starter) | `solution` |
|---|---|---|
| `agent/src/main_agent.py` | Tool registration commented out | `sample_tool` wired in via `FunctionTool` + `ToolSet`; run steps printed for learning |
| `agent/tools/sample_tool.py` | Manual JSON schema + dispatcher | Docstring-driven SDK pattern; auto-generated tool definition |
| `webapp/src/app.py` | Basic `/api/chat` endpoint + minimal UI | Auto-resolves agent ID; SOLUTION badge in UI |
| `SOLUTION.md` | Not present | This file |

## How to use this branch

### As a facilitator fallback

If a participant is blocked during a lab, point them to the equivalent file in this branch:

```bash
# View the solution agent on GitHub
https://github.com/kellandamm/microsoft-foundry-workshop/blob/solution/agent/src/main_agent.py

# Or clone just the solution branch
git clone --branch solution https://github.com/kellandamm/microsoft-foundry-workshop.git foundry-solution
```

### Running the solution agent

```bash
# 1. Install dependencies
pip install -r agent/src/requirements.txt

# 2. Configure environment
cp agent/src/.env.example agent/src/.env
# Edit agent/src/.env with your values

# 3. Run
python agent/src/main_agent.py

# Try: "Tell me about Microsoft Foundry"
# You should see a [tool call] line in the output showing the tool being invoked.
```

### Running the solution web app

```bash
# 1. Install dependencies
pip install -r webapp/src/requirements.txt

# 2. Configure environment
cp webapp/config/.env.example webapp/config/.env
# Edit webapp/config/.env — set AGENT_ID to the ID printed when you ran main_agent.py

# 3. Run
python webapp/src/app.py

# Open http://localhost:5000
# Try: "Tell me about Azure AI Search"
```

## Key concepts demonstrated

- **FunctionTool + ToolSet**: The recommended SDK pattern for registering Python functions as agent tools.
- **Docstring-driven tool definitions**: The SDK reads your function's docstring and type hints to auto-generate the JSON schema — no manual schema authoring needed.
- **Auto-resolved agent ID**: The web app falls back to listing agents in the project if `AGENT_ID` is not set — useful when running end-to-end for the first time.
- **Run step inspection**: `print_run_steps()` shows the tool call trace, helping participants understand how the agent reasons and when it invokes tools.
