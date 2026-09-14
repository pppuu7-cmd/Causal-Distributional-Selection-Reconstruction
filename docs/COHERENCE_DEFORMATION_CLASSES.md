# Coherence Deformation Classes — Neutral Search Space

This document prepares notation for a future source-derived gate. It does **not** classify any deformation class, choose a coefficient group, choose regularity, or assert physical relevance.

## Reference control

CD002-A tested the conditional normalized multiplicative law

```text
f(gh)=f(g)f(h),
f(e)=1
```

on `SU(2)^4` and proved that, under that frozen law, `f=1`.

The law itself has not been derived from causal many-vertex physics.

## Nearest deformation families

The following are schematic search classes only. Their domains, codomains, coefficient objects, regularity classes, and equivalence relations are future-gate data.

### Projective / scalar multiplier form

```text
f(gh)=omega(g,h) f(g) f(h).
```

If an associative composition law and an invertible scalar coefficient object are later established, consistency may lead schematically to a condition of the form

```text
omega(g,h) omega(gh,k)
=
omega(h,k) omega(g,hk).
```

This is only a notation template. No claim is made that the physical `omega` is scalar, nonzero, smooth, continuous, normalized, or defined on all of `SU(2)^4 x SU(2)^4`.

### Weighted multiplicativity

Schematic possibility:

```text
f(g ⋆ h)=W(g,h; source data) f(g) f(h).
```

Here even the operation `⋆`, weight `W`, and its source dependence are undefined until an actual composition object is pinned. A freely chosen `W` is a no-smuggling risk, not a solution.

### Affine / cochain deformation

Schematic possibility:

```text
f(g ⋆ h)=A_{g,h}(f(g),f(h)) + b(g,h)
```

or a linear-plus-inhomogeneous transport on a function/jet space. No algebraic structure is assumed by this notation.

### Functorial / naturality formulation

Instead of a scalar equation, the physical object may define maps between extension spaces,

```text
Phi_C : Ext_B(boundary data) -> Ext_B(composed/refined data),
```

with coherence imposed by equality/compatibility of maps associated with different decompositions. Whether such maps exist and how they act on supported distributions are open source questions.

### Jet-valued coherence

A future source object may act on a finite collection of normal-jet coefficient data rather than on a single scalar function. Schematic notation:

```text
J=(f_alpha)_{|alpha|<=8},
J_{composed}=C(J_1,J_2; source data).
```

No representation, dimension count, or independence statement is implied.

## Parameters that must be frozen before classification

A future terminal cocycle/projective/coherence gate must prospectively define at least:

- the actual source-derived composition/refinement domain;
- the exact extension-space sector acted upon;
- the coefficient group/vector space/category, if any;
- normalization conditions, if any;
- continuity/smoothness/measurability class, if required;
- associativity or higher-coherence statement actually supplied by the physical object;
- gauge and causal-label action;
- equivalence relation among deformations;
- effect on scalar normalization;
- effect on all relevant normal jets;
- no-smuggling audit for `omega`, `W`, kernels, maps, and boundary data.

## Explicitly unresolved

The following are all `OPEN`:

```text
H^2 or any cohomology group relevant to the physical problem
triviality/nontriviality of projective multipliers
physical coefficient group
physical domain of the cocycle
regularity class
whether composition is associative in the needed sense
whether the source produces scalar rather than operator/kernel-valued transport
whether such deformations preserve or remove K5 ambiguity
```

CDSR must not compute a convenient cohomology and then retrofit the physical domain. The source/composition object determines the mathematical problem, not the reverse.
