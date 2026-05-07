#!/usr/bin/env python3
"""
main_agent.py — Workshop starter: Microsoft Foundry Agent (Python)

Prerequisites:
  pip install azure-ai-projects azure-identity python-dotenv

Usage:
  python agent/src/main_agent.py
"""

import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
load_dotenv()

PROJECT_CONNECTION = os.environ["FOUNDRY_PROJECT_CONNECTION"]
MODEL_DEPLOYMENT   = os.environ["FOUNDRY_MODEL_DEPLOYMENT"]
AGENT_NAME         = "workshop-agent"
AGENT_INSTRUCTIONS = (
    "You are a helpful assistant for the Microsoft Foundry workshop. "
    "Answer questions clearly and concisely. "
    "When you need to look up information or perform a calculation, use the tools provided. "
    "If you are unsure, say so rather than guessing."
)

# ---------------------------------------------------------------------------
# Client
# ---------------------------------------------------------------------------
credential = DefaultAzureCredential()
client = AIProjectClient.from_connection_string(
    conn_str=PROJECT_CONNECTION,
    credential=credential,
)

# ---------------------------------------------------------------------------
# Create or retrieve the agent
# ---------------------------------------------------------------------------
def get_or_create_agent():
    """Create the workshop agent (or reuse if it already exists)."""
    # LAB 2 — register tools here by passing a `tools=` list
    agent = client.agents.create_agent(
        model=MODEL_DEPLOYMENT,
        name=AGENT_NAME,
        instructions=AGENT_INSTRUCTIONS,
    )
    print(f"[agent] created: {agent.id}")
    return agent


# ---------------------------------------------------------------------------
# Run a single conversation turn
# ---------------------------------------------------------------------------
def chat(agent_id: str, thread_id: str | None, user_message: str):
    """Send a message and return (thread_id, assistant_reply)."""
    # Create or reuse a thread
    if thread_id is None:
        thread = client.agents.create_thread()
        thread_id = thread.id
        print(f"[thread] created: {thread_id}")

    # Add the user message
    client.agents.create_message(
        thread_id=thread_id,
        role="user",
        content=user_message,
    )

    # Run the agent
    run = client.agents.create_and_process_run(
        thread_id=thread_id,
        agent_id=agent_id,
    )
    print(f"[run] status: {run.status}")

    # Get the latest assistant message
    messages = client.agents.list_messages(thread_id=thread_id)
    for msg in messages.data:
        if msg.role == "assistant":
            reply = msg.content[0].text.value if msg.content else "(no response)"
            return thread_id, reply

    return thread_id, "(no response)"


# ---------------------------------------------------------------------------
# Interactive REPL
# ---------------------------------------------------------------------------
def main():
    agent = get_or_create_agent()
    thread_id = None

    print("\nWorkshop Agent ready. Type 'quit' to exit.\n")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            break
        if not user_input:
            continue

        thread_id, reply = chat(agent.id, thread_id, user_input)
        print(f"Agent: {reply}\n")

    # Cleanup
    client.agents.delete_agent(agent.id)
    print("[agent] deleted.")


if __name__ == "__main__":
    main()
