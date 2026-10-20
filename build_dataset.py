import json
import yaml
from mutators import MUTATORS

with open("seeds.yaml") as f:
    seeds = yaml.safe_load(f)

rows = []

for i, attack in enumerate(seeds["attacks"]):
    for tactic_id, mutate in MUTATORS.items():
        rows.append({
            "id": f"atk-{i:02d}-{tactic_id}",
            "type": "attack",
            "harm": attack["harm"],
            "tactic": tactic_id,
            "prompt": mutate(attack["seed"]),
        })

for i, item in enumerate(seeds["benign"]):
    rows.append({
        "id": f"ben-{i:02d}",
        "type": "benign",
        "harm": item["harm"],
        "tactic": "none",
        "prompt": item["prompt"],
    })

    with open("data/dataset.jsonl", "w") as f:
        for row in rows:
            f.write(json.dumps(row) + "\n")

print(f"Wrote {len(rows)} prompts to data/dataset.jsonl")
