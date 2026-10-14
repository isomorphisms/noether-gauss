# Noether–Gauss

A reading and reconstruction project on the mathematics and history surrounding Gauss, Riemann, and related work. Start with the sources; distinguish what an author actually wrote from later interpretations.

**Working question, not an adopted position:** do the accounts of action, physical constraints, and global function theory change our understanding of linear regression? Considering these claims does not mean endorsing them. Distinguish the choice of an admissible physical model from the adjustment of that model to imperfect observations.

## Topic-focused readings

| Reading | What has actually been examined |
| --- | --- |
| [Gauss: Theoria motus](sources/gauss-theoria-motus.md) | Complete original and English-edition links; the preface, physical assumptions, and §§175–181 on probability and least squares, with a modern derivation. |
| [Chris Quigg: A Century of Noether's Theorem](sources/quigg-noether.md) | Full article text read and summarized for the symmetry/action question. [Official Fermilab lecture page, video and slides](https://events.fnal.gov/colloquium/events/event/quigg-colloq-2018/). The recording itself has not been watched. |
| [Leibniz, Riemann, and Director: action and regression](sources/action-regression-reading-notes.md) | Source-specific summaries, stated reading coverage, the actual Part 63 pairwise claim, a catenary derivation, Riemann's quadratic functional, and counterexamples separating local terms from global dependence. |
| [Ceres and regression](sources/ceres-and-regression.md) | Selected passages from Tennenbaum and Director on lines of sight, physical constraints, numerical sensitivity, and successive correction. Not a claim to have reproduced the entire orbit calculation. |
| [Newton manuscript image audit](sources/newton-manuscript-audit.md) | The worked five-ring series compared with a photographic manuscript reproduction; RMS distinguished from averaging differences of squared diameters. Overwriting and uncertain far-right digits are recorded. |

These notes are not claims to have read every linked book. Cotes's complete *Logometria*, Buchwald's complete 2006 article, the whole Ceres essay, and the remainder of Director's series still need their own completed readings. The Newton audit is a focused image check, not a full diplomatic transcription of the manuscript.

## Reading catalog

- **[How Gauss Determined the Orbit of Ceres](https://archive.schillerinstitute.com/fid_97-01/982_Gauss_Ceres.html)** — Jonathan Tennenbaum **and Bruce Director**, *Fidelio*, Summer 1998. The publisher's page links the full PDF and individual chapters.
- **[Riemann for Anti-Dummies — Bruce Director](sources/riemann-for-anti-dummies.md)** — series archive, selected individual installments, and a Gauss/Riemann reading trail.
- **[Newton and discrepant measurements — Jed Buchwald](sources/newton-discrepant-measurements.md)** — historical source trail, the account-derived lecture, and Newton's own description of taking means.
- **[Worked Newton ring series](sources/newton-rings-1671-reconstruction.md)** — historical numerical input, exact arithmetic, and a modern least-squares comparison. Read with the subsequent [image audit and qualifications](sources/newton-manuscript-audit.md), which supersede the earlier unaudited status for the inspected portion.

## Account-derived reading

- [@for_gP3 source catalog](sources/for-gp3.md): the actual Ceres, Cotes, Leibniz, Riemann, Buchwald, and Noether posts, plus related history and geometry. Retrieved 114 visible repost targets; original-post dates, source identities, edition mismatches, image-only leads, and missing thread context are distinguished.
- [Complete 114-post URL inventory](sources/for-gp3-inventory.tsv): original permalinks and exposed outbound links, in collection order.

## Working rules

- Keep author, title, date (when established), URL, and the distinction between a contemporaneous source, a later interpretation, and our own reconstruction.
- Use Director and Tennenbaum as sources to investigate, not substitutes for Gauss's and Riemann's papers. Do not ascribe a modern introduction's claims to a historical author.
- Reproduce mathematical constructions and calculations independently; record discrepancies rather than silently correcting an author's claims. State the actual reading and verification coverage.

## Primary papers: Leibniz → Cotes → Gauss → Riemann

- [Primary-source catalog](sources/PRIMARY.md): original 1684/1686/1691 *Acta Eruditorum* volumes, Cotes's 1714 *Logometria* and 1722 *Harmonia mensurarum*, Gauss's 1799 dissertation and 1809 *Theoria motus*, and Riemann's 1851/1857 papers. Original-edition facsimiles are distinguished from modern re-typesettings.
- [Director/Tennenbaum/LYM citation trail and books](sources/RECEPTION.md): original papers to compare, scholarship by Viktor Blåsjö, Michel Serfati, and Jesper Lützen, and claims still needing page-level checking.
- [Mathematical reconstruction questions](sources/QUESTIONS.md): catenary/logarithms; Cotes and angle; Riemann's `log(z − a)`, branches and Abelian functions; hypergeometric monodromy; Ceres observations.
- [PDF download manifest](sources/downloads.tsv) and [fetch-primary.sh](scripts/fetch-primary.sh): complete editions accessible from the repository. From its root, run `bash scripts/fetch-primary.sh core`, or `bash scripts/fetch-primary.sh all` for the larger corpus. PDF bytes are not committed; the script downloads them to `papers/`, validates the PDF header, and writes checksums. The Gauss reading note records checksums of the complete editions actually retrieved.

**Source priority:** original pages > critical/collected editions > modern transcriptions/translations > later interpretive essays. Later essays can supply questions without establishing their historical or philosophical conclusions.


## Original-page and manuscript audits

- [Cotes, *Logometria* (1714)](sources/cotes-logometria-primary-audit.md): **original page images** show logarithms as measures of ratios (p. 6), logistic curve (p. 27), hyperbola quadrature (p. 29), and **the logarithm/circular-arc relation using √−1 (p. 32)**. The same material was reprinted as Part I of *Harmonia mensurarum* (1722), with **p. 32 of 1714 corresponding to Part I p. 28 of 1722**.
- [Leibniz's catenary (1691)](sources/leibniz-catenary-primary-audit.md): original Latin print, *Leibniz-Akademie-Ausgabe* letters to von Bodenhausen, unpublished catenary analysis, and the hidden exponential ratio approximating **e**; includes a modern derivation with its scaling assumptions.
- [Riemann's Dirichlet principle vs Director's interpretation](sources/director-riemann-dirichlet-audit.md): source-by-source §1/§3 notes, Weierstrass's existence criticism, Schwarz's subsequent constructive work and a worked counterexample showing **infimum ≠ attained minimum**.

**Work still open:** the complete original PDF scans have not been checked into Git; the full Latin journal pages (including Leibniz's Plate VII), the original *Harmonia mensurarum* argument, and an exhaustive, line-by-line Director/LYM citation concordance remain to be completed. See the individual audit status statements.
