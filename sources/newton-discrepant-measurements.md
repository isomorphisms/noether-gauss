# Newton, discrepant measurements, and Buchwald's claim

**Question.** Jed Z. Buchwald argues that Newton developed an unusual way of working with inconsistent observations: instead of selecting one supposedly best measurement and discarding the others, he could **combine multiple individually unreliable measurements by taking an average**. How does that practice relate to Gauss's later work on observation errors and orbit determination?

## Exact lecture recovered from the account

The [2025-03-19 post](https://x.com/isomorphisms/status/1902308168790618423), selected in @for_gP3's Reposts, links **Jed Buchwald, “How Calculations Invaded the Deep Past”**, published by the Qualcomm Institute: [video](https://youtu.be/l7GoDsDlyMY), [post's original shortlink](https://t.co/5MxBFipl6C).

The linked video's opening transcript was retrieved. Buchwald discusses Newton's handling of discrepant experimental numbers, introduces an early surviving experimental manuscript as an averaging example, and connects this practice to his work with Mordechai Feingold. This is the exact account-derived lecture behind the user's recollection, rather than a guessed substitute from the same speaker.

The post additionally uses the word “regression” and names Huygens/Hooke as comparators. Those details need passage-level checking; the recovered opening does not by itself establish modern regression or the priority claim. The transcript is a finding aid, not a substitute for the manuscript page or a verified numerical reconstruction. See [the account catalog](for-gp3.md).

## What Buchwald actually claims

- In the abstract for his lecture **“The Newtonian Origins of Experimental Error”** (advertised for 2020 by the Niels Bohr Archive), Buchwald contrasts Tycho Brahe, Robert Hooke, René Descartes, and Johannes Hevelius with the young Newton. He says Newton was the first to see that unreliable individual numbers could be combined to produce a better estimate. This is **Buchwald's historical priority claim**, not a priority judgment independently established here. [Niels Bohr Archive lecture announcement](https://nbarchive.ku.dk/nba_calendar/2020/buchwald/).
- In his [NOVA interview, “A Complicated Man”](https://www.pbs.org/wgbh/nova/newton/buchwald.html), Buchwald explains the issue using repeated astronomical measurements: readings of the same position differ; Newton's use of an average was exceptional in the seventeenth and early eighteenth centuries. Buchwald describes Newton as unusually sophisticated at handling numerical data but does **not** claim he invented all prior uses of arithmetic means.
- In the abstract for a [Caltech lecture given November 7, 2007](https://www.caltech.edu/campus-life-events/calendar/isaac-newton-and-the-origins-of-civilization-jed-z-buchwald), Buchwald says Newton applied early procedures for handling discrepant data to ancient chronology. The announcement also cautions that sophisticated calculation can yield error when data are adjusted to fit prior conviction.

The historically specific idea is **retaining multiple observations of the same quantity and allowing their discrepancies to inform a combined estimate**. It is **not** a claim that Newton invented arithmetic averaging, modern statistical error theory, or a general rule that every anomalous datum should always be retained unaltered. Nor does averaging by itself resolve systematic errors, different observational reliability, or conflicts between models.

## Buchwald's research: reading order

1. **Jed Z. Buchwald**, “Discrepant Measurements and Experimental Knowledge in the Early Modern Era,” *Archive for History of Exact Sciences* **60** (2006), 565–649. [DOI: 10.1007/s00407-006-0116-6](https://doi.org/10.1007/s00407-006-0116-6). The bibliographic identity has been checked; **the complete paper and its original-source citations have not yet been audited here**.
2. **Jed Z. Buchwald and Mordechai Feingold**, *Newton and the Origin of Civilization* (Princeton University Press, 2013), particularly chapter 1, “Troubled Senses,” pp. 8–43; chapter 2, **“Troubled Numbers,” pp. 44–106**; chapter 8, “Interpreting Words,” pp. 246–306; appendix B, “Newton's Computational Methods,” pp. 441–446; and appendix C, “Commented Extracts from Newton's MS Calculations,” pp. 447–463. [Book](https://doi.org/10.23943/princeton/9780691154787.001.0001); [chapter 2](https://academic.oup.com/princeton-scholarship-online/book/21215/chapter-abstract/180862816); [appendix C](https://academic.oup.com/princeton-scholarship-online/book/21215/chapter-abstract/180883148). The page spans and scope are verified from the published table of contents, **not** from an inspection of each page.
3. **Buchwald's own account**, [NOVA interview](https://www.pbs.org/wgbh/nova/newton/buchwald.html), and his [2020 lecture description](https://nbarchive.ku.dk/nba_calendar/2020/buchwald/). These are directly accessible statements of his thesis, not Newton's manuscripts.

## Link to Gauss without collapsing the history

Newton's early method of combining repeated measures of **one quantity** is conceptually different from estimating several parameters of an orbital model from numerous observations. For a modern mathematical comparison only,

- The arithmetic mean of measurements `x₁, …, xₙ` is `μ̂ = (x₁ + ⋯ + xₙ)/n`.
- That mean also minimizes `Σᵢ(xᵢ − μ)²` when observations receive equal weights: differentiating the sum gives `−2Σᵢ(xᵢ − μ) = 0`, hence `μ = μ̂`.
- **This modern identity is not evidence that Newton derived least squares.** It supplies one exact point of comparison with the later mathematical theory of errors.
- Least-squares methods for overdetermined systems were published by **Legendre in 1805**; **Gauss's** discussion appeared in *Theoria motus* (1809), where he also claimed prior use. See the [original 1809 edition](https://www.e-rara.ch/zut/content/titleinfo/142787?lang=en) and the [repository's Gauss/Ceres research questions](QUESTIONS.md). Passage-level comparison with Legendre and Gauss remains to be completed.

## Primary-source work still required

1. Find the **specific Newton optical notebooks, observation tables, and calculations** on which Buchwald's 2006 article bases its argument. Transcribe dates, measured values, selection/weighting, and the exact numerical steps before describing the calculation as averaging.
2. Locate Newton's **original astronomical chronology calculations** that Buchwald and Feingold analyze, using their appendix C as a finding aid; distinguish ancient source statements, Newton's transformations, and his computed estimates.
3. Compare the original data and output to the alternatives available to Hooke, Hevelius, Tycho, and other contemporaries. In particular, check the scope of the word **“first”** against earlier practices involving averages.
4. Reproduce one actual Newton data reduction with *all* documented inputs and a separate tabulation of discrepancies. Test sensitivity to a shifted datum, a systematic offset, and different weights. **Do not substitute invented pedagogical observations for historical data.**
5. In a separate reconstruction, read Gauss's *Theoria motus* §§175–186 and Legendre's 1805 text; calculate residuals of an overdetermined orbit fit and explicitly separate the 1801 Ceres episode from claims made in Gauss's 1809 publication.

## Evidence status

- **Verified:** Buchwald stated the historical interpretation; the lecture/interview pages and scholarly publications can be identified.
- **Not yet verified from Newton's own pages:** which observations Newton retained, the exact arithmetic, and how broadly Buchwald's priority claim holds.
- **Not claimed:** that Newton's method was a modern probabilistic estimator or that Newton and Gauss solved the same numerical problem.

Keep this note in the **reception/history** layer until Newton's numerical manuscripts are checked. The methodological contrast is a research question to test, not an established uninterrupted historical lineage.
