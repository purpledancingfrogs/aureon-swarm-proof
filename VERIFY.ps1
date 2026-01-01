Write-Host "Running Aureon Swarm Verification..."

$required = @(
  "FINAL_ARCHIVE_CHECK.md",
  "FINAL_ARCHIVE_CHECK.sig",
  "VERIFICATION_REPORT.md",
  "FINAL_GLOBAL_SHA256_LOCK.json",
  "AGI_BENCHMARK_METADATA.json",
  "convergence_matrix.csv"
)

foreach ($f in $required) {
  if (-not (Test-Path $f)) { throw "Missing required file: $f" }
}

Write-Host "Required files present."

Get-ChildItem -File |
  Where-Object { $_.Name -ne "PROOF_MANIFEST_SHA256.csv" } |
  Get-FileHash -Algorithm SHA256 |
  Sort-Object Path |
  ForEach-Object { "$($_.Hash)  $($_.Path)" } |
  Set-Content audit\FULL_REPO_REHASH.sha256

Write-Host "Verification complete."
