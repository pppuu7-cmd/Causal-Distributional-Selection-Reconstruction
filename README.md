# Causal Distributional Selection Reconstruction (CDSR)

Independent research program on **selection principles for source-compatible distributional extensions** in causal Lorentzian spin-foam amplitudes.

## Current authoritative state

- CDSR terminal scientific iteration: **CD002-A** (`PASS_EXACT_CONDITIONAL_SCOPED`).
- Current fundamental frontier: `SOURCE_FAITHFUL_CAUSAL_COMPOSITION_TO_EXTENSION_COHERENCE_LAW`.
- No physical K5 selector is derived; no unique K5 extension is established.
- The authoritative recovery entrypoint is `recovery/CURRENT_FRONT.md`.
- The next deep-run handoff is `recovery/PRO_FRONTIER.md`.
- Machine-readable state is `recovery/state.json`.
- Claim firewalls are `authority/CLAIM_LOCKS.md` and `authority/SOURCE_DERIVATION_REQUIRED.md`.

A new session should recover the repository from those files rather than from chat history.

## Central question

The upstream CRQN/MSQGR analysis has reached a scoped but strong obstruction: after the off-collision K5 object and the already-frozen source constraints are fixed, the admissible local extension freedom still contains an infinite-dimensional tangential subspace. CDSR asks:

> **Is there an independently motivated physical or structural principle that uniquely selects the joint K5 distributional extension?**

CDSR is deliberately separate from MSQGR/CRQN. It does not retroactively promote a new axiom into CRQN v0.2. A positive selector discovered here would be new model content unless an independent derivation establishes that it was already source-forced.

## Frozen upstream baseline

Primary upstream anchor:

- `Mechanism-Synthesis-QG-Reconstruction/results/ITER077Q_SM_INVARIANT_TANGENTIAL_AMBIGUITY_RESULT.md`
- result blob SHA `26aa90965ccfe495f55df2f4c190f7bbe09093f4`.

The exact construction gives a source-compatible linearly independent family

```text
{ Q(y)^n F(y) delta_N(x) : n = 0,1,2,... }
```

on the common-collision manifold `N = SU(2)^4`, before additional allowed normal-derivative sectors are exhausted. This proves at least a countably infinite-dimensional tangential subspace; it does **not** provide a complete characterization of the full ambiguity space.

Important upstream controls already exist and must not be rediscovered as new:

1. **Finite K5 permutation covariance alone is insufficient.** Upstream Iter080A leaves an infinite-dimensional invariant tangential ambiguity.
2. **Wavefront/conormal admissibility alone is insufficient.** Upstream Iter080J shows the smooth tangential witness family survives the tested WF condition.
3. **Bare combinatorial gluing is insufficient.** Upstream Iter079C exhibits exact pairing-normalization/internal-weight nonuniqueness in a frozen minimal two-vertex control.
4. **The frozen primary source corpus has no explicit complete joint-K5 selector.** Repaired Iter080E is the controlling source-census authority.
5. **Historical Iter080K is not a new-authority result.** Its Critic review is `INVALID_PROVENANCE` because arXiv:2604.24945 was already represented in Iter080E. Its one-wedge source observations are corroborative only.
6. **Selected Toller branches cannot inherit the standard Han bound unchanged on the frozen Iter081E control.** Iter081E gives exact scoped counterexamples.
7. **Iter081F currently has no terminal result.** At the state read, only the prospective branch-subset boundedness gate commit `01b4ad5369798a4548576bb282afdd89375e4a59` exists.

Exact imported authority and ceilings are in `authority/UPSTREAM_IMPORT_MANIFEST.md`.

## Mathematical object

Let `t0` denote the already-defined off-singular K5 distribution on `X \ N`, and let `B` denote the frozen CRQN v0.2 admissibility constraints. Define

```text
Ext_B(t0) = { T in D'(X) : T|_(X\N) = t0 and B[T] = 0 }.
```

When nonempty, choose a reference extension and write affine notation

```text
Ext_B(t0) = T_* + A_B.
```

The safe established inclusions are only

```text
A_B ⊇ A_tan,
A_tan ⊇ span_C{Q^n F delta_N : n>=0}.
```

