# Leibniz's 1691 catenary: printed construction vs private calculation

**Status (2026-10-13):** a first reconstruction from a located original 1691 *Acta Eruditorum* **facsimile catalog**, the entire Beaudry 2001 **translated article**, the Leibniz-Akademie-Ausgabe **primary correspondence**, and Raugh–Probst's 2019 research using Leibniz's handwritten calculations. The archived *Acta* volume was catalogued but its 87 MB PDF was **not retrieved and viewed page-by-page during this audit**. Do not call the translated English text itself an original facsimile.

## Source chain, in chronological order

### 1. Original journal publications — 1691

- Gottfried Wilhelm Leibniz, *De linea in quam flexile se pondere proprio curvat, ejusque usu insigni ad inveniendas quotcunque medias proportionales et logarithmos*, *Acta Eruditorum* **June 1691**, pp. **277–281** (especially associated with engraved **Plate VII**). Latin.
- Leibniz, *De solutionibus problematis catenarii vel funicularis in Actis Junii A. 1691, aliisque a Dn. J. Bernoullio propositis*, *Acta Eruditorum* **September 1691**, pp. **435–439**. Latin.
- [The entire 1691 journal, contemporary facsimile, 636 pages, 87.09 MB](https://commons.wikimedia.org/wiki/File:Acta_eruditorum._1691_(IA_s1id13206570).pdf) ([direct original PDF](https://archive.org/download/s1id13206570/s1id13206570.pdf)). **Printed page numbers are not PDF image indices.**
- Closely related other papers **in the same June issue** that should also be read: Johann Bernoulli, *Solutio problematis funicularii*, pp. **274–276**; Huygens, *Christiani Hugenii … solutio ejusdem problematis*, pp. **281–282**; Jakob Bernoulli, *Specimen alterum calculi differentialis … spirali … logarithmica …*, pp. **282–290**. These are independently published competing/contemporaneous constructions, not parts of Leibniz's paper.
- Source checks for the bibliographic page numbers: [Leibniz correspondence scholarly edition](https://www.gwlb.de/leibniz/digitale-ressourcen/repositorium-des-leibniz-archivs/laa-bd-iii-5) and [2019 historical analysis by Raugh and Probst](https://www.sciencedirect.com/science/article/pii/S0315086018301290).

### 2. Important primary correspondence and original unpublished derivation — June/August 1691

**This correspondence should not be left out of the primary corpus.** The printed 1691 June article gives a Euclidean-geometric *construction* but does not print the complete procedure that led Leibniz to it.

In the authoritative **Leibniz-Akademie-Ausgabe**, Series III, vol. 5, *Mathematischer, naturwissenschaftlicher und technischer Briefwechsel, 1691–1693* (H.-J. Heß and James G. O'Hara, eds., Akademie Verlag, 2003):

- **No. 24, pp. 118 ff.:** Leibniz to Rudolf Christian von Bodenhausen, **12/22 June 1691**. His own explanation explicitly reports that he **withheld the constant proportion** from the published construction, and gives ordinates in proportion **0.3678794 : 1.0000000 : 2.7182818**. In modern notation, these approximate `e⁻¹ : 1 : e`.
- **No. 33, pp. 143 ff.:** Leibniz to von Bodenhausen, **10/20 August 1691**.
- **No. 34, p. 154 ff.:** Leibniz's attached Latin derivation, *Analysis problematis catenarii*. This is a **primary manuscript transmitted with correspondence**, not an additional *Acta Eruditorum* article.

[Official repository/edition information and downloads, Leibniz-Archiv](https://www.gwlb.de/leibniz/digitale-ressourcen/repositorium-des-leibniz-archivs/laa-bd-iii-5); [hosted edition PDF (series III, volume 5, part A)](https://rep.adw-goe.de/bitstream/handle/11858/2441/III5A.pdf).

**Rights/provenance:** this is a 2003 scholarly edition of seventeenth-century correspondence, released by the host under **CC BY-NC 4.0**, not an unrestricted original printed journal. Cite its editorial page and letter number; do not silently reproduce the entire modern edition.

### 3. Modern translated article in the Director/LYM orbit — 2001

[Pierre Beaudry, “G. W. Leibniz: Two Papers on the Catenary Curve and Logarithmic Curve,” *Fidelio* X/1 (Spring 2001)](https://archive.schillerinstitute.com/fid_97-01/011_catenary.html).

**Important provenance qualification:** Beaudry states in his own introductory note that he translated **from Marc Parmentier's 1989 French translation** and consulted the Latin in **Gerhardt's collected writings**. This is a modern **translation of a translation with comparison**, not a direct facsimile of *Acta Eruditorum* and not an English manuscript by Leibniz. The philosophical introduction and translator's footnotes are **Beaudry's**, not Leibniz's.

The translated June paper's first substantive sections make these concrete constructions:

- Set equal horizontal steps and build ordinates in a **geometric progression**: a logarithmic/exponential curve.
- Take the **arithmetic mean of the corresponding ordinates** on the two sides to obtain points on the catenary.
- Invert the construction: use the physical catenary to recover proportional means and logarithmic quantities.
- Express arc length and some enclosed areas through the same geometrical construction.

The September paper refers back to the June paper, compares Huygens and the Bernoullis, and explicitly links the chain problem to **logarithms**, quadrature of the hyperbola, tangency, rectification and construction of transcendental curves.

### 4. Modern independent research from Leibniz's surviving worksheets — 2019

**Michael Raugh and Siegmund Probst**, [*The Leibniz catenary and approximation of e — an analysis of his unpublished calculations*](https://www.sciencedirect.com/science/article/pii/S0315086018301290), *Historia Mathematica* **49** (November 2019), pp. **1–19**, DOI [10.1016/j.hm.2019.06.001](https://doi.org/10.1016/j.hm.2019.06.001). This journal article is open access, but still distinguishes editorial transcription from Leibniz's handwritten manuscripts.

Their relevant independent observations:

- The 1691 printed geometric construction **does not disclose the full discovering calculation**.
- The published catenary construction depends on a specific, nonarbitrary ratio corresponding to the constant now called `e`.
- In Leibniz's **letter** the approximate number `2.7182818` appears explicitly.
- Further **unpublished handwritten worksheets** at the Gottfried Wilhelm Leibniz Bibliothek in Hannover show how Leibniz calculated that number. Their paper reports a stronger approximation derivable from his arithmetic than the number he copied in his letter.
- The journal article's Figure 1 caption points out that the asserted arc-length/line-segment equality requires a specific scale in the logarithmic ordinates. **A freely chosen geometric ratio alone is insufficient.**

This finding materially changes how to read the 1691 publication and Beaudry's introduction. It also gives direct original-data leads: the correspondence numbers, archive folios (including **LH 35, 6, 8, fols. 3–4** for a draft construction), and actual handwritten calculation sheets.

## A modern mathematical reconstruction to test against the figures

The following formulas are **ours in modern notation**, not a claim about equations Leibniz printed. Take `a > 0`, midpoint `x₀`, and coordinate `t = (x − x₀)/a`. Define two exponential ordinates

```math
g₊(x) = a eᵗ,    g₋(x) = a e⁻ᵗ.
```

Their arithmetic mean is the catenary

```math
y(x) = [g₊(x) + g₋(x)]/2 = a cosh((x−x₀)/a).
```

For equally spaced values `xₙ = x₀ + nh`, this yields the **actual geometric progression** and mean

```math
q = e^{h/a},
g₊(xₙ) = a qⁿ,
g₋(xₙ) = a q⁻ⁿ,
y(xₙ) = a(qⁿ + q⁻ⁿ)/2.
```

These are **scalar ordinates** at successive points; the vector of point coordinates, if assembled, belongs in an actual `(N,2)` vector/matrix representation, not an implicit list named “vector.”

### Why the suppressed constant matters

Choosing an arbitrary fixed progression ratio `q > 0` instead would produce

```math
y(x) = a cosh((x−x₀)log(q)/h).
```

This is some rescaled hyperbolic cosine, but it is the **physical catenary with vertex height/parameter a** only if `log(q)/h = 1/a` (up to sign). For one horizontal unit step `h=a`, the required ratio is **`q=e`**. That reconciles the letters' explicit numerical ratio with the modern equation.

The derivatives and integral checks are

```math
y′(x) = sinh(t),
sqrt(1 + y′(x)²) = cosh(t),
s(x) = ∫_{x₀}^x sqrt(1+y′²)du = a sinh(t),
∫_{x₀}^x y(u)du = a² sinh(t) = a s(x).
```

With oriented integrals on the left side, signs follow the integration orientation. This gives a **falsifiable** test for the printed geometric arc-length and area claims, once Plate VII and its labeled lengths are transcribed.

For `h=a`, point ordinates `yₙ/a` are `(eⁿ+e⁻ⁿ)/2`, so at `n=0,1,2` they are approximately `1, 1.543081, 3.762196`. Check numerical accuracy without guessing the original drawing's scale.

## What remains to verify before declaring an exhaustive comparison

1. Read the *Acta Eruditorum* **Plate VII** (June 1691) at original image resolution, align every label with the published Latin—not just Beaudry's modern rendering.
2. Read the full **letter No. 33 + attachment No. 34** and the original **letter No. 24** in the scholarly edition; the present identification is verified by the edition's searchable content and Raugh–Probst's cited locations, but full text/diagrams have not been checked here.
3. Locate the Hannover worksheets described by Raugh–Probst and log stable manuscript shelfmarks, images if public, and the actual arithmetic of `e`.
4. Work the construction with *non*-unit ratios in a small exact experiment, preserving dimensional parameters, and compare with manuscript and original print.
5. Keep the mathematical comparison **separate** from Beaudry's political/philosophical introduction.

**Most important preliminary result:** Leibniz's *printed* 1691 article is not the whole mathematical record. His **1691 letters and attached analysis** and surviving private arithmetic are indispensable to any study of what he actually understood about the transcendental/exponential curve.
