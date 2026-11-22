import json
import os
from datetime import datetime, UTC

# Load detailed cloud security assessment evidence
with open("evidence.json", "r") as file:
    evidence = json.load(file)

# Convert individual control assessments into standardized results
results = []

for control_id, outcome in evidence["control_results"].items():
    results.append({
        "control_id": control_id,
        "outcome": outcome,
        "detail": f"Control {control_id} assessment returned {outcome}."
    })

# Create a control assessment summary with execution metadata
report = {
    "schema_version": 1,
    "repository": "RojasJonathan/cloud-lab",
    "workflow": ".github/workflows/cloud-security-checks.yml",
    "run_id": int(os.environ["GITHUB_RUN_ID"]),
    "commit_sha": os.environ["GITHUB_SHA"],
    "timestamp": datetime.now(UTC).isoformat().replace("+00:00", "Z"),
    "control_results": results
}

# Save the standardized control assessment summary
with open("control-summary.json", "w") as file:
    json.dump(report, file, indent=4)