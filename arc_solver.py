import json, hashlib

# Define deterministic tasks
tasks = [
    {"id": 1, "choices": ["A", "B", "C", "D"]},
    {"id": 2, "choices": ["X", "Y", "Z"]},
    {"id": 3, "choices": ["Red", "Green", "Blue"]}
]

results = []

# Deterministic solver: always pick first choice
for task in tasks:
    results.append({"task_id": task["id"], "solution": task["choices"][0]})

# Write results to JSON
with open("arc_agi_2_results.json", "w") as f:
    json.dump(results, f, indent=4)

# Generate SHA256 hash of each solution
hashes = []
for r in results:
    h = hashlib.sha256(r["solution"].encode()).hexdigest()
    hashes.append({"task_id": r["task_id"], "hash": h})

with open("arc_agi_2_hashes.json", "w") as f:
    json.dump(hashes, f, indent=4)
