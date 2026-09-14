# CD003 - structural coherence and test-jet duality, source-corrected

Controlling erratum: `results/CD003_SOURCE_LOCK_ERRATUM.md`, commit `05f678e1e8e087a1a85b3bbb75ac1a58b5317317`.
Original preregistration: `c3f898a975b56f3f707c00d3e01cf5388934d9f7`.
The frozen mathematical hypotheses and 12 controls are unchanged. The exact original derivation is preserved at `derivations/archive/CD003_PRE_CORRECTION_SNAPSHOT.md`; its PHYSICAL W-subspace premise is withdrawn, not silently repaired. This document restates the surviving proofs and their corrected application.

## 1. Correct domain, not a preferred extension

Let E_corr = Ext_{B_corr}(t0) on the established local common-collision domain, with node-wise right SU(2) covariance included in B_corr. In the affine setting write E_corr=T_*+A_corr; the notation does not choose T_*. Do not assume a global all-strata extension or that adding positivity preserves an affine domain.

Historical W=span{Q^n F delta_N} is mathematically independent but is NOT an established physical subspace of A_corr. Upstream Iter081R/S instead demonstrate a scalar invariant normal-jet subspace J_inv subset A_corr of dimension28, grades (1,0,1,0,3,0,7,0,16) through order8. This is a lower bound, not the total dimension. These are imported results, not new calculations in CD003. Exact pins are in sources/CD003_SOURCE_CORRECTION_MANIFEST.json.

## 2. Theorem T4/S - structural reassociation does not constrain generators

Fix a finite decorated graph Gamma with prescribed local tensor spaces, port wiring, edge pairings/weights and boundary operations. Define

`Z_Gamma(v_1,...,v_n) = C_Gamma(v_1 tensor ... tensor v_n)`.

All structural equalities considered here compare canonical reparenthesizations or legal contraction orders of that SAME decorated graph. Let D be the common domain on which the prescribed operations are well-defined.

**Theorem.** Every such identity holds for every assignment in D. Their joint solution set on an extension family E is exactly E intersect D, even for an infinite collection of these structural identities.

**Proof.** In finite-dimensional bases each output is a finite sum over identical internal indices of the identical product of tensor entries and fixed edge factors. Reparenthesization changes neither indices nor factors nor their connections. Canonical permutations relabel paired indices; they do not reverse noncommuting operations along a wire. Thus both expressions are the same polynomial in the arbitrary generator entries. Every permitted structural identity has the whole common domain as its solution set, and so does their intersection. For prescribed adjoint slots, prove the identity with independent slots before substituting the adjoints. QED.

For distributions, a concrete legitimate common domain is external tensor products on independent vertex variables paired with K_Gamma in C_c^infinity(product X_v):

`Z_Gamma(T_1,...,T_n)=<T_1 tensor ... tensor T_n,K_Gamma>`.

Iterated test pairing represents the same external tensor product. This is not a definition of singular diagonal gluing or the noncompact causal integral.

**Correct physical application:** E_struct=E_corr intersect D. If J_inv directions lie in the actual D, structural reassociation does not remove them. Membership in the physical D is NOT established. Source-derived continuity, wavefront, convergence or closure restrictions may constrain D and remain possible selectors. No physical infinite-W corollary survives.

The theorem is not CD001: arbitrarily many high-degree polynomial identities may all be identities rather than restrictions. It is not a no-go for all associativity: associativity of an UNKNOWN multiplication tensor mu, `mu(mu tensor 1)=mu(1 tensor mu)`, compares different wiring graphs and can constrain mu. Refinement/Pachner equalities, dynamical units, idempotency and spectral laws are likewise outside the tested structural class.

## 3. Fixed-pairing countermodel

Use B=diag(2,3), X star Y=X B Y and the fixed unit B^{-1}. For A_lambda=[[1,lambda],[0,1]], either parenthesization of the three-vertex chain is

`[[4,19 lambda],[0,9]]`.

The SAME upper-right boundary probe yields 0 and19 for lambda=0 and1. Pairing, unit, weights and probe never vary. All structural associativity/unit equations hold. This refutes the implication from those equations to generator selection, not a claim about the actual K5 amplitude or physical equivalence.

Negative control: C_lambda=diag(1/2,lambda/3) obeys

`C_lambda B C_lambda-C_lambda=diag(0,(lambda^2-lambda)/3)`.

The extra equation C star C=C constrains lambda; it is a different-graph relation, not structural reassociation. It is not proposed as physics.

## 4. Supported insertion and sensitivity

On the regular context domain, varying all slots by u gives exactly a sum over nonempty subsets of vertices in which u replaces T; this is the multilinear expansion of `(T+u) tensor ... tensor (T+u)`. Structural identities hold for each assignment even when boundary outputs differ. A one-slot variation is linear in u.

