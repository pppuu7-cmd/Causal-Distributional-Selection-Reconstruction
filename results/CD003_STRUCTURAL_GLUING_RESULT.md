# CD003 structural gluing and extension selection

Date: 2026-09-14.

## Terminal decision

- Mathematical result: `PASS_EXACT_SCOPED`.
- Physical source bridge: `BLOCKED_SOURCE_BRIDGE`.
- Aggregate status: `PASS_MATHEMATICS_BLOCKED_PHYSICAL_BRIDGE`.
- Classification: `CD003_STRUCTURAL_GLUING_COHERENCE_IS_SELECTOR_BLIND_PHYSICAL_EXTENSION_TRANSPORT_UNESTABLISHED_SCOPED`.

No source-derived physical selector was obtained. The new result is a scoped mathematical exclusion of same-graph structural coherence as a standalone selector, together with an exact regular-context normal-jet sensitivity criterion. It is not a repetition of CD001 or a claim that every composition/refinement law fails.

## Prospective authority and artifacts

- Recovery baseline: `1f6a30f813ff712d2935c66b712d3399bf229a03`.
- Preregistration: `prereg/CD003_STRUCTURAL_GLUING_VS_EXTENSION_SELECTION.md`, commit `c3f898a975b56f3f707c00d3e01cf5388934d9f7`.
- Source equation/version record: `sources/CD003_SOURCE_MANIFEST.md`, commit `3023d95ebb97ef5360554979f1af8aed2c0a67c1`; companion `.json` supplies machine pins.
- Derivation: `derivations/CD003_STRUCTURAL_COHERENCE_AND_JET_DUALITY.md`, commit `12d2c3afd9f426aebc994f6761def4fccff4c1d5`.
- Executed code and raw control output: commit `e4034bffb90964232d68025468a8dbffc4dbc36d`.
- Self-review: `results/CD003_ADVERSARIAL_REVIEW.md`; no independent external referee or second agent is claimed.

The controlling science is the analytic argument, not successful execution or keyword validation of source claims.

## The exact new mathematical facts

### T4 - structural reassociation is non-selective

For fixed contractions of the same decorated graph,

`Z_Gamma(v_1,...,v_n) = C_Gamma(tensor_product_v v_v)`.

Canonical reparenthesization and legal contraction-order identities hold for every generator assignment in the common well-defined domain D. Therefore, for an extension family E, structural coherence selects exactly `E intersect D`.

If E is contained in D, no ambiguity direction is removed; in particular the proven W survives. This statement applies to finite tensor contractions and to the explicitly defined regular distributional context domain. It does NOT prove all physical K5 extensions lie in a physical gluing domain. A source-derived restriction of D can have genuine selection power.

Unlike CD001 this is not a finite-linear-rank obstruction. An arbitrarily large or infinite family of nonlinear-looking graph identities may still be identically satisfied. Unlike Iter079C all pairings, measures/weights and normalization data remain fixed.

### Exact countermodel with fixed gluing data

With `B=diag(2,3)`, `X star Y=X B Y` and unit `B^{-1}`, take

`A_lambda = [[1,lambda],[0,1]]`.

Both parenthesizations of its three-vertex chain equal

`[[4,19 lambda],[0,9]]`.

The same output probe gives 0 at lambda=0 and 19 at lambda=1, while all structural associativity/unit identities remain true. This is a tensor-calculus countermodel, not a computed physical K5 amplitude.

### T5 - regular contexts act through the normal test jets

In a fixed local chart/density, for an admissible term represented as

`u = sum_{|alpha|<=m} a_alpha(y) partial_x^alpha delta(x)`, `m<=8`,

the exact diagnostic identity is

`<u,K> = sum_{|alpha|<=m} (-1)^|alpha| <a_alpha, partial_x^alpha K(y,0)>`.

For a declared regular context family K, the residual invisible space is exactly

`N_K = ker J_K = A_adm^(m) intersect (span j_N^m K)^perp`.

If source-fixed values of these probes are imposed and a solution T0 exists, the solution family is `T0 + N_K`. Full smooth test jets separate the displayed supported distributions, but physical boundary contexts have not been shown to realize those jets. An injective probe map alone distinguishes extensions; it does not select one without source-fixed values or relations.

Theorems T4/T5 have FACT_LEVEL `CDSR_EXACT_THEOREM`, with physical application conditional on the specified domain and source map. No physical law receives `SOURCE_DERIVED` status in this gate.

## Source and composition verdict

The inspected versions are BCG 2601.23162v1, BCG 2604.24945v1, Beltran 2603.22661v2 and KKL 0909.0939v5. Equation-level anchors and signature/domain qualifications are recorded in the source manifest. No published-version delta or universal literature absence theorem is claimed.

The still-missing physical chain is:

`local extension T --I_v--> complete physical boundary functional --G_Gamma--> causal composition --R--> source-fixed extension-sensitive condition`.

