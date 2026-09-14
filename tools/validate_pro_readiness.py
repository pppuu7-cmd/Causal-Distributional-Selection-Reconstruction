#!/usr/bin/env python3
"""State-only consistency check. Never a scientific proof or readiness score.

This replaces the historical CD002-A-only check so legitimate newer terminal
results are not mislabeled invalid. Run from a full repository checkout.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re

FALSE_LOCKS = (
    "UNIQUE_K5_EXTENSION", "PHYSICAL_SELECTOR_DERIVED", "CRQN_V0_3_AUTHORIZED",
    "REGULATOR_INDEPENDENCE", "RG_CLOSURE", "CAUSAL_MULTIVERTEX_CLOSURE",
    "NEW_PHYSICS_FOUND", "QUANTUM_GRAVITY_SOLVED",
)


def check(root: Path) -> dict:
    errors = []
    try:
        state = json.loads((root / "recovery/state.json").read_text(encoding="utf-8"))
        locks = (root / "authority/CLAIM_LOCKS.md").read_text(encoding="utf-8")
        current = (root / "recovery/CURRENT_FRONT.md").read_text(encoding="utf-8")
        pro = (root / "recovery/PRO_FRONTIER.md").read_text(encoding="utf-8")
        paths = state["current_artifacts"]
        for rel in paths:
            p = (root / rel).resolve()
            if not p.is_relative_to(root.resolve()) or not p.is_file():
                errors.append("missing or invalid local artifact: " + rel)
        result = (root / state["current_terminal_result"]).read_text(encoding="utf-8")
        classification = state["current_terminal_classification"]
        if classification not in current or classification not in result:
            errors.append("terminal classification mismatch")
        if state["current_terminal_iteration"] not in current:
            errors.append("terminal iteration missing from CURRENT")
        if state["current_frontier"] not in pro:
            errors.append("operational frontier mismatch")
        for key in FALSE_LOCKS:
            if state["prohibited_claims"].get(key) is not False:
                errors.append("unauthorized state flag: " + key)
            if not re.search(r"\b" + key + r"\s*=\s*false\b", locks):
                errors.append("missing false claim lock: " + key)
        # Check authoritative flags, not quotations of forbidden claims in old notes.
        if state["current_terminal_iteration"] == "CD003":
            script = root / "analysis/cd003_exact_controls.py"
            output = root / "results/CD003_EXACT_CONTROLS.json"
            for p, key in [(script, "script_sha256"), (output, "output_sha256")]:
                if hashlib.sha256(p.read_bytes()).hexdigest() != state["execution"][key]:
                    errors.append("execution artifact digest mismatch: " + str(p.name))
            raw = json.loads(output.read_text(encoding="utf-8"))
            if raw["physical_selector_established"] or raw["physical_k5_amplitude_computed"]:
                errors.append("unexpected physical promotion in controls")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(type(exc).__name__ + ": " + str(exc))
    return {"valid": not errors, "errors": errors,
            "scope": "repository state and artifact identity only; not scientific truth"}


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    a = ap.parse_args()
    out = check(a.root)
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if out["valid"] else 1)
