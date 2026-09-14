# Structural gluing and extension-sensitive coherence

## 1. Objects and the question actually decided

CD003 distinguishes an identity of a prescribed contraction calculus from a condition on its local amplitudes. The former can hold for every choice of amplitude; the latter must exclude at least one choice. Confusing them would promote the conditional power theorem CD002-A into a physical selection principle without deriving its hypothesis.

The authoritative local extension problem is denoted by

\[
 E=\operatorname{Ext}_{B}(t_0)=T_*+A_B,
 \qquad W=\operatorname{span}_{\mathbb C}\{Q^n F\delta_N:n\geq0\}\subseteq A_B.
\]

These are the established affine domain and ambiguity witness, not a complete classification. The translation notation is used only where the frozen conditions are affine and preserve the indicated ambiguity directions. In particular, an additional positivity cone or an analytic gluing-domain restriction need not be affine. The local minimal-spin common-collision setting has codimension 12 and transverse scaling degree 20; the allowed normal-order ceiling from Iter077L is 8. The word local is essential: this does not extend the result to all partial-collision strata or to the global noncompact group integral. [U077L, U077Q]

The prospective contract is `prereg/CD003_STRUCTURAL_GLUING_VS_EXTENSION_SELECTION.md`, commit `c3f898a975b56f3f707c00d3e01cf5388934d9f7`. Source identifiers below resolve in `sources/CD003_SOURCE_MANIFEST.md` and `.json`.

## 2. Two meanings of coherence

**Structural coherence** compares two evaluation orders of the same decorated graph. The vertices, their ports, their assignments, the edge contractions, the causal labels and the boundary remain fixed. Canonical associators and legal wire permutations change notation or evaluation order, not the graph or its generators.

**Extension-sensitive coherence** compares objects not already identified by those structural identities. Examples include a refined complex versus a coarse one, a generator versus a composite, a specified identity amplitude versus a dynamical local amplitude, or a source-derived equation for an unknown multiplication. Such relations can constrain the generator and are not excluded by this gate.

An especially important distinction is associativity of an unknown multiplication tensor \(\mu\). The equation \(\mu(\mu\otimes1)=\mu(1\otimes\mu)\) usually compares different port-wiring graphs. It can impose genuine polynomial equations on \(\mu\). It is not the canonical associativity of tensor products and is not covered by the non-selection theorem below.

## 3. Theorem S: same-graph structural coherence does not select generators

Fix a finite decorated graph \(\Gamma\). Each vertex has a prescribed tensor space \(V_v\); edge tensors, pairings, boundary dualities and numerical weights are fixed independently of the variable generators. Define the graph evaluation

\[
 Z_\Gamma((v_v)_v)=C_\Gamma\left(\bigotimes_{v\in V(\Gamma)}v_v\right).
\]

For this theorem, the permitted equalities are precisely those obtained by canonical reparenthesization or by legally reordering the contractions of this same decorated graph. Contraction maps must be defined on a common domain. In finite dimensions this is automatic. In a distributional implementation it is a substantive additional assumption, addressed below.

**Statement.** Every permitted structural equality holds for every generator assignment in that common domain. Consequently, imposing any collection of these equalities, even infinitely many, removes no generator assignment from the domain.

**Proof.** In bases, each output component of the graph is a finite sum over internal indices of the same product of tensor components and fixed edge factors. Reparenthesization changes neither that set of indices nor any factor nor its port assignment. Summing one internal index before another gives the same finite sum. Canonical wire permutations simply relabel matching indices and do not interchange the order of noncommuting operations on a wire. Thus the component expressions are identical polynomials in the entries of all variable generators. This proves equality for arbitrary assignments, not just sampled assignments.

Equivalently, the canonical tensor associators and permutations make the two expressions representations of the same multilinear map \(C_\Gamma\). Its equality to itself supplies no equation restricting the inputs. Taking any intersection of such identity solution sets still leaves the whole domain. Fixed structural identity maps obey their unit equations for arbitrary inputs as well. This does not identify a variable physical vertex with the structural unit. If a prescribed dual slot contains an adjoint, prove the identity with independently named slots and then substitute the adjoint; the identity still holds. No new physical duality convention is chosen. QED.

The proof is not the finite-rank argument of CD001. The residuals here can be polynomials of arbitrarily high degree when one generator is reused at many vertices; they nevertheless vanish identically. Counting diagrams or writing a formally infinite coherence family does not make those identities selective.

