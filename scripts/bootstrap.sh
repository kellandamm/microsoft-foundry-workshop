#!/usr/bin/env bash
# bootstrap.sh — pre-flight check for the Microsoft Foundry workshop
# Run: bash scripts/bootstrap.sh

set -euo pipefail

echo "======================================="
echo " Microsoft Foundry Workshop — Bootstrap"
echo "======================================="
echo ""

# Check Git
if command -v git &>/dev/null; then
  echo "[OK] git: $(git --version)"
else
  echo "[MISSING] git — install from https://git-scm.com"
fi

# Check Azure CLI
if command -v az &>/dev/null; then
  echo "[OK] Azure CLI: $(az version --query '\"azure-cli\"' -o tsv 2>/dev/null || echo 'installed')"
else
  echo "[MISSING] Azure CLI — install from https://aka.ms/installazurecli"
fi

# Check Azure login
if az account show &>/dev/null; then
  ACCOUNT=$(az account show --query name -o tsv 2>/dev/null || echo 'unknown')
  echo "[OK] Azure login: $ACCOUNT"
else
  echo "[ACTION] Not logged in to Azure — run: az login"
fi

# Check for .env file
if [ -f ".env" ]; then
  echo "[OK] .env file found"
else
  echo "[ACTION] No .env file found — copy .env.example and fill in your values"
fi

echo ""
echo "Bootstrap complete. Fix any [MISSING] or [ACTION] items above before the workshop."
