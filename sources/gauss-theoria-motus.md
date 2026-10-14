# Gauss: Theoria motus — physical constraints and least squares

The question is exploratory: do these sources change our understanding of regression? This note does not assume that they establish an alternative to it.

## Editions and reading coverage

Carl Friedrich Gauss, *Theoria motus corporum coelestium in sectionibus conicis solem ambientium* (1809).

- [1809 original edition: record](https://www.e-rara.ch/zut/content/titleinfo/142787) and [complete facsimile PDF](https://www.e-rara.ch/zut/download/pdf/142787).
- Charles Henry Davis's 1857 English translation: [record](https://archive.org/details/theoryofmotionof00gausuoft), [complete PDF](https://www.karlin.mff.cuni.cz/~tuma/Aplikace21/theoryofmotionof00gausuoft.pdf), [searchable OCR](https://archive.org/download/theoryofmotionof00gausuoft/theoryofmotionof00gausuoft_djvu.txt).

Read for this note: the author's preface; Book I, §§1–2; Book II, §§175–181. This is a topic-specific reading, not a claim to have read every orbit-computation chapter. The mean-postulate argument was checked visually on printed p. 258 of Davis (PDF page 282). OCR is not authoritative for formulas. The 1809 scan was retrieved, but the Latin wording has not been collated throughout against Davis.

## Summary of the relevant argument

Gauss separates a physical model from adjustment to imperfect observations. Book I specifies conic motion and the area law; the preface explains why one must understand the forward calculation before recovering orbital elements. His claim to avoid hypothetical assumptions does not remove these laws: it avoids prematurely fixing special orbital elements or a conic type. He also warns that his published method differs substantially from his first Ceres calculation.

In §§175–179 he introduces observation functions, independent errors, and inverse probability with an equal-prior assumption. He asks which error law supports the customary rule that the arithmetic mean is the most probable estimate. His answer is Gaussian; he acknowledges its imperfect description of extreme errors. Unequal precision leads to weighted squared residuals. Section 180 derives simultaneous normal equations and explains successive linear approximations for nonlinear functions. These are not separately optimized observation pairs.

## What the mathematical argument commits us to

The following is our modern reconstruction, not Gauss's notation.

Suppose independent additive errors have a common positive differentiable density f. Write ψ(e) = d(log f(e))/de. If the arithmetic mean must maximize the likelihood for every sample, the score equation must hold whenever the residuals sum to zero. With residuals x, y, −x−y, and the symmetry condition, this gives

    ψ(x) + ψ(y) = ψ(x+y).

Under continuity, ψ(e) = −2h²e, hence

    f(e) = (h/√π) exp(−h²e²).

This argument characterizes an error law from a chosen estimation principle. It does not establish by observation that every instrument has Gaussian errors. Reversing the argument—assuming Gaussian errors and deriving least squares—is another direction of implication, not independent empirical confirmation.

For unequal precisions hᵢ, maximizing the product density is equivalent to minimizing

    Q(θ) = Σᵢ hᵢ² [observationᵢ − predictionᵢ(θ)]².

In present variance notation, hᵢ² = 1/(2σᵢ²). The factor 1/2 does not change the minimizer. Correlated errors require a joint model; independent-error multiplication cannot simply be retained.

For a linear observation map Xθ, the normal equation and curvature are

    XᵀW(Xθ − observations) = 0,
    Hessian(Q) = 2XᵀWX.

With positive weights this Hessian is positive semidefinite. Every local minimum is global; full column rank gives uniqueness. Each observation contributes to the same parameter vector. This is global estimation even when the objective is a sum of individual residual penalties.

For nonlinear orbit predictions, a local linearization does not make the entire problem convex or guarantee convergence. Physical restrictions determine which predictions can occur; least squares ranks their agreement with measurements. Neither role substitutes for the other.

## Retrieved edition checksums

These identify the complete files retrieved during the reading; they do not assert complete reading or permanently committed PDF bytes.

| Edition | SHA-256 |
| --- | --- |
| Original 1809 PDF | `f3d8ad6462d246174c94eeefc5ea539f4cf4216b84fb5d83a2d8e93f69b2fcc8` |
| Davis 1857 PDF | `5f41b78b0a77a9c2001571a880b78893200d0452ed7328a5554682e9a3a45787` |
| Davis OCR | `fce5340d6b7bf5f73772a0b1fbe96bdb0b3f5404ac2431d7a002ab0d76c1a32e` |

The useful unresolved issue is not whether Gauss rejects regression. It is how physical assumptions, identifiability, error assumptions, and later observations jointly warrant confidence in an inferred orbit.
