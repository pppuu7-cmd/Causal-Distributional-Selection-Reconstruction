# Theorem and Obstruction Registry

**Rule:** entries are state records, not a substitute for their controlling result files. Every theorem keeps its interpretation ceiling; every obstruction remains open until a later authoritative result explicitly closes it.

## T1 — infinite-dimensional ambiguity witness

- `FACT_LEVEL`: `UPSTREAM_ESTABLISHED`
- Authority: upstream Iter077Q.
- Classification: `ITER077Q_SM_SOURCE_COMPATIBLE_K5_EXTENSION_AMBIGUITY_CONTAINS_INFINITE_DIMENSIONAL_TANGENTIAL_SUBSPACE_EXACT_THEOREM_SCOPED`.
- Statement: the source-compatible supported K5 ambiguity contains the linearly independent family

```text
{ Q(y)^n F(y) delta_N(x) : n=0,1,2,... }
```

on `N=SU(2)^4`, hence at least a countably infinite-dimensional smooth tangential subspace.
- Ceiling: lower-bound witness only; not a full description of `A_B`.

## T2 — finite-linear-selector impossibility

- `FACT_LEVEL`: `CDSR_EXACT_THEOREM`
- Authority: CD001, prereg `124374857f3bfaedc9dea8aefc88801eb2a9976c`, result `d5e296eff8cf76a97b32ac623ba7ffd59935350e`.
- Classification: `CD001_FINITE_LINEAR_SCALAR_SELECTOR_CANNOT_UNIQUELY_SELECT_INFINITE_DIMENSIONAL_K5_AMBIGUITY_EXACT_SCOPED`.
- Statement: if an admissible affine extension space contains an infinite-dimensional ambiguity subspace and the selected set is nonempty, any fixed finite family of affine-linear scalar constraints leaves a nontrivial, indeed infinite-dimensional, kernel and cannot select a singleton.
- Ceiling: does not rule out nonlinear/infinite/functional/analytic/coherence/naturality/spectral/positivity conditions.

## T3 — normalized multiplicative character triviality on `SU(2)^4`

- `FACT_LEVEL`: `CONDITIONAL_SELECTOR_POWER`
- Authority: CD002-A, prereg `473bf95e258cf2ac0e43cb9452fb04f39e9f88cc`, result `17d14afca62a91daef4a9ad66739f03956374f40`.
- Classification: `CD002A_SU2_4_MULTIPLICATIVE_COHERENCE_COLLAPSES_SMOOTH_TANGENTIAL_MULTIPLIER_TO_CONSTANT_EXACT_CONDITIONAL_SCOPED`.
- Statement: for smooth `f:SU(2)^4->C`, normalized multiplicativity `f(gh)=f(g)f(h)`, `f(e)=1` implies `f=1`.
- Ceiling: proves mathematical selector power only. No source-derived causal composition law of this form has been established; overall supported scalar and normal jets remain open.

## O1 — physical composition law not derived

- Status: `OPEN`.
- `FACT_LEVEL`: `OPEN_PHYSICAL_BRIDGE`.
- Exact issue: no authority establishes that the actual source-faithful causal many-vertex/refinement construction acts on supported K5 extension data by the CD002-A multiplication law or by any alternative functional law with a defined domain/codomain.
- Blocking dependencies: upstream Iter080B `BLOCKED_SOURCE_BRIDGE`; supported extension transport E7/E8 not established.

## O2 — overall scalar supported coefficient not fixed by CD002-A

- Status: `OPEN`.
- `FACT_LEVEL`: `OPEN_PHYSICAL_BRIDGE`.
- Exact issue: CD002-A fixes the shape of a normalized multiplier under its conditional hypothesis. It does not establish a physical normalization equation fixing an overall coefficient multiplying a supported term.

## O3 — normal-derivative sectors untouched

- Status: `OPEN`.
- `FACT_LEVEL`: `OPEN_PHYSICAL_BRIDGE`.
- Authority for existence of the issue: upstream Iter077L permits extension differences involving normal derivatives through order 8 in the frozen scaling-degree scope.
- Exact issue: no CDSR theorem yet specifies how a physical composition/coherence law acts on this normal-jet tower.

## O4 — cocycle/projective/weighted/affine escape classes not classified

- Status: `OPEN`.
- `FACT_LEVEL`: `OPEN_PHYSICAL_BRIDGE` for physical relevance; mathematical search space only is defined in `docs/COHERENCE_DEFORMATION_CLASSES.md`.
- Exact issue: domain, coefficient object, regularity class, equivalence of deformations, and source relation must be frozen before any terminal classification.

## O5 — physical equivalence quotient not yet sufficient for unique-extension claim

- Status: `OPEN`.
- `FACT_LEVEL`: `OPEN_PHYSICAL_BRIDGE`.
- Exact issue: CDSR has not defined which extension differences are gauge-null, source-null, boundary-null, observationally null, or exact reparameterizations in a way sufficient to state uniqueness modulo physical equivalence.
- Consequence: `UNIQUE_K5_EXTENSION=true` is prohibited.

## O6 — source-faithful many-vertex causal bridge incomplete

- Status: `OPEN`.
- `FACT_LEVEL`: `UPSTREAM_ESTABLISHED` for the blocker; its future closure is `OPEN_PHYSICAL_BRIDGE`.
- Authority: upstream Iter080B.
- Exact issue: parent E3/E4/E6 data and causal local/generalized vertices are separately present, but their complete physical inheritance into a causal many-vertex functional is not source-explicit in the frozen corpus.

## Registry dependency rule

A future result may close an `O*` entry only by citing an exact prospective gate and terminal authority that addresses that obstruction. Closing one obstruction does not silently close neighboring ones. In particular:

```text
O1 closed  !=  O2 closed  !=  O3 closed  !=  O5 closed.
```

A unique physical extension claim requires every mandatory dependency on the path to uniqueness to be closed explicitly.
