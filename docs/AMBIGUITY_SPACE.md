# Ambiguity Space — Neutral Notation

This document records only structure already supported by upstream authority. It is intentionally weaker than a decomposition theorem.

## Base extension problem

Let `t0` be the frozen source-ordered K5 distribution away from the common-collision set and `B` the frozen admissibility conditions. Define

```text
Ext_B(t0) = {T in D'(X) : T|_(X\N)=t0 and B[T]=0}.
```

If nonempty, choose one reference extension `T_*` and define the ambiguity vector space by differences of admissible extensions:

```text
A_B = {T-T_* : T in Ext_B(t0)}.
```

Then, as affine notation,

```text
Ext_B(t0)=T_*+A_B.
```

No preferred `T_*` is asserted by this notation.

## Proven tangential sector

Upstream Iter077Q proves only an inclusion. Introduce `A_tan` as a label for the smooth tangential supported sector known to contain the Iter077Q witness. The safe statements are

```text
A_B ⊇ A_tan
```

and

```text
A_tan ⊇ W,
W := span_C{Q(y)^n F(y) delta_N(x) : n>=0}.
```

`W` is countably infinite-dimensional because the displayed family is linearly independent.

Do **not** infer any of the following without a new theorem:

```text
A_B = A_tan
A_tan = W
A_B = W ⊕ A_normal
```

or any other exhaustive/direct-sum decomposition.

## Scalar coefficient versus tangential shape

Two notions must be kept distinct:

- **tangential shape freedom:** variation of the smooth function multiplying a supported distribution along `N`; Iter077Q proves an infinite-dimensional witness for this;
- **overall supported scalar coefficient:** even if a conditional law reduces a multiplier shape to a constant function, a coefficient multiplying the supported term may remain unless a separate normalization/coherence rule fixes it.

CD002-A acts only on a prospectively assumed normalized multiplicative tangential multiplier. It does not prove that the physical ambiguity is exhausted by such multipliers and it does not provide a physical scalar normalization law.

## Normal-derivative / normal-jet sectors

Upstream Iter077L establishes in the frozen scaling-degree scope:

- `N=SU(2)^4`;
- real codimension `12`;
- transverse scaling degree `20`;
- extension differences may involve normal derivatives through order `8`, with coefficient data along `N` subject to further conditions.

It is therefore safe to say that the current extension problem includes a **normal-jet frontier through order 8**. It is not safe to declare a specific direct-sum basis or to assert that every formal normal derivative is independently physically admissible.

## Potentially other supported sectors

Current authority does not provide an exhaustive classification of all source-compatible supported differences. Therefore CDSR reserves the label

```text
A_other := potentially remaining supported sectors not classified by current theorems
```

only as prose shorthand. `A_other` is **not** a defined vector-space summand and must not appear in algebraic decompositions unless a later gate defines it.

## What CD002-A actually controls

Conditional hypothesis:

```text
f:SU(2)^4 -> C,
f(gh)=f(g)f(h),
f(e)=1.
```

Exact conditional conclusion:

```text
f=1.
```

Thus CD002-A demonstrates that such a functional law has enough mathematical power to eliminate nonconstant smooth tangential **shape** freedom in its domain.

It does not establish:

- that actual causal composition induces that law;
- that all of `A_tan` is parameterized by one such `f`;
- that the overall supported scalar is fixed;
- that the normal-jet tower is fixed;
- that two remaining extensions are physically inequivalent;
- unique K5 extension.

## Minimum burden for a future uniqueness claim

A future uniqueness theorem must state explicitly:

1. which sector(s) of `A_B` the selector acts on;
2. which sectors are proved absent, quotient-null, or fixed;
3. how the overall scalar is handled;
4. how all allowed normal jets are handled;
5. the physical equivalence relation used in “unique”;
6. the source authority or explicit new-principle status of every selector datum.
