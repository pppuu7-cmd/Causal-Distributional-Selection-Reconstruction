#!/usr/bin/env python3
"""CD003 exact regression controls, not a proof engine or physical selector.

Run: python analysis/cd003_exact_controls.py --output results/CD003_EXACT_CONTROLS.json
Requires SymPy. The general theorems and domain restrictions are in the derivation.
No source predicates are inferred from keyword matches or from green execution.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import platform
import sympy as sp

PREREG = "c3f898a975b56f3f707c00d3e01cf5388934d9f7"


def zero_matrix(a: sp.MatrixBase) -> bool:
    return all(sp.expand(x) == 0 for x in a)


def matrix_strings(a: sp.MatrixBase) -> list[list[str]]:
    return [[str(sp.expand(a[i, j])) for j in range(a.cols)] for i in range(a.rows)]


def run() -> dict:
    checks = {}
    b = sp.diag(2, 3)
    unit = b.inv()

    def glue(x, y):
        return x * b * y

    variables = sp.symbols("x0:16")
    x, y, z, w = [sp.Matrix(2, 2, variables[k:k + 4]) for k in (0, 4, 8, 12)]
    left = glue(glue(x, y), z)
    right = glue(x, glue(y, z))
    checks["generic_three_vertex_reassociation"] = {
        "passed": zero_matrix(left - right),
        "kind": "exact polynomial identity, twelve independent entries",
    }
    four = [
        glue(glue(glue(x, y), z), w),
        glue(glue(x, glue(y, z)), w),
        glue(glue(x, y), glue(z, w)),
        glue(x, glue(glue(y, z), w)),
        glue(x, glue(y, glue(z, w))),
    ]
    checks["all_five_four_vertex_parenthesizations"] = {
        "passed": all(zero_matrix(q - four[0]) for q in four),
        "kind": "exact polynomial identity, sixteen independent entries",
    }
    checks["fixed_structural_unit"] = {
        "passed": zero_matrix(glue(unit, x) - x) and zero_matrix(glue(x, unit) - x),
        "unit": matrix_strings(unit),
    }
    checks["orientation_reversal_control"] = {
        "passed": zero_matrix(glue(x, y).T - glue(y.T, x.T)),
        "scope": "transpose duality for this fixed symmetric pairing only",
    }
    checks["illegal_vertex_swap_is_not_identity"] = {
        "passed": not zero_matrix(glue(x, y) - glue(y, x)),
        "kind": "negative control: noncommuting vertex order is preserved",
    }

    lam = sp.symbols("lambda")
    a = sp.Matrix([[1, lam], [0, 1]])
    triple = sp.expand(glue(glue(a, a), a))
    expected = sp.Matrix([[4, 19 * lam], [0, 9]])
    checks["fixed_pairing_distinct_output_countermodel"] = {
        "passed": zero_matrix(triple - expected)
        and triple[0, 1].subs(lam, 0) != triple[0, 1].subs(lam, 1),
        "pairing": matrix_strings(b),
        "generator": matrix_strings(a),
        "three_vertex_output": matrix_strings(triple),
        "fixed_probe": "row 1 / column 2 open-boundary component",
        "outputs_at_0_and_1": [str(triple[0, 1].subs(lam, k)) for k in (0, 1)],
        "scope": "finite tensor countermodel, NOT the physical K5 tensor",
    }

    c = sp.diag(sp.Rational(1, 2), lam / 3)
    defect = sp.expand(glue(c, c) - c)
    checks["different_vertex_count_relation_has_content"] = {
        "passed": not zero_matrix(defect)
        and zero_matrix(defect.subs(lam, 0))
        and zero_matrix(defect.subs(lam, 1))
        and not zero_matrix(defect.subs(lam, 2)),
        "defect": matrix_strings(defect),
        "scope": "C B C = C is extra generator dynamics, not reassociation; not a proposed law",
    }

    n1, n2 = sp.symbols("n1 n2")
    h0, h1, h2, h8 = sp.symbols("h0 h1 h2 h8")
    test = h0 + h1 * n1 + h2 * n1 ** 2 / 2 + h8 * n1 ** 8 / sp.factorial(8)
    jet_values = {
        str(k): sp.simplify((-1) ** k * sp.diff(test, n1, k).subs(n1, 0))
        for k in (0, 1, 2, 8)
    }
    checks["normal_jet_dual_signs_and_order_eight"] = {
        "passed": list(jet_values.values()) == [h0, -h1, h2, h8],
        "values": {k: str(v) for k, v in jet_values.items()},
        "scope": "polynomial jets of a smooth compact test with cutoff equal to one near N",
    }
    mixed = sp.diff(n1 ** 2 * n2, n1, 2, n2, 1).subs({n1: 0, n2: 0}) * (-1) ** 3
    checks["mixed_normal_derivative"] = {"passed": mixed == -2, "value": str(mixed)}
    invisible = -sp.diff(sp.Integer(1), n1)
    visible = -sp.diff(n1, n1)
    checks["zeroth_trace_does_not_detect_first_normal_jet"] = {
        "passed": invisible == 0 and visible == -1,
        "delta_prime_on_flat_test": str(invisible),
        "delta_prime_on_linear_test": str(visible),
    }
    t, a0 = sp.symbols("t a")
    # Pushforward convention: (Phi_*u)(test) = u(test composed with Phi).
    composed_test = h0 + h1 * (t + a0 * t ** 2) + h2 * (t + a0 * t ** 2) ** 2 / 2
    pushed_d2 = sp.diff(composed_test, t, 2).subs(t, 0)
    checks["local_coordinate_pushforward_can_mix_jet_orders"] = {
        "passed": sp.expand(pushed_d2 - (h2 + 2 * a0 * h1)) == 0,
        "dual_value": str(sp.expand(pushed_d2)),
        "distribution_expression": "delta_second - 2*a*delta_first",
        "scope": "Phi(t)=t+a*t^2 near zero only; NOT a source-derived refinement map",
    }

    plus = [1] + [0] * 11
    minus = [-v for v in plus]
    checks["diagonal_pullback_transversality_warning"] = {
        "passed": any(plus) and any(minus) and all(p + q == 0 for p, q in zip(plus, minus)),
        "conormals": [plus, minus],
        "classification": "STANDARD_WAVEFRONT_PRODUCT_CRITERION_NOT_SATISFIED",
        "scope": "no attempted delta squared; failure of sufficient criterion is NOT an all-prescriptions impossibility theorem",
    }
    ok = all(c["passed"] for c in checks.values())
    return {
        "gate": "CD003_STRUCTURAL_GLUING_VS_EXTENSION_SELECTION",
        "prereg_commit": PREREG,
        "execution_valid": ok,
        "control_count": len(checks),
        "control_results": checks,
        "runtime": {"python": platform.python_version(), "sympy": sp.__version__},
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "verdict": "PASS_EXACT_CONTROLS" if ok else "INVALID_IMPLEMENTATION",
        "scientific_authority": "analytic derivation, NOT this finite suite",
        "physical_selector_established": False,
        "physical_k5_amplitude_computed": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("verdict", "control_count", "execution_valid", "script_sha256")}, indent=2))
    if not report["execution_valid"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
