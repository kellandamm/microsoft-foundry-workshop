# Sample FAQ — Workshop Grounding Data

This file contains sample FAQ content you can use as grounding data for the workshop agent.
Upload it to Foundry IQ, Azure AI Search, or any retrieval source of your choice.

---

## What is Microsoft Foundry?

Microsoft Foundry is an AI platform on Azure for building, deploying, and managing AI agents and models.
It provides a hub-and-project model for organising resources, model deployments, and agent configurations.

## What is the Foundry Agent Service?

The Foundry Agent Service is a managed service that hosts and runs AI agents.
It handles conversation state, tool calling, and model orchestration so you can focus on your agent's logic.

## What is a tool in the context of agents?

A tool is a function or API the agent can call during a conversation to retrieve information or take an action.
Examples include: looking up a database record, calling a REST API, performing a calculation, or searching a knowledge base.

## What is grounding?

Grounding connects the agent to your own data (documents, databases, knowledge bases) so it can answer questions
based on your specific content rather than relying solely on the model's training data.

## How do I deploy a model in Foundry?

1. Open your Foundry project in the Azure portal or at https://ai.azure.com.
2. Navigate to Models + endpoints.
3. Click Deploy model and select the model you want (e.g. gpt-4o).
4. Give the deployment a name — this is what you use as FOUNDRY_MODEL_DEPLOYMENT.

## How do I find my project connection string?

1. Open your Foundry project.
2. Go to Overview.
3. Copy the Project connection string value.
4. Paste it into your .env file as FOUNDRY_PROJECT_CONNECTION.
