# Working mathematical and historiographical questions

This is a reading and computation program, not a declaration that seventeenth-, eighteenth-, and nineteenth-century uses of “transcendental” meant the same thing.

## 1. Leibniz's actual catenary vs modern cosh

- Read *Acta Eruditorum* June 1691, pp. 277–281, and September 1691, pp. 435–439, from the original-volume scan in [PRIMARY.md](PRIMARY.md).
- Transcribe Leibniz's construction, figure labels and argument. Keep figures separate from modern rendering.
- In modern coordinates derive the static uniform-chain equation `y(x) = a cosh((x − x₀)/a) + y₀` from force balance and a choice of origin. State the uniform weight assumption and the meaning of `a`.
- Check which modern expressions are **equivalent to**, but not literally **printed in**, Leibniz's article.
- Compare with the first appearance of logarithms in the paper's title and actual construction; mark what the paper does and does not prove.

## 2. Cotes's logarithms, angle and quadrature

- Work through *Logometria* (1714), citing original pages.
- Identify relationships between circular arc, logarithmic measure and the hyperbola without silently introducing Euler's later notation.
- Reconstruct each geometric construction and translate it into modern formulas only **after** the historical reasoning is stated.
- Check any claims that Cotes “discovered Euler's formula” against the expression and branch convention actually published.

## 3. Riemann on transcendentals, not just “Riemann surfaces”

In *Theorie der Abel'schen Functionen* (1857):

- At the very beginning (§1), identify what Riemann says he intends by studying various “Transcendenten”.
- Reproduce his example `log(z − a)` and continuation around `a`; check the stated increase by `2πi` and the orientation convention.
- Draw two paths with the same endpoints, one winding around `a` and one not. Record sheet changes, not only points in the complex plane.
- Read §3's conditions for determining a function, including Dirichlet's principle; name assumptions needed for existence.
- Build the simplest branched cover `w² = z`, then compare with logarithm's infinitely many sheets, then with the Abelian discussion.
- Treat Riemann's later theta-functions paper as a continuation, not a substitute.

## 4. Riemann's 1857 hypergeometric paper

- Starting from his *Beiträge zur Theorie der durch die Gauss'sche Reihe … darstellbaren Functionen*, describe the differential equation, its three regular singular points, and local solution behavior.
- Carry out analytic continuation around each singular point and calculate its effect on a basis of solutions.
- Match any claim in Director Part 64 to an exact place in Riemann's paper. Record mathematical disagreement separately from philosophical disagreement.

## 5. Gauss and Ceres: primary observation data

- Obtain contemporary observations of Ceres attributed to Piazzi and the other astronomers, not modern retellings of Gauss's success.
- Read Gauss's preface to his 1809 *Theoria motus*; distinguish the algorithm printed in the later book from the actual computation performed in 1801.
- Build the orbit from dated observations, then predict an observation **not used** to fit the orbit.
- Compare orbital elements, residuals and missing assumptions with Tennenbaum–Director's 1998 reconstruction.
- Record precisely which data came from an original observation, which were inferred, and which were invented for a pedagogical example.

## 6. What does “transcendental” mean at each date?

Create a dated glossary rather than a retrospective single definition:

| Topic | Primary author | Question |
| --- | --- | --- |
| Curves not obtainable by a stipulated class of algebraic constructions | Leibniz, 1691 | Which operations count as admissible constructions? |
| Logarithmic and angular measurement | Cotes, 1714/1722 | What is being measured, and how are periods treated? |
| Algebraic equations / existence of roots | Gauss, 1799 | What exactly does “algebraic” refer to here? |
| Multivalued complex functions, branch loci, continuation, Abelian periods | Riemann, 1851/1857 | Which properties of a function survive a change of formula or coordinate? |
| Modern transcendental numbers vs algebraic numbers | Later nineteenth-century work | When did that precise meaning become standard? |

See [secondary histories](RECEPTION.md), particularly Blåsjö, Serfati, and Lützen, for checks against a presentist reading.

## Evidence record format

For each comparison save:

```text
historical-claim:
primary-author:
original-title:
publication/year/pages:
facsimile-url:
primary-quotation-and-page:
translation-if-needed:
later-interpreter-and-page:
what-follows-mathematically:
what-remains-unverified:
worked-calculation-or-figure:
```
