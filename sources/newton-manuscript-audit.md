# Newton's ring manuscript: direct image audit and the RMS question

## Primary evidence inspected

The worked table is on **Cambridge University Library, MS Add. 3970, folio 350v**. This identification is confirmed by the library's labelled IIIF manifest and direct page image, not inferred merely from a later caption.

- [Direct manuscript viewer at folio 350v](https://cudl.lib.cam.ac.uk/view/MS-ADD-03970/714).
- [Cambridge IIIF manifest](https://cudl.lib.cam.ac.uk/iiif/MS-ADD-03970).
- [Direct Cambridge image of 350v](https://images.lib.cam.ac.uk/iiif/MS-ADD-03970-003-00678.jp2/full/3000,/0/default.jpg).
- [Preceding folio 350r: propositions](https://images.lib.cam.ac.uk/iiif/MS-ADD-03970-003-00677.jp2/full/3000,/0/default.jpg).
- 350v downloaded JPEG SHA-256: `bcd92da8c5d2309e3e16500d79821526c23cf8644c4bc7b99ea1cdc36ab99bd4`.
- 350r downloaded JPEG SHA-256: `4b4b3e4151703805e872fffa4961bfb8d39073c28cb13881041c111b25d037bc`.

Both sides of folio 350 were visually inspected, with enlarged views of the table and the prose immediately below it. Images of 351r–353v were also retrieved and their page arrangement surveyed, but a full transcription of those pages is not claimed. The image service returned 1613 × 2000-pixel pages despite the requested size; the actual bytes, not the requested dimensions, define this audit's resolution.

The earlier black-and-white reproduction agrees with this page: [reproduction](https://res.cloudinary.com/rzhlimlt/image/upload/v1786918344/asimov-press/clone-1a1fa44c26203aff.png), with [caption and provenance](https://press.asimov.com/articles/lab-notebooks) crediting Alan E. Shapiro, “Newton's Optical Notebooks: Public Versus Private Data,” in *Reworking the Bench* (2003), pp. 43–65. Its SHA-256 is `80872390b0df53568024cb11c302e9670744cc77b7335450871f9fe76583f88c`.

## Findings from the autograph

Folio 350r begins with propositions about the rings' areas and the spaces through which rays pass. Folio 350v contains Experiments 1–3 and further observations. Its table explicitly separates diameters, squared diameters, and differences of squared diameters. Its introductory prose identifies the left-hand figures as sines associated with viewing obliquity, not degrees.

The note immediately below the first table compares the differences with their mean and treats their closeness as support for the first rule. Thus the interpretation as a mean of squared-diameter differences is supported by Newton's own prose, not only by our reconstruction.

The worked row is consistent with the following transcription:

| Ring | Diameter D | D² | Next successive difference |
| ---: | ---: | ---: | ---: |
| 1 | 45 | 2025 | 1819 |
| 2 | 62 | 3844 | 2085 |
| 3 | 77 | 5929 | 1992 |
| 4 | 89 | 7921 | 1880 |
| 5 | 99 | 9801 | — |

**Diplomatic limits:** the first diameter is overwritten, as are several figures elsewhere. The squared values, middle diameters, and difference sequence provide cross-checks, but they do not restore every overwritten stroke. The far-right columns are especially difficult near the binding. The later transcription's mean 1944 and remainder 81 are arithmetically confirmed below; do not claim an equally certain independent visual reading of every summary digit, particularly 81.

A separate first-row entry reads **51⅓**, not the **51⅔** in the discrepant later transcription discussed in our original reconstruction. The direct colour scan supports the one-third reading. It agrees with the displayed 2635 as a whole-number approximation:

    (51⅓)² = 2635⅑,
    (51⅔)² = 2669⁴⁄₉.

This is an image-supported correction to the later transcription, not permission to silently alter the historical record.

## What was computed — and what was not

The arithmetic is

    (1819 + 2085 + 1992 + 1880) / 4 = 1944,
    2025 − 1944 = 81.

No square root occurs in this operation. Nor are those four inputs squared residuals. Calling this operation RMS, root-mean-square error, or a least-squares regression is incorrect.

A further important limitation follows by telescoping:

    average successive difference = (D₅² − D₁²) / 4.

The interior squared diameters cancel from that particular average. They still reveal departures from the proposed progression, but do not affect its endpoint-based average step. Thus “using all the observations” needs a more exact description.

## Why squared diameters are relevant

Newton's published explanation is in *Opticks*, Book II, Part I, Observations V–VI, printed pp. 7–11: [primary text](https://newtonproject.ox.ac.uk/view/texts/normalized/NATP00035). He relates the ring progression to the thickness between a plane and a spherical surface.

Our geometric derivation makes this explicit. For a sphere of radius R and a plane tangent at its lowest point, the gap at ring radius r is

    thickness = R − √(R² − r²) ≈ r²/(2R) = D²/(8R).

Squaring D expresses a physical/geometric hypothesis about film thickness. This is distinct from choosing to square an observation error. The modern interference explanation is not needed to establish what quantity Newton was manipulating.

## Comparison with regression: our calculation, not Newton's

Fitting Dₙ² = intercept + slope × n by ordinary unweighted least squares gives

    intercept = 15.3, slope = 1962.9,
    sum of squared residuals = 15999.9.

The endpoint-based progression 81 + 1944n has squared-residual sum 19977. They are different estimators on the same transformed data. These figures and the two fractional-diameter squares were independently checked using exact rational arithmetic.

If squared-diameter errors were independent with variance σ², consecutive differences would have variance 2σ² and adjacent covariance −σ². Treating differences as independent replicates changes the assumptions. If errors instead have constant variance in diameter, squaring generally produces unequal variances. Geometry alone does not decide regression weights.

## Retrieval correction and completion boundary

The initial archive's eight tiny `.jpg` files were IIIF metadata, not images, and were never used as visual evidence. The retrieval script was corrected to request rendered images and validate their signatures. The subsequent run retrieved actual Cambridge JPEGs for all eight sides; the direct 350r–v inspection above uses those corrected files.

The focused manuscript check underlying our worked numerical example is complete: the page identity, operation, supporting prose, and disputed fraction have been checked against the direct scan. A full diplomatic edition, reconstruction of overwritten states, and certain reading of every far-right digit remain separate tasks. No claim that Newton invented all averaging or regression follows from this audit.