### Corollary for an extension domain

Let \(D\) be the common domain on which the prescribed structural graph calculus is defined. For an extension family \(E\) mapped into that calculus, its structural solution set is exactly

\[
 E_{\rm struct}=E\cap D.
\]

If the entire affine extension family is in \(D\), every admissible supported variation survives the structural equations, including \(W\). If not, the theorem asserts nothing about which variations lie in \(D\). Requiring existence, continuity, a wavefront-compatible pullback or closure under gluing may itself restrict the domain and could supply selection information. **This is not a theorem that every physical K5 extension admits composition.**

A restriction imposed by the domain must be identified and sourced separately; it cannot be credited to reassociation after the domain has been assumed.

## 4. Exact fixed-pairing countermodel

Use two-dimensional boundary vector spaces and the fixed nondegenerate pairing

\[
 B=\begin{pmatrix}2&0\\0&3\end{pmatrix},
 \qquad X\star Y=XBY,\qquad U=B^{-1}.
\]

Then \((X\star Y)\star Z=X\star(Y\star Z)\) and \(U\star X=X=X\star U\) for every matrix. For this symmetric pairing, transpose implements the reversal control \((X\star Y)^t=Y^t\star X^t\). None of these statements changes the pairing or normalization with the local assignment.

Set

\[
 A_\lambda=\begin{pmatrix}1&\lambda\\0&1\end{pmatrix}.
\]

The same open three-vertex graph evaluates exactly to

\[
 (A_\lambda\star A_\lambda)\star A_\lambda
 =A_\lambda\star(A_\lambda\star A_\lambda)
 =\begin{pmatrix}4&19\lambda\\0&9\end{pmatrix}.
\]

A fixed boundary probe taking the upper-right entry distinguishes \(\lambda=0\) from \(\lambda=1\): the outputs are 0 and 19. Every structural identity holds in both cases. Thus structural consistency and dependence of a boundary amplitude on local data coexist.

This is a tensor-calculus countermodel, not an actual causal K5 vertex or a demonstration of physical inequivalence in CRQN. Unlike Iter079C, it does not exploit freedom to change the pairing or internal weights. [U079C]

A negative control guards the theorem's boundary. For \(C_\lambda=\operatorname{diag}(1/2,\lambda/3)\),

\[
 C_\lambda B C_\lambda-C_\lambda
 =\operatorname{diag}\left(0,\frac{\lambda^2-\lambda}{3}\right).
\]

The additional equation \(C_\lambda\star C_\lambda=C_\lambda\) restricts \(\lambda\) to 0 or 1. It compares different vertex counts and is not a structural identity. This example is not a proposed physical selector, and it does not select uniquely even in this small family.

## 5. A legitimate distributional realization

For local distributions on independent copies of the vertex variables, choose a smooth compactly supported context kernel

\[
 K_\Gamma\in C_c^\infty(X_1\times\cdots\times X_n).
\]

Define

\[
 Z_\Gamma(T_1,\ldots,T_n)
 =\langle T_1\otimes\cdots\otimes T_n,K_\Gamma\rangle.
\]

The external tensor product is well-defined because the variables are independent. Iterated distributional pairing with this test kernel represents that same tensor product and gives the structural equalities on the whole stated domain. The construction can be made componentwise for a finite boundary-intertwiner sector. It does not justify multiplying distributions at a shared singular point or replacing a noncompact physical integration by a smooth compact kernel.

In this regular-context domain, the exact change when the same extension is varied at several vertices is

\[
 Z_\Gamma(T+u,\ldots,T+u)-Z_\Gamma(T,\ldots,T)
 =\sum_{\varnothing\ne S\subseteq V(\Gamma)}
 C_\Gamma\left(\bigotimes_v T_v^{(S)}\right),
 \quad T_v^{(S)}=\begin{cases}u&v\in S,\\T&v\notin S.\end{cases}
\]

For slots carrying a prescribed adjoint, replace the inserted variation by its adjoint as well. This is a dependence formula, not a vanishing identity. Structural coherence holds on each side separately regardless of whether this difference vanishes. With one slot varied, the expression is linear in \(u\); with several slots varied it need not be linear.

For the order-zero witness \(u=a(y)\delta_N\ne0\), a compact chart test with restriction \(\overline{a(y)}\chi(y)\), \(\chi\geq0\) supported where \(a\ne0\), gives a nonzero integral of \(|a|^2\chi\). A normal cutoff equal to one near zero extends it to a legitimate smooth test. Therefore the witness is detectable as a distribution. This separating test is mathematical, not a declaration that the source supplies it as a physical boundary state.