See `docs/AMBIGUITY_SPACE.md` for the no-overclaim notation and `docs/NORMAL_JET_FRONTIER.md` for the upstream order-8 normal-jet ceiling.

A candidate principle `P` defines schematically

```text
Sol(P) = { T in Ext_B(t0) : P[T] = 0 }.
```

A physical CDSR selector succeeds only if the selected set is one **defined physical equivalence class** and the specification of `P` does not hide arbitrary data equivalent to choosing the extension by hand.

## Established CDSR science

### CD001 — finite-linear selector impossibility

Preregistration `124374857f3bfaedc9dea8aefc88801eb2a9976c`; result `d5e296eff8cf76a97b32ac623ba7ffd59935350e`.

Classification:

`CD001_FINITE_LINEAR_SCALAR_SELECTOR_CANNOT_UNIQUELY_SELECT_INFINITE_DIMENSIONAL_K5_AMBIGUITY_EXACT_SCOPED`.

A fixed finite family of affine-linear scalar conditions cannot select a singleton from a nonempty affine extension space whose ambiguity contains an infinite-dimensional subspace.

### CD002-A — multiplicative selector-power control

Preregistration `473bf95e258cf2ac0e43cb9452fb04f39e9f88cc`; result `17d14afca62a91daef4a9ad66739f03956374f40`.

Classification:

`CD002A_SU2_4_MULTIPLICATIVE_COHERENCE_COLLAPSES_SMOOTH_TANGENTIAL_MULTIPLIER_TO_CONSTANT_EXACT_CONDITIONAL_SCOPED`.

For smooth `f:SU(2)^4->C`, the conditional equations

```text
f(gh)=f(g)f(h),
f(e)=1
```

imply `f=1`.

This proves **selector power**, not physical source derivation. The actual causal many-vertex/refinement object has not been shown to induce this law; the overall supported scalar and normal jets remain open. The repository therefore strictly separates

```text
IF P THEN reduction/uniqueness
```

from

```text
SOURCE IMPLIES P.
```

See `authority/FACT_LEVEL.md`.

## No-smuggling and source-authority discipline

A physical selector law must be one of:

- `SOURCE_DERIVED`, or
- `NEW_PHYSICAL_PRINCIPLE`.

A mathematical control is `CONDITIONAL_SELECTOR_POWER_ONLY`. There is no implicit “reasonable assumption” category.

The operational selector audit is `protocol/NO_SMUGGLING_TEST.md`. Physical-equivalence status is `docs/PHYSICAL_EQUIVALENCE.md`. Current selector classes and unknowns are `docs/SELECTOR_POWER_MATRIX.md`.

## Research fronts

### F01 — source-faithful composition/coherence

Determine what transport/coherence law, if any, follows from an actual causal many-vertex/refinement construction and how it acts on supported extension data. Do not assume the CD002-A law.

### F02 — joint causal analyticity

Test only a genuinely joint K5 boundary-value/analytic object if independently source-defined or prospectively introduced as new principle. One-wedge Toller uniqueness is not itself a joint collision-extension theorem.

### F03 — refinement/RG naturality

Test compatible families of extensions only after the physical coarse/fine maps and extension transport are defined. Do not confuse a chosen RG scheme with unique selection.

### F04 — boundary/source naturality

Ask whether a genuinely universal source/boundary naturality law constrains the ambiguity without replacing it by an arbitrary complete probe family.

## Next deep-run frontier

The exact handoff is `recovery/PRO_FRONTIER.md`. The central question is whether actual source-faithful causal many-vertex/refinement structure induces a functional coherence law on **full supported K5 extension data** with enough power to reduce `Ext_B(t0)` to one physical equivalence class without selector-data smuggling, and if not, what residual functional/cohomological/normal-jet freedom survives.

Possible organizational directions CD003-A/B/C are deliberately **not** preregistered as a mandatory sequence. The next deep run is free to reorder them by information gain after source recovery.

## Interpretation ceiling

Current claim locks remain:

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

Read `authority/CLAIM_LOCKS.md` before any downstream promotion.
