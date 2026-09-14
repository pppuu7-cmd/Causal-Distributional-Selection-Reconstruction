# Causal Distributional Selection Reconstruction (CDSR)

Independent research on physically justified selection of distributional extensions of causal spin-foam amplitudes. CDSR does not rewrite CRQN v0.2 or select counterterms by convenience.

## Current science

**CD003 is terminal:** `PASS_MATHEMATICS_BLOCKED_PHYSICAL_BRIDGE`.
Result commit: `f49040aac1a7be0dcd9ccf30484620c5cc028003`.

The new theorem excludes same-graph structural reassociation as a standalone selector on a common well-defined gluing domain. A separate exact formula describes how regular contexts see supported normal jets. No physical causal K5 selector or unique extension was obtained.

Start with [current state](recovery/CURRENT_FRONT.md), [CD003 result](results/CD003_STRUCTURAL_GLUING_RESULT.md), [derivation](derivations/CD003_STRUCTURAL_COHERENCE_AND_JET_DUALITY.md), and [source versions/equation anchors](sources/CD003_SOURCE_MANIFEST.md). The next question is in [PRO_FRONTIER](recovery/PRO_FRONTIER.md).

## Baseline

The local extension problem is `E = Ext_B(t0) = T_* + A_B` in its established affine scope. Upstream Iter077Q proves only a lower-bound inclusion: `span_C{Q^n F delta_N:n>=0} subset A_B`, on N=SU(2)^4. Iter077L gives the local codim12/sd20 normal-order ceiling8; it does not classify all physically admissible jets or all collision strata.

CD001 excludes fixed finite affine-linear scalar lists as unique selectors. CD002-A proves normalized multiplicativity forces a smooth multiplier f=1, but its physical hypothesis is not derived. Their original preregistrations/results are unchanged.

CD003 distinguishes canonical reassociation from genuine equations between different complexes or for unknown multiplication tensors. Those stronger equations, as well as source-derived domain restrictions and joint analyticity, remain open possibilities.

## Reproduction and limits

```sh
python -m pip install -r analysis/requirements-cd003.txt
python analysis/cd003_exact_controls.py --output /tmp/cd003-controls.json
```

Twelve exact controls were executed locally, not on GitHub Actions. The proof, not the finite controls, establishes the general mathematical result. Mathematical probes are not automatically physical boundary states; no full physical quotient or jet transport is defined.

Read [claim locks](authority/CLAIM_LOCKS.md), [theorem registry](authority/THEOREM_AND_OBSTRUCTION_REGISTRY.md), [source-authority firewall](authority/SOURCE_DERIVATION_REQUIRED.md), and [no-smuggling audit](protocol/NO_SMUGGLING_TEST.md). Current machine state is [state.json](recovery/state.json); [research history](research_log/CDSR_LEDGER.md) is append-only.

No unique K5 extension, physical selector, CRQN v0.3, regulator independence, causal multivertex closure, RG closure, new physics or complete quantum gravity is claimed. The prior 10/10 score is historical preparation readiness, not a scientific success probability.
