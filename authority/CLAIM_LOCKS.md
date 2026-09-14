# Claim Locks

These booleans are the authoritative CDSR preparation locks at the CD002-A terminal front. `false` means the claim is not currently authorized; it does not mean an impossibility theorem has been proved.

## Prohibited / not established

```text
UNIQUE_K5_EXTENSION = false
PHYSICAL_SELECTOR_DERIVED = false
CRQN_V0_3_AUTHORIZED = false
REGULATOR_INDEPENDENCE = false
RG_CLOSURE = false
CAUSAL_MULTIVERTEX_CLOSURE = false
NEW_PHYSICS_FOUND = false
QUANTUM_GRAVITY_SOLVED = false
```

Additional locks:

```text
PHYSICAL_EQUIVALENCE_QUOTIENT_COMPLETE = false
NORMAL_JET_SELECTOR_COMPLETE = false
OVERALL_SUPPORTED_SCALAR_FIXED = false
JOINT_K5_REGULATOR_DERIVED = false
ITER081F_TERMINAL_RESULT_IMPORTED = false
ITER080K_NEW_PRIMARY_AUTHORITY_VALID = false
```

## Established scoped facts

```text
INFINITE_DIMENSIONAL_AMBIGUITY_WITNESS = true
FINITE_LINEAR_SELECTOR_IMPOSSIBILITY_SCOPED = true
MULTIPLICATIVE_SELECTOR_POWER_CONDITIONAL_SCOPED = true
```

Supporting statuses:

```text
CURRENT_CDSR_TERMINAL_ITERATION = CD002-A
CURRENT_FRONTIER = SOURCE_FAITHFUL_CAUSAL_COMPOSITION_TO_EXTENSION_COHERENCE_LAW
```

## Interpretation

- `INFINITE_DIMENSIONAL_AMBIGUITY_WITNESS=true` means an infinite-dimensional subspace is proved to exist; it does not mean all of `A_B` is classified.
- `FINITE_LINEAR_SELECTOR_IMPOSSIBILITY_SCOPED=true` is CD001's exact scoped theorem.
- `MULTIPLICATIVE_SELECTOR_POWER_CONDITIONAL_SCOPED=true` is CD002-A's conditional theorem and **does not** imply `PHYSICAL_SELECTOR_DERIVED=true`.

## Mutation rule

A future commit may change a `false` lock to `true` only when a cited terminal prospective result establishes that exact claim and all mandatory dependencies are closed. Administrative readiness, a passing validator, or a successful conditional theorem cannot flip a scientific claim lock.
