#!/usr/bin/env python3
"""Infrastructure-only CDSR Pro-readiness validator.

This script checks repository state consistency. It is deliberately incapable of
validating scientific truth, physical source derivations, uniqueness, or a future
selector. Green output is not scientific evidence.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "prereg/CD001_SELECTOR_POWER_BASELINE.md",
    "prereg/CD002A_MULTIPLICATIVE_COMPOSITION_COHERENCE.md",
    "prereg/PRO_GATE_TEMPLATE.md",
    "results/CD001_SELECTOR_POWER_BASELINE_RESULT.md",
    "results/CD002A_MULTIPLICATIVE_COMPOSITION_COHERENCE_RESULT.md",
    "recovery/CURRENT_FRONT.md",
    "recovery/PRO_FRONTIER.md",
    "recovery/DEPENDENCY_DAG.md",
    "recovery/state.json",
    "authority/FACT_LEVEL.md",
    "authority/UPSTREAM_IMPORT_MANIFEST.md",
    "authority/UPSTREAM_IMPORT_MANIFEST.json",
    "authority/THEOREM_AND_OBSTRUCTION_REGISTRY.md",
    "authority/SOURCE_COMPOSITION_INVENTORY.md",
    "authority/SOURCE_DERIVATION_REQUIRED.md",
    "authority/CLAIM_LOCKS.md",
    "docs/AMBIGUITY_SPACE.md",
    "docs/PHYSICAL_EQUIVALENCE.md",
    "docs/SELECTOR_POWER_MATRIX.md",
    "docs/COHERENCE_DEFORMATION_CLASSES.md",
    "docs/NORMAL_JET_FRONTIER.md",
    "protocol/NO_SMUGGLING_TEST.md",
    "research_log/CDSR_LEDGER.md",
]

CD001_CLASS = (
    "CD001_FINITE_LINEAR_SCALAR_SELECTOR_CANNOT_UNIQUELY_SELECT_"
    "INFINITE_DIMENSIONAL_K5_AMBIGUITY_EXACT_SCOPED"
)
CD002A_CLASS = (
    "CD002A_SU2_4_MULTIPLICATIVE_COHERENCE_COLLAPSES_SMOOTH_"
    "TANGENTIAL_MULTIPLIER_TO_CONSTANT_EXACT_CONDITIONAL_SCOPED"
)

FALSE_LOCKS = [
    "UNIQUE_K5_EXTENSION",
    "PHYSICAL_SELECTOR_DERIVED",
    "CRQN_V0_3_AUTHORIZED",
    "REGULATOR_INDEPENDENCE",
    "RG_CLOSURE",
    "CAUSAL_MULTIVERTEX_CLOSURE",
    "NEW_PHYSICS_FOUND",
    "QUANTUM_GRAVITY_SOLVED",
]
TRUE_LOCKS = [
    "INFINITE_DIMENSIONAL_AMBIGUITY_WITNESS",
    "FINITE_LINEAR_SELECTOR_IMPOSSIBILITY_SCOPED",
    "MULTIPLICATIVE_SELECTOR_POWER_CONDITIONAL_SCOPED",
]


def text(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def check() -> dict:
    errors: list[str] = []
    checks: dict[str, bool] = {}

    missing = [p for p in REQUIRED_FILES if not (ROOT / p).is_file()]
    checks["required_files_exist"] = not missing
    if missing:
        errors.append(f"missing required files: {missing}")

    if missing:
        return {"valid": False, "checks": checks, "errors": errors}

    cd001 = text("results/CD001_SELECTOR_POWER_BASELINE_RESULT.md")
    cd002a = text("results/CD002A_MULTIPLICATIVE_COMPOSITION_COHERENCE_RESULT.md")
    front = text("recovery/CURRENT_FRONT.md")
    pro = text("recovery/PRO_FRONTIER.md")
    locks = text("authority/CLAIM_LOCKS.md")
    manifest = text("authority/UPSTREAM_IMPORT_MANIFEST.md")
    ledger = text("research_log/CDSR_LEDGER.md")
    state = json.loads(text("recovery/state.json"))

    checks["cd001_classification_consistent"] = CD001_CLASS in cd001 and CD001_CLASS in front and CD001_CLASS in ledger
    checks["cd002a_classification_consistent"] = CD002A_CLASS in cd002a and CD002A_CLASS in front and CD002A_CLASS in ledger
    if not checks["cd001_classification_consistent"]:
        errors.append("CD001 classification mismatch")
    if not checks["cd002a_classification_consistent"]:
        errors.append("CD002-A classification mismatch")

    checks["terminal_front_is_cd002a"] = (
        state.get("current_terminal_iteration") == "CD002-A"
        and "Authoritative CDSR terminal front:** `CD002-A`" in front
    )
    if not checks["terminal_front_is_cd002a"]:
        errors.append("terminal front is not consistently CD002-A")

    checks["pro_frontier_present"] = (
        "SOURCE_FAITHFUL_CAUSAL_COMPOSITION_TO_EXTENSION_COHERENCE_LAW" in pro
        and "Does the actual source-faithful causal many-vertex/refinement structure induce" in pro
    )
    if not checks["pro_frontier_present"]:
        errors.append("PRO_FRONTIER central question/frontier missing")

    false_ok = all(re.search(rf"\b{re.escape(k)}\s*=\s*false\b", locks) for k in FALSE_LOCKS)
    true_ok = all(re.search(rf"\b{re.escape(k)}\s*=\s*true\b", locks) for k in TRUE_LOCKS)
    checks["mandatory_claim_locks_present"] = false_ok and true_ok
    if not checks["mandatory_claim_locks_present"]:
        errors.append("mandatory claim locks incomplete")

    checks["iter080k_provenance_firewall"] = "INVALID_PROVENANCE" in manifest and "must never be cited as authoritative `NEW_PRIMARY_AUTHORITY`" in manifest
    checks["iter081f_not_promoted"] = "PROSPECTIVE_ONLY / NO_TERMINAL_RESULT" in manifest
    if not checks["iter080k_provenance_firewall"]:
        errors.append("Iter080K provenance firewall missing")
    if not checks["iter081f_not_promoted"]:
        errors.append("Iter081F no-terminal-result lock missing")

    # Selected local references that must resolve. Upstream paths are intentionally
    # excluded because they belong to another repository and are pinned in the manifest.
    local_refs = [
        "authority/FACT_LEVEL.md",
        "authority/UPSTREAM_IMPORT_MANIFEST.md",
        "authority/THEOREM_AND_OBSTRUCTION_REGISTRY.md",
        "authority/SOURCE_COMPOSITION_INVENTORY.md",
        "authority/SOURCE_DERIVATION_REQUIRED.md",
        "authority/CLAIM_LOCKS.md",
        "docs/AMBIGUITY_SPACE.md",
        "docs/PHYSICAL_EQUIVALENCE.md",
        "docs/SELECTOR_POWER_MATRIX.md",
        "docs/COHERENCE_DEFORMATION_CLASSES.md",
        "docs/NORMAL_JET_FRONTIER.md",
        "protocol/NO_SMUGGLING_TEST.md",
        "prereg/PRO_GATE_TEMPLATE.md",
        "recovery/CURRENT_FRONT.md",
        "recovery/PRO_FRONTIER.md",
        "recovery/DEPENDENCY_DAG.md",
        "recovery/state.json",
        "research_log/CDSR_LEDGER.md",
    ]
    unresolved = [p for p in local_refs if not (ROOT / p).is_file()]
    checks["selected_local_references_resolve"] = not unresolved
    if unresolved:
        errors.append(f"unresolved local refs: {unresolved}")

    md_text = "\n".join(p.read_text(encoding="utf-8") for p in ROOT.rglob("*.md"))
    stale_patterns = [
        r"\bCD001\s+active\b",
        r"\bCD002-A\s+active\b",
        r"CURRENT_CDSR_TERMINAL_ITERATION\s*=\s*CD001\b",
    ]
    stale = [pat for pat in stale_patterns if re.search(pat, md_text, flags=re.IGNORECASE)]
    checks["no_stale_active_front_markers"] = not stale
    if stale:
        errors.append(f"stale front markers: {stale}")

    dangerous = []
    for p in ROOT.rglob("*"):
        if not p.is_file() or p.suffix not in {".md", ".json", ".py"}:
            continue
        t = p.read_text(encoding="utf-8")
        # Ignore validator source literals themselves.
        if p.resolve() == Path(__file__).resolve():
            continue
        for key in ("UNIQUE_K5_EXTENSION", "NEW_PHYSICS_FOUND"):
            if re.search(rf"\b{key}\s*=\s*true\b", t):
                dangerous.append(f"{p.relative_to(ROOT)}:{key}=true")
    checks["no_accidental_scientific_promotions"] = not dangerous
    if dangerous:
        errors.append(f"accidental promotions: {dangerous}")

    # State sanity only; readiness score is deliberately not treated as scientific evidence.
    checks["state_has_required_sections"] = all(
        k in state
        for k in [
            "repository", "state_date", "programme_status", "current_terminal_iteration",
            "current_frontier", "established_theorem_ids", "open_blockers",
            "source_locks", "prohibited_claims", "recommended_pro_target",
            "dependency_graph", "readiness"
        ]
    )
    if not checks["state_has_required_sections"]:
        errors.append("state.json missing required keys")

    return {"valid": not errors and all(checks.values()), "checks": checks, "errors": errors}


if __name__ == "__main__":
    result = check()
    print(json.dumps(result, indent=2, sort_keys=True))
    sys.exit(0 if result["valid"] else 1)
