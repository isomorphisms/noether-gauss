# Newton's ring manuscript: image audit and the RMS question

## Evidence actually inspected

The numerical reconstruction previously relied on a later table transcription. This audit additionally inspects a photograph of Newton's handwritten experimental page, reproduced from Alan E. Shapiro, “Newton's Optical Notebooks: Public Versus Private Data,” in *Reworking the Bench* (2003), pp. 43–65. The repository's manuscript reference is Cambridge University Library, MS Add. 3970, ff. 350–353v.

- [Cambridge manuscript viewer](https://cudl.lib.cam.ac.uk/view/MS-ADD-03970/1).
- [Cambridge IIIF manifest](https://cudl.lib.cam.ac.uk/iiif/MS-ADD-03970).
- [Reproduction and caption identifying Shapiro's source](https://press.asimov.com/articles/lab-notebooks).
- [Photographic reproduction inspected](https://res.cloudinary.com/rzhlimlt/image/upload/v1786918344/asimov-press/clone-1a1fa44c26203aff.png).
- Reproduction SHA-256: `80872390b0df53568024cb11c302e9670744cc77b7335450871f9fe76583f88c`.

The photograph was examined both as a complete page and as an enlarged table. It contains Experiments 1–3 and further notes. Its caption calls it the second page of the coloured-circles manuscript. The exact individual folio of this reproduction is not independently established here; do not silently replace the folio range with a guessed folio.

**Scope:** the five-ring series underlying our worked example, the organization of the table, and the disputed fractional entry in another row. This is not a diplomatic transcription of all eight manuscript sides.

## Findings

The page explicitly organizes measurements as diameters, squares of diameters, and differences between those squares. Its prose discusses sines of viewing obliquities and a mean difference. The left-hand numbers are not degree labels.

The worked row is consistent with the following transcription:

| Ring | Diameter D | D² | Next successive difference |
| ---: | ---: | ---: | ---: |
| 1 | 45 | 2025 | 1819 |
| 2 | 62 | 3844 | 2085 |
| 3 | 77 | 5929 | 1992 |
| 4 | 89 | 7921 | 1880 |
| 5 | 99 | 9801 | — |

Several entries on the page were overwritten. The squared values and central entries are clearer than the first diameter and the far-right summary columns. The later transcription's mean 1944 and remainder 81 are arithmetically confirmed below; the photograph is not sharp enough to claim an independent, equally certain reading of every far-right digit.

A separate first-row entry appears as **51⅓**, not the **51⅔** given in the discrepant later transcription discussed in our original note. This reading agrees with 2635 as a whole-number approximation: (51⅓)² = 2635⅑, whereas (51⅔)² = 2669⁴⁄₉. Preserve this as an image-supported correction with the photograph's resolution qualification, rather than silently rewriting the historical source.

## What was computed — and what was not

The arithmetic is

    (1819 + 2085 + 1992 + 1880) / 4 = 1944,
    2025 − 1944 = 81.

No square root occurs in this operation. Nor are those four inputs squared residuals. Calling this operation RMS, root-mean-square error, or a least-squares regression is incorrect.

There is a further important limitation:

    average successive difference = (D₅² − D₁²) / 4.

The interior squared diameters cancel from that particular average. They still show departures from the proposed progression, but they do not affect its endpoint-based average step. Thus “using all the observations” needs a more exact description.

## Why squared diameters are relevant

Newton's published explanation is in *Opticks*, Book II, Part I, Observations V–VI, printed pp. 7–11: [primary text](https://newtonproject.ox.ac.uk/view/texts/normalized/NATP00035). He relates the ring progression to the thickness between a plane and a spherical surface.

Our geometric derivation makes this explicit. For a sphere of radius R and a plane tangent at its lowest point, the gap at ring radius r is

    thickness = R − √(R² − r²) ≈ r²/(2R) = D²/(8R).

Squaring D therefore expresses a physical/geometric hypothesis about film thickness. This is distinct from choosing to square an observation error. The modern interference explanation is not needed to establish what quantity Newton was manipulating.

## Comparison with regression: our calculation, not Newton's

Fitting Dₙ² = intercept + slope × n by ordinary unweighted least squares gives

    intercept = 15.3, slope = 1962.9,
    sum of squared residuals = 15999.9.

The endpoint-based progression 81 + 1944n has squared-residual sum 19977. They are different estimators of a step, even on the same transformed data.

If the squared-diameter measurement errors were independent with variance σ², their consecutive differences would have variance 2σ² and adjacent covariance −σ². Treating those differences as independent replicates would change the statistical assumptions. If errors instead have constant variance in diameter, squaring introduces a different, generally unequal-variance error model. Geometry alone does not decide the appropriate regression weights.

## Retrieval limitation recorded, not concealed

The initial reading-evidence archive contains eight files named `newton-00-350r.jpg` through `newton-07-353v.jpg`. They are actually 834-byte IIIF metadata responses, not Cambridge page images. Their successful HTTP retrieval is **not image verification**. None supports this audit. The separately retrieved photographic reproduction above does.

The numerical question is resolved at the level of the inspected reproduction and exact arithmetic. A full autograph transcription and a sharper reading of the overwritten and far-right entries remain open. Neither this page nor the published passage establishes a claim that Newton invented all averaging or regression.
