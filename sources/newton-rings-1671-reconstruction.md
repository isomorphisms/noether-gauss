# Newton's ring measurements: an exact reconstruction

**Result:** one reported five-ring series reproduces Newton's mean difference **1944** and first-square mismatch **81** exactly. A modern calculation also shows that this particular mean of successive differences telescopes: its value depends only on the two endpoint squares. The intermediate measurements still reveal departures from the proposed progression.

**Evidence level:** the numbers below come from a later published transcription of Newton's table, not an independently inspected autograph. The calculation is checked; the manuscript transcription is not yet independently checked. Do not describe this as recovery of his original repeated trial readings.

## 1. Source chain

The working numerical source is **Jed Z. Buchwald and Mordechai Feingold, _Newton and the Origin of Civilization_ (2013), chapter 2, pp. 90–92, Table 2.1 on p. 91** ([book DOI](https://doi.org/10.23943/princeton/9780691154787.001.0001); [accessed text rendering](https://dokumen.pub/newton-and-the-origin-of-civilization-course-booknbsped-9781400845187.html)). Their notes identify:

- **Cambridge University Library, MS Add. 3970, fols. 350–353v**, the circa-1671 experiments. [Cambridge item](https://cudl.lib.cam.ac.uk/view/MS-ADD-03970/1). This item link is not a verified mapping to the particular table image.
- **Richard S. Westfall**, “Isaac Newton's coloured circles twixt two contiguous glasses,” _Archive for History of Exact Sciences_ 2, 181–196, especially the primary-text transcription on pp. 191–196 and table on p. 192. [DOI](https://doi.org/10.1007/BF00327404). The book cites this as 1965; catalogue records also give 1964. The issue imprint has not been checked here.
- **Alan E. Shapiro**, “Newton's Optical Notebooks: Public Versus Private Data,” in _Reworking the Bench_ (2003), pp. 43–65, especially table p. 48, manuscript reproduction p. 49, and note 12 on p. 63. [Publisher](https://link.springer.com/chapter/10.1007/0-306-48152-9_3). These page locations are supplied by Buchwald and Feingold; the pages themselves remain to be inspected.

The book distinguishes final recorded diameter values from unpreserved individual repeat readings. Its account describes measuring dark-ring diameters, squaring them, averaging their successive differences, and comparing that mean with the first square. It does not establish that every recorded diameter was itself an average of repeats. The exact angular label for this series is not assigned here: the accessible table text has a scrambled column order. Identify it instead by its five diameters, beginning with **45**.

## 2. Historical numerical input

[Machine-readable data](../data/newton-rings-1671.csv).

| Ring number | Diameter, in hundredths of an inch | Recorded square | Recorded difference to the next square |
| --- | ---: | ---: | ---: |
| 1 | 45 | 2025 | 1819 |
| 2 | 62 | 3844 | 2085 |
| 3 | 77 | 5929 | 1992 |
| 4 | 89 | 7921 | 1880 |
| 5 | 99 | 9801 | Not recorded: no sixth value in this series |

Squares and their differences are in units of **1/10000 square inch**, not inches. None of these five reported diameter values has been discarded. This is one series, not the entire five-series table and not a log of every experimental trial.

Other series in the accessible table rendering contain fractional diameters and rounding. In particular, an apparent `51 2/3` paired with square `2635` requires visual checking: these are not arithmetically consistent, whereas `(51 1/3)^2 = 2635 1/9`. **Do not silently substitute the latter or attribute the mismatch to Newton.** It could arise in the manuscript, edition, or text extraction.

## 3. Reproducing the recorded operations

The successive differences are unequal:

```text
3844 − 2025 = 1819
5929 − 3844 = 2085
7921 − 5929 = 1992
9801 − 7921 = 1880
```

Their arithmetic mean is

```text
(1819 + 2085 + 1992 + 1880) ÷ 4 = 7776 ÷ 4 = 1944.
```

The first square exceeds this mean by

```text
2025 − 1944 = 81.
```

Both results match the table's reported mean and mismatch. The differences depart from their mean by **−125, +141, +48, −64**. Averaging has not made their disagreement disappear.

**Historical boundary:** the supported operation is calculating the mean and the mismatch. The endpoint line below is our mathematical reconstruction; this note does not claim that Newton explicitly fitted that line or subtracted 81 from every square.

## 4. A modern consequence: the mean telescopes

Let `squareₙ` denote the squared diameter of ring `n`, and let `number_of_rings` be the number observed. Then

```text
mean_difference
  = Σₙ(squareₙ₊₁ − squareₙ) ÷ (number_of_rings − 1)
  = (last_square − first_square) ÷ (number_of_rings − 1).
```

Here that is `(9801 − 2025) ÷ 4 = 1944`.

Consequently, altering an intermediate square can change two adjacent differences but leave their average unchanged. The intervening measurements matter for checking the progression, even though their contributions to this particular scalar estimate cancel.

For a numerical comparison, define the endpoint line

```text
predicted_squareₙ = 81 + 1944 × n.
```

Its residuals, `recorded_square − predicted_square`, are **0, −125, +16, +64, 0**. The zero endpoint residuals follow from the construction; they are not independent confirmation of the law.

## 5. Compare with least squares, without attributing it to Newton

A modern equal-weight fit minimizes

```text
Σₙ(recorded_squareₙ − offset − spacing × n)².
```

Exact arithmetic gives

```text
offset = 153/10 = 15.3
spacing = 19629/10 = 1962.9
```

The sum of squared residuals is **15999.9**, compared with **19977** for the endpoint line. These sums have units of the square of our squared-diameter unit. They are descriptive comparisons, not confidence statements or independent experimental validation.

Equal weighting here is a choice about errors in **squared diameter**. Equal errors in measured diameter do not automatically imply equal errors after squaring. No probability distribution or known instrument precision has been inferred from these five numbers.

This gives a precise question for the later Gauss comparison: **which discrepancies remain in the estimate, which cancel, and what error assumptions justify the weighting?** It does not establish a historical transmission of the method from Newton to Gauss.

## 6. Newton's own account supplies separate evidence

Newton's **1675 communication**, preserved in **Thomas Birch's _History of the Royal Society_, vol. 3 (1757), p. 262**, explicitly describes repeated spectrum-marking observations and “taking means between those differences.” [Newton Project diplomatic transcription, NATP00002](https://newtonproject.ox.ac.uk/view/texts/diplomatic/NATP00002).

He explains that the assistant had better colour discrimination and had not been told his ideas; the observations were repeated within and across days. This is Newton's own description, transmitted through Birch's edition—not Buchwald's paraphrase and not a newly inspected 1675 autograph. The passage supplies no list of trial values, so it cannot independently supply another numerical reconstruction.

Compare **_Opticks_ (1704), Book I, Part II, Proposition III, Experiment VII, p. 92**: repeated observations and agreement remain in the presentation, but that paragraph does not repeat the explicit phrase about taking means. [NATP00034](https://newtonproject.ox.ac.uk/view/texts/normalized/NATP00034).

Also compare **Book II, Part I, Observations V–VI, pp. 7–10**. Newton reports repeated ring measurements and revisits measurements after considering pressure and lens shape. His published discussion therefore does not support a blanket claim that he concealed all discrepancies or simply averaged every defective experiment. [NATP00035](https://newtonproject.ox.ac.uk/view/texts/normalized/NATP00035).

## 7. Run and check

From the repository root:

```sh
python3 scripts/reconstruct-newton-rings.py --check
```

The standard-library script reads the CSV relative to its own location, preserves the input, and uses exact rational arithmetic. **Twelve checks passed** in the working environment: reported values, differences, mean/mismatch, both lines' residuals, least-squares normal equations, sums of squares, invalid short inputs, and three deliberately synthetic sensitivity checks.

Those sensitivity checks are not historical measurements:

- Add 100 to the second squared diameter: the mean difference stays 1944; the modern least-squares slope changes to 1952.9.
- Add 100 to every squared diameter: the mean difference stays 1944; the first-square mismatch becomes 181.
- Add one hundredth of an inch to every diameter before squaring: the mean difference becomes 1971. A systematic diameter offset does **not** cancel.

Passing these checks verifies the arithmetic and code against the supplied transcription. It does not verify that the transcription matches Newton's handwriting, nor independently reproduce his physical experiment.

## Remaining source work

Inspect the autograph or Shapiro's manuscript reproduction; confirm this series and its viewing-angle label; transcribe the remaining series without silently fixing apparent errors; recover the subsequent lens/water comparisons; and test the scope of Buchwald's priority claim against earlier observers. The existing source trail for Newton's later astronomical calculations remains a separate project.
