# CD002-A — Multiplicative Composition/Coherence Power Result

**Date:** 2026-09-14  
**Status:** `PASS_EXACT_CONDITIONAL_SCOPED`

## Prospective authority

- CD001 result: `d5e296eff8cf76a97b32ac623ba7ffd59935350e`.
- CD002-A preregistration: `473bf95e258cf2ac0e43cb9452fb04f39e9f88cc`.

The theorem below is derived after the frozen gate. No physical source-authority claim is added.

## Frozen theorem

Let

```text
N = SU(2)^4
```

and let `f:N -> C` be smooth with

```text
f(gh)=f(g)f(h),
f(e)=1.
```

Then

```text
f(g)=1
```

for every `g in N`.

## Exact proof I — perfect-group argument

For every `g`,

```text
1 = f(e) = f(g g^{-1}) = f(g) f(g^{-1}),
```

so `f(g)` is nonzero. Thus `f` is a group homomorphism

```text
f : SU(2)^4 -> C^*.
```

The target `C^*` is abelian, so every homomorphism to it kills the commutator subgroup. But `SU(2)` is perfect, and a finite direct product of perfect groups is perfect. Therefore

```text
[SU(2)^4,SU(2)^4] = SU(2)^4.
```

Hence the homomorphism kills all of `SU(2)^4`, i.e. `f(g)=1` identically.

Smoothness is stronger than necessary for this argument; multiplicativity and normalization already suffice once the group-homomorphism statement is meaningful.

## Exact proof II — Lie-algebra cross-check

Differentiate `f` at the identity. Because the target is abelian, the differential is a Lie-algebra homomorphism

```text
df_e : su(2)^4 -> C
```

and therefore annihilates all brackets. Since

```text
su(2)^4 = [su(2)^4,su(2)^4],
```

we get `df_e=0`. A smooth homomorphism from the connected group `SU(2)^4` with zero differential has discrete image; connectedness forces the image to be the identity component point `{1}`.

This independently reproduces `f=1`.

## Upstream-witness control

The Iter077Q invariant

```text
Q(g) = sum_(a<b) tr_(1/2)(g_b^{-1} g_a)
```

is nonconstant. Therefore `Q^n` for `n>0` cannot satisfy the frozen normalized multiplicative law, because the theorem shows every such solution must be constant `1`.

For `n=0`, `Q^0=1` is the unique normalized multiplicative member of that witness family.

This is a control/consequence, not the proof of the theorem.

## Scientific meaning

CD001 showed that finitely many scalar linear constraints cannot uniquely remove the Iter077Q infinite-dimensional tangential ambiguity. CD002-A now shows that a **single functional coherence law can, in principle, have infinite-dimensional selector power**: normalized multiplicativity on the compact semisimple collision group collapses the whole smooth coefficient function to one constant function.

This is the first positive structural result in CDSR. It demonstrates that the selector search need not consist of infinitely many separately tuned moments; a compact, independently motivated functional law can be powerful enough.

## What remains unfixed

The result does **not** yet select the physical K5 extension.

1. The actual causal many-vertex composition has not been shown to act on the collision data by componentwise multiplication in `SU(2)^4`.
2. Bare gluing is already known upstream to contain independent pairing/weight normalization freedom, so the physical derivation of the coherence law cannot be assumed.
3. The theorem collapses the **shape** of the smooth tangential multiplier to a constant. An overall scalar coefficient multiplying a supported term can remain unless a separately justified normalization/coherence equation fixes it.
4. The higher normal-derivative ambiguity sectors are untouched.
5. Cocycles, projective laws, affine laws, weighted composition and geometry-dependent transport are outside this frozen gate and may possess nontrivial solutions.

## Classification

`CD002A_SU2_4_MULTIPLICATIVE_COHERENCE_COLLAPSES_SMOOTH_TANGENTIAL_MULTIPLIER_TO_CONSTANT_EXACT_CONDITIONAL_SCOPED`

Scientific verdict: **PASS_EXACT_CONDITIONAL_SCOPED**.

## New research direction forced by the result

The most informative next question is no longer merely “can composition constrain the ambiguity?” — the answer is yes, conditionally. The next hard gate is:

> Does a source-faithful causal composition/refinement construction imply a multiplicative, cocyclic or otherwise coherent transport law on supported K5 extension data, and if so, which cohomology class is actually allowed?

This suggests splitting the next composition front into:

- `CD003-A`: derive the weakest source-faithful coefficient transport equation from a two-/three-vertex causal complex;
- `CD003-B`: classify scalar cocycle/projective deformations of the multiplicative law, because these are the nearest mathematical escape from the trivial-character theorem;
- `CD003-C`: extend coherence from the order-zero tangential coefficient to the finite normal-jet tower allowed by the upstream scaling-degree theorem.

No CRQN v0.3 or new-physics promotion is allowed at this stage.
