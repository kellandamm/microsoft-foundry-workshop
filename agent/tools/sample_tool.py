#!/usr/bin/env python3
"""
sample_tool.py — SOLUTION BRANCH

This version is ready to use with the FunctionTool SDK pattern.
The get_topic_summary function has type hints and a docstring that the SDK
uses to auto-generate the tool definition — no manual JSON schema needed.

See:
  https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling
"""

import json


# ---------------------------------------------------------------------------
# Tool handler
# The SDK reads the docstring and type hints to build the tool definition.
# ---------------------------------------------------------------------------
def get_topic_summary(topic: str) -> str:
    """
    Returns a short summary for a given topic.
    Use this when the user asks about a specific subject or technology.

    :param topic: The topic to summarise, e.g. 'Microsoft Foundry' or 'Azure AI Search'.
    :type topic: str
    :return: A JSON string with 'topic' and 'summary' fields.
    :rtype: str
    """
    summaries = {
        "microsoft foundry": (
            "Microsoft Foundry is an AI platform on Azure for building, deploying, and managing "
            "AI agents and models. It provides a hub-and-project model for organising resources, "
            "model deployments, and agent configurations."
        ),
        "azure ai search": (
            "Azure AI Search is a cloud search service with built-in AI capabilities for "
            "indexing and querying structured and unstructured data at scale."
        ),
        "foundry agent service": (
            "The Foundry Agent Service is a managed service that hosts and runs AI agents. "
            "It handles conversation state, tool calling, and model orchestration."
        ),
        "semantic kernel": (
            "Semantic Kernel is an open-source SDK from Microsoft that helps you integrate "
            "AI models and plugins into your applications using .NET, Python, or Java."
        ),
    }
    result = summaries.get(
        topic.lower(),
        f"No summary found for '{topic}'. Extend the summaries dict or connect a real data source."
    )
    return json.dumps({"topic": topic, "summary": result})


# ---------------------------------------------------------------------------
# Kept for backward compatibility with starter branch dispatcher pattern
# ---------------------------------------------------------------------------
SAMPLE_TOOL_DEFINITION = {}  # not needed when using FunctionTool SDK pattern

def dispatch_tool_call(tool_name: str, tool_args: dict) -> str:
    if tool_name == "get_topic_summary":
        return get_topic_summary(**tool_args)
    raise ValueError(f"Unknown tool: {tool_name}")
