# Gauss and Ceres: first source notebook

Research date: 2026-10-13. Initial notes, not a completed historical reconstruction.

## Starting text

Jonathan Tennenbaum and Bruce Director, **How Gauss Determined the Orbit of Ceres**, *Fidelio*, vol. VII, no. 2, Summer 1998.

- [Publisher's landing page](https://archive.schillerinstitute.com/fid_97-01/982_Gauss_Ceres.html)
- [Complete article](https://archive.schillerinstitute.com/fid_97-01/982_orbit_ceres.pdf)
- [Chapters 10–12](https://archive.schillerinstitute.com/fid_97-01/982_orbit_ceres_chaps/982_chap_10-12.pdf)
- [Chapter 15 onward](https://archive.schillerinstitute.com/fid_97-01/982_orbit_ceres_chaps/982_chap_15-end.pdf)

Begin with the sightline construction and the distinction between swept sectors and triangles in chapters 10–12; then examine the correction in chapter 15. These reading notes do not certify every historical or philosophical claim in the article.

## First mathematical question: what did the observations determine?

The starting observations supply directions at specified times, not three known positions in space. See the article's printed pp. 44–54, particularly figure 12.1 on p. 54.

Our notation for an idealized observation model:

```text
position_Ceres(tᵢ)
    = position_observer(tᵢ) + distanceᵢ × directionᵢ

length(directionᵢ) = 1
          distanceᵢ > 0
```

All positions use the same Sun-centred inertial frame. `directionᵢ` points from the observer towards the object. `distanceᵢ` is an unknown length, not an observed angle. This first model ignores light-travel time and apparent-direction corrections; a historical reconstruction must introduce them explicitly rather than silently treating telescope readings as corrected vectors. The observer is not automatically the Earth's centre.

Each sighting leaves a whole ray of possible locations. Requiring the selected locations to belong to **one orbit traversed at the specified times** imposes a further restriction. Picking arbitrary points on those rays and drawing an ellipse through them does not solve that problem.

Keep four questions separate:

1. Which trajectories satisfy the assumed equations of motion and the observations?
2. Does the information select one trajectory, several, or none?
3. How much does a candidate change when the measured angles change slightly?
4. Does it predict observations withheld from the calculation?

A small residual answers none of these questions automatically. An animation must not imply that distances were measured when they were inferred.

### An identity and an approximation are different objects

Within the idealized Kepler model, let `swept_area₁₂` denote the signed area swept about the Sun between the first two times, and similarly for `swept_area₂₃`. Constant areal speed gives

```text
swept_area₁₂ ÷ swept_area₂₃
    = (time₂ − time₁) ÷ (time₃ − time₂).
```

These are **curved sectors**, not automatically the triangles obtained by joining their endpoints to the Sun. Replacing sectors by triangles introduces an approximation. A later implementation should keep them as distinct quantities and retain the assumptions attached to each equality or approximation.

## Checked finding: the printed dates and intervals disagree

Printed p. 45 gives these mean-solar-time timestamps, expressed here in 24-hour notation:

| Label | Timestamp as printed |
|---|---|
| time₁ | 1801-01-02 20:39:04.6 |
| time₂ | 1801-01-22 19:20:21.7 |
| time₃ | 1801-02-11 18:11:58.2 |

The [page image](https://archive.schillerinstitute.com/fid_97-01/982_orbit_ceres_chaps/982_chap_10-12.pdf#page=2) was inspected; the discrepancy is present in the printed page, not just extracted text.

Subtracting **those timestamps**, on one consistent time basis, gives:

| Interval | Article, hours | Recomputed from its dates, hours |
|---|---:|---:|
| time₂ − time₁ | 454.68808 | 478.6880833333 |
| time₃ − time₂ | 478.86014 | 478.8601388889 |
| time₃ − time₁ | 933.54842 | 957.5482222222 |

For example:

```text
20 × 24 + (19 − 20) + (20 − 39) ÷ 60 + (21.7 − 4.6) ÷ 3600
    = 478.6880833333 hours.
```

The first printed interval is one day too short, apart from rounding. The printed total also differs from the sum of its two printed intervals, which is 933.54822 hours.

Ratios recomputed from the timestamps:

```text
(time₂ − time₁) ÷ (time₃ − time₂) = 0.999640697687
(time₂ − time₁) ÷ (time₃ − time₁) = 0.499910158282
(time₃ − time₂) ÷ (time₃ − time₁) = 0.500089841718
```

**Scope:** this checks internal arithmetic, not which historical timestamps or corrections Gauss actually used. Preserve the original entries alongside the recomputation. Do not silently substitute these numbers for primary observations. The angular entries on p. 54 remain unverified against the original records.

## Reconstruction work

Recover the observational tables and Gauss's own accounts before claiming to reproduce his calculation. In particular:

- Establish the observing location, time convention, angular reference frame, and corrections for each input.
- Identify the observations used in each historical calculation; keep different versions distinct.
- Reconstruct the sightlines and solve for the unknown distances under explicitly stated orbital assumptions.
- Measure the effect of the sector-to-triangle approximation and its correction.
- Compare predictions against observations not used to determine the candidate orbit.

A located primary-source edition is Gauss's *Theory of the Motion of the Heavenly Bodies Moving about the Sun in Conic Sections*, Charles Henry Davis's 1857 translation of *Theoria motus*: [University of Toronto / Internet Archive scan](https://archive.org/details/theoryofmotionof00gausuoft). **Located, not yet read here.**

The starting article also points to Gauss's early summary concerning the two new planets. Recover its original publication; do not assume that this earlier account and the later *Theoria motus* describe identical procedures.

Do not substitute a generic least-squares demonstration for the historical construction. Separate initial determination from later refinement.

## `@for_gp3` intake status

**Updated 2026-10-13:** signed-in access recovered the account's Reposts collection. The [2022-07-03 original post selected by @for_gP3](https://x.com/isomorphisms/status/1543794785537953793) links Tennenbaum and Director's Ceres essay through [its actual shortlink](https://t.co/xHVQEXVMTp), which returned the essay text. The earlier retrieval failure is superseded; it was never evidence of an empty account.

See the [annotated account-derived catalog](for-gp3.md) and [114-row inventory](for-gp3-inventory.tsv). The dates recorded are original-post dates, not repost dates. The collection also supplies Cotes's *Logometria*, Gauss's later least-squares discussion, Leibniz's catenary papers, Buchwald's exact Newton lecture, and Quigg's Noether history.

The posts establish source provenance. They do not verify every caption, historical claim, image, or complete thread. The mathematical checks and unresolved primary-observation questions above remain at their stated evidence levels.
