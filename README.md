# Aureon Swarm Proof — Canonical Repository

This repository is the single authoritative execution, verification, and audit surface for Aureon / ASIOS.

## Structure

/execution     All executable intelligence, agents, runners, ARC submission code  
/verification  Hashes, seals, reproducibility artifacts  
/audit         Validators, invariants, audit proofs  

No submodules. No split repositories. No external execution dependencies.

## Guarantees

- Deterministic execution
- Reproducible artifacts
- Hash-anchored auditability
- Single-repository verification surface

This repository alone is sufficient for independent third-party audit and replay.
