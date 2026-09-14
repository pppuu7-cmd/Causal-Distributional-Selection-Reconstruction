# Prospective Pro Gate Template

**Template status:** infrastructure only. Do not treat blank/template fields as a preregistered scientific hypothesis.

```text
GATE_ID:

TARGET_HYPOTHESIS:

EXACT_OBJECT:

SOURCE_AUTHORITY:

DOMAIN:

EXTENSION_SPACE_SECTOR:

PHYSICAL_EQUIVALENCE:

CANDIDATE_COHERENCE_LAW:

DERIVATION_ROUTE:

NO_SMUGGLING_AUDIT:

EXISTENCE_TEST:

UNIQUENESS_TEST:

COUNTEREXAMPLE_SEARCH:

COCYCLE/PROJECTIVE_ESCAPE:

NORMAL_JET_EFFECT:

POSITIVE_CONTROLS:

NEGATIVE_CONTROLS:

PASS:

FAIL:

BLOCKED:

INVALID:

INTERPRETATION_CEILING:

DOWNSTREAM_AUTHORIZATION:
```

## Mandatory prereg rules

1. Fill `EXACT_OBJECT`, `SOURCE_AUTHORITY`, `DOMAIN`, and `EXTENSION_SPACE_SECTOR` before testing outcomes.
2. `CANDIDATE_COHERENCE_LAW` may be blank if the gate is a source audit whose purpose is to determine whether a law is explicitly derivable; do not invent one merely to complete the template.
3. `DERIVATION_ROUTE` must classify any physical law as `SOURCE_DERIVED` or `NEW_PHYSICAL_PRINCIPLE`. A mathematical control uses `CONDITIONAL_SELECTOR_POWER_ONLY`.
4. `PHYSICAL_EQUIVALENCE` must either cite a defined quotient or state explicitly that no physical-uniqueness claim is permitted in this gate.
5. `NO_SMUGGLING_AUDIT` must freeze the selector inputs and their authority before result inspection.
6. `COUNTEREXAMPLE_SEARCH` must include at least the strongest known ambiguity witnesses relevant to the frozen sector.
7. `COCYCLE/PROJECTIVE_ESCAPE` must not be filled with a precomputed terminal classification unless that is itself the prospectively frozen target.
8. `NORMAL_JET_EFFECT` must say `OUT_OF_SCOPE` only with an explicit claim ceiling preventing full-extension uniqueness promotion.
9. `PASS`, `FAIL`, `BLOCKED`, and `INVALID` must be mutually distinguishable before implementation.
10. `DOWNSTREAM_AUTHORIZATION` must list exactly which next claims/gates become admissible; it cannot silently authorize CRQN v0.3, regulator independence, or new physics.
