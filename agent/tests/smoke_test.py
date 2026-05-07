#!/usr/bin/env python3
"""
smoke_test.py — Quick validation that the agent starts and responds.

Usage:
  python agent/tests/smoke_test.py
"""

import os
import sys
from dotenv import load_dotenv

load_dotenv(dotenv_path="agent/src/.env")

PROJECT_CONNECTION = os.environ.get("FOUNDRY_PROJECT_CONNECTION", "")
MODEL_DEPLOYMENT   = os.environ.get("FOUNDRY_MODEL_DEPLOYMENT", "")

def test_env_vars():
    assert PROJECT_CONNECTION, "FOUNDRY_PROJECT_CONNECTION is not set"
    assert MODEL_DEPLOYMENT,   "FOUNDRY_MODEL_DEPLOYMENT is not set"
    print("[PASS] environment variables are set")

def test_agent_response():
    from azure.identity import DefaultAzureCredential
    from azure.ai.projects import AIProjectClient

    client = AIProjectClient.from_connection_string(
        conn_str=PROJECT_CONNECTION,
        credential=DefaultAzureCredential(),
    )

    agent = client.agents.create_agent(
        model=MODEL_DEPLOYMENT,
        name="smoke-test-agent",
        instructions="Reply with exactly: SMOKE_TEST_OK",
    )

    thread = client.agents.create_thread()
    client.agents.create_message(thread_id=thread.id, role="user", content="ping")
    run = client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)

    messages = client.agents.list_messages(thread_id=thread.id)
    reply = ""
    for msg in messages.data:
        if msg.role == "assistant":
            reply = msg.content[0].text.value if msg.content else ""
            break

    client.agents.delete_agent(agent.id)

    assert "SMOKE_TEST_OK" in reply, f"Unexpected reply: {reply}"
    print(f"[PASS] agent responded correctly: {reply}")

if __name__ == "__main__":
    try:
        test_env_vars()
        test_agent_response()
        print("\nAll smoke tests passed.")
    except Exception as e:
        print(f"\n[FAIL] {e}")
        sys.exit(1)
