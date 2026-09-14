# CD003 source authority and composition map

Prospective gate: `c3f898a975b56f3f707c00d3e01cf5388934d9f7`.
CDSR recovery baseline: `1f6a30f813ff712d2935c66b712d3399bf229a03`.
Upstream snapshot: `pppuu7-cmd/Mechanism-Synthesis-QG-Reconstruction` at `9b2f9e5f31e294470c630ebff196f67a2de5ad18`.

The physical source corpus is the four versions below. None is claimed to be newly discovered primary authority. Version metadata was checked before the gate; equation-level examination followed its prospective freeze. Versioned HTML was inspected; no raw-source-byte SHA256 or published-version delta is claimed. Existing upstream production artifacts were not rerun in CDSR.

## Primary records

### P1 - Bianchi, Chen, Gamonal: causal vertex

[Causal spinfoam vertex for 4d Lorentzian quantum gravity, arXiv:2601.23162v1](https://arxiv.org/html/2601.23162v1), version date 2026-01-30; [version record](https://arxiv.org/abs/2601.23162v1).

Equation anchors: (3), one-wedge spectral Toller prescription; (4), fixed-causal ten-wedge vertex with four root-gauge-fixed SL(2,C) integrations and relative variables g_b^{-1}g_a. The boundary data are the ten spins and five intertwiners. Section V(ii) leaves causal-vertex finiteness to investigation; V(vi) identifies the single vertex as a building block for a future many-vertex construction. These are local/formal vertex data, not an explicit map inserting an arbitrary supported K5 extension into a completed causal state sum. An HTML date heading is not evidence of an additional arXiv version.

### P2 - Bianchi, Chen, Gamonal: Toller matrices

[Toller matrices and the Feynman i epsilon in spinfoams, arXiv:2604.24945v1](https://arxiv.org/html/2604.24945v1), version date 2026-04-27; [version record](https://arxiv.org/abs/2604.24945v1).

Equation anchors: (7)-(12), reduced-branch analytic/asymptotic/pole conditions and sum rule; (14), explicit failure of the Lorentz representation-composition identity for Toller matrices; (15), T+ + T- = D; Section III.1, one-wedge projector/uniqueness argument. No joint-K5 supported-extension transport equation is identified at these anchors. A product of functions on SL(2,C) must not be silently replaced by a representation law. The historical Iter080K new-authority claim is invalid; this is an already-audited source, not a repaired novelty claim.

### P3 - Beltran: generalized causal vertex

[Causal Structure for Generalized Spinfoams, arXiv:2603.22661v2](https://arxiv.org/html/2603.22661v2), version date 2026-08-03; [version record](https://arxiv.org/abs/2603.22661v2).

Equation anchors: (15), parent Lorentzian vertex; (25)-(27), orientation decomposition and generalized Toller local vertex; (36), eta-plus causal sum. Section 5.2 discusses replacing local vertices in a multivertex discretization as a semiclassically motivated proposal. Section 6 leaves generalized causal-vertex finiteness open. Arbitrary-2-complex causal orientations and a generalized vertex do not by themselves specify supported-extension insertion, collision pullback, a jet transport operator, or a physical quotient of extension choices.

### P4 - Kaminski, Kisielowski, Lewandowski: parent contraction calculus

[Spin-Foams for All Loop Quantum Gravity, arXiv:0909.0939v5](https://arxiv.org/html/0909.0939v5), version date 2011-09-23; [version record](https://arxiv.org/abs/0909.0939v5).

Equation anchors: Section II, compact-group spin networks and Haar boundary Hilbert structure; (38)-(40), vertex tensor contraction; (41)-(44), boundary factors and trace behavior under gluing/conjugation. Section IV specializes to Euclidean models. The explicit parent trace normalization is source data, but is not a Lorentzian causal measure or a law on the independent K5 tangential multiplier f. Cuts that create boundary factors are not automatically instances of CD003's fixed-map reassociation theorem after an arbitrary vertex replacement.

## Composition-data inventory for the physical target

| Required datum | Established entry | Remaining source requirement |
|---|---|---|
| local boundary data | P1 ten-spin/five-intertwiner vertex; U077Q true boundary-linear F | map I_v from local extensions to complete physical boundary functionals |
| two-/three-vertex object | parent graph/trace composition P4; causal orientations P3 | completed causal functional, not just a graph and a formal replacement |
| local variables | four SL(2,C) variables after root fixing for P1 | all shared/internal variables and sums for the proposed causal complex |
| measures and weights | source local Haar integration; parent normalization in its own scope | causal internal face/edge weights, convergence and normalization inheritance |
| orientation and order | fixed branches and source order; P3 causal sign compatibility | justified operations on extended distributions respecting these labels |
| gauge quotient | root fixing for a local vertex | full causal quotient/fixing normalization under composition |
| supported insertion | local supported ambiguity U077Q | a defined action on T_*+u, not a termwise product of contact distributions |
| refinement comparison | no such map is imported | source-fixed R between different complexes, including boundary embeddings |
| normal jets | U077L ceiling 8; CD003 supplies regular-context dual identity | physical kernel/pullback/pushforward and its test-jet image |
| physical equivalence | not defined sufficiently | source-defined probes/redefinitions and contextual closure |

The table does not assert nonexistence of all possible maps. Its OPEN entries identify precisely what has not been established in the pinned chain. CD003's mathematical regular kernels are test objects, not substitutions for these physical data.

## Upstream pins

All upstream paths in this section belong to `pppuu7-cmd/Mechanism-Synthesis-QG-Reconstruction`. Exact commit/path links and available blob hashes are also stored in the companion JSON.

| ID | Exact path | Commit pin | Blob where checked | Imported scope |
|---|---|---|---|---|
| U077L | `results/ITER077L_SM_TRANSVERSE_SCALING_DEGREE_EXTENSION_THEOREM_RESULT.md` | `9b2f9e5f31e294470c630ebff196f67a2de5ad18` (snapshot, not original result commit) | `e48d8a3e1899c5e064aaf0da33c48c7466bccdc5` | local codim12/sd20 extension theorem, normal-order ceiling8, not all jets physically allowed |
| U077Q | `results/ITER077Q_SM_INVARIANT_TANGENTIAL_AMBIGUITY_RESULT.md` | `5941b3a064d93f2898d9e9a48545826e950455f1` | `26aa90965ccfe495f55df2f4c190f7bbe09093f4` | countable independent supported witness W, not all of A_B |
| U079C | `results/ITER079C_SM_MINIMAL_TWO_VERTEX_COMPOSITION_UNIQUENESS_RESULT.md` | `0a502c439e3e1069d19b66bb7a8bd65928f537bf` | `197f4c7892e41b7c28a1ecfb0390fa39b013f67d` | old variable-pairing/weight obstruction, not CD003's fixed-map theorem |
| U080B | `results/ITER080B_SM_E3_E4_E6_JOINT_SOURCE_BRIDGE_RESULT.md` | `3a21afe528ca098fc7258388bc03ac125f26b5c8` | see exact commit | established causal E3/E4/E6 source bridge blocker |
| U080E | `results/ITER080E_SM_CONTROL_ONLY_SOURCE_PREDICATE_REPAIR_RESULT.md` | `bc5acbb8fd5b5ea93b267a382ef9a833ea2422c7` | see exact commit | repaired frozen-corpus joint-selector blocker, not universal absence |
| U080J | `results/ITER080J_SM_MICROLOCAL_WF_ONLY_SELECTOR_POWER_RESULT.md` | `e9d1867fc8a1026ed678aac0e3c768c654c39487` | see exact commit | WF-only non-selection, not all microlocal restrictions |
| U080K_REVIEW | `results/ITER080K_ADVERSARIAL_PROVENANCE_REVIEW.md` | `691436f7c8e14ee7efd77b1e85146136f73e8553` | see exact commit | INVALID_PROVENANCE for false new-source trigger |
| U081H | `results/ITER081H_CRITIC_BELTRAN_CAUSAL_SUM_L1_COROLLARY.md` | `56a7d831da5b7703fe55bc4c91d949960b60a8bd` | `d5c29586fa8dae93028547f18a9b15d6df20d370` | Critic exact eta-plus local non-L1 corollary, not full divergence |
| U081I | `results/ITER081I_CRITIC_BELTRAN_CAUSAL_SUM_EXTENSION_AMBIGUITY_COROLLARY.md` | `411719e26129fc7ab2a4b9ad9ccf5750c5843917` | `3e31db93204ed7982dfbcbf18b35217ec5537a86` | Critic exact persistence of W after eta-plus sum |
| U081K | `results/ITER081K_CRITIC_BOTH_CAUSAL_SIGNATURE_SECTORS_L1_COROLLARY.md` | `2793da94390a226217360bf6fbeb97ff4d8e3bde` | `2ee156aed61ef300e16519b7d4eccf661afbe20b` | both proper causal signatures retain local leading singularity and ambiguity |
| U081L | `results/ITER081L_CRITIC_NONCAUSAL_SECTORS_REQUIRED_FOR_EPRL_LEADING_POLE_CANCELLATION.md` | `b29aa4a6e49dff412b0eea43834ba72bd855c074` | `058e53b6e680e002dfd728c53e6bb8972e0a56ec` | unrestricted leading cancellation uses noncausal contributions; not a physical requirement to include them |

The U081H/I/K/L records are new to the CDSR recovery snapshot and are imported as scoped upstream Critic corollaries, not relabeled as newly executed CDSR production results. Iter081F still has no terminal boundedness atlas to import at the pinned snapshot. The source-order contact erratum remains controlling; CD003 does not perform contact-distribution multiplication.

## Source-level conclusion

No additional physical K5 extension-transport law has been established here. This is bounded by the explicit versions, objects and upstream authority above, not an assertion about all literature or every future consequence of these papers. The new CD003 science is the fixed-map structural non-selection theorem and the regular-context jet criterion, not another source-corpus census.
