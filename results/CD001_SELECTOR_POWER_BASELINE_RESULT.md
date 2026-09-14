# CD001 — Selector Power Baseline Result

**Date:** 2026-09-14  
**Status:** `PASS_EXACT_SCOPED`

## Prospective authority

- Project charter committed before this result: `087d8b63c387efe727aff986b102c2ad0741f05b`.
- Prospective preregistration committed before this result: `124374857f3bfaedc9dea8aefc88801eb2a9976c`.
- Upstream K5 ambiguity authority: MSQGR/CRQN Iter077Q, result blob SHA `26aa90965ccfe495f55df2f4c190f7bbe09093f4`.

## Frozen theorem

Let the admissible extension space be an affine space

```text
E = T_* + A
```

and suppose `A` contains an infinite-dimensional vector subspace `V`.

Let a candidate selector impose a fixed finite family of affine-linear scalar conditions

```text
L_i(T-T_*) = c_i,   i=1,...,m,
```

where each `L_i` is linear on the ambiguity space and `m<infinity`.

If the selected set is nonempty, it cannot contain exactly one extension.

## Exact proof

Restrict the finite-rank linear map

```text
L = (L_1,...,L_m): V -> K^m.
```

If `ker L = {0}`, then `V` would inject linearly into the finite-dimensional space `K^m`, contradicting the infinite dimensionality of `V`. Therefore choose `0 != v in ker L`.

If `T` satisfies all selector equations, then for every scalar `lambda`,

```text
L_i((T + lambda v)-T_*)
 = L_i(T-T_*) + lambda L_i(v)
 = c_i.
```

Because `v` is an admissible ambiguity direction, `T+lambda v` remains in `E`. Hence the same finite selector admits a nontrivial affine family and does not select uniquely.

In fact `ker(L|_V)` is infinite-dimensional because a finite-codimension subspace of an infinite-dimensional vector space remains infinite-dimensional.

## K5 corollary

Upstream Iter077Q supplies the explicit linearly independent family

```text
{ Q(y)^n F(y) delta_N(x) : n=0,1,2,... }
```

inside the already source-compatible K5 ambiguity space. Therefore any proposed K5 selector whose entire action on this family reduces to a fixed finite list of linear scalar moments, normalizations, projections or pairings **cannot** select a unique extension.

This converts a methodological concern into an exact scoped obstruction: a successful selector must have greater functional power — for example an infinite family of conditions, a functional equation/coherence law, analyticity with uniqueness strength, a nonlinear naturality condition, or another mechanism that genuinely restricts the function space.

## No-smuggling consequence

Merely replacing the old scalar counterterm by an arbitrary smooth function, kernel, subtraction map or boundary functional does not solve the problem. If that new free datum can encode the same ambiguity directions, the choice has only been moved from the extension to the selector input.

The preceding sentence is a workflow diagnostic, not a general equivalence theorem. Future proposals will be audited case by case.

## Classification

`CD001_FINITE_LINEAR_SCALAR_SELECTOR_CANNOT_UNIQUELY_SELECT_INFINITE_DIMENSIONAL_K5_AMBIGUITY_EXACT_SCOPED`

Scientific verdict: **PASS_EXACT_SCOPED**.

## Interpretation ceiling

This result does not rule out:

- nonlinear constraints;
- infinitely many linear constraints;
- joint analyticity/boundary-value uniqueness;
- composition laws that become functional equations;
- cylindrical/refinement consistency;
- RG naturality or fixed-point principles;
- positivity/spectral principles;
- a source-derived law that first reduces the admissible ambiguity space.

It also does not establish a unique K5 extension, CRQN v0.3, regulator independence, RG closure, or new physics.

## Next admissible gate

Test a genuinely high-power coherence condition rather than another finite list of moments. `CD002-A` will ask whether a prospectively frozen multiplicative composition law on the compact collision manifold can collapse the smooth tangential coefficient freedom, while keeping the separate source-authority question explicit.