### Singular gluing is not included by fiat

A physical edge identification may require a diagonal pullback, a singular kernel or a noncompact pushforward. Those operations need domain, wavefront, support and convergence justification. For example, the opposite nonzero conormal directions of \(\delta_N\) fail the standard sufficient wavefront test for its self-product. No \(\delta_N^2\) is formed here. Failure of that sufficient test is not a theorem against every renormalized definition; choosing such a definition would require additional authority. [U080J]

## 6. Theorem J: regular contexts see a supported term through normal jets

Fix a tubular coordinate chart \((y,x)\) with \(N=\{x=0\}\), a density convention and a finite normal-order supported term in that chart,

\[
 u=\sum_{|\alpha|\leq m}a_\alpha(y)\,\partial_x^\alpha\delta(x),
 \qquad m\leq8.
\]

This notation specifies a class of terms on which the following identity is evaluated. It does not prove that every displayed term is physically admissible or that these coefficients form a canonical global direct-sum description of \(A_B\).

For a regular context \(K(y,x;b)\), with any external boundary probe already paired into \(b\),

\[
 \boxed{\langle u,K(\cdot;b)\rangle
 =\sum_{|\alpha|\leq m}(-1)^{|\alpha|}
 \left\langle a_\alpha,
       \partial_x^\alpha K(y,0;b)\right\rangle.}
\]

**Proof.** By the definition of a distributional derivative, moving \(\partial_x^\alpha\) from the distribution to the test contributes \((-1)^{|\alpha|}\). Pairing the remaining delta in the normal variable evaluates the differentiated test at \(x=0\); the tangential coefficient then acts on that restriction. Summing the finitely many terms proves the formula. QED.

The formula is an exact transport-to-context-evaluation law under the regular-kernel assumption. It is not a derived physical refinement map, a law on \(f(gh)\), or a proof that normal jets decouple. Different external contexts can mix coefficient components through the family of differentiated kernels.

The coordinate-independent content is that a finite normal-order supported distribution annihilates tests whose normal jets through order \(m\) vanish along \(N\). It therefore acts on the appropriate test-jet quotient. Writing individual coefficient functions requires chart/density choices; no canonical splitting is inferred.

## 7. Exact residual freedom for a declared context family

Let \(\mathcal K\) be any declared family of regular one-slot contexts and \(A_{\rm adm}^{(m)}\) the admissible supported variations in the finite-order class being tested. Define the linear map

\[
 J_\mathcal K u=(\langle u,K\rangle)_{K\in\mathcal K}.
\]

The invisible variations are exactly

\[
 \boxed{\mathcal N_\mathcal K
 =\ker J_\mathcal K
 =A_{\rm adm}^{(m)}\cap
       \bigl(\operatorname{span}j_N^m\mathcal K\bigr)^\perp.}
\]

The last expression means the annihilator under the signed pairing of Theorem J. It is not a dimension estimate and requires no finite sampling or presumed completeness of physical states.

If a source independently specifies the values \(b_K\) in equations \(\langle T,K\rangle=b_K\), and one solution \(T_0\) exists in the tested affine family, its exact solution set is \(T_0+\mathcal N_\mathcal K\). Thus uniqueness in this family requires \(\mathcal N_\mathcal K=0\), or a separately justified physical quotient identifying precisely the remaining invisible directions.

**Separation alone is not selection.** Even an injective evaluation map only labels different extensions unless a source fixes target values or relations. Assigning those values from a desired extension would encode the original choice in the selector input.

### Complete mathematical tests versus physical tests

Arbitrary compactly supported smooth coefficient jets can be prescribed locally: multiply

\[
 \sum_{|\alpha|\leq m}\frac{x^\alpha}{\alpha!}h_\alpha(y)
\]

by a normal cutoff equal to one near zero. Its normal jet is the chosen collection \(h_\alpha\). Taking these tests separately for each index proves that all compact smooth tests separate the displayed supported distributions. This is not a claim that the actual spin-network boundary state space induces all these group-variable tests. That image, including its normal derivatives at the collision, is a missing physical map.

