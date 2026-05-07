#!/usr/bin/env python3
"""
app.py — Minimal Flask chat web app that calls the Foundry agent.

Prerequisites:
  pip install flask azure-ai-projects azure-identity python-dotenv

Usage:
  flask --app webapp/src/app run --port 5000
  # or
  python webapp/src/app.py

Then open http://localhost:5000 in your browser.
"""

import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template_string
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

load_dotenv(dotenv_path="webapp/config/.env")

PROJECT_CONNECTION = os.environ["FOUNDRY_PROJECT_CONNECTION"]
MODEL_DEPLOYMENT   = os.environ["FOUNDRY_MODEL_DEPLOYMENT"]
AGENT_ID           = os.environ.get("AGENT_ID", "")  # set after Lab 1

app = Flask(__name__)
credential = DefaultAzureCredential()
client = AIProjectClient.from_connection_string(
    conn_str=PROJECT_CONNECTION,
    credential=credential,
)

# In-memory thread store (resets on restart — fine for workshop)
threads: dict[str, str] = {}  # session_id -> thread_id


# ---------------------------------------------------------------------------
# Chat endpoint
# ---------------------------------------------------------------------------
@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    session_id  = data.get("session_id", "default")
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"error": "message is required"}), 400

    if not AGENT_ID:
        return jsonify({"error": "AGENT_ID is not set. Complete Lab 1 first."}), 500

    # Get or create thread for this session
    thread_id = threads.get(session_id)
    if thread_id is None:
        thread = client.agents.create_thread()
        thread_id = thread.id
        threads[session_id] = thread_id

    # Send message and run agent
    client.agents.create_message(thread_id=thread_id, role="user", content=user_message)
    run = client.agents.create_and_process_run(thread_id=thread_id, agent_id=AGENT_ID)

    # Get latest assistant reply
    messages = client.agents.list_messages(thread_id=thread_id)
    reply = "(no response)"
    for msg in messages.data:
        if msg.role == "assistant":
            reply = msg.content[0].text.value if msg.content else reply
            break

    return jsonify({"reply": reply, "thread_id": thread_id})


# ---------------------------------------------------------------------------
# Chat UI (single-page, inline HTML — swap for a real framework if preferred)
# ---------------------------------------------------------------------------
CHAT_UI = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Microsoft Foundry Workshop — Chat</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Segoe UI', system-ui, sans-serif; background: #f3f2f1; display: flex; flex-direction: column; height: 100dvh; }
    header { background: #0078d4; color: #fff; padding: 1rem 1.5rem; font-size: 1.1rem; font-weight: 600; }
    #chat { flex: 1; overflow-y: auto; padding: 1.5rem; display: flex; flex-direction: column; gap: 0.75rem; }
    .msg { max-width: 70%; padding: 0.6rem 1rem; border-radius: 1rem; line-height: 1.5; font-size: 0.95rem; }
    .msg.user { background: #0078d4; color: #fff; align-self: flex-end; border-bottom-right-radius: 0.25rem; }
    .msg.agent { background: #fff; color: #1b1b1b; align-self: flex-start; border-bottom-left-radius: 0.25rem; box-shadow: 0 1px 4px rgba(0,0,0,0.08); }
    form { display: flex; gap: 0.5rem; padding: 1rem 1.5rem; background: #fff; border-top: 1px solid #edebe9; }
    input { flex: 1; padding: 0.6rem 1rem; border: 1px solid #c8c6c4; border-radius: 0.5rem; font-size: 0.95rem; outline: none; }
    input:focus { border-color: #0078d4; }
    button { padding: 0.6rem 1.25rem; background: #0078d4; color: #fff; border: none; border-radius: 0.5rem; font-size: 0.95rem; cursor: pointer; }
    button:hover { background: #106ebe; }
    button:disabled { opacity: 0.5; cursor: not-allowed; }
  </style>
</head>
<body>
  <header>&#129302; Microsoft Foundry Workshop — Chat</header>
  <div id="chat"></div>
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

    function addMsg(text, role) {
      const div = document.createElement('div');
      div.className = 'msg ' + role;
      div.textContent = text;
      chat.appendChild(div);
      chat.scrollTop = chat.scrollHeight;
    }

    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const msg = input.value.trim();
      if (!msg) return;
      input.value = '';
      send.disabled = true;
      addMsg(msg, 'user');
      addMsg('Thinking…', 'agent');
      try {
        const res = await fetch('/api/chat', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ session_id: sessionId, message: msg }),
        });
        const data = await res.json();
        chat.lastChild.remove();
        addMsg(data.reply || data.error, 'agent');
      } catch (err) {
        chat.lastChild.remove();
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
