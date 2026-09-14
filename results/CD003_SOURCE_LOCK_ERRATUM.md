# CD003 source-lock erratum and dependency reconciliation

Date: 2026-09-14.
Disposition: mandatory source correction; not a new selector gate and not a change of the frozen mathematical hypothesis.

## Why this erratum is controlling

CD003 was preregistered against CDSR recovery commit `1f6a30f813ff712d2935c66b712d3399bf229a03` and upstream snapshot `9b2f9e5f31e294470c630ebff196f67a2de5ad18`. After its mathematical result and recovery update were committed, the final upstream-head check found `920144abf49cf4a5a50a8ad016c37fd83fa400f7`. That snapshot contains a material source-lock correction, not merely a new title or green CI status.

The prior CDSR claim of a proven infinite-dimensional SOURCE-COMPATIBLE tangential W is withdrawn. The old linearly independent family is a correct mathematical construction, but its physical admissibility premise omitted an exact source symmetry. Current recovery, not the pre-correction records, must govern subsequent research.

## Exact new authority

Upstream repository: `pppuu7-cmd/Mechanism-Synthesis-QG-Reconstruction`.

| Object | Exact path | Commit | Blob |
|---|---|---|---|
| source-lock re-review | `results/ITER077Q_ADVERSARIAL_RIGHT_SU2_SOURCE_LOCK_REVIEW.md` | `c0ae0ef208a3eccef4ece7960cdf5337e7d5fa2e` | `9c682046d7e2e386c0e29c0d5c822d66f3f91b23` |
| corrected jet result | `results/ITER081R_SM_RIGHT_SU2_S5_INVARIANT_JET_CLASSIFICATION_RESULT.md` | `5fe42e766aab2660b36c654502a029930db28890` | `bdc216e18ba5b4e61834383adab28036ea69c175` |
| repaired consequences | `results/ITER081S_CRITIC_REPAIRED_SELECTOR_CONSEQUENCES.md` | `8c2fc23084e89c39f624853ac0d445e3103850d1` | `0ece8b5d52c3140936806f6493ae10062b3b133b` |
| current authority snapshot | `status/CURRENT.md` | `920144abf49cf4a5a50a8ad016c37fd83fa400f7` | `9167d5b1427744c7b2081a66a73ba4bed6a098f8` |

The Iter081R source result records preregistration `18945b681978cf22a8253a6489034e68a1cae372`, production head `22f87a8cb1e5a87285066ac658e7823b223a3bc9`, terminal run `34882711232`, artifact `10363029817`, and artifact ZIP SHA256 `260017c1b2ac7186f8f2d5e10a499f40293315fec3d26ad174f3ba67726bf8a8`. These are imported upstream records, not CDSR reruns.

## Source reason for the correction

The already-pinned BCG Toller formula (arXiv:2604.24945v1, Eq. 13) has exact bi-SU(2) covariance in the projected spin blocks. The causal vertex's magnetic indices are contracted with SU(2)-invariant boundary intertwiners. Consequently the fully contracted integrand has independent node-wise compact right gauge transformations, not just the common-left Lorentz covariance checked in historical Iter077Q.

After root fixing, the action `g_a -> g_a u_a` for a=2,...,5 is transitive on `N=SU(2)^4`: choose `u_a=g_a^{-1}`. A smooth scalar tangential coefficient compatible with that action is constant along the orbit. This is an existing source constraint restored, not a newly selected physical axiom.

The historical Q has `Q(t)=12+8 cos(t)` on gauge-equivalent compact configurations, while at the identity it is 20. Therefore the nonconstant factors Q^n do not meet this source lock. The invariant compact boundary functional cannot compensate them. Failure of the general Lorentz representation law for Toller matrices does not negate their exact compact covariance.

## Corrected admissible target

Use `E_corr = Ext_{B_corr}(t0)` with B_corr including the omitted node-wise compact covariance. The historical W must not be asserted to be a subspace of its ambiguity A_corr.

Iter081R establishes a scalar invariant normal-jet subspace J_inv with

`dim J_inv = 28`,

and normal fiber

`V = spin1_SO(3) tensor Std5_S5`, dimension 12.

