# Tennenbaum and Director: Ceres and the regression question

**Source:** Jonathan Tennenbaum and Bruce Director, *How Gauss Determined the Orbit of Ceres*, *Fidelio* VII, no. 2 (Summer 1998), [complete 85-page PDF](https://archive.schillerinstitute.com/fid_97-01/982_orbit_ceres.pdf).

**Reading coverage:** selected passages in Chapter 3 (printed p. 18), Chapter 15 (pp. 73–77), and Chapter 16 (pp. 77–79), with surrounding text and the opening of the concluding chapter. This is not a completed reading of all 85 pages or an independently executed reconstruction of the orbital algorithm. The original Gauss–Olbers correspondence and *Summary Overview* cited by the authors have not yet been collated against their claims.

## Summary relevant to the question

The observations give directions from a moving Earth, not three known spatial positions of Ceres. Chapter 3 therefore argues against simply fitting a spatial curve to the apparent motion. Orbital geometry and the time law supply additional conditions. Chapters 15–16 describe successive approximations, including correction of sector/triangle area ratios and improving the middle position. The authors distinguish geometrically possible constructions from ones numerically stable enough for prediction. Their own account ends by comparing the constructed orbit with further observations. It therefore does not dispense with correction by data. The philosophical contrast with curve fitting must be evaluated alongside that actual procedure, rather than read as a theorem against least squares.

## Our formulation of what is genuinely different

Write the heliocentric observer position at time tᵢ as observerᵢ and the measured unit viewing direction as directionᵢ. The unknown object position has the form

    positionᵢ = observerᵢ + distanceᵢ × directionᵢ,

where distanceᵢ is unknown. A regression that treats apparent sky coordinates as directly observed spatial positions has the wrong observation model.

Given orbital parameters θ and a physical trajectory position(t;θ), the predicted direction is instead

    predictionᵢ(θ) = [position(tᵢ;θ) − observerᵢ]
                     / ‖position(tᵢ;θ) − observerᵢ‖.

Now a residual can compare predicted and observed angles, with an error model appropriate to angular measurements. The admissible trajectories can already incorporate the physical laws. Constructing this forward map is not accomplished by merely selecting a loss function.

This distinguishes three questions:

1. What quantities did the observer actually measure?
2. Which trajectories and observation maps are physically admissible?
3. How should discrepancies among the admissible predictions be weighted and reduced?

The first two questions can radically change the problem without abolishing the third. Gauss's own treatment of adjustment is summarized in [Theoria motus](gauss-theoria-motus.md).

## What remains to be demonstrated

A complete numerical audit requires the actual selected observations, their units and corrections, the specific historical algorithm, its intermediate values, and comparison with observations not forced by the construction. No successful orbit reconstruction is claimed by this reading note. Nor should the 1809 presentation be silently substituted for every step of the earlier Ceres calculation.
