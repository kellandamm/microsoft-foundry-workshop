#!/usr/bin/env python3
"""
main_agent.py — SOLUTION BRANCH: Microsoft Foundry Agent with tool calling (Python)

Differences from the starter (main branch):
  - sample_tool is imported and registered with the agent at creation time.
  - The run loop handles tool calls: dispatches to sample_tool and submits output.
  - A helper print_run_steps() shows the reasoning trace for learning purposes.

Prerequisites:
  pip install azure-ai-projects azure-identity python-dotenv

Usage:
  python agent/src/main_agent.py
"""

import os
import json
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import FunctionTool, ToolSet

# Import the workshop tool
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from tools.sample_tool import get_topic_summary, SAMPLE_TOOL_DEFINITION, dispatch_tool_call

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
load_dotenv()

PROJECT_CONNECTION = os.environ["FOUNDRY_PROJECT_CONNECTION"]
MODEL_DEPLOYMENT   = os.environ["FOUNDRY_MODEL_DEPLOYMENT"]
AGENT_NAME         = "workshop-agent-solution"
AGENT_INSTRUCTIONS = (
    "You are a helpful assistant for the Microsoft Foundry workshop. "
    "Answer questions clearly and concisely. "
    "When the user asks about a topic, use the get_topic_summary tool to retrieve information. "
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
# Register tools
# ---------------------------------------------------------------------------
functions = FunctionTool(functions={get_topic_summary})
toolset = ToolSet()
toolset.add(functions)


# ---------------------------------------------------------------------------
# Create or retrieve the agent
# ---------------------------------------------------------------------------
def get_or_create_agent():
    agent = client.agents.create_agent(
        model=MODEL_DEPLOYMENT,
        name=AGENT_NAME,
        instructions=AGENT_INSTRUCTIONS,
        toolset=toolset,
    )
    print(f"[agent] created: {agent.id}")
    return agent


# ---------------------------------------------------------------------------
# Print reasoning trace (learning aid)
# ---------------------------------------------------------------------------
def print_run_steps(thread_id: str, run_id: str):
    steps = client.agents.list_run_steps(thread_id=thread_id, run_id=run_id)
    for step in reversed(steps.data):
        if step.type == "tool_calls":
            for tc in step.step_details.tool_calls:
                fn = tc.function
                print(f"  [tool call] {fn.name}({fn.arguments}) -> {fn.output}")


# ---------------------------------------------------------------------------
# Run a single conversation turn
# ---------------------------------------------------------------------------
def chat(agent_id: str, thread_id: str | None, user_message: str):
    if thread_id is None:
        thread = client.agents.create_thread()
        thread_id = thread.id
        print(f"[thread] created: {thread_id}")

    client.agents.create_message(
        thread_id=thread_id,
        role="user",
        content=user_message,
    )

    # create_and_process_run handles tool call loops automatically
    run = client.agents.create_and_process_run(
        thread_id=thread_id,
        agent_id=agent_id,
    )
    print(f"[run] status: {run.status}")
    print_run_steps(thread_id, run.id)

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

    print("\nSolution Agent ready. Try asking: 'Tell me about Microsoft Foundry'")
    print("Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            break
        if not user_input:
            continue
        thread_id, reply = chat(agent.id, thread_id, user_input)
        print(f"Agent: {reply}\n")

    client.agents.delete_agent(agent.id)
    print("[agent] deleted.")


if __name__ == "__main__":
    main()
