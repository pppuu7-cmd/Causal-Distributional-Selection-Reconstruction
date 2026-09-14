# CD002-A — Multiplicative Composition/Coherence Power Gate

Status: **prospectively frozen before derivation/result**  
Date: 2026-09-14

## Question

Can a composition/coherence law have enough mathematical power to collapse the infinite-dimensional smooth tangential K5 ambiguity, without yet claiming that the law is physically source-derived?

## Frozen toy domain

Use the compact common-collision manifold from the upstream K5 theorem,

```text
N = SU(2)^4,
```

with componentwise group multiplication.

Let `f:N -> C` be a smooth tangential multiplier of a supported ambiguity term of schematic form

```text
u_f = f(y) F(y) delta_N(x).
```

This gate acts only on the coefficient `f`. It does not modify `F`, the normal-jet sectors, or the off-collision distribution.

## Frozen candidate coherence law

Test the conditional law

```text
f(gh) = f(g) f(h)      for all g,h in N,
f(e) = 1.
```

No additive/affine correction, cocycle, geometry-dependent weight, fitted kernel or post-result modification is allowed in this iteration.

## Frozen theorem target

Prove or disprove:

> Every smooth `f:SU(2)^4 -> C` obeying the frozen multiplicative law and normalization is identically `1`.

If true, classify:

`CD002A_SU2_4_MULTIPLICATIVE_COHERENCE_COLLAPSES_SMOOTH_TANGENTIAL_MULTIPLIER_TO_CONSTANT_EXACT_CONDITIONAL_SCOPED`

If a nonconstant smooth solution exists, classify:

`CD002A_NONTRIVIAL_SMOOTH_MULTIPLICATIVE_TANGENTIAL_CHARACTER_EXISTS_EXACT_SCOPED`

If the group-theoretic assumptions fail to decide the frozen complex-valued problem, classify `INSUFFICIENT`.

## Proof route frozen in advance

The allowed proof route is group-theoretic:

1. use `f(e)=1` and multiplicativity to show `f(g) != 0` for every `g`, hence `f:N -> C^*`;
2. recognize `f` as a smooth one-dimensional character/homomorphism;
3. use the trivial abelianization/perfectness of `SU(2)^4` to decide whether such a character can be nontrivial.

An independent Lie-algebra cross-check is permitted: the differential at the identity is a Lie-algebra homomorphism from `su(2)^4` to the abelian Lie algebra `C`, hence must vanish because `su(2)^4=[su(2)^4,su(2)^4]`; connectedness then controls the global map.

## Mandatory controls

- Explicitly distinguish **selector power** from **source authority**.
- Explicitly test the upstream witness functions `Q^n`: the conclusion may state that they fail the multiplicative law unless `n=0`, but this must not be used as the proof of the theorem.
- Do not claim the scalar coefficient multiplying `F delta_N` is fixed unless a separate normalization acts on that scalar.
- Do not claim anything about the additional normal-derivative ambiguity sectors.
- Do not claim physical composition actually induces componentwise multiplication on `N`.

## Interpretation ceiling

A PASS would establish only a conditional mathematical fact:

```text
IF physical composition induces this exact normalized multiplicative law on the tangential multiplier,
THEN the smooth tangential functional freedom collapses to f=1.
```

It would not establish the antecedent. The next physics gate would be to derive (or falsify) such a law from a source-faithful many-vertex causal object without importing arbitrary gluing data.
