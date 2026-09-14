#!/usr/bin/env python3
"""
Deterministic helper for comparing swarm run scorecards.

Input JSON format:
{
  "baseline": {
    "name": "single",
    "quality": 0..100,
    "verification": 0..100,
    "robustness": 0..100,
    "diversity": 0..100,
    "efficiency": 0..100,
    "hard_constraints_pass": true
  },
  "candidates": [
    {same fields, "name": "topology-a"},
    ...
  ]
}

This script does not decide whether something is truly emergent.
It computes a weighted score and score lift only.
"""
import json
import sys
from pathlib import Path

WEIGHTS = {
    "quality": 0.35,
    "verification": 0.30,
    "robustness": 0.20,
    "diversity": 0.10,
    "efficiency": 0.05,
}

def score(item):
    if not item.get("hard_constraints_pass", True):
        return 0.0
    total = 0.0
    for key, weight in WEIGHTS.items():
        value = float(item.get(key, 0))
        if value < 0 or value > 100:
            raise ValueError(f"{key} must be in [0,100]")
        total += weight * value
    return round(total, 2)

def main():
    if len(sys.argv) != 2:
        print("usage: score_run.py metrics.json", file=sys.stderr)
        raise SystemExit(2)

    path = Path(sys.argv[1])
    data = json.loads(path.read_text())
    baseline = data["baseline"]
    baseline_score = score(baseline)

    rows = []
    for candidate in data.get("candidates", []):
        s = score(candidate)
        rows.append({
            "name": candidate.get("name", "unnamed"),
            "score": s,
            "lift_vs_baseline": round(s - baseline_score, 2),
            "hard_constraints_pass": candidate.get("hard_constraints_pass", True),
        })

    rows.sort(key=lambda x: x["score"], reverse=True)
    result = {
        "baseline": {
            "name": baseline.get("name", "baseline"),
            "score": baseline_score,
        },
        "ranking": rows,
        "winner": rows[0] if rows else None,
    }
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
