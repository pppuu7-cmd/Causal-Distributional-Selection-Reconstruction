# Physical Equivalence Frontier

## Question that must be answered before a physical uniqueness claim

For

```text
T1, T2 in Ext_B(t0),
```

when should CDSR regard `T1` and `T2` as the same physical equivalence class?

CDSR currently has **no complete answer**. This document prevents mathematical uniqueness in a chosen representation from being silently promoted to physical uniqueness.

## Status vocabulary

- `DEFINED`: a precise equivalence relation relevant to the extension problem has already been established by authority.
- `UNDEFINED`: the candidate notion is only a label; no usable equivalence relation is currently defined.
- `REQUIRES_NEW_GATE`: enough structure exists to formulate a future question, but using it to quotient `Ext_B(t0)` requires a prospective derivation/test.

## Candidate equivalence notions

| Candidate | Status | What is established | What remains required |
|---|---|---|---|
| gauge-equivalent extensions | `REQUIRES_NEW_GATE` | common-left gauge covariance/fixing structures exist in upstream source scope | define the action on the full supported extension data and prove which extension differences are pure gauge after the relevant quotient/fixing |
| source-null differences | `UNDEFINED` | source ordering and admissibility conditions `B` are part of the extension problem | define a source-null subspace/ideal and prove nullity for all source observables relevant to the amplitude |
| boundary-null differences | `UNDEFINED` | upstream Iter077Q uses true boundary functionals and proves nonzero witnesses exist | define the complete admissible boundary probe class and prove which supported differences vanish against all such probes |
| observationally null for all admissible physical probes | `UNDEFINED` | no complete physical probe set is defined in CDSR | prospectively define the probe algebra/class and prove universal nullity, not nullity on a finite convenience sample |
| exact reparameterization/redefinition equivalence | `REQUIRES_NEW_GATE` | no specific redefinition group is imported | define allowed field/source/amplitude redefinitions and prove they preserve every physical structure used by the selector |

## Negative rules

The following are not enough to establish physical equivalence:

- two extensions agree away from `N` — that is already true by construction of the extension problem;
- a difference vanishes on one or finitely many boundary states;
- a difference can be absorbed by an arbitrarily chosen counterterm function;
- two choices are related by a redefinition whose admissibility has not been source-derived;
- a numerical observable happens to agree on a finite test set.

## Uniqueness lock

Until a quotient sufficient for the intended physical claim is defined, CDSR may state only mathematical results inside a frozen representation/sector. It may not set

```text
UNIQUE_K5_EXTENSION = true
```

or say that `Ext_B(t0)` has been reduced to one physical equivalence class.

A future gate may discover that no nontrivial quotient is needed, or that a nontrivial quotient removes residual ambiguity. Both outcomes are open.
