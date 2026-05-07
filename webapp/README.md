# Web App

This folder contains a minimal chat web application that calls the Foundry agent.

---

## Folder structure

```
webapp/
├── README.md
├── src/
│   ├── index.*          ← main UI entry point (HTML, JSX, Razor, etc.)
│   └── api/
│       └── chat.*       ← server-side endpoint that calls the agent
└── config/
    └── .env.example     ← copy to .env and fill in your values
```

---

## Configuration

Copy `config/.env.example` to `config/.env` (or your framework's equivalent) and fill in:

| Variable | Description |
|---|---|
| `AGENT_ENDPOINT_URL` | Full URL of the hosted agent endpoint |
| `AGENT_AUTH_INFO` | API key, token, or managed identity reference |

> **Never commit `.env` files.** They are included in `.gitignore`.

---

## Running locally

1. Install dependencies for your chosen framework.
2. Fill in `config/.env`.
3. Start the dev server.

```bash
# Example (Node.js / Next.js)
npm install && npm run dev

# Example (Python / Flask)
pip install -r requirements.txt && flask run

# Example (.NET)
dotnet run --project webapp/src
```

4. Open `http://localhost:<port>` in your browser.
5. Send a message and confirm the agent's response renders in the chat UI.

---

## How it works

1. The user types a message in the chat UI.
2. The UI sends the message to `api/chat.*` (server-side endpoint).
3. The server forwards the message to the Foundry agent endpoint using `AGENT_ENDPOINT_URL`.
4. The agent processes the message (optionally calling tools) and returns a response.
5. The server returns the response to the UI, which renders it in the chat thread.

---

## Deploying

See `infrastructure/README.md` for templates to deploy this web app to Azure.
After deploying, update `AGENT_ENDPOINT_URL` in your hosted app's configuration.
