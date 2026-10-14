# Action, constraints, and regression: topic-focused reading notes

These are questions under consideration, not an adopted philosophical position. An author's philosophical claims, the mathematics in a primary source, and our deductions are kept separate.

## 1. Leibniz's two catenary papers, June and September 1691

**Read:** both translated essays in [Pierre Beaudry's 2001 presentation](https://archive.schillerinstitute.com/fid_97-01/011_catenary.html), including the introduction. The translation works through Marc Parmentier's French edition and consults Latin; this is not a completed collation against the 1691 originals. Original-volume links are in [PRIMARY.md](PRIMARY.md).

**Summary relevant here.** The June paper uses the chain to construct logarithms and proportional means, relates its ordinate to two reciprocal exponential quantities, and gives geometric constructions for tangents, lengths, and areas. It explicitly states the lowest-centre-of-gravity property for a flexible, inextensible chain of fixed length and suspension points. The September paper compares methods and connects the construction to further quadrature and geometric problems. These passages supply more than an empirical curve shape, but they do not present Hamilton's later action integral. The presentation's stronger anti-Newton polemic belongs to its modern introduction, not automatically to Leibniz's two essays.

### Our reconstruction: one chain, two equivalent descriptions

Let y increase upwards, ρ be mass per unit length, and g be uniform gravitational acceleration. The potential energy and fixed-length condition are

    U[y] = ρg ∫ y√(1+y′²) dx,
    ∫ √(1+y′²) dx = length.

The suspension points are fixed. Introduce a length multiplier λ. The Beltrami identity for the augmented integrand gives

    (ρg y + λ)/√(1+y′²) = constant.

Integrating yields the catenary family y = a cosh((x−b)/a) + c, with a > 0.

Local force balance gives the same curve: if H is the constant horizontal tension, the vertical balance is

    H y″ = ρg√(1+y′²).

Thus global energy minimization and local balance do not constitute incompatible mechanics. What is global includes the shared tension, total length, and endpoint constraints. Fitting measured coordinates to the derived catenary family is a further estimation problem; it need not replace the derivation.

## 2. Riemann's 1857 function-theoretic construction

**Read:** the preliminary essay *Bestimmung einer Function einer veränderlichen complexen Grösse durch Grenz- und Unstetigkeitsbedingungen*, and selected opening sections of the main *Theorie der Abel'schen Functionen*, in [Wilkins's transcription](https://www.emis.de/classics/Riemann/AbelFn.pdf). The PDF bundles several works: the variational argument is in the preliminary essay, printed pp. 11–14, not simply “§3 of the main paper.” The functional and quadratic expansion were visually checked on printed p. 12, PDF page 13. The entire 56-page collection has not been read.

**Summary relevant here.** Riemann starts from conditions sufficient to determine a function. His preliminary construction uses a nonnegative quadratic integral and boundary-preserving variations. In the main paper, branching, specified singularities, cuts, and periods constrain the functions being constructed. This is not a rejection of squared minimization. Its distinctive content is what is varied, what is fixed, and which global continuation conditions a function must satisfy.

For fixed β, his displayed functional is

    Ω(α) = ∫ [(αₓ − βᵧ)² + (αᵧ + βₓ)²] dT.

At a stationary u, for the admitted zero-boundary variation σ, the expansion is

    Ω(u+hσ) = Ω(u) + h² ∫(σₓ² + σᵧ²) dT.

### Our comparison and qualification

For a least-squares stationary point θ, the corresponding identity is

    ‖observations − X(θ+δ)‖²
      = ‖observations − Xθ‖² + ‖Xδ‖².

Both calculations remove a first-order term and control the remainder by a nonnegative quadratic expression. Their admissible spaces and interpretations differ. This mathematical resemblance does not prove identical philosophies, but it disproves a proposed distinction based merely on the presence of squares.

An existence argument still has to be supplied: nonnegativity alone does not imply attainment. For example, exp(x) is bounded below on the real line and has no minimum there. Riemann's minimum-attainment step must therefore be distinguished from the subsequent conditional variation and uniqueness calculation. This is a logical qualification of the displayed argument, not a claim to have completed its historical or modern existence theory.

## 3. Director, Riemann for Anti-Dummies, Part 63

**Read:** the full prose of [“Dynamics not Mechanics”](https://lymcanada.org/63/). The embedded animations have not been audited frame by frame. This is Director's own philosophical exposition, not Riemann's text.

**Summary relevant here.** Director contrasts explanations based on a whole process with descriptions of separate parts. The pendulum and chain lead to boundary conditions and potential fields. In “How Things Hang Together,” he explicitly opposes pairwise linkage to dependence on the whole manifold. This is the closest located source for our conversation's wording. The essay extends these claims to history, economics, and creativity, but those extensions are not mathematical consequences of the examples.

### What the example establishes — and what it does not

The useful question is how shared constraints make a system's response global. That does not require denying local interactions. Here is an explicit counterexample to an opposition between pairwise terms and global determination:

    E(u₁,u₂) = (u₁−0)² + (u₂−u₁)² + (3−u₂)².

Every term concerns neighboring values. Simultaneous stationarity gives

    2u₁ − u₂ = 0,
    2u₂ − u₁ = 3,

so the unique global minimum is u₁ = 1, u₂ = 2. Minimizing each edge separately would be impossible: it would require all four values, including the incompatible boundaries 0 and 3, to be equal. Local terms and global dependence coexist.

Two other assertions in the essay need correction rather than adoption. Scalar-valued does not mean linear: v ↦ v² is a counterexample, and kinetic energy is quadratic in velocity. Absence of discontinuities is not a criterion for simple connectedness: the constant function is continuous on an annulus, but a loop around the hole cannot contract within it. Boundary response, curvature, topology, and nonlinearity must not be used interchangeably.

## 4. Stationary action is a separate mathematical condition

Our comparison uses Hamilton's functional, not an attribution of this notation to Leibniz:

    S[q] = ∫ L(q,q̇,t) dt,
    δS = 0.

For fixed endpoints and regularity permitting integration by parts, this gives

    d/dt(∂L/∂q̇) − ∂L/∂q = 0.

An integral condition on complete paths therefore produces local differential equations. It need not select a minimum. For L = m(q̇²−ω²q²)/2 on [0,τ], q = 0 is stationary with endpoints zero. Along η(t) = sin(πt/τ),

    S[εη] − S[0] = ε²mτ[(π/τ)²−ω²]/4.

For τ > π/ω this is negative, while sufficiently high-frequency sine variations give a positive value. The stationary path is a saddle. One cannot treat a general mechanical action as a nonnegative regression penalty.

## 5. Three distinctions to keep separate

A local density can define a global variational problem. A local minimum concerns a neighborhood in parameter or function space. A local numerical update concerns how a computation is performed. These are different meanings of “local.”

[Gauss](gauss-theoria-motus.md) combines physical restrictions and statistical adjustment. [Quigg's Noether discussion](quigg-noether.md) explains how symmetries supply conservation laws. Neither reduces to a choice between local arithmetic and global physical meaning.

A precise working question is: **Which assumptions determine the admissible family of explanations, and what can a small residual establish once that family has already been chosen?**
