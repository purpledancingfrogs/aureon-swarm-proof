import json, random

tasks_file = "asios-execution-set/tasks.json"
output_file = "asios-execution-set/results.json"

with open(tasks_file, "r") as f:
    tasks = json.load(f)

results = []
for task in tasks:
    results.append({"task_id": task["id"], "solution": random.choice(task["choices"])})

with open(output_file, "w") as f:
    json.dump(results, f, indent=4)
