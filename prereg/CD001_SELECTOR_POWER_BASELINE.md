# CD001 — Selector Power Baseline

Status: **prospectively frozen before any CDSR selector implementation**  
Date: 2026-09-14

## 1. Purpose

Establish the minimum mathematical power a proposed K5 extension selector must have once the admissible ambiguity space is known to contain an infinite-dimensional linear subspace.

This iteration does **not** test a positive new physical principle. It proves a floor: several broad classes of weak selectors cannot uniquely determine the extension unless they introduce additional infinite-dimensional or nonlinear/coherence structure.

## 2. Frozen baseline

Let `E = T_* + A` be an affine space of admissible extensions of the same off-singular distribution, and let `V subset A` be an infinite-dimensional vector subspace. For the K5 application, upstream Iter077Q supplies an explicit countably infinite linearly independent family inside `V`.

A selector is evaluated on `E` only. Two extensions that differ by an element of `A` agree off the collision set by definition.

## 3. Theorem CD001-A — finite linear selector impossibility

Let `L_1,...,L_m` be linear functionals on `A`, with `m < infinity`. Suppose `E_P` is cut out from `E` by finitely many affine-linear constraints

```text
L_i(T - T_*) = c_i,   i=1,...,m.
```

If `E_P` is nonempty and `V` is infinite-dimensional, then `E_P` cannot be a singleton.

### Proof skeleton

Restrict the linear map

```text
L = (L_1,...,L_m): V -> K^m.
```

Since `V` is infinite-dimensional while the codomain is finite-dimensional, `ker(L|_V)` is nonzero (indeed infinite-dimensional). If `T in E_P` and `0 != v in ker(L|_V)`, then `T+v` satisfies the same affine constraints. Hence uniqueness fails.

The theorem applies only to a **fixed finite family of linear scalar conditions**. It does not rule out infinitely many constraints, nonlinear equations, analyticity classes, functorial/coherence laws, positivity cones with additional structure, or conditions that shrink the admissible space before the finite constraints are imposed.

## 4. Corollary CD001-B — finite moment/normalization lists are insufficient

Any selector that acts on the Iter077Q ambiguity only through a fixed finite list of scalar linear moments, normalizations, projections or pairings cannot uniquely select the K5 extension.

This includes a finite list of conditions of the schematic form

```text
<T, phi_i> = a_i
```

provided the induced conditions on the supported ambiguity are linear and finite in number.

## 5. Non-theorem / scope locks

CD001 does **not** claim:

- every finite-parameter physical principle fails;
- every nonlinear selector fails;
- analyticity cannot imply infinitely many effective constraints;
- composition/coherence cannot produce uniqueness;
- RG fixed-point conditions cannot produce uniqueness;
- positivity/reflection/spectral conditions cannot produce uniqueness;
- all functional equations are merely disguised counterterm choices.

Those stronger statements require separate prospective gates.

## 6. No-smuggling audit v0.1

For a proposed selector `P`, record its free input data `D_P`. Classify the proposal as `SMUGGLED_OR_UNRESOLVED` if, before solving the selector equations, any of the following hold:

1. `D_P` contains an arbitrary smooth function on the collision manifold or an arbitrary normal-jet family;
2. `D_P` contains an arbitrary kernel/operator whose unrestricted action on the ambiguity space can encode a target extension;
3. the selector is defined by explicitly referencing the desired extension/counterterm or its fitted coefficients;
4. the number/type of free functional inputs is not independently constrained by source, symmetry, composition, analyticity, or another preregistered external principle.

This is a diagnostic rule for CDSR workflow, not yet a theorem of equivalence between all such data and `A`.

## 7. Selector power matrix

Freeze the following expectations before implementation:

| Candidate class | CD001 uniqueness status | Reason / next gate |
|---|---|---|
| finite scalar linear constraints | `NO_UNIQUENESS` | theorem CD001-A |
| finite moment/normalization conditions | `NO_UNIQUENESS` | corollary CD001-B |
| WF/conormal admissibility alone | `UPSTREAM_NO_UNIQUENESS` | Iter080J baseline |
| bare two-vertex gluing | `UPSTREAM_NO_UNIQUENESS` | Iter079C baseline |
| one-wedge analyticity alone | `NO_JOINT_SELECTOR_ESTABLISHED` | must lift to joint K5 |
| joint holomorphic boundary-value principle | `OPEN_HIGH_POWER` | may encode infinite effective constraints |
| multi-decomposition composition/coherence | `OPEN_HIGH_POWER` | functional equations may reduce function space |
| cylindrical/refinement naturality | `OPEN_HIGH_POWER` | must distinguish unique natural section from scheme family |
| RG fixed-point condition | `OPEN` | uniqueness and scheme dependence both unresolved |
| universal boundary/source naturality | `OPEN_HIGH_POWER` | requires true-source functional class, not fitted probes |

## 8. First post-CD001 gates

Run three independent lanes without allowing one lane's outcome to alter another lane's preregistered criterion:

- `CD002-A`: composition/coherence toy theorem — determine when associativity across two refinement paths forces a tangential multiplier to be constant or a fixed character.
- `CD002-B`: joint analyticity feasibility — formulate a multi-variable edge-of-the-wedge / boundary-value uniqueness criterion whose input data are fixed independently of the K5 extension.
- `CD002-C`: RG natural-section theorem — characterize whether a semigroup-compatible selector can still carry arbitrary scheme functions.

A lane may end in a no-go theorem, a source-definition blocker, or a positive candidate. No lane is allowed to fit its principle after observing the preferred K5 extension.
