# Source audit 01 — Riemann, Director, and Dirichlet's principle

**Status (2026-10-13):** first passage-level comparison completed from the full German Riemann text and Director's published article. Original 1857 facsimile is linked in [PRIMARY.md](PRIMARY.md), but the detailed check below uses D. R. Wilkins's **complete German transcription** of the 1857 paper (2000 corrected edition), **not** an original page-image edition. The original *Journal für die reine und angewandte Mathematik* 54 (1857) pagination is 101–155. The Wilkins transcription numbers the paper 1–55.

## A. Exact texts used

**Riemann:** Bernhard Riemann, *Theorie der Abel'schen Functionen*, *Journal für die reine und angewandte Mathematik* **54** (1857), pp. 101–155.
- [German paper, complete transcription by D. R. Wilkins](https://www.emis.de/classics/Riemann/AbelFn.pdf).
- [Contemporary separate-edition facsimile, ETH e-rara](https://www.e-rara.ch/zut/content/titleinfo/13599822).
- Working references below give the **1857 journal page**, then Wilkins's own page in parentheses.

**Director:** Bruce Director, [“Bernhard Riemann's ‘Dirichlet's Principle’”](https://archive.schillerinstitute.com/fid_02-06/2004/044_riemann_dirichlet.html), *Fidelio* XIII/4, Winter 2004 (publisher page header; it also contains the internally inconsistent sentence “reprinted from the Winter 2000 FIDELIO”). **Use Winter 2004 tentatively until the print issue is examined.** Direct source citations are to paragraph locations/headings, since the HTML has no printed pagination.

**Weierstrass:** Karl Weierstrass, *Über das sogenannte Dirichlet'sche Princip*, **read** to the Berlin Academy 14 July 1870; **printed in** *Mathematische Werke*, vol. II (1895), pp. 49–54. [Full German text and scan provenance](https://readthemasters.org/works/weierstrass-1895-dirichletsche-princip/) (**AI-draft transcription, not checked against print by its host**). [Original scan at Internet Archive linked from that page](https://readthemasters.org/works/weierstrass-1895-dirichletsche-princip/). Date of delivery ≠ date of print.

**Schwarz:** Hermann Amandus Schwarz, *Zur Integration der partiellen Differentialgleichung d²u/dx² + d²u/dy² = 0 unter vorgeschriebenen Grenz- und Unstetigkeitsbedingungen*, Berlin Academy proceedings (1870), pp. 767–795. [Original printed pamphlet facsimile](https://www.e-rara.ch/zut/content/titleinfo/29398928), [DOI 10.3931/e-rara-119446](https://doi.org/10.3931/e-rara-119446). Distinct from Weierstrass's criticism: this gives a **constructive alternative** for existence in cases where the original argument is not justified.

**Modern historical check:** [MacTutor, Riemann biography](https://mathshistory.st-andrews.ac.uk/Biographies/Riemann/) and [From Attraction Theory to Existence Proofs: The Evolution of Potential-Theoretic Methods in the Study of Boundary-Value Problems, 1860–1890](https://www.numdam.org/item/RHM_1996__2_1_67_0/).

## B. What Riemann actually says

| Passage in Riemann | Mathematical content | Question for Director |
| --- | --- | --- |
| §1, **p. 101** (Wilkins p. 1) | Announces research on `Transcendenten` including Abelian functions. Takes the complex plane `z = x + yi` and `i ∂w/∂x = ∂w/∂y` as analytic starting points. | “Transcendental” is the author's term here; neither a generic maxim about all change nor a definition of a transcendental number. |
| §1, **p. 102** (Wilkins p. 2) | Continuation of `log(z − a)` around `a` changes a chosen branch by `2πi` (with Riemann's signed-side convention). Functions can be continued along paths with distinct values at the same projected point. | Singularities and sheets are analytical/geometrical **structures**, not merely physical “introductions of a new principle.” |
| §3, **p. 111** (Wilkins p. 11) | Asks for a sufficient set of **independent conditions** determining a transcendental function; discusses Dirichlet's principle and prescribed discontinuities on a possibly multiple-sheeted surface. | It is specifically a mathematical boundary/singularity problem. |
| §3, **p. 112** (Wilkins p. 12) | Defines the nonnegative integral below and *infers the existence of a minimizing function from finite nonnegative values.* | **This is exactly the contested existence step**; it is not settled by asserting that a physical process is bounded. |
| §3, **p. 113** (Wilkins p. 13) | Varies the alleged minimizer, derives a vanishing first variation, then constructs a conjugate function (locally) and the analytic combination `u+iv`. | Derivation of an Euler–Lagrange equation **assuming a minimizer** is distinct from proving such a minimizer exists. |

Write Riemann's functional on the two-dimensional surface `T` as

```math
Ω(α) = ∫_T [(∂ₓα − ∂ᵧβ)² + (∂ᵧα + ∂ₓβ)²] dT .
```

He varies the real part through `α−μ`, with prescribed conditions on the boundary and admissible discontinuities. This is **not** an abstract assertion that nature always takes “the least action.” Note that the expression involves **derivatives across a continuous domain** and constraints; there is no “local pairwise minima” algorithm here.

The decisive passage at p. 112 is an explicit inference: `Ω` is always finite and nonnegative, **therefore** a minimum must occur for some `u = α−μ`. That “therefore” is not a valid general theorem without existence hypotheses. It is the mathematical point in dispute, including within Riemann's own paper.

## C. What Director says (and where it goes wrong)

The 2004 Director article, sections “The Potential” and “From Gauss, to Dirichlet, to Riemann,” argues from the physical catenary and boundary changes to harmonic potential and then to Riemann's principle. That can suggest a **useful reading question**: what properties are global, which are local, and how do boundary/singularity conditions constrain the function?

But specific assertions are not justified:

1. **Existence of a minimum.** In its final paragraphs Director calls Weierstrass's demand for a mathematical demonstration of existence “sophistry” and treats physical boundedness as sufficient. That is false in general. A nonnegative variational integral can have an infimum with no admissible minimizer. This is precisely Weierstrass's 1870 objection, not an objection to mathematics studying physical systems.
2. **Harmonicity vs curvature.** Under “The Potential,” Director calls harmonic functions orthogonal families whose **curvatures change at the same rate**. Harmonicity is a *differential equation*: `Δu = 0`. In two dimensions, the level sets of a harmonic function and a locally defined harmonic conjugate are orthogonal **where the gradient is nonzero**, but their geometric curvatures need not equal one another or vary at the same rate. Example `u = log r`, `v = θ` (locally): their level sets are circles (curvature `1/r`) and radial lines (curvature `0`). Both potentials are locally harmonic, and their gradients are orthogonal.
3. **Physical arguments and mathematical conditions.** A hanging chain is governed by equilibrium, mass distribution, length and anchor constraints. Existence, uniqueness and stability of a minimizer depend on a defined admissible class and assumptions. “Both endpoints are fixed” is not the same as specifying the full problem.
4. **Elliptic functions and topology.** Director describes *all* elliptic functions as surfaces with “two boundaries.” On the usual complex torus, an elliptic function is meromorphic on a **compact genus-one surface without boundary**. A chosen *cut-open fundamental polygon* has boundary edges that are identified; this is not a topological boundary of the torus. A particular picture may show a cut presentation, not a theorem about “all elliptical functions.”

None of these corrections negates Riemann's influence or the importance of global structure. It simply distinguishes the mathematical conclusion from a historical-philosophical analogy.

## D. Exact counterexample: Weierstrass's functional

Let admissible `φ` be continuously differentiable on `[-1,1]`, satisfying `φ(-1)=0` and `φ(1)=1`. Consider

```math
J[φ] = ∫_{-1}^1 x²(φ′(x))² dx ≥ 0.
```

**The infimum equals zero, but no admissible `φ` attains zero.**

1. If `J[φ]=0`, continuity of `φ′` implies `xφ′(x)=0` for every `x`; hence `φ′(x)=0` everywhere except possibly at `0`, and continuity forces `φ′(0)=0` as well. Thus `φ` is constant, contradicting the boundary values.
2. Nevertheless, for every `ε>0` define the explicit smooth function

```math
φ_ε(x) = [arctan(x/ε) + arctan(1/ε)]/[2 arctan(1/ε)].
```

Its endpoint values are 0 and 1, and elementary integration gives, with `A = arctan(1/ε)`,

```math
J[φ_ε] = ε/(4A) − ε²/[4A²(1+ε²)] → 0
as ε → 0⁺.
```

Numerical values from direct evaluation (rounded):

| ε | J[φ_ε] |
| ---: | ---: |
| 1 | 0.1156675 |
| 0.1 | 0.0158501 |
| 0.01 | 0.00159148 |
| 0.001 | 0.000159155 |

The interval is finite, endpoints fixed, each competitor smooth, and the integral nonnegative. **None of those facts forces existence of a minimizer.** This is an illustrative version of Weierstrass's objection; it uses the same type of weighted integral, not Riemann's exact two-dimensional integral. Weierstrass's example by itself does **not** disprove all valid versions of Dirichlet's principle; it invalidates the *unqualified inference* of a minimizer from a finite lower bound.

### Independently executable numerical test (Python standard library)

```python
from math import atan

def J(epsilon):
    assert epsilon > 0
    angle = atan(1 / epsilon)
    return (epsilon / (4 * angle)
            - epsilon**2 / (4 * angle**2 * (1 + epsilon**2)))

values = [J(e) for e in (1, 0.1, 0.01, 0.001)]
assert all(0 < value for value in values)
assert all(values[i+1] < values[i] for i in range(len(values)-1))
for e, value in zip((1, 0.1, 0.01, 0.001), values):
    print(f"{e}: {value:.9g}")
```

## E. Read next

- [Weierstrass's original 1870 Academy paper, printed 1895](https://readthemasters.org/works/weierstrass-1895-dirichletsche-princip/) and [Schwarz's original 1870 pamphlet scan](https://www.e-rara.ch/zut/content/titleinfo/29398928) should be compared to Riemann's own p. 112. Recheck Weierstrass against page images because the online transcription is AI-generated.
- Riemann's **1851 dissertation** already applies related reasoning; study Arts. 17–18 and the independently formulated existence assumptions.
- For the philosophical question of **action integrals vs pairwise pointwise relationships**, distinguish an integral/functional `J[u]`, a local differential equation for its stationary points, and the global existence/uniqueness of a minimizer. Neither one alone implies the other.
- Test Director's other central claims from first editions before moving to historical intent: whether Gauss's 1799 dissertation uses harmonic potential in the manner ascribed, and whether the asserted Leibniz–Gauss influence chain is documented rather than inferred.

**Audit boundaries:** this document directly checks Riemann's German §1/§3 and Director's full HTML text, and uses a separately verified algebraic counterexample. It **does not yet** certify the wording from a 1857 original page image or a complete text-to-text audit of the entire Director series.
