# REPRODUCE
pip install .
asiosctl run decision-decomposition
asiosctl verify decision-decomposition
### ARC-AGI-2 Accuracy Reproduction

```powershell
Import-Csv .\convergence_matrix.csv | % { $_ } | Tee-Object -Variable rows | Out-Null; $total=$rows.Count; $correct=($rows | ? { $_.solved -in @("true","True","1",1,$true) }).Count; if($total -eq 0){ throw "No ARC tasks present" }; [Math]::Round($correct/$total,4)
````

