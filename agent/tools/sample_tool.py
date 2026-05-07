#!/usr/bin/env python3
"""
sample_tool.py — Example tool for the workshop agent.

This tool takes a topic string and returns a simple summary placeholder.
Replace the implementation with any real logic: REST API call, DB lookup, calculation, etc.

Registration:
  In main_agent.py, import and pass this function definition to the agent's tools= list.
  See: https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling
"""

import json


# ---------------------------------------------------------------------------
# Tool definition (passed to the agent at creation time)
# ---------------------------------------------------------------------------
SAMPLE_TOOL_DEFINITION = {
    "type": "function",
    "function": {
        "name": "get_topic_summary",
        "description": "Returns a short summary for a given topic. Use this when the user asks about a specific subject.",
        "parameters": {
            "type": "object",
            "properties": {
                "topic": {
                    "type": "string",
                    "description": "The topic to summarise, e.g. 'Microsoft Foundry', 'Azure AI Search'.",
                }
            },
            "required": ["topic"],
        },
    },
}


# ---------------------------------------------------------------------------
# Tool handler (called when the agent invokes this tool)
# ---------------------------------------------------------------------------
def get_topic_summary(topic: str) -> str:
    """
    Return a summary for the given topic.
    Replace this stub with a real implementation.
    """
    # TODO: replace with a real lookup, API call, or RAG query
    summaries = {
        "microsoft foundry": "Microsoft Foundry is an AI platform for building, deploying, and managing AI agents and models on Azure.",
        "azure ai search": "Azure AI Search is a cloud search service with built-in AI capabilities for indexing and querying data.",
    }
    result = summaries.get(topic.lower(), f"No summary available for '{topic}'. Add it to the tool!")
    return json.dumps({"topic": topic, "summary": result})


# ---------------------------------------------------------------------------
# Tool dispatcher (called from the agent run loop when a tool call arrives)
# ---------------------------------------------------------------------------
def dispatch_tool_call(tool_name: str, tool_args: dict) -> str:
    """Route a tool call by name to the correct handler."""
    if tool_name == "get_topic_summary":
        return get_topic_summary(**tool_args)
    raise ValueError(f"Unknown tool: {tool_name}")