A nonzero scalar term a(y) delta_N is separated mathematically by a compact test whose restriction is conjugate(a) chi, chi nonnegative supported where a is nonzero. This proves detectability as a distribution, NOT availability of that test as a physical boundary context. The restored source symmetry restricts which a are admissible; it cannot be ignored.

Singular gluing needs a separate pullback/product/pushforward theorem. Opposite nonzero conormal directions make the standard sufficient wavefront criterion fail for a delta self-product; no delta squared is used here. Failure of a sufficient criterion is not nonexistence of all renormalized prescriptions.

## 5. Theorem T5/J - exact normal test-jet pairing

In a fixed local tubular chart/density, consider an admissible finite-normal-order term represented as

`u=sum_{|alpha|<=m} a_alpha(y) partial_x^alpha delta(x)`, m<=8.

This is a class of terms, not a canonical global decomposition or proof that every formal coefficient is physically allowed. After the source correction coefficient data must meet node covariance and other source constraints.

For every smooth compact regular context K,

`<u,K>=sum_{|alpha|<=m} (-1)^|alpha| <a_alpha,partial_x^alpha K(y,0)>`.

**Proof.** By definition of distributional derivative, moving partial_x^alpha onto a test contributes (-1)^|alpha|. Delta evaluates its normal argument at zero; the tangential coefficient pairs with the restricted derivative. Sum the finitely many terms. QED.

Intrinsic content: u acts on the test-function quotient by tests with vanishing normal jets through orderm along N. Individual coefficient coordinates depend on chart/density; no intrinsic direct-sum splitting is inferred.

For a DECLARED context family Kset and admissible linear variation sector A_adm^(m), define J_Kset u=(<u,K>)_K. Then

`N_Kset=ker J_Kset=A_adm^(m) intersect (span j_N^m Kset)^perp`.

The perpendicular denotes annihilation in the signed dual pairing above. If independently fixed equations `<T,K>=b_K` have a solution T0, their solution family is T0+N_Kset. Probe separation alone is not selection: targets or relations must also be source-fixed.

All local compact smooth jets can be prescribed using `sum x^alpha h_alpha(y)/alpha!` times a cutoff equal to one near zero. They separate the displayed distributions mathematically. The physical state space need not realize this test-jet image.

For context kernels independent of normal coordinates near N, positive normal derivatives are invisible. Delta-prime evaluates a flat-normal test as0 and a linear-normal test as-1. On the corrected physical sector, only admissible invariant combinations are relevant; no physical order-one invariant direction is asserted (Iter081R has d1=0).

A local pushforward diagnostic gives `Phi_*delta''=delta''-2a delta'` for Phi(t)=t+a t^2, using `<Phi_*u,phi>=<u,phi composed Phi>`. This follows from the chain rule and illustrates possible order mixing. It is NOT physical jet transport, and need not preserve the corrected invariant sector.

## 6. Corrected invariant-jet application and physical equivalence

Restrict T5 to J_inv or another explicitly source-admissible sector. For a chosen basis u_A of J_inv, actual source contexts would define `M_iA=<u_A,K_i>`; their invisible coefficient directions are ker M. CD003 does not supply the actual physical K_i or M or its rank. The bound m<28 and possible injectivity at m>=28 are imported from Iter081S, not a new gate. Rank on this subspace alone would not prove complete physical uniqueness.

For a compositional equivalence, a difference must be null in ALL allowed one-slot contexts, including further gluings and admissible other vertices. In a regular multilinear calculus, telescoping one slot at a time shows this condition suffices to replace such differences in larger graphs. No actual physical all-context quotient has been derived. The node-wise gauge orbit is now correctly identified; that does not settle all observational or redefinition equivalences.

The scalar c F delta_N remains a nonzero admissible direction and cannot simply be called normalization of t0, which it does not change off N. Its physical effect requires the actual insertion map and contexts.

## 7. Missing source maps and surviving alternatives

The missing chain is `T --I_v--> full local physical boundary functional --G_Gamma--> causal composed amplitude --R--> source-fixed extension-sensitive relation`.

I_v must incorporate admissible supported terms into the actual vertex, G_Gamma must supply measures, orientations, quotient and legitimate composition domain, and R must constrain the extension rather than re-evaluate one graph. Alternatively a genuine source-derived restriction on the gluing domain might carry that constraint.

No physical groupoid/coefficient module/action/regularity or coboundary equivalence was derived, so no physical cohomology is computed. No source-derived physical selector is claimed.

T4/T5 have FACT_LEVEL CDSR_EXACT_THEOREM. Their physical premises remain conditional. The original aggregate is PASS mathematics / BLOCKED physical bridge, now with the mandatory disposition ITER077Q_PHYSICAL_APPLICATION_WITHDRAWN. Upstream R/S restore the correct physical target; they are not CDSR discoveries. No universal no-go, exact total dimension, regulator prescription, CRQN v0.3, RG closure or new physics follows.
