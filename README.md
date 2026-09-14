# Causal Distributional Selection Reconstruction (CDSR)

## Current source-corrected result

**CD003: mathematical PASS, physical extension transport still BLOCKED.**
Read the [mandatory source erratum](results/CD003_SOURCE_LOCK_ERRATUM.md), then the [corrected result](results/CD003_STRUCTURAL_GLUING_RESULT.md), [proof](derivations/CD003_STRUCTURAL_COHERENCE_AND_JET_DUALITY.md), and [current front](recovery/CURRENT_FRONT.md).

A final upstream audit withdrew historical Iter077Q's physical infinite-dimensional tangential W: an exact node-wise right SU(2) gauge condition had been omitted. The independent Q^n family is mathematical, not source-compatible. Scalar tangential dependence along N is fixed by that existing gauge symmetry.

The corrected upstream result demonstrates a **28-dimensional scalar invariant normal-jet subspace**, not the full physical extension space. CD001's formal infinite-dimensional theorem remains valid but its universal finite-list K5 application is withdrawn. At least28 independent conditions would be needed to remove this subspace by scalar linear equations; even28 are not automatically physically justified or sufficient for all sectors.

CD003's dimension-independent theorems survive: same-graph structural reassociation imposes no restriction beyond a common legitimate gluing domain; regular contexts act through normal test jets and leave their annihilator invisible. No actual physical gluing domain, full context image or unique extension was derived.

## Next research entry

[PRO_FRONTIER](recovery/PRO_FRONTIER.md): `RIGHT_SU2_COVARIANT_INVARIANT_JET_SELECTOR_AND_TRANSPORT`.
Find source-derived coefficient relations or extension-sensitive gluing/domain conditions on corrected invariant jets, with the full physical quotient and additional sectors explicit. A corrected prospectively registered candidate-axiom census is eligible; finite physical conditions are not rejected in advance.

Current authority: [correction manifest](sources/CD003_SOURCE_CORRECTION_MANIFEST.json), [theorem registry](authority/THEOREM_AND_OBSTRUCTION_REGISTRY.md), [claim locks](authority/CLAIM_LOCKS.md), [machine state](recovery/state.json), and [append-only ledger](research_log/CDSR_LEDGER.md). Old CD001/CD002-A proofs and pre-correction CD003 snapshots remain preserved and qualified, not silently rewritten.

## Reproduction

```sh
python -m pip install -r analysis/requirements-cd003.txt
python analysis/cd003_exact_controls.py --output /tmp/cd003-controls.json
```

Twelve exact controls were executed locally and repeated with identical output. They do not depend on the invalid physical W premise. No GitHub Actions execution or independent external review is claimed for CDSR. Upstream's28-dimensional invariant count was imported, not rerun here.

No unique K5 extension, new physical principle, CRQN v0.3, regulator independence, causal multivertex closure, RG closure or complete quantum gravity is claimed. The previous10/10 score is historical preparation readiness, not scientific validation of its source assumptions.
