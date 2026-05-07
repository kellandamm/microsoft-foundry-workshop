# bootstrap.ps1 — pre-flight check for the Microsoft Foundry workshop
# Run: .\scripts\bootstrap.ps1

Write-Host "======================================="
Write-Host " Microsoft Foundry Workshop — Bootstrap"
Write-Host "======================================="
Write-Host ""

# Check Git
if (Get-Command git -ErrorAction SilentlyContinue) {
    $gitVersion = git --version
    Write-Host "[OK] git: $gitVersion"
} else {
    Write-Host "[MISSING] git — install from https://git-scm.com"
}

# Check Azure CLI
if (Get-Command az -ErrorAction SilentlyContinue) {
    Write-Host "[OK] Azure CLI: installed"
} else {
    Write-Host "[MISSING] Azure CLI — install from https://aka.ms/installazurecli"
}

# Check Azure login
try {
    $account = az account show --query name -o tsv 2>$null
    if ($account) {
        Write-Host "[OK] Azure login: $account"
    } else {
        Write-Host "[ACTION] Not logged in to Azure — run: az login"
    }
} catch {
    Write-Host "[ACTION] Not logged in to Azure — run: az login"
}

# Check for .env file
if (Test-Path ".env") {
    Write-Host "[OK] .env file found"
} else {
    Write-Host "[ACTION] No .env file found — copy .env.example and fill in your values"
}

Write-Host ""
Write-Host "Bootstrap complete. Fix any [MISSING] or [ACTION] items above before the workshop."
