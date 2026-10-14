# Noether–Gauss

A reading and reconstruction project on the mathematics and history surrounding Gauss, Riemann, and related work. Start with the sources; distinguish what an author actually wrote from later interpretations.

## Reading

- **[How Gauss Determined the Orbit of Ceres](https://archive.schillerinstitute.com/fid_97-01/982_Gauss_Ceres.html)** — Jonathan Tennenbaum **and Bruce Director**, *Fidelio*, Summer 1998. The publisher's page links the full PDF and individual chapters.
- **[Riemann for Anti-Dummies — Bruce Director](sources/riemann-for-anti-dummies.md)** — series archive, selected individual installments, and a Gauss/Riemann reading trail.
- **[Newton and discrepant measurements — Jed Buchwald](sources/newton-discrepant-measurements.md)** — evidence for Newton's unusual averaging of conflicting observations, with an explicit distinction from Gauss's later error theory and a primary-manuscript verification plan.

## Account-derived reading

- [@for_gP3 source catalog](sources/for-gp3.md): the actual Ceres, Cotes, Leibniz, Riemann, Buchwald, and Noether posts, plus related history and geometry. Retrieved 114 visible repost targets; original-post dates, source identities, edition mismatches, image-only leads, and missing thread context are distinguished.
- [Complete 114-post URL inventory](sources/for-gp3-inventory.tsv): original permalinks and exposed outbound links, in collection order.

## Working rules

- Keep author, title, date (when established), URL, and the distinction between a contemporaneous source, a later interpretation, and our own reconstruction.
- Use Director and Tennenbaum as *sources to investigate*, not as substitutes for Gauss's and Riemann's papers.
- Reproduce mathematical constructions and calculations independently; record discrepancies rather than silently correcting an author's claims.

## Primary papers: Leibniz → Cotes → Gauss → Riemann

- [Primary-source catalog](sources/PRIMARY.md): original 1684/1686/1691 *Acta Eruditorum* volumes (including Leibniz's catenary papers), Cotes's 1714 *Logometria* and 1722 *Harmonia mensurarum*, Gauss's 1799 dissertation and 1809 *Theoria motus*, and Riemann's 1851/1857 papers. **Actual original-edition facsimile links** are distinguished from later modern re-typesettings.
- [Director/Tennenbaum/LYM citation trail and books](sources/RECEPTION.md): identifies which original papers to compare, modern historical scholarship by Viktor Blåsjö, Michel Serfati, and Jesper Lützen, and what citation claims still need page-level checking.
- [Mathematical reconstruction questions](sources/QUESTIONS.md): catenary/logarithms; Cotes and angle; Riemann's `log(z − a)`, branches and Abelian functions; hypergeometric monodromy; Ceres observation data.
- [PDF download manifest](sources/downloads.tsv) and [fetch-primary.sh](scripts/fetch-primary.sh): reproducible access to full original scans and labelled transcriptions. From the repository root: `bash scripts/fetch-primary.sh core` (includes the ~87 MB 1691 volume), or `bash scripts/fetch-primary.sh all` for the larger corpus. PDF bytes are **not presently committed** to the repository; the script downloads them to `papers/`, validates the PDF header, and writes checksums.

**Source priority:** original pages > critical/collected editions > modern transcriptions/translations > Director/Tennenbaum essays. The last category is useful for finding questions, not proof of historical facts. In Riemann's 1857 *Theorie der Abel'schen Functionen*, the opening sections directly treat “Transcendenten”, branches of `log(z − a)`, and continuation on multi-sheeted surfaces.
