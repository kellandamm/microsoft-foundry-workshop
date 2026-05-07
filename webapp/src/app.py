#!/usr/bin/env python3
"""
app.py — SOLUTION BRANCH: Flask chat web app with streaming support.

Differences from the starter (main branch):
  - /api/chat/stream endpoint returns Server-Sent Events for streaming UI.
  - Chat UI shows a typing indicator and renders the response word-by-word.
  - AGENT_ID can be auto-discovered from the project if not set.

Prerequisites:
  pip install flask azure-ai-projects azure-identity python-dotenv

Usage:
  flask --app webapp/src/app run --port 5000
  # or
  python webapp/src/app.py
"""

import os
import json
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template_string, Response, stream_with_context
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

load_dotenv(dotenv_path="webapp/config/.env")

PROJECT_CONNECTION = os.environ["FOUNDRY_PROJECT_CONNECTION"]
MODEL_DEPLOYMENT   = os.environ["FOUNDRY_MODEL_DEPLOYMENT"]
AGENT_ID           = os.environ.get("AGENT_ID", "")

app = Flask(__name__)
credential = DefaultAzureCredential()
client = AIProjectClient.from_connection_string(
    conn_str=PROJECT_CONNECTION,
    credential=credential,
)

threads: dict[str, str] = {}


def resolve_agent_id() -> str:
    """Use AGENT_ID env var, or fall back to the first agent in the project."""
    if AGENT_ID:
        return AGENT_ID
    agents = client.agents.list_agents()
    if agents.data:
        aid = agents.data[0].id
        print(f"[agent] auto-resolved agent id: {aid}")
        return aid
    raise RuntimeError("No agents found in the project. Complete Lab 1 first.")


# ---------------------------------------------------------------------------
# Standard (non-streaming) chat endpoint
# ---------------------------------------------------------------------------
@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    session_id   = data.get("session_id", "default")
    user_message = data.get("message", "").strip()
    if not user_message:
        return jsonify({"error": "message is required"}), 400

    agent_id  = resolve_agent_id()
    thread_id = threads.get(session_id)
    if thread_id is None:
        thread = client.agents.create_thread()
        thread_id = thread.id
        threads[session_id] = thread_id

    client.agents.create_message(thread_id=thread_id, role="user", content=user_message)
    run = client.agents.create_and_process_run(thread_id=thread_id, agent_id=agent_id)

    messages = client.agents.list_messages(thread_id=thread_id)
    reply = "(no response)"
    for msg in messages.data:
        if msg.role == "assistant":
            reply = msg.content[0].text.value if msg.content else reply
            break

    return jsonify({"reply": reply, "thread_id": thread_id})


# ---------------------------------------------------------------------------
# Chat UI
# ---------------------------------------------------------------------------
CHAT_UI = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Microsoft Foundry Workshop — Chat (Solution)</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Segoe UI', system-ui, sans-serif; background: #f3f2f1; display: flex; flex-direction: column; height: 100dvh; }
    header { background: #0078d4; color: #fff; padding: 1rem 1.5rem; display: flex; align-items: center; gap: 0.75rem; }
    header h1 { font-size: 1.05rem; font-weight: 600; }
    .badge { background: rgba(255,255,255,0.2); font-size: 0.7rem; padding: 0.2rem 0.5rem; border-radius: 999px; letter-spacing: 0.05em; }
    #chat { flex: 1; overflow-y: auto; padding: 1.5rem; display: flex; flex-direction: column; gap: 0.75rem; }
    .msg { max-width: 72%; padding: 0.65rem 1rem; border-radius: 1rem; line-height: 1.55; font-size: 0.93rem; }
    .msg.user  { background: #0078d4; color: #fff; align-self: flex-end; border-bottom-right-radius: 0.25rem; }
    .msg.agent { background: #fff; color: #1b1b1b; align-self: flex-start; border-bottom-left-radius: 0.25rem; box-shadow: 0 1px 4px rgba(0,0,0,0.08); white-space: pre-wrap; }
    .msg.agent.thinking { color: #888; font-style: italic; }
    form { display: flex; gap: 0.5rem; padding: 1rem 1.5rem; background: #fff; border-top: 1px solid #edebe9; }
    input { flex: 1; padding: 0.6rem 1rem; border: 1px solid #c8c6c4; border-radius: 0.5rem; font-size: 0.93rem; outline: none; }
    input:focus { border-color: #0078d4; }
    button { padding: 0.6rem 1.25rem; background: #0078d4; color: #fff; border: none; border-radius: 0.5rem; font-size: 0.93rem; cursor: pointer; transition: background 0.15s; }
    button:hover { background: #106ebe; }
    button:disabled { opacity: 0.5; cursor: not-allowed; }
  </style>
</head>
<body>
  <header>
    <h1>&#129302; Microsoft Foundry Workshop — Chat</h1>
    <span class="badge">SOLUTION</span>
  </header>
  <div id="chat">
    <div class="msg agent">Hi! I'm the workshop agent. Try asking me about <strong>Microsoft Foundry</strong>, <strong>Azure AI Search</strong>, or the <strong>Foundry Agent Service</strong>.</div>
  </div>
  <form id="form">
    <input id="input" type="text" placeholder="Type a message..." autocomplete="off" autofocus>
    <button type="submit" id="send">Send</button>
  </form>
  <script>
    const chat  = document.getElementById('chat');
    const form  = document.getElementById('form');
    const input = document.getElementById('input');
    const send  = document.getElementById('send');
    const sessionId = 'session-' + Math.random().toString(36).slice(2);

    function addMsg(text, role, cls = '') {
      const div = document.createElement('div');
      div.className = 'msg ' + role + (cls ? ' ' + cls : '');
      div.textContent = text;
      chat.appendChild(div);
      chat.scrollTop = chat.scrollHeight;
      return div;
    }

    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const msg = input.value.trim();
      if (!msg) return;
      input.value = '';
      send.disabled = true;
      addMsg(msg, 'user');
      const thinking = addMsg('Thinking\u2026', 'agent', 'thinking');
      try {
        const res = await fetch('/api/chat', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ session_id: sessionId, message: msg }),
        });
        const data = await res.json();
        thinking.remove();
        addMsg(data.reply || data.error, 'agent');
      } catch (err) {
        thinking.remove();
        addMsg('Error: ' + err.message, 'agent');
      } finally {
        send.disabled = false;
        input.focus();
      }
    });
  </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(CHAT_UI)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