At the other extreme, if every context is locally independent of the normal coordinates, every positive-order normal derivative is invisible to that family. An order-one term acts on a constant-normal test as zero, while \(\delta'(x_1)\) acts on \(x_1\chi(x)\) as \(-1\). Hence a zeroth-order boundary restriction cannot be assumed to control the jet tower. When tangential coefficients vary freely in any admissible positive-order sector, this invisibility may be infinite-dimensional; this gate does not assert that the physical admissible sector has that size.

### A controlled example of jet-order mixing

For the local normal-coordinate diffeomorphism \(\Phi(t)=t+a t^2\), with pushforward convention \(\langle\Phi_*u,\varphi\rangle=\langle u,\varphi\circ\Phi\rangle\), the chain rule gives

\[
 \Phi_*\delta''=\delta''-2a\delta'.
\]

Indeed the action on a test is \(\varphi''(0)+2a\varphi'(0)\). This is an exact local diagnostic, not a source-derived refinement. It prevents assuming that an unspecified transport must preserve each normal derivative order diagonally.

## 8. Physical equivalence requires all allowed contexts

Mathematical equality, equality under a chosen family of probes, and physical equivalence are different assertions. The actual physical context family has not been identified. Therefore \(\mathcal N_\mathcal K\) above is a conditional diagnostic and is not installed as the physical quotient of CDSR.

Even after a family is proposed, nullity for one boundary test need not persist when the term is inserted into a larger diagram. To support a compositional equivalence, its null directions must remain null in every permitted one-slot context, including contexts obtained by inserting other admissible vertices, applying duality, and making allowed further gluings. For regular multilinear contractions, this all-context property is sufficient for replacing a null difference at any number of slots: telescope the difference of the two graph evaluations one slot at a time. Whether the physical source supplies such a closed family remains open.

This addresses the scalar issue too. The direction \(F\delta_N\) is a nonzero mathematical distribution and can change regular-context evaluations. It cannot be dismissed as an overall normalization of the off-collision amplitude, which it does not change at all. Whether its coefficient is observable, redundant or fixed by a physical law still requires the actual source-defined contexts and quotient.

## 9. Source result and missing arrows

The four pinned sources locate the relevant objects but do not supply the missing supported-extension transport. Their equation anchors and qualifications are recorded in the source manifest rather than treated as a new source census. In particular, a source trace/gluing identity is not a homomorphism condition on an independent coefficient function on \(SU(2)^4\). [P1-P4, U080B, U080E]

The minimum unresolved chain is

\[
 T\ \xrightarrow{\ I_v\ }\ \text{physical local boundary functional}
 \ \xrightarrow{\ G_\Gamma\ }\ \text{causal composed amplitude}
 \ \xrightarrow{\ R\ }\ \text{source-fixed comparison or condition}.
\]

Here \(I_v\) must explain how the full local supported extension enters a physical vertex, including compatibility with the rest of the group-variable domain. \(G_\Gamma\) must have specified causal labels, measures, quotient normalization and a legitimate singular/infinite-dimensional composition domain. \(R\) must impose an extension-sensitive condition, not merely another evaluation order of the same graph. To infer physical uniqueness, the actual probe/jet image and the physical quotient must also be supplied.

This does not establish that these data cannot be derived. It says exactly which objects are not established by the current chain and what structural coherence cannot do in their place. A missing item could eventually be derived from source assumptions, or introduced as an explicitly new independently motivated CDSR principle. A convention fixing notation, a structural unit or an evaluation order alone is insufficient.

No physical cocycle module, groupoid, regularity class or coboundary quotient has emerged from this gate. Computing a convenient cohomology of \(SU(2)^4\) would therefore answer a different question. The physical cocycle/projective alternatives remain open, not proved trivial.

## 10. Verdict and scope

The mathematical result is `PASS_EXACT_SCOPED`: same-graph structural coherence is non-selective, and regular-context sensitivity is governed exactly by the test-jet pairing and its annihilator. These are new recorded results for CDSR, based on standard tensor/distribution reasoning; no worldwide mathematical novelty claim is made.

The physical result is `BLOCKED_SOURCE_BRIDGE`: no actual source-derived full K5 supported-extension transport or selecting law was established. This result incorporates, rather than repeats as new science, the previously established source blockers and the new upstream causal-sum corollaries. [U080B, U080E, U081H, U081I, U081K, U081L]

No universal impossibility of selection, no physical equivalence classification, no complete normal-jet parameterization, no unique K5 amplitude, no regulator prescription/independence, no causal multivertex closure, no CRQN v0.3, no RG closure and no new physics follow.
