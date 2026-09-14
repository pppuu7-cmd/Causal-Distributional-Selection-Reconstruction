# Causal Distributional Selection Reconstruction (CDSR)

Independent research program on **selection principles for source-compatible distributional extensions** in causal Lorentzian spin-foam amplitudes.

## Central question

The upstream CRQN/MSQGR analysis has reached a scoped but strong obstruction: after the off-collision K5 object and the already-frozen source constraints are fixed, the admissible local extension freedom still contains an infinite-dimensional tangential subspace. CDSR asks:

> **Is there an independently motivated physical or structural principle that uniquely selects the joint K5 distributional extension?**

CDSR is deliberately separate from MSQGR/CRQN. It does not retroactively promote a new axiom into CRQN v0.2. A positive selector discovered here would be **new model content** until independently justified.

## Frozen upstream baseline

Primary upstream anchor:

- `Mechanism-Synthesis-QG-Reconstruction/results/ITER077Q_SM_INVARIANT_TANGENTIAL_AMBIGUITY_RESULT.md`
- upstream result commit lineage recorded there; result blob SHA `26aa90965ccfe495f55df2f4c190f7bbe09093f4`.

The exact construction gives a source-compatible linearly independent family

```text
{ Q(y)^n F(y) delta_N(x) : n = 0,1,2,... }
```

on the common-collision manifold `N = SU(2)^4`, before the additional allowed normal-derivative sectors are used. Thus the already-admissible K5 extension is function-space underdetermined, not merely ambiguous by one scalar finite part.

Important upstream negative controls already exist and must not be rediscovered as if new:

1. **Wavefront/conormal admissibility alone is insufficient.** Upstream Iter080J shows that smooth tangential multipliers preserve the relevant WF admissibility, so the infinite family survives.
2. **Bare combinatorial gluing is insufficient.** Upstream Iter079C shows exact normalization/internal-weight nonuniqueness already for a minimal two-vertex composition unless extra inheritance data are supplied.
3. **One-wedge Toller analyticity is not yet a joint-K5 selector.** Bianchi--Chen--Gamonal, arXiv:2604.24945, uniquely characterize the individual Toller branches through analytic/asymptotic conditions and the additive split `T+ + T- = D`; upstream Iter080K found no explicit simultaneous ten-wedge collision-extension rule in that source.
4. **Selected Toller branches cannot simply inherit standard boundedness estimates unchanged.** Upstream Iter081E gives exact minimal-spin pure-boost counterexamples; the upstream Iter081F branch-subset cancellation gate is currently a separate boundedness question, not a K5-extension selection theorem.

## Mathematical object

Let `t0` denote the already-defined off-singular K5 distribution on `X \ N`, and let `B` denote the frozen CRQN v0.2 admissibility constraints. Define

```text
Ext_B(t0) = { T in D'(X) : T|_(X\N) = t0 and B[T] = 0 }.
```

When nonempty this is an affine space

```text
Ext_B(t0) = T_* + A_B,
```

where the ambiguity space `A_B` consists of distributions supported on `N`. Iter077Q proves that `A_B` contains at least a countably infinite-dimensional smooth-tangential subspace.

A candidate new principle `P` defines

```text
Sol(P) = { T in Ext_B(t0) : P[T] = 0 }.
```

A CDSR selector succeeds only if `Sol(P)` is exactly one physical equivalence class **and** the specification of `P` does not itself contain arbitrary data equivalent to choosing that class by hand.

## No-smuggling criterion

A proposed selector is not explanatory if its definition requires freely chosen functional data whose independent degrees of freedom can encode the same ambiguity directions it claims to remove. Such a prescription is a reparameterization of the extension choice, not a reconstruction.

This criterion will be sharpened prospectively. It is initially a methodological lock, not a claimed general theorem.

## Acceptance gates for any selector

A candidate principle must be tested for all of the following before promotion:

- **existence** on the frozen off-collision object;
- **uniqueness** modulo a prospectively declared physical equivalence;
- **source fidelity**: fixed causal labels, boundary-state linearity, common-left gauge covariance, relabeling covariance;
- **distributional admissibility**: support/scaling/wavefront requirements appropriate to the frozen object;
- **coherence** under every composition/refinement operation that the principle invokes;
- **nontriviality**: it cannot select only by reverting to the full non-causal/Wigner object unless that is the explicit scientific conclusion;
- **no smuggling** of arbitrary coefficient functions, kernels, measures, subtraction maps, boundary maps or normalization data;
- **out-of-sample stability** across controls not used to formulate the rule.

## Research fronts

### F01 — Composition/coherence selector

Test whether a genuinely source-derived many-vertex composition law plus associativity/coherence across multiple decompositions can impose an effectively infinite family of constraints on `A_B`. Bare two-vertex gluing is already known to be insufficient, so the target is a **coherence law**, not a single contraction formula.

### F02 — Joint causal analyticity

Lift the one-wedge Toller uniqueness mechanism to the actual simultaneous K5 collision problem. The question is not whether each wedge branch is unique; it is whether a joint holomorphic/boundary-value object with prospectively fixed growth, spectrum and compatibility conditions has a unique boundary distribution at the common collision.

### F03 — Refinement/RG naturality

Treat extensions across refinements as a compatible family. Test whether cylindrical consistency, semigroup/functorial composition, or an RG fixed/natural-section condition selects a unique extension rather than merely an RG scheme/orbit. Existing finite tensor controls from upstream MSQGR are motivation only, not authority for the physical selector.

### F04 — Boundary/source naturality

Ask whether compatibility with a sufficiently rich class of true boundary states and source compositions determines the tangential coefficient functions. This front must distinguish a genuinely universal naturality law from an arbitrarily chosen complete set of probes.

## First iteration

`CD001` establishes the project floor:

1. formalize the affine ambiguity space and selector map;
2. prove the finite-linear-selector impossibility lemma for an infinite-dimensional ambiguity subspace;
3. freeze the no-smuggling test and the distinction between finite scalar constraints and functional/coherence laws;
4. produce a selector power matrix that determines which fronts can still plausibly yield uniqueness.

See `prereg/CD001_SELECTOR_POWER_BASELINE.md` once committed.

## Interpretation ceiling

CDSR begins with **no unique K5 extension**, **no CRQN v0.3**, **no regulator-independence claim**, **no RG closure**, and **no new-physics claim**. Negative selector results are first-class scientific outputs.

A future positive result is credited to CDSR as a new principle unless and until an independent derivation shows that it was already forced by the original CRQN source data.
