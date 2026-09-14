# CURRENT FRONT — CDSR

**State date:** 2026-09-14  
**State-read CDSR head:** `17d14afca62a91daef4a9ad66739f03956374f40`  
**Authoritative CDSR terminal front:** `CD002-A` (`PASS_EXACT_CONDITIONAL_SCOPED`)  
**Preparation purpose:** recovery/provenance/readiness only. This document does not preregister or solve CD003.

## Established upstream

Let `t0` denote the already-defined source-ordered off-collision K5 distribution on `X \ N`, and let `B` denote the frozen CRQN v0.2 admissibility conditions imported only in their established scope. The CDSR working notation is

```text
Ext_B(t0) = { T in D'(X) : T|_(X\N) = t0 and B[T] = 0 }.
```

When nonempty, choose a reference extension `T_*` and write the affine space schematically as

```text
Ext_B(t0) = T_* + A_B.
```

This notation does not claim a complete classification of `A_B`.

### Iter077L scaling-degree authority

Upstream Iter077L establishes the common-collision manifold

```text
N = SU(2)^4 subset SL(2,C)^4,
```

with real codimension `12`, transverse scaling degree `20`, existence but nonuniqueness of same-scaling-degree local extensions, and normal-derivative freedom through order `8`. It explicitly does not assert that every allowed order-8 local term is physically admissible.

### Iter077Q ambiguity theorem

Upstream Iter077Q proves that `A_B` contains at least a countably infinite-dimensional smooth tangential subspace. In particular, for an authorized nonzero tangential boundary coefficient `F` and nonconstant invariant `Q`, the family

```text
{ Q(y)^n F(y) delta_N(x) : n = 0,1,2,... }
```

is linearly independent and source-compatible in the frozen scope.

Therefore CDSR may use only the inclusions

```text
A_B ⊇ A_tan,
A_tan ⊇ span_C{Q^n F delta_N : n>=0}.
```

No equality, direct-sum decomposition, or complete description of `A_B` is imported.

## Relevant upstream obstructions

- Iter079C: local one-vertex data plus a bare combinatorial two-vertex gluing skeleton do not uniquely fix the composed functional; pairing normalization and internal weight freedom survive. This is a scoped underdetermination result, not a no-go theorem for causal multivertex theory.
- Iter080B: parent EPRL/KKL E3/E4/E6 structures and causal local/generalized vertices exist separately, but the complete physical causal many-vertex E3/E4/E6 inheritance bridge is not source-explicit in the frozen corpus. Verdict `BLOCKED_SOURCE_BRIDGE`.
- repaired Iter080E: the frozen Bianchi–Chen–Gamonal / Beltran corpus contains no explicit P1–P5-complete correlated joint-K5 selector acting on the full Iter077Q function-space ambiguity. Verdict `BLOCKED_OBJECT_DEFINITION` in that corpus.
- Iter080J: support plus ordinary conormal/wavefront admissibility alone preserves the Iter077Q smooth tangential witness family and does not uniquely select the extension.
- Iter080K: historical gate is `INVALID_PROVENANCE` because it falsely treated arXiv:2604.24945 as new primary authority although it was already frozen in Iter080E. Its independently rechecked source observations may be used only as corroboration, not as a new-authority terminal result.
- Iter081B: direct transport of Han's standard face/stack conclusions to a single Toller branch is not source-proven.
- Iter081E: exact minimal-spin pure-boost counterexamples show that the unchanged Han projected contraction / `d_j^2` face bound cannot simply be transplanted to the frozen selected-Toller objects. This is not a theorem that every causal face functional diverges.
- Iter081F: as of the state read, only the prospective branch-subset boundedness pre-gate exists (`01b4ad5369798a4548576bb282afdd89375e4a59`); there is no terminal Iter081F result to import.

## CD001 — exact CDSR theorem

Authority:
- prereg `124374857f3bfaedc9dea8aefc88801eb2a9976c`;
- result `d5e296eff8cf76a97b32ac623ba7ffd59935350e`.

If an admissible ambiguity space contains an infinite-dimensional subspace and the selected set is nonempty, any **fixed finite family of affine-linear scalar conditions** cannot select a unique extension.

Classification:

`CD001_FINITE_LINEAR_SCALAR_SELECTOR_CANNOT_UNIQUELY_SELECT_INFINITE_DIMENSIONAL_K5_AMBIGUITY_EXACT_SCOPED`.

This does not rule out nonlinear, infinite, analytic, coherence, naturality, positivity, spectral, or source-derived conditions with greater functional power.

## CD002-A — conditional selector-power theorem

Authority:
- prereg `473bf95e258cf2ac0e43cb9452fb04f39e9f88cc`;
- result `17d14afca62a91daef4a9ad66739f03956374f40`.

For smooth

```text
f : SU(2)^4 -> C
```

with

```text
f(gh)=f(g)f(h),
f(e)=1,
```

one has

```text
f=1.
```

Classification:

`CD002A_SU2_4_MULTIPLICATIVE_COHERENCE_COLLAPSES_SMOOTH_TANGENTIAL_MULTIPLIER_TO_CONSTANT_EXACT_CONDITIONAL_SCOPED`.

**Critical ceiling:** this proves selector power only. It does **not** prove that actual source-faithful causal composition induces componentwise multiplication on `SU(2)^4`, does not fix an overall supported scalar coefficient, and does not act on the higher normal-jet sectors.

## Four authority levels

Every statement entering future CDSR reasoning must have exactly one `FACT_LEVEL` defined in `authority/FACT_LEVEL.md`:

1. `UPSTREAM_ESTABLISHED`
2. `CDSR_EXACT_THEOREM`
3. `CONDITIONAL_SELECTOR_POWER`
4. `OPEN_PHYSICAL_BRIDGE`

Never promote

```text
IF P THEN UNIQUE
```

to

```text
SOURCE IMPLIES P.
```

## Current open blockers

1. `O1_PHYSICAL_COMPOSITION_LAW_NOT_DERIVED`.
2. `O2_OVERALL_SUPPORTED_SCALAR_NOT_FIXED_BY_CD002A`.
3. `O3_NORMAL_DERIVATIVE_SECTORS_UNTOUCHED_BY_CD002A`.
4. `O4_COCYCLE_PROJECTIVE_WEIGHTED_AFFINE_ESCAPE_CLASSES_UNCLASSIFIED`.
5. `O5_PHYSICAL_EQUIVALENCE_QUOTIENT_NOT_DEFINED_ENOUGH_FOR_UNIQUENESS`.
6. `O6_SOURCE_FAITHFUL_CAUSAL_MULTIVERTEX_BRIDGE_INCOMPLETE`.

## Current fundamental frontier

```text
SOURCE_FAITHFUL_CAUSAL_COMPOSITION_TO_EXTENSION_COHERENCE_LAW
```

The next deep run may choose the highest-information exact gate only after recovering the authority above. This preparation does not preregister the substantive hypothesis and does not select a physical law.

## Claim ceiling

At this front:

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