The map I_v, legitimate causal composition domain, internal measure/quotient normalization, actual normal-jet image and a non-structural comparison relation are not supplied as a complete supported-extension construction by the current authority. Existing upstream Iter080B and repaired Iter080E blockers remain controlling; this is not a new repeated source census.

New upstream Critic corollaries Iter081H/I/K/L were read and pinned. Proper causal orientation sums retain the local obstruction and supported ambiguity in their stated minimal-spin scope. They are imported as upstream context, not newly executed CDSR results. Iter081F remains without a terminal atlas in the pinned snapshot; Iter080K remains provenance-invalid as a new-authority claim.

## Sector ledger

| Sector | Exact result | What is not established |
|---|---|---|
| TANGENTIAL_SHAPE | same-graph structural coherence does not remove W on a common regular domain | physical insertion domain and any stronger source-selected shape law |
| OVERALL_SCALAR | F delta_N is a nonzero distribution, detectable by suitable mathematical contexts | physical observability, redundancy, or scalar normalization |
| NORMAL_JETS | exact dual test-jet formula and annihilator; zeroth normal trace alone misses positive jets | actual physical jet transport, mixing matrix, kernel dimension or elimination |
| OTHER_SUPPORTED_SECTORS | structural theorem is independent of coefficients wherever operations exist | exhaustive A_B classification or treatment of additional physical strata |
| PHYSICAL_EQUIVALENCE | all-context nullity gives a conditional compositional criterion | actual source-defined probe class, its closure, and a physical quotient |
| COCYCLE_PROJECTIVE_ESCAPE | no physical domain/module/action derived; no irrelevant H^2 computed | physical deformation classification |

## No-smuggling audit

The fixed pairing and probe in the matrix countermodel are mathematical controls. Smooth compact kernels are diagnostic contexts, not a physical regulator or a replacement for the causal measure. Their choice is not advertised as selecting an extension.

A future positive selector must fix its physical contexts, comparison maps and target values independently. Setting the target values to evaluations of a preferred T would move extension ambiguity into selector input. The physical no-smuggling status here is `BLOCKED_NO_PHYSICAL_SELECTOR_OBJECT`, not PASS. No new physical principle was introduced.

## Counterexamples and controls

Twelve exact controls were actually executed locally with Python 3.13.5 / SymPy 1.14.0. They include symbolic three-/four-vertex reassociation, fixed unit, reversal, illegal swapping, distinct output at fixed pairing, a non-structural generator equation, normal orders 0/1/2/8, mixed derivatives, an invisible/visible first-jet pair, local jet-order mixing and the diagonal wavefront warning.

`analysis/cd003_exact_controls.py` SHA256:
`08a1e9e09c8a00f97c59c1aec174967e33eb0471ad889b9553671774d0fb7d49`.

`results/CD003_EXACT_CONTROLS.json` SHA256:
`7296c0790b56dc2afad6054afd6d2ad0c3bcae5940fe0e07fe1e88bd63583cdf`.

Reproduction:

```sh
python -m pip install -r analysis/requirements-cd003.txt
python analysis/cd003_exact_controls.py --output /tmp/cd003-controls.json
```

No GitHub Actions execution, full-amplitude computation or finite-sample proof of the general theorem is claimed. The recorded runtime is an execution record, not a package compatibility claim for every Python environment.

## Scope boundaries that remain decisive

Associativity of an unknown multiplication, a Pachner/refinement comparison, an idempotency equation for a generator, a source-fixed spectral condition or a closure/domain restriction may constrain the extension. These are NOT identical to structural reassociation and are NOT ruled out. Singular gluing requires independent distributional justification. The local normal-order expression is not a canonical complete physical decomposition. Mathematical distinguishability is not physical inequivalence.

## New physics and claim ceiling

New physical selection principle: NONE ESTABLISHED.
New recorded CDSR mathematics: T4/T5 and the explicit fixed-map countermodel. These use standard tensor/distribution reasoning, with no worldwide novelty claim.

All eight major false claim locks remain false: UNIQUE_K5_EXTENSION, PHYSICAL_SELECTOR_DERIVED, CRQN_V0_3_AUTHORIZED, REGULATOR_INDEPENDENCE, RG_CLOSURE, CAUSAL_MULTIVERTEX_CLOSURE, NEW_PHYSICS_FOUND, QUANTUM_GRAVITY_SOLVED.

## Exact next admissible question

Identify or derive an independently source-fixed, extension-sensitive relation OR a genuine gluing-domain restriction, and define its insertion map on supported K5 distributions. Then determine its actual normal test-jet image and residual kernel modulo a source-justified physical equivalence.

Do not reopen same-graph reassociation, finite moments, finite orientation sums or the unchanged source census as possible cures. Do not manufacture the comparison kernel, its target values, or a physical quotient from the desired extension. A new source derivation or an explicitly new prospectively motivated principle is required for the next positive physical step; this result does not prove that the latter is unavoidable.