For orders k=0,...,8 the invariant-symbol counts are

`dim Sym^k(V)^(SO(3) x S5) = (1,0,1,0,3,0,7,0,16)`.

The sum is 28. This is a demonstrated subspace/lower bound, NOT the exact dimension of all physical extensions. Other boundary-covariant or representation-valued sectors have not been fully classified. Scalar order-zero tangential shape freedom is removed by the exact gauge action; a nonzero scalar supported coefficient and higher invariant jets remain.

## What survives and what is withdrawn

| Record | Mathematical statement | Physical applicability now |
|---|---|---|
| Iter077Q | independence of the artificial Q^n family remains valid | SOURCE-COMPATIBLE qualifier INVALID_SOURCE_LOCK |
| CD001 | finite-rank theorem under an infinite-dimensional premise remains valid | universal finite-list K5 exclusion is NOT established without another valid infinite-dimensional physical subspace |
| CD002-A | normalized multiplicativity on SU(2)^4 still implies f=1 | remains conditional; the formerly presumed arbitrary physical scalar function on N is not available after the source quotient |
| CD003 T4 | structural reassociation is non-selective on its common domain, irrespective of dimension | valid conditional application to E_corr intersect D; no physical W corollary |
| CD003 T5 | regular-context test-jet duality and annihilator identity remain valid | restrict admissible variations to corrected source-covariant sectors; physical context image still missing |
| Iter080A/J and causal sums | qualitative non-selection is repaired by Iter081R/S | old infinite-W justifications must not be used |
| Iter080B | causal E3/E4/E6 source bridge remains blocked | unaffected |
| repaired Iter080E | narrow absence of an explicit correlated joint extension prescription remains useful | full-W target language obsolete; no universal selector census for J_inv inferred |
| Iter080H | old candidate census depended on predicates against W | a corrected, prospectively frozen jet-target census is a different legitimate future question |

For a complex-linear family `L:J_inv -> C^m`, Iter081S gives `dim ker L >= 28-m`. Only m<28 is excluded by this bound. At m>=28 injectivity on J_inv is algebraically possible, not established physically. Neither 28 arbitrary conditions nor rank on J_inv alone selects the complete physical extension space.

## CD003 disposition

The original mathematical gate and its 12 exact controls are unchanged. The fixed-pairing countermodel does not use Iter077Q. The regular-context theorem applies to any explicitly admissible finite-normal-order subspace. There is no post-hoc modification of H_struct and no new substantive gate has been run.

The original aggregate classification remains scoped to structural gluing and missing physical transport:

`CD003_STRUCTURAL_GLUING_COHERENCE_IS_SELECTOR_BLIND_PHYSICAL_EXTENSION_TRANSPORT_UNESTABLISHED_SCOPED`.

Its current interpretation is qualified by this erratum:

`MATHEMATICS_VALID / ITER077Q_PHYSICAL_APPLICATION_WITHDRAWN / PHYSICAL_TRANSPORT_OPEN`.

The physical source bridge is still BLOCKED. This does not erase the mathematical results, but the earlier explanation in terms of an established infinite physical W must not be retained. The pre-correction result and derivation are preserved in Git history and archived with explicit warnings in the current tree.

## No-smuggling and next admissible work

A finite coefficient target can also smuggle a preferred answer: 28 freely chosen target values may encode the very scalar jet choice being reconstructed. Thus independent source derivation is still essential, even though infinite functional power is no longer known to be necessary.

The next target is `RIGHT_SU2_COVARIANT_INVARIANT_JET_SELECTOR_AND_TRANSPORT`: identify source-derived coefficient constraints or an extension-sensitive gluing/domain rule acting on J_inv and any additional sectors. A corrected candidate-axiom census may be admissible because its old W-based predicates were invalid; it must be newly preregistered against the actual jet target. Do not manufacture conditions, assume exact total dimension28, or compute a physical cohomology without its domain/module/action.

All unique-extension, new-physics, regulator, RG and CRQN reintegration claim locks remain false. No physical source-compatible infinite tangential subspace is now claimed. The historical preparation readiness score is not scientific validation of its source premises.
