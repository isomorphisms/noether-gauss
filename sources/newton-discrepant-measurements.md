# Newton, discrepant measurements, and Buchwald's claim

**Question.** Jed Z. Buchwald argues that Newton developed an unusual way of working with inconsistent observations: instead of selecting one supposedly best measurement and discarding the others, he could **combine discrepant measurements, or quantities derived from them, by taking an average**. How does that practice relate to Gauss's later work on observation errors and orbit determination?

## Exact lecture recovered from the account

The [2025-03-19 post](https://x.com/isomorphisms/status/1902308168790618423), selected in @for_gP3's Reposts, links **Jed Buchwald, “How Calculations Invaded the Deep Past”**, published by the Qualcomm Institute: [video](https://youtu.be/l7GoDsDlyMY), [post's original shortlink](https://t.co/5MxBFipl6C).

The linked video's opening transcript was retrieved. Buchwald discusses Newton's handling of discrepant experimental numbers, introduces an early surviving experimental manuscript as an averaging example, and connects this practice to his work with Mordechai Feingold. This is the exact account-derived lecture behind the user's recollection, rather than a guessed substitute from the same speaker.

The post additionally uses the word “regression” and names Huygens/Hooke as comparators. Those details need passage-level checking; the recovered opening does not by itself establish modern regression or the priority claim. The transcript is a finding aid, not a substitute for the manuscript page or a verified numerical reconstruction. See [the account catalog](for-gp3.md).

## Checked calculation and primary wording

The [worked ring reconstruction](newton-rings-1671-reconstruction.md) now reproduces one five-ring series from Buchwald and Feingold's Table 2.1: squared diameters **2025, 3844, 5929, 7921, 9801** give mean successive difference **1944** and first-square mismatch **81**. The CSV and exact-arithmetic script include twelve passing checks. The historical numbers are a **later transcription**, not yet independently verified against Newton's autograph.

A separate primary-text passage is now identified: Newton's **1675 communication**, preserved in Thomas Birch's *History of the Royal Society*, vol. 3 (1757), **p. 262**, describes repeated spectrum observations and “taking means between those differences.” [Newton Project, NATP00002](https://newtonproject.ox.ac.uk/view/texts/diplomatic/NATP00002). This verifies Newton's own report of combining discrepant observations; it does not establish priority or provide the individual spectrum readings.

## What Buchwald actually claims

- In the abstract for his lecture **“The Newtonian Origins of Experimental Error”** (advertised for 2020 by the Niels Bohr Archive), Buchwald contrasts Tycho Brahe, Robert Hooke, René Descartes, and Johannes Hevelius with the young Newton. He says Newton was the first to see that unreliable individual numbers could be combined to produce a better estimate. This is **Buchwald's historical priority claim**, not a priority judgment independently established here. [Niels Bohr Archive lecture announcement](https://nbarchive.ku.dk/nba_calendar/2020/buchwald/).
- In his [NOVA interview, “A Complicated Man”](https://www.pbs.org/wgbh/nova/newton/buchwald.html), Buchwald explains the issue using repeated astronomical measurements: readings of the same position differ; Newton's use of an average was exceptional in the seventeenth and early eighteenth centuries. Buchwald describes Newton as unusually sophisticated at handling numerical data but does **not** claim he invented all prior uses of arithmetic means.
- In the abstract for a [Caltech lecture given November 7, 2007](https://www.caltech.edu/campus-life-events/calendar/isaac-newton-and-the-origins-of-civilization-jed-z-buchwald), Buchwald says Newton applied early procedures for handling discrepant data to ancient chronology. The announcement also cautions that sophisticated calculation can yield error when data are adjusted to fit prior conviction.

The historically specific idea is **combining discrepant observations, or quantities derived from them under a proposed relation, rather than merely selecting one favoured result**. It is **not** a claim that Newton invented arithmetic averaging, modern statistical error theory, or a general rule that every anomalous datum should always be retained unaltered. Nor does averaging by itself resolve systematic errors, different observational reliability, or conflicts between models.

## Buchwald's research: reading order

1. **Jed Z. Buchwald**, “Discrepant Measurements and Experimental Knowledge in the Early Modern Era,” *Archive for History of Exact Sciences* **60** (2006), 565–649. [DOI: 10.1007/s00407-006-0116-6](https://doi.org/10.1007/s00407-006-0116-6). The bibliographic identity has been checked; **the complete paper and its original-source citations have not yet been audited here**.
2. **Jed Z. Buchwald and Mordechai Feingold**, *Newton and the Origin of Civilization* (Princeton University Press, 2013), particularly chapter 1, “Troubled Senses,” pp. 8–43; chapter 2, **“Troubled Numbers,” pp. 44–106**; chapter 8, “Interpreting Words,” pp. 246–306; appendix B, “Newton's Computational Methods,” pp. 441–446; and appendix C, “Commented Extracts from Newton's MS Calculations,” pp. 447–463. [Book](https://doi.org/10.23943/princeton/9780691154787.001.0001); [chapter 2](https://academic.oup.com/princeton-scholarship-online/book/21215/chapter-abstract/180862816); [appendix C](https://academic.oup.com/princeton-scholarship-online/book/21215/chapter-abstract/180883148). The broad page spans were checked against the contents. The ring discussion on pp. 90–93 and Table 2.1 have now been inspected in an accessible text rendering; this is not a visual audit of the printed page or autograph. The other chapters and appendices have not been read in full here.
3. **Buchwald's own account**, [NOVA interview](https://www.pbs.org/wgbh/nova/newton/buchwald.html), and his [2020 lecture description](https://nbarchive.ku.dk/nba_calendar/2020/buchwald/). These are directly accessible statements of his thesis, not Newton's manuscripts.

## Link to Gauss without collapsing the history

The ring example averages **differences of squared diameters**, not repeated readings of one unchanged ring. Its mean telescopes to an endpoint difference; the [worked comparison](newton-rings-1671-reconstruction.md) shows exactly how it differs from a modern least-squares fit. For a more general modern mathematical comparison only:

- The arithmetic mean of measurements `x₁, …, xₙ` is `μ̂ = (x₁ + ⋯ + xₙ)/n`.
- That mean also minimizes `Σᵢ(xᵢ − μ)²` when observations receive equal weights: differentiating the sum gives `−2Σᵢ(xᵢ − μ) = 0`, hence `μ = μ̂`.
- **This modern identity is not evidence that Newton derived least squares.** Averaging transformed differences is not the same estimation problem as fitting the original measurements.
- Least-squares methods for overdetermined systems were published by **Legendre in 1805**; **Gauss's** discussion appeared in *Theoria motus* (1809), where he also claimed prior use. See the [original 1809 edition](https://www.e-rara.ch/zut/content/titleinfo/142787?lang=en) and the [repository's Gauss/Ceres research questions](QUESTIONS.md). Passage-level comparison with Legendre and Gauss remains to be completed.

## Primary-source work still required

1. Inspect **CUL MS Add. 3970, fols. 350–353v**, or Shapiro's manuscript reproduction, and check the numerical transcription against the image. The source chain and one reproduced series are now recorded in the [worked note](newton-rings-1671-reconstruction.md); the complete 2006 article still needs auditing.
2. Locate Newton's **original astronomical chronology calculations** that Buchwald and Feingold analyze, using their appendix C as a finding aid; distinguish ancient source statements, Newton's transformations, and his computed estimates.
3. Compare the original data and output to the alternatives available to Hooke, Hevelius, Tycho, and other contemporaries. In particular, check the scope of the word **“first”** against earlier practices involving averages.
4. Extend the checked five-ring reconstruction to the other series, pressure/lens changes, and water experiments. Preserve every reported input in each series; do not silently repair ambiguous fractions. Sensitivity tests are explicitly synthetic and separate from the historical CSV. **Do not substitute invented pedagogical observations for historical data.**
5. In a separate reconstruction, read Gauss's *Theoria motus* §§175–186 and Legendre's 1805 text; calculate residuals of an overdetermined orbit fit and explicitly separate the 1801 Ceres episode from claims made in Gauss's 1809 publication.

## Evidence status

- **Verified in Newton's own reported wording:** the repeated spectrum observations and taking of means, in the 1675 communication as transmitted by Birch's 1757 edition and the Newton Project.
- **Arithmetically reproduced:** one later-transcribed circa-1671 ring series, including the mean 1944, mismatch 81, and a separate modern least-squares comparison; twelve code checks pass.
- **Not yet independently verified:** the optical table against the autograph, its individual repeated trials, the full set of optical/chronological calculations, and the scope of the historical priority claim.
- **Not claimed:** that Newton used the modern fitted lines printed by our script, that his estimator was probabilistically justified, or that Newton and Gauss solved the same numerical problem.

The bibliographic argument remains in the **reception/history** layer; primary quotations, later transcriptions, and our arithmetic are marked separately. A checked calculation does not establish an uninterrupted historical lineage.
