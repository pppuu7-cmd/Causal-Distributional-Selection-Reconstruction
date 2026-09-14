# No-Smuggling Test

**Purpose:** operational audit for any candidate selector `P`. This protocol is a diagnostic checklist, not a general theorem that two formulations are equivalent.

A candidate physical selector must be audited **before** its success/failure outcome is used to tune its free data.

## Mandatory questions

1. **What new mathematical data does `P` introduce?** List every function, kernel, measure, normalization, contour, map, boundary object, transport rule, reference scale, subtraction term, and auxiliary choice.
2. **Are those data fully source-derived?** For each datum record exact authority. If not, classify it explicitly as `NEW_PHYSICAL_PRINCIPLE` or reject physical promotion.
3. **Does `P` contain an arbitrary function?** If yes, identify its domain, codomain, regularity and independent degrees of freedom.
4. **Does `P` contain an arbitrary kernel?** If yes, determine whether the kernel can encode extension coefficients or correlations that are otherwise free.
5. **Does `P` introduce a measure?** If yes, identify whether its density/normalization/scheme is fixed independently of the desired extension.
6. **Does `P` introduce a normalization map?** If yes, determine whether changing it changes the selected extension.
7. **Does `P` introduce a subtraction map or finite-part rule?** If yes, establish whether it is source-derived rather than a renamed extension choice.
8. **Does `P` introduce a contour or boundary-value prescription?** If yes, prove that the relevant *joint K5* contour/order-of-limits object is defined; one-wedge authority is not enough.
9. **Does `P` introduce a boundary functional or probe family?** If yes, establish completeness/relevance independently; a handpicked finite probe set cannot silently encode the answer.
10. **Does `P` introduce a transport map?** If yes, pin its domain/codomain, composition law, gauge/orientation behavior and action on supported terms.
11. **Can the selector data encode arbitrary directions in `A_B`?** Test this on the proven Iter077Q witness `W=span{Q^n F delta_N}` and, where defined, on the normal-jet frontier.
12. **If selector data vary, does the selected extension vary?** Map selector-input variation to output variation. If the output tracks unconstrained input, the ambiguity may only have moved.
13. **How many independent degrees of freedom are in the selector input?** Distinguish finite scalar parameters from function/kernel/jet-valued data; do not call an infinite object “one condition” merely because it has one name.
14. **Has the transformation `extension ambiguity -> selector ambiguity` merely occurred?** Give an explicit argument either way. A positive answer blocks explanatory promotion until the selector data themselves are independently fixed.

## Required audit output

For each candidate selector record:

```text
SELECTOR_ID:
FACT_LEVEL:
SOURCE_STATUS: SOURCE_DERIVED | NEW_PHYSICAL_PRINCIPLE | CONDITIONAL_SELECTOR_POWER_ONLY
NEW_DATA:
FREE_DATA_DIMENSION_OR_STRUCTURE:
CAN_ENCODE_W_DIRECTIONS: YES | NO | OPEN
OUTPUT_VARIES_WITH_SELECTOR_DATA: YES | NO | OPEN
TANGENTIAL_SHAPE_EFFECT:
SCALAR_EFFECT:
NORMAL_JET_EFFECT:
PHYSICAL_EQUIVALENCE_USED:
NO_SMUGGLING_STATUS: PASS | FAIL | BLOCKED | OPEN
EVIDENCE:
```

## Interpretation

`NO_SMUGGLING_STATUS=PASS` means only that the audited rule has not hidden the tested extension choice in unauthorized free selector data. It does **not** prove existence, correctness, physical truth, uniqueness, regulator independence, or phenomenological validity.

`FAIL` means the rule's free inputs can reproduce the ambiguity it claims to remove without independent authority. `BLOCKED` means the audit cannot yet be completed because the selector object/domain is not defined. `OPEN` is used before a candidate is frozen.

## Anti-post-hoc rule

Do not first inspect which function/kernel/measure/normalization gives a finite or aesthetically preferred amplitude and then declare that datum part of the selector. The selector's data and motivation must be prospectively frozen or independently source-derived before outcome inspection.
