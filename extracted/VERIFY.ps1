param(
  [string]$Root = (Get-Location).Path
)

Write-Host "Recomputing SHA256 manifest..."
Get-ChildItem $Root -Recurse -File |
  Where-Object { $_ .Name -ne 'PROOF_MANIFEST_SHA256.csv' } |
  Get-FileHash -Algorithm SHA256 |
  Sort-Object Path |
  Export-Csv $Root\RECOMPUTED_SHA256.csv -NoTypeInformation

Write-Host "Compare RECOMPUTED_SHA256.csv with PROOF_MANIFEST_SHA256.csv"
