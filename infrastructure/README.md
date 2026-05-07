# Infrastructure

This folder contains optional templates to provision the Azure resources needed for the workshop.

---

## Resources typically provisioned

| Resource | Purpose |
|---|---|
| AI Hub | Top-level Foundry resource grouping projects and shared connections |
| AI Project | Isolated workspace; deploy models and agents here |
| Model Deployments | Chat and (optional) embedding models |
| App Hosting | Hosting for the chat web app (e.g., Azure Container Apps, App Service) |
| Managed Identity | Secure, keyless auth between the web app and agent endpoint |
| Storage | Required by Foundry hub; also used for grounding data |
| Logging / Monitoring | Application Insights or Log Analytics for observability |

---

## Files

| File | Description |
|---|---|
| `main-template.json` | ARM / Bicep template (replace with your preferred IaC format) |
| `parameters.workshop.json` | Workshop-specific parameter values |

---

## Deploying

Update `parameters.workshop.json` with your subscription, resource group, and naming preferences, then deploy:

```bash
# Azure CLI — ARM template
az deployment group create \
  --resource-group <your-rg> \
  --template-file infrastructure/main-template.json \
  --parameters @infrastructure/parameters.workshop.json

# Azure CLI — Bicep (if using Bicep)
az deployment group create \
  --resource-group <your-rg> \
  --template-file infrastructure/main.bicep \
  --parameters @infrastructure/parameters.workshop.json

# Azure Developer CLI (azd)
azd up
```

---

## Notes

- For a workshop, a single resource group per participant (or one shared group) works well.
- Use the [Basic Foundry Chat reference architecture](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/basic-microsoft-foundry-chat) for a minimal workshop deployment.
- Use the [Baseline Foundry Chat reference architecture](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/baseline-microsoft-foundry-chat) as the target for a production-grade follow-on.
