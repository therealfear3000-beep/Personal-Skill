#!/usr/bin/env python3

import json
import sys
from pathlib import Path

WEIGHTS = {
    "problem_fit": 15,
    "case_specificity": 10,
    "novelty": 10,
    "mechanism": 15,
    "evidence": 10,
    "impact": 10,
    "feasibility": 10,
    "economics": 8,
    "adoption": 7,
    "defensibility": 5,
}

REQUIRED = set(WEIGHTS)


def score(option):
    ratings = option.get("ratings", {})
    missing = REQUIRED - set(ratings)
    if missing:
        raise ValueError(
            f"{option.get('name', 'Unnamed option')} missing ratings: "
            + ", ".join(sorted(missing))
        )

    total = 0.0
    weak = []

    for dimension, weight in WEIGHTS.items():
        value = float(ratings[dimension])

        if not 0 <= value <= 10:
            raise ValueError(
                f"{option.get('name', 'Unnamed option')}: "
                f"{dimension} must be 0-10"
            )

        total += (value / 10.0) * weight

        if value < 5:
            weak.append(dimension)

    fatal = option.get("fatal_flaws", [])

    return {
        "name": option.get("name", "Unnamed option"),
        "score": round(total, 1),
        "weak_dimensions": weak,
        "fatal_flaws": fatal,
        "eligible": len(fatal) == 0,
    }


def main():
    if len(sys.argv) != 2:
        print("Usage: python scripts/score_options.py options.json")
        sys.exit(1)

    path = Path(sys.argv[1])

    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    options = data["options"] if isinstance(data, dict) else data
    results = [score(o) for o in options]

    results.sort(
        key=lambda x: (x["eligible"], x["score"]),
        reverse=True
    )

    print("\nHR CASE OPTION SCORECARD\n")
    print(f"{'Option':32} {'Score':>7} {'Eligible':>10}")
    print("-" * 53)

    for r in results:
        print(
            f"{r['name'][:32]:32} "
            f"{r['score']:>6.1f} "
            f"{str(r['eligible']):>10}"
        )

        if r["fatal_flaws"]:
            print("  RED FLAGS:", "; ".join(r["fatal_flaws"]))

        if r["weak_dimensions"]:
            print("  WEAK:", ", ".join(r["weak_dimensions"]))

    print("\nWeights:")
    for k, v in WEIGHTS.items():
        print(f"  {k}: {v}%")


if __name__ == "__main__":
    main()
