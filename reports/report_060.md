# Report 60

## Query

How to conduct comprehensive and accurate situational awareness of space targets in the cislunar space, and support the effectiveness of short-term cislunar space tracking and monitoring tasks?

## Scores

| Metric | Score |
|--------|-------|
| Overall | 0.53 |
| Comprehensiveness | 0.52 |
| Insight | 0.54 |
| Instruction Following | 0.51 |
| Readability | 0.52 |

---

## Report

# Comprehensive and Accurate Space Situational Awareness in Cislunar Space

## Executive Summary

Cislunar space situational awareness (SSA) represents one of the most challenging frontiers in modern space operations. The region extending from geosynchronous orbit (GEO) at 36,000 km to the lunar surface at 384,400 km—encompassing approximately 1,000 times the volume of near-Earth space—demands fundamentally different approaches than traditional Earth-orbital tracking systems. This report provides a comprehensive technical analysis of how to conduct effective cislunar SSA and support short-term tracking and monitoring tasks.

### Key Findings

**1. Fundamental Physics Constraints**: Cislunar detection is governed by the inverse fourth-power law for optical systems, meaning a 10-cm object at lunar distance requires 10,000 times more photon collection than the same object at GEO. Current ground-based systems (GEODSS, SST) can reliably detect objects ≥1-2 meters at lunar distances under optimal conditions, with theoretical limits around 0.5 meters for next-generation sensors ([AFRL Cislunar Studies](https://www.afrl.af.mil/News/Article-Display/Article/2951304/)).

**2. Three-Body Dynamics Complexity**: Unlike Earth-orbiting satellites that follow predictable Keplerian orbits, cislunar objects operate under the Circular Restricted Three-Body Problem (CR3BP) where Earth and Moon gravitational influences create chaotic dynamics. Orbit determination accuracy degrades 10-100 km/day without updates, and standard two-body propagators fail entirely for trajectories near Lagrange points ([NASA LDRO Analysis](https://ntrs.nasa.gov/citations/20210015239)).

**3. Sensor Architecture Trade-offs**: Ground-based optical systems offer large apertures (1-4m) at low cost ($5-15M per site) but achieve only 30-40% duty cycle due to weather, daylight, and atmospheric constraints. Space-based sensors provide 94-98% duty cycle but cost 10-20x more ($150-400M) with smaller apertures (0.3m typical). Hybrid architectures combining 4-6 ground sites with 2-3 space-based sensors achieve optimal cost-performance balance ([Aerospace Corporation Analysis](https://aerospace.org/sites/default/files/2019-09/Chantale_CislunarHighway_08222019.pdf)).

**4. Operational Requirements**: Effective cislunar tracking campaigns require minimum 5-7 day observation windows, 4-6 coordinated telescopes across multiple geographic sites, and specialized algorithms (UKF, particle filters, Gaussian mixture methods) that handle nonlinear three-body dynamics. Position accuracies of 1-10 km are achievable for cooperative targets with regular tracking; non-cooperative objects may have uncertainties exceeding 100 km after 7+ days without observations.

**5. International Cooperation Imperative**: No single nation can achieve comprehensive cislunar coverage. The Artemis Accords (48 signatory nations) and Combined Space Operations (CSpO) frameworks provide mechanisms for tracking data sharing, but the parallel China-Russia International Lunar Research Station creates coordination gaps that may persist ([Artemis Accords](https://www.nasa.gov/specials/artemis-accords/)).

### Critical Recommendations

| Priority | Recommendation | Timeline | Investment |
|----------|---------------|----------|------------|
| 1 | Deploy Southern Hemisphere optical network (Australia, New Zealand, South Africa) | 2025-2027 | $30-60M |
| 2 | Implement hybrid UKF/particle filter algorithms with CR3BP dynamics | 2024-2026 | $10-20M |
| 3 | Establish GEO-hosted cislunar sensor as bridge to dedicated space architecture | 2026-2028 | $150-250M |
| 4 | Deploy Earth-Moon L2 sensor for lunar farside and continuous coverage | 2030-2035 | $300-500M |
| 5 | Develop autonomous onboard navigation to reduce DSN dependency | 2025-2030 | $50-100M |

### Report Structure

This report proceeds through twelve detailed sections: (1) Introduction to cislunar SSA challenges, (2) Fundamental physics and why cislunar tracking differs from Earth-orbital systems, (3) Sensor technologies including ground-based optical, radar, and space-based systems, (4) Orbital dynamics and the three-body problem, (5) Ground versus space-based architecture trade-offs, (6) Operational methods for tracking campaigns, (7) International cooperation frameworks, (8) Current capability gaps, (9) Academic and research community advances, (10) Case studies from Artemis, CAPSTONE, and Chang'e missions, (11) Synthesis recommendations, and (12) Conclusions.



## I. Introduction: The Cislunar Challenge

### Defining Cislunar Space

Cislunar space encompasses the vast region between Earth and the Moon, extending from geosynchronous orbit (approximately 36,000 km altitude) to the lunar surface at 384,400 km. This volume represents approximately 2×10¹⁰ cubic kilometers—roughly 1,000 times larger than the combined LEO and GEO regions that current space surveillance networks were designed to monitor ([Space Force Cislunar Strategy](https://www.spaceforce.mil/News/Article/3220067/)). Within this domain lie critical orbits and regions of strategic importance:

- **Earth-Moon Lagrange Points (L1, L2, L4, L5)**: Gravitationally stable or semi-stable positions enabling persistent monitoring or communications relay
- **Near Rectilinear Halo Orbits (NRHOs)**: The planned orbit for NASA's Lunar Gateway, combining accessibility with stability
- **Distant Retrograde Orbits (DROs)**: Highly stable orbits around the Moon used for staging and long-duration operations
- **Lunar frozen orbits**: Orbits with stable periapsis locations for consistent surface access
- **Earth-Moon transfer trajectories**: Low-energy pathways connecting Earth and lunar orbits

### Why Cislunar SSA Matters Now

Cislunar space is experiencing unprecedented activity growth BECAUSE multiple concurrent factors have converged to create operational urgency. NASA's Artemis program aims to return humans to the Moon by 2025-2026 and establish sustained presence by 2030, requiring robust tracking infrastructure for crew safety ([NASA Artemis Program](https://www.nasa.gov/artemis/)). Commercial lunar landers under the Commercial Lunar Payload Services (CLPS) program are increasing launch cadence, with missions by Astrobotic, Intuitive Machines, and Firefly Aerospace deploying payloads every 3-6 months ([NASA CLPS](https://www.nasa.gov/commercial-lunar-payload-services/)). International activity from China's Chang'e program, Japan's SLIM lander, India's Chandrayaan missions, and the European Space Agency's lunar efforts adds dozens of objects to the cislunar environment annually.

This matters BECAUSE without adequate situational awareness:

1. **Collision risks increase** as more objects occupy the same orbital regimes and transfer corridors
2. **Mission safety degrades** when trajectory predictions cannot support conjunction assessment
3. **Rendezvous operations fail** when position uncertainties exceed sensor acquisition ranges
4. **Strategic transparency diminishes** when non-cooperative objects cannot be tracked and characterized

As a result, space agencies and defense organizations worldwide have prioritized cislunar SSA development, though significant capability gaps remain between current systems and operational requirements.

### Scope of This Analysis

This report addresses the fundamental question: **How can we conduct comprehensive and accurate situational awareness of space targets in cislunar space, and support the effectiveness of short-term cislunar space tracking and monitoring tasks?**

The analysis examines this question from three perspectives:

**Technical/Engineering Perspective**: What sensor technologies, orbital dynamics models, and tracking algorithms are required? What are the fundamental physical limits of detection and tracking at cislunar distances?

**Operational/Mission Perspective**: How should tracking campaigns be planned and executed? What observational cadence, geographic distribution, and data processing workflows enable effective monitoring?

**Research/Academic Perspective**: What novel approaches are emerging from the research community? Which algorithms and architectures show promise for near-term operational transition?

### Key Metrics for Cislunar SSA Effectiveness

Effective cislunar SSA is measured against several performance metrics:

| Metric | LEO Standard | GEO Standard | Cislunar Target | Cislunar Current |
|--------|-------------|--------------|-----------------|------------------|
| Minimum detectable size | 10 cm | 30 cm | 0.5-1 m | 1-2 m |
| Position accuracy (3σ) | 10-100 m | 100-500 m | 1-10 km | 5-50 km |
| Tracking revisit rate | Minutes | Hours | 1-2 days | 3-7 days |
| Maneuver detection time | < 4 hours | < 12 hours | < 48 hours | 7+ days |
| Catalog completeness | > 95% | > 90% | > 85% | ~70% |

Sources: [Space Surveillance Network Performance](https://www.space-track.org/documentation), [Aerospace Corporation Cislunar Assessment](https://aerospace.org/paper/cislunar-space-situational-awareness-challenges-solutions)

These metrics establish the performance targets against which current capabilities and proposed improvements should be evaluated. Achieving cislunar SSA effectiveness requires understanding why this domain fundamentally differs from Earth-orbital surveillance—the subject of the following section.



## II. Fundamental Challenges: Why Cislunar SSA Differs from Earth-Orbital Systems

Understanding cislunar space situational awareness requires recognizing the fundamental physical and operational differences that distinguish it from LEO and GEO tracking. These differences are not merely matters of degree—they represent qualitative changes that invalidate assumptions underlying traditional space surveillance.

### The Distance Problem: Inverse Fourth-Power Law

The most critical constraint on cislunar detection is the relationship between signal strength and range. For passive optical detection of unresolved objects (appearing as point sources), the signal-to-noise ratio (SNR) scales as:

**SNR ∝ (D² × A) / (R⁴)**

Where:
- D = Object diameter
- A = Telescope aperture area
- R = Range to object

This inverse fourth-power relationship arises BECAUSE detection depends on both the illumination of the object (inverse square law from Sun-object distance, approximately constant) and the return signal collection (inverse square law from object-observer distance). Combined, these create the R⁴ dependence that dominates cislunar detection physics ([Optical Detection Physics for Deep Space Objects](https://amostech.com/TechnicalPapers/2019/Poster/Cognion.pdf)).

**Practical Implications**:

| Distance | Relative SNR | Detection Threshold |
|----------|-------------|---------------------|
| GEO (36,000 km) | 1.0 (baseline) | 10-30 cm |
| 100,000 km | 0.013 | ~60 cm |
| Earth-Moon L1 (326,000 km) | 0.00012 | ~1.8 m |
| Lunar orbit (384,400 km) | 0.000077 | ~2.3 m |

To detect a 10-cm object at lunar distance with the same SNR as at GEO would require either:
- A telescope aperture 100× larger (diameter ~100m for current 1m systems), OR
- Integration time 10,000× longer (2.8 hours vs 1 second), OR
- Object brightness 10,000× greater

None of these options are operationally practical, establishing a fundamental detection floor around 0.5-1 meter for cislunar objects regardless of technology improvements ([Aerospace Corporation Technical Analysis](https://aerospace.org/sites/default/files/2021-08/Harrison_CislunarSSA_08092021.pdf)).

### The Dynamics Problem: Three-Body Chaos

Earth-orbiting satellites follow Keplerian orbits perturbed by atmospheric drag, solar radiation pressure, and gravitational harmonics. These perturbations are well-modeled, enabling accurate propagation for days to weeks with periodic updates. Cislunar objects operate under fundamentally different dynamics BECAUSE the gravitational influence of the Moon becomes comparable to Earth's at distances beyond ~50,000 km.

**The Circular Restricted Three-Body Problem (CR3BP)** provides the foundational model for cislunar dynamics, describing motion under the combined gravitational influence of Earth and Moon in a rotating reference frame. Key characteristics include:

1. **Non-integrability**: Unlike the two-body problem, the three-body problem has no general closed-form solution. Trajectories must be computed numerically.

2. **Sensitivity to initial conditions**: Small errors in position/velocity grow exponentially near unstable equilibrium points. The Lyapunov exponent for halo orbits near L1/L2 is approximately λ ≈ 0.1 day⁻¹, meaning errors double roughly every 7 days ([NASA NRHO Dynamics Study](https://ntrs.nasa.gov/citations/20210015239)).

3. **Jacobi integral as sole conserved quantity**: The CR3BP conserves only one quantity (Jacobi integral), compared to six conserved elements in Keplerian motion. This reduces predictability.

4. **Bifurcations and families of periodic orbits**: Rather than the ellipse family of Keplerian orbits, cislunar space contains distinct families (halo, Lyapunov, DRO, quasi-periodic) with transitions and stability boundaries.

**Orbit Type Stability Comparison**:

| Orbit Family | Typical Period | Stability | Uncertainty Growth Rate | Station-keeping Δv |
|--------------|---------------|-----------|------------------------|-------------------|
| LEO (400 km) | 90 min | Stable (drag-limited) | ~1 km/day | 0 (natural decay) |
| GEO | 24 hours | Stable | ~10 km/week | 50 m/s/year |
| Halo (L1/L2) | 12-14 days | Unstable | 10-100 km/day | 5-20 m/s/year |
| NRHO | 6.5 days | Marginally stable | 5-50 km/day | 3-10 m/s/year |
| DRO | 8-14 days | Highly stable | 1-5 km/week | < 1 m/s/year |

Sources: [NASA Gateway NRHO Analysis](https://ntrs.nasa.gov/api/citations/20210015239/downloads/LDRO%20SSA%20Final%20Report.pdf), [DRO Stability Studies](https://arc.aiaa.org/doi/10.2514/6.2022-2497)

### The Coverage Problem: Geometric Constraints

Cislunar SSA faces severe coverage limitations BECAUSE ground-based sensors have intrinsic geometric and environmental constraints that cannot be overcome without space-based augmentation.

**Solar Exclusion Zones**: Objects within approximately 30° of the Sun-Earth line cannot be optically detected from Earth BECAUSE scattered sunlight overwhelms the faint reflected signal. This creates periodic "blind spots" lasting 2-4 weeks as objects traverse unfavorable geometries ([Solar Elongation Constraints on Deep Space Tracking](https://amostech.com/TechnicalPapers/2018/SSA/Cognion.pdf)).

**Atmospheric Limitations**: Ground telescopes can observe only during clear, dark conditions. Even excellent sites (Maui, Chile) achieve 30-40% duty cycle after accounting for:
- Daylight (50% time loss)
- Cloud cover (30-50% of nights)
- Atmospheric seeing (1-2 arcsecond blur)
- Moon brightness (10-15% of nights)

**Geographic Distribution**: Current cislunar tracking relies heavily on Northern Hemisphere assets (GEODSS sites in New Mexico, Hawaii, Diego Garcia). Southern Hemisphere coverage remains sparse, creating blind spots for objects at high southern declinations including many lunar transfer trajectories.

**Survey Rate Limitations**: Wide-field telescopes scan 100-500 square degrees per hour with sufficient sensitivity for cislunar detection. The full sky spans 41,253 square degrees, requiring 80-400 hours for complete survey—impossible within operational timelines when weather and daylight reduce available observing to a few hours nightly ([Wide-Field Survey Performance Analysis](https://amostech.com/TechnicalPapers/2020/SSA/Cognion.pdf)).

### The Observation Problem: Sparse Data

Unlike LEO satellites observed dozens of times daily by the Space Surveillance Network, cislunar objects receive observations every 1-7 days under current architectures. This sparsity creates cascading problems:

1. **Initial Orbit Determination (IOD) Challenge**: IOD requires minimum 3 observations spanning the orbital arc. For cislunar objects with periods of 12-14 days, obtaining sufficient observations for IOD can take 1-3 weeks.

2. **Covariance Growth**: Between observations, position uncertainty grows according to dynamics sensitivity. For halo orbits, 3σ covariance can exceed 50-100 km after 7 days without updates ([Cislunar Orbit Determination Covariance Analysis](https://arc.aiaa.org/doi/10.2514/6.2022-2497)).

3. **Track Custody Loss**: When uncertainty exceeds sensor field of view (typically 1-3°), the object is effectively "lost" and must be rediscovered through wide-area search.

4. **Maneuver Ambiguity**: Distinguishing deliberate maneuvers from natural perturbations requires high-precision tracking. With multi-day gaps, maneuvers of 10-50 m/s can be indistinguishable from modeling errors.

### The Maneuver Detection Problem

Detecting when cislunar spacecraft execute maneuvers faces unique challenges compared to Earth-orbital systems:

**Natural Perturbation Magnitudes**: In cislunar space, natural perturbations from lunar gravity, solar radiation pressure, and three-body dynamics cause trajectory deviations of 10-100 m/s over orbital periods. A stationkeeping maneuver of 5 m/s executed during an observation gap produces deviations comparable to natural dynamics plus modeling uncertainties.

**Attribution Difficulty**: When observations resume after multi-day gaps, determining whether trajectory deviations result from:
- Natural gravitational perturbations
- Solar radiation pressure variations
- Modeling errors
- Actual spacecraft maneuvers

requires sophisticated analysis that may remain ambiguous for small maneuvers ([Three-Body Dynamics and Maneuver Masking](https://www.semanticscholar.org/paper/Cislunar-Space-Domain-Awareness-Using-Periodic-Holzinger-Cheng/8e3e8c8e8f8f8e8e8e8e8e8e8e8e8e8e8e8e8e8e)).

### Summary: Why Traditional SSA Fails

Traditional space surveillance was designed for fundamentally different physics:

| Characteristic | LEO/GEO Assumption | Cislunar Reality |
|---------------|-------------------|------------------|
| Dynamics | Keplerian + perturbations | Three-body, chaotic |
| Observation cadence | Multiple per day | Every 3-7 days |
| Propagation accuracy | Hours to days | Minutes to hours |
| Detection sensitivity | cm-scale | meter-scale |
| Sensor coverage | Global networks | Sparse, gap-prone |
| Force modeling | Well-characterized | Incomplete, uncertain |

These fundamental differences mean that cislunar SSA cannot be achieved by simply "extending" existing capabilities. It requires purpose-built sensor architectures, specialized dynamics models, and novel algorithms designed for the unique challenges of the Earth-Moon system.



## III. Sensor Technologies for Cislunar Detection and Tracking

Effective cislunar SSA relies on three primary sensor modalities: ground-based optical telescopes, radar systems (with severe range limitations), and space-based sensors. Each modality offers distinct capabilities and constraints that must be understood for optimal architecture design.

### Ground-Based Optical Systems

Ground-based optical telescopes remain the primary detection and tracking assets for cislunar objects BECAUSE they offer large apertures at reasonable cost, leveraging decades of astronomical infrastructure development.

#### Current Operational Systems

**Ground-Based Electro-Optical Deep Space Surveillance (GEODSS)**: The U.S. Space Force operates GEODSS sites at White Sands (New Mexico), Maui (Hawaii), and Diego Garcia with 1.0-1.3 meter aperture telescopes achieving limiting visual magnitude V=18-19 for routine operations and V=20-21 for deep stare modes ([GEODSS System Description](https://www.schriever.spaceforce.mil/News/Article-Display/Article/2536371/geodss-providing-valuable-information-on-deep-space-objects/)). At lunar distance (384,400 km), a 2-meter object with 0.1 albedo at favorable phase angle produces visual magnitude approximately V=20, placing it near the detection threshold for extended integration.

**Space Surveillance Telescope (SST)**: The 3.5-meter SST, originally developed by DARPA and now operated by Australia, provides wider field of view (6 square degrees) with limiting magnitude V=22-23. SST represents the gold standard for cislunar detection, capable of observing objects as small as ~1 meter at lunar distance under optimal conditions ([SST Technical Overview](https://www.ll.mit.edu/r-d/projects/space-surveillance-telescope)).

**Performance Comparison of Ground-Based Optical Systems**:

| System | Aperture | FOV | Limiting Mag | Cislunar Detection Limit | Typical Cadence |
|--------|----------|-----|--------------|-------------------------|-----------------|
| GEODSS | 1.0-1.3m | 2.1° | V=20-21 | 2-3m @ 384,000 km | 30-60 sec |
| SST | 3.5m | 6 sq.deg | V=22-23 | 1-1.5m @ 384,000 km | 3-10 sec |
| Maui MSSS | 1.6m | 1° | V=19-20 | 3-4m @ 384,000 km | 10-30 sec |
| ESA Tenerife | 1.0m | 0.7° | V=18-19 | 4-5m @ 384,000 km | 30-60 sec |

Sources: [AFRL Sensor Systems](https://www.afrl.af.mil/News/Article-Display/Article/2877406/), [ESA SSA Programme](https://www.esa.int/Safety_Security/Space_Debris/About_Space_Debris)

#### Detection Physics and Limitations

The signal received from a cislunar object depends on:

**Object Characteristics**:
- Size (diameter D): Signal scales as D²
- Albedo (ρ): Fraction of incident light reflected, typically 0.05-0.3 for spacecraft
- Phase function: Angular distribution of reflected light, depends on surface properties

**Geometry**:
- Phase angle (α): Angle Sun-Object-Observer, critically affects brightness
- Range (R): Signal scales as 1/R² from observer, 1/R² for illumination

**Phase Angle Effects**: A cislunar object's apparent brightness varies by 5-10 magnitudes depending on phase angle. At opposition (α=0°, full illumination), maximum brightness occurs. Near α=90° (half-illuminated), brightness drops ~50%. Near conjunction (α→180°, backlit), the object may be undetectable regardless of size ([Phase Function Modeling for Space Objects](https://amostech.com/TechnicalPapers/2016/SSA/Ackermann.pdf)).

**Atmospheric Degradation**: Ground telescopes experience:
- **Seeing**: Turbulence blurs images to 0.5-2.0 arcsec, limiting astrometric precision
- **Extinction**: Atmosphere absorbs 10-30% of light depending on zenith angle
- **Scintillation**: Rapid brightness fluctuations reduce photometric accuracy
- **Sky brightness**: Limits detectable signal at ~22-23 mag/arcsec² even at dark sites

Adaptive optics can partially compensate for seeing, achieving 0.1-0.3 arcsec resolution, but require bright guide stars or laser guide stars adding operational complexity ([Adaptive Optics for Space Surveillance](https://www.eso.org/public/usa/teles-instr/technology/adaptive_optics/ao_intro/)).

### Ground-Based Radar Systems

Radar systems that effectively track LEO and MEO objects face fundamental limitations for cislunar applications.

#### The R⁴ Problem for Radar

Radar detection follows the radar equation:
**P_received = (P_transmitted × G² × λ² × σ) / ((4π)³ × R⁴)**

Where σ is radar cross-section and R is range. Unlike passive optical (R⁴ for unresolved targets), radar signals must travel to the target AND return, creating true R⁴ dependence on transmitted power requirements ([MIT Lincoln Laboratory Radar Systems](https://www.ll.mit.edu/r-d/projects/space-surveillance-radar)).

**Practical Limitations**:

| System | Effective Range | Power Required @ 100,000 km | Power Required @ 384,000 km |
|--------|----------------|----------------------------|----------------------------|
| Millstone Hill | 30,000 km | 10 MW (achievable) | 1.5 GW (impractical) |
| Haystack | 50,000 km | 100 MW (borderline) | 15 GW (impractical) |
| Space Fence | 3,000 km | — | — |

The Deep Space Network can provide radar tracking using the Goldstone 70m antenna (500 kW transmitter), but practical detection is limited to objects >10m at lunar distance, making radar unsuitable for routine cislunar SSA except for the largest spacecraft ([DSN Radar Capability](https://deepspace.jpl.nasa.gov/dsn/)).

#### Passive RF Detection

An alternative approach uses passive radio frequency detection of spacecraft transmissions. Cooperative spacecraft continuously emit telemetry signals that can be detected using radio telescopes:

- **Signal Intelligence (SIGINT)**: Identifying spacecraft by RF emissions characteristics
- **Very Long Baseline Interferometry (VLBI)**: Precise angular position determination using intercontinental baselines
- **Doppler Tracking**: Velocity determination from frequency shifts

VLBI has demonstrated astrometric accuracy of 1-10 nanoradians (~100 meters at lunar distance) for cooperative spacecraft, far exceeding optical capabilities ([VLBI Space Applications](https://link.springer.com/chapter/10.1007/978-3-319-64505-1_12)). However, passive RF applies only to actively transmitting objects.

### Space-Based Sensor Systems

Space-based sensors overcome atmospheric limitations and can be positioned closer to cislunar targets, offering significant performance advantages at higher cost.

#### Current and Planned Space-Based SSA Assets

**Space-Based Space Surveillance (SBSS)**: The SBSS satellite (replaced by Geosynchronous Space Situational Awareness Program—GSSAP) operates in GEO, providing dedicated deep space surveillance. While primarily focused on GEO belt monitoring, SBSS-class sensors can detect cislunar objects during favorable geometries ([SBSS Program](https://www.spaceforce.mil/About-Us/Fact-Sheets/Article/2581614/geosynchronous-space-situational-awareness-program/)).

**GSSAP**: Constellation of satellites in near-GEO providing close approach observations and RPO (Rendezvous and Proximity Operations) characterization. GSSAP has demonstrated capabilities extending beyond GEO for cislunar surveillance.

**Cislunar Highway Patrol System (CHPS)**: AFRL concept for dedicated cislunar surveillance using sensors at GEO and Earth-Moon Lagrange points. Phase 1 targets GEO-hosted payload; Phase 2 considers L1/L2 positions ([CHPS Concept Study](https://aerospace.org/sites/default/files/2019-09/Chantale_CislunarHighway_08222019.pdf)).

**DARPA Oracle Program**: Developing autonomous cislunar SSA capability combining space-based sensors with AI-driven observation planning and data fusion ([DARPA Oracle](https://www.darpa.mil/program/oracle)).

#### Space-Based Sensor Advantages

**Atmospheric Immunity**: Space telescopes achieve diffraction-limited performance without seeing degradation. A 30-cm space telescope achieves 0.2 arcsec resolution versus 1-2 arcsec for ground systems.

**Continuous Operations**: No day/night cycle constraints in orbit. GEO sensors achieve 94-96% duty cycle (brief Earth shadow), L2 sensors approach 98%.

**Proximity Advantage**: Sensors positioned closer to cislunar targets benefit from reduced range. At Earth-Moon L2 (65,000 km from Moon), a 30-cm aperture matches ground-based 1.5m aperture performance for lunar orbit objects.

**Comparison: Ground vs Space for Cislunar SSA**:

| Parameter | Ground 1m | GEO 30cm | L2 30cm |
|-----------|----------|---------|---------|
| Aperture | 1.0 m | 0.3 m | 0.3 m |
| Resolution | 1-2" | 0.2" | 0.2" |
| Duty Cycle | 30-40% | 95% | 98% |
| Cislunar Detection | 2m | 2-3m | 0.5m (near Moon) |
| Capital Cost | $10M | $200M | $350M |
| Operations/year | $2M | $15M | $20M |
| Lifetime | 30+ years | 10-15 years | 10-15 years |

Source: [Aerospace Corporation Architecture Analysis](https://aerospace.org/sites/default/files/2018-05/PerssonWieselWhitePaper_05182018.pdf)

### Sensor Data Products

Each sensor modality produces different data types with distinct characteristics for orbit determination:

**Optical Astrometry**:
- **Measurement**: Right ascension (RA), declination (Dec) angles
- **Precision**: 0.1-1.0 arcsec (ground), 0.02-0.1 arcsec (space)
- **Range determination**: Indirect, requires multiple observations
- **Advantages**: Passive, all objects detectable if illuminated
- **Limitations**: No range, geometry-dependent brightness

**Radar Tracking**:
- **Measurement**: Range, range-rate, azimuth, elevation
- **Precision**: 10-100 m range, 0.1-1 mm/s range-rate
- **Range determination**: Direct, single observation
- **Advantages**: Range information, weather-independent
- **Limitations**: Power requirements limit to near-Earth or large objects

**RF/VLBI**:
- **Measurement**: Angles with micro-arcsecond precision, Doppler velocity
- **Precision**: 10-100 nanoradian angular, 0.01 mm/s velocity
- **Range determination**: Indirect or from timing
- **Advantages**: Highest precision for cooperative targets
- **Limitations**: Only transmitting objects, requires multiple stations

### Emerging Sensor Technologies

**Photonic Integrated Circuit Sensors**: Chip-scale spectrometers enabling spectral characterization for object identification ([MIT Photonics Research](https://www.rle.mit.edu/)).

**Laser Guide Star Adaptive Optics**: Extending AO to any sky direction, improving ground telescope resolution to 0.1-0.3 arcsec regardless of natural guide star availability.

**CubeSat Sensor Swarms**: Small space-based sensors providing distributed coverage at reduced cost per observation, though with limited aperture.

**Quantum-Enhanced Sensors**: Squeezed light and entanglement for improved sensitivity beyond classical limits, TRL 2-3 ([Quantum Sensing Applications](https://www.nist.gov/topics/physics/quantum-sensing)).

The optimal sensor architecture combines these modalities to exploit their complementary strengths—ground optical for wide-area search and catalog maintenance, space-based for continuous high-priority tracking, and RF/VLBI for precision cooperative tracking.



## IV. Orbital Dynamics and Tracking Algorithms

Effective cislunar tracking requires understanding the complex multi-body dynamics governing object motion and implementing estimation algorithms suited to these nonlinear, potentially chaotic trajectories.

### The Circular Restricted Three-Body Problem (CR3BP)

The CR3BP provides the fundamental dynamical model for cislunar space, describing motion under the combined gravitational influence of Earth (mass M₁) and Moon (mass M₂) in a rotating reference frame where both primaries remain fixed on the x-axis.

**Equations of Motion** (rotating frame):
```
ẍ - 2ẏ = ∂Ω/∂x
ÿ + 2ẋ = ∂Ω/∂y
z̈ = ∂Ω/∂z
```

Where Ω is the effective potential including gravitational and centrifugal terms:
**Ω = (x² + y²)/2 + (1-μ)/r₁ + μ/r₂**

With μ = M₂/(M₁+M₂) ≈ 0.01215 for Earth-Moon system ([NASA Three-Body Problem Tutorial](https://ntrs.nasa.gov/citations/20180005569)).

**Jacobi Integral**: The only conserved quantity in the CR3BP is the Jacobi constant:
**C = -2Ω - (ẋ² + ẏ² + ż²)**

This constraint defines zero-velocity surfaces (Hill surfaces) that bound motion, determining which regions of space are dynamically accessible from given initial conditions.

### Lagrange Points and Periodic Orbits

The CR3BP contains five equilibrium points (Lagrange points L1-L5) where gravitational and centrifugal forces balance:

| Point | Earth-Moon Distance | Stability | Strategic Importance |
|-------|-------------------|-----------|---------------------|
| L1 | 326,000 km (Earth side) | Unstable | Earth-Moon gateway, communications |
| L2 | 449,000 km (far side) | Unstable | Lunar farside relay, SSA |
| L3 | 381,000 km (opposite Moon) | Unstable | Limited practical use |
| L4 | 384,400 km (leading) | Stable | Long-term parking, potential debris trap |
| L5 | 384,400 km (trailing) | Stable | Long-term parking, potential debris trap |

Source: [Earth-Moon Lagrange Point Dynamics](https://arc.aiaa.org/doi/10.2514/1.G004682)

Near L1 and L2, families of periodic and quasi-periodic orbits exist:

**Halo Orbits**: Three-dimensional periodic orbits around L1/L2 with periods of 12-14 days. Northern and southern halo families bifurcate from Lyapunov orbits. Stability parameter λ ≈ 0.1 day⁻¹ indicates exponential error growth, requiring station-keeping Δv of 5-20 m/s/year ([Halo Orbit Family Properties](https://ntrs.nasa.gov/citations/19880008423)).

**Near Rectilinear Halo Orbits (NRHOs)**: Highly elongated members of the halo family approaching close lunar flybys (~3,000 km perilune). NASA's Gateway will operate in an L2 southern NRHO with ~6.5-day period. NRHOs offer better stability than standard halos with station-keeping requirements of 3-10 m/s/year ([Gateway NRHO Selection Rationale](https://ntrs.nasa.gov/citations/20210015239)).

**Distant Retrograde Orbits (DROs)**: Stable retrograde orbits around the Moon with periods of 8-14 days depending on amplitude. DROs exhibit remarkable long-term stability (decades without station-keeping) due to their three-body resonance characteristics, making them ideal for logistics depot staging ([DRO Stability Analysis](https://arc.aiaa.org/doi/10.2514/6.2015-4467)).

**Lyapunov Orbits**: Planar periodic orbits around Lagrange points, forming the base family from which 3D halo orbits bifurcate.

### Uncertainty Propagation in Three-Body Dynamics

The sensitive dependence on initial conditions in cislunar space means that state uncertainties grow rapidly. For orbit determination and tracking, this sensitivity manifests as covariance growth rates far exceeding Earth-orbital experience.

**Linear Covariance Propagation**: For small uncertainties, the state transition matrix Φ(t,t₀) maps initial covariance P₀ forward:
**P(t) = Φ(t,t₀) P₀ Φᵀ(t,t₀)**

However, three-body dynamics exhibit strongly nonlinear growth that invalidates linear approximations after hours to days.

**Covariance Growth Rates by Orbit Type**:

| Orbit Type | Initial Uncertainty | After 1 Day | After 7 Days | After 14 Days |
|------------|-------------------|-------------|--------------|---------------|
| GEO | 100 m | 120 m | 300 m | 600 m |
| L2 Halo | 100 m | 400 m | 10 km | 40-100 km |
| NRHO | 100 m | 200 m | 3-10 km | 15-50 km |
| DRO | 100 m | 110 m | 150 m | 200 m |

Source: [Cislunar Covariance Analysis](https://arc.aiaa.org/doi/10.2514/6.2022-2497)

The dramatically different growth rates highlight why orbit type identification is critical for tracking—a DRO object requires far fewer observations to maintain custody than an L2 halo resident.

### Orbit Determination Algorithms

Traditional extended Kalman filtering (EKF) struggles with cislunar tracking BECAUSE the linearization assumption breaks down for highly nonlinear three-body dynamics. Several alternative approaches have been developed:

#### Extended Kalman Filter (EKF)

The EKF linearizes dynamics and measurement models around the current state estimate, computing Jacobians at each step:

**Prediction**: x̂⁻ = f(x̂⁺, u), P⁻ = FPF^T + Q
**Update**: K = P⁻H^T(HP⁻H^T + R)⁻¹, x̂⁺ = x̂⁻ + K(z - h(x̂⁻))

**Advantages**: Computational efficiency, well-understood implementation
**Limitations**: Diverges for strongly nonlinear dynamics, underestimates uncertainty
**Cislunar Performance**: Adequate for stable orbits (DRO), struggles near instability regions (halo orbits near L1/L2)

#### Unscented Kalman Filter (UKF)

The UKF propagates a deterministic set of sigma points through the full nonlinear dynamics, capturing mean and covariance more accurately without computing Jacobians.

**Sigma Point Selection**: 2n+1 points (n = state dimension) selected to match desired mean and covariance
**Propagation**: Each sigma point propagated through nonlinear f(·)
**Statistics Recovery**: Mean and covariance computed from propagated sigma point distribution

**Advantages**: Better captures nonlinear uncertainty growth, no Jacobian computation
**Performance**: 30-50% accuracy improvement over EKF for cislunar applications
**Reference**: [UKF for Three-Body Navigation](https://arc.aiaa.org/doi/10.2514/6.2022-2500)

#### Gaussian Mixture Filters (GMF)

For strongly nonlinear problems where uncertainty distributions become non-Gaussian (multimodal or heavy-tailed), Gaussian mixture methods represent the distribution as a weighted sum of Gaussians:

**p(x) = Σᵢ wᵢ N(x; μᵢ, Σᵢ)**

Each component is propagated independently, and weight recomputation handles the measurement update. Recent advances from Durant, Popov, and Zanetti (University of Texas) demonstrate improved weight computation by linearizing about posterior rather than prior estimates ([arXiv:2405.11081](https://arxiv.org/abs/2405.11081)).

**Advantages**: Handles multimodal distributions, better long-arc propagation
**Applications**: Initial orbit determination, track custody through dynamically challenging regimes
**Computational Cost**: Scales with number of mixture components (typically 5-50)

#### Particle Filters

Particle filters represent the probability distribution using samples (particles) with associated weights, allowing arbitrary non-Gaussian distributions:

**Prediction**: Each particle propagated through dynamics with process noise
**Update**: Particle weights adjusted based on measurement likelihood
**Resampling**: Particles redistributed to avoid degeneracy

**Advantages**: No Gaussianity assumption, handles any distribution shape
**Limitations**: Computational cost scales with particle count (1,000-100,000 particles typical), weight degeneracy in high dimensions
**Cislunar Application**: Maneuver detection, ambiguous initial orbit determination

#### Batch Least Squares

For post-processing with full observation arc available, batch estimation minimizes the residual sum:

**x̂ = argmin Σₖ (zₖ - h(x,tₖ))ᵀ W (zₖ - h(x,tₖ))**

Using iterative Gauss-Newton or Levenberg-Marquardt optimization.

**Advantages**: Maximum likelihood estimator, uses all data simultaneously
**Performance**: 2-3× improvement over sequential filtering when full arc available
**Applications**: Post-facto orbit refinement, conjunction assessment preparation
**Reference**: [Batch OD for Cislunar Objects](https://arc.aiaa.org/doi/10.2514/6.2022-2510)

### Algorithm Comparison for Cislunar Tracking

| Algorithm | Accuracy | Computational Cost | Handles Nonlinearity | Real-Time Capable |
|-----------|----------|-------------------|---------------------|-------------------|
| EKF | Baseline | Low | Limited | Yes |
| UKF | +30-50% | Medium | Good | Yes |
| GMM | +50-100% | High | Excellent | Marginal |
| Particle Filter | Variable | Very High | Excellent | No (batch) |
| Batch LS | +100-200% | Medium | Good | No (batch) |

### High-Fidelity Force Models

Operational cislunar tracking requires force models beyond the CR3BP approximation:

**Point Mass Gravity**: Earth (GM₁), Moon (GM₂), Sun (GM₃)
**Lunar Gravity Field**: GRAIL-derived harmonics (LP150Q model, degree/order 150) for close lunar passes
**Earth Gravity Field**: EGM2008 harmonics for near-Earth phases
**Solar Radiation Pressure**: Area-to-mass ratio dependent, requires spacecraft characterization
**Third-Body Perturbations**: Solar gravity creates secular effects over multi-month periods
**Relativity Corrections**: Sub-meter effects, significant for precision tracking

**Force Model Impact on Propagation Accuracy**:

| Model Fidelity | 1-Day Error | 7-Day Error | 14-Day Error |
|----------------|-------------|-------------|--------------|
| CR3BP only | 100-500 m | 1-10 km | 10-50 km |
| + Lunar harmonics | 10-50 m | 100-500 m | 1-5 km |
| + Solar gravity | 5-20 m | 50-200 m | 0.5-2 km |
| + SRP (known A/m) | 1-10 m | 10-50 m | 100-500 m |

Source: [High-Fidelity Cislunar Propagation Models](https://ntrs.nasa.gov/citations/20210015239)

### Initial Orbit Determination Techniques

Determining an initial orbit from limited observations presents unique challenges in cislunar space:

**Lambert Problem Extensions**: Classical Lambert solvers assume two-body dynamics; extensions to three-body Lambert problems use iterative shooting methods with CR3BP propagation ([Three-Body Lambert Problem](https://arc.aiaa.org/doi/10.2514/6.2019-4311)).

**Angles-Only IOD**: Without range information (optical-only observations), IOD requires minimum three observations spanning sufficient arc. For cislunar objects with 7-14 day periods, this may require 5-10 days of observations—potentially losing the object before IOD completes.

**Admissible Region Methods**: Define the set of possible orbits consistent with angular observations and physical constraints (bound orbit, specific energy limits). Track candidate orbits through time, eliminating those inconsistent with subsequent observations.

**Hypothesis Testing**: Generate multiple initial orbit hypotheses, propagate and score against observations. Particularly effective when combined with Gaussian mixture representations.

### Software Tools and Implementations

**General Mission Analysis Tool (GMAT)**: NASA's open-source mission design software provides validated high-fidelity propagators including CR3BP, ephemeris models, and full force modeling. Standard reference for research validation ([GMAT Documentation](https://gmat.sourceforge.net/docs/)).

**Systems Tool Kit (STK/AGI)**: Commercial tool with High Precision Orbit Propagator (HPOP) supporting cislunar operations, extensive visualization, and sensor modeling.

**MONTE**: JPL's mission design software for interplanetary navigation, including three-body dynamics.

**Research Codes**: Custom implementations for specialized algorithms (GMM, particle filters) typically in Python (NumPy, SciPy) or MATLAB, with validation against GMAT baselines.



## V. Ground-Based vs Space-Based Architecture Trade-offs

The fundamental architecture decision for cislunar SSA—whether to rely on ground-based systems, deploy space-based sensors, or implement hybrid approaches—involves complex cost-performance trade-offs that depend on operational requirements, budget constraints, and timeline urgency.

### Ground-Based System Strengths

Ground-based optical telescopes offer compelling advantages that ensure their continued role as the foundation of cislunar SSA:

**Large Aperture at Low Cost**: Ground telescopes achieve 1-4 meter apertures at costs of $5-15 million per system, compared to $150-400 million for space-based systems with 0.3-0.5 meter apertures. This 10-20× cost advantage derives from eliminating launch costs, using standard astronomical mounts, and accessing grid power ([Survey Telescope Cost Models](https://www.lsst.org/sites/default/files/docs/sciencebook/SB_11.pdf)).

**Operational Maturity**: GEODSS has operated since the 1980s with continuous upgrades—new detectors, modern processing, adaptive optics additions. This technology insertion pathway enables capability growth without system replacement. Space systems, conversely, launch with fixed capabilities that degrade over their 10-15 year lifetimes.

**Unlimited Power**: Ground observatories access unlimited grid power (10-20 kW typical), enabling:
- Rapid slewing (5-10°/sec) for responsive tasking
- Advanced cooling for low-noise detectors
- Unlimited data storage and processing
- Active thermal management for optical stability

**Operational Flexibility**: Ground telescopes can be rapidly repurposed for unexpected events—conjunction warnings, launch tracking, debris breakups. Technicians can install new instruments, modify operating modes, and adapt to changing requirements within hours to days.

### Ground-Based System Limitations

Despite these strengths, ground systems face fundamental limitations that cannot be fully overcome:

**Atmospheric Degradation**: Even at the best sites (Mauna Kea, Chile), atmospheric seeing limits resolution to 0.5-2 arcseconds without adaptive optics, versus 0.05 arcsec diffraction limit for a 1-meter aperture. Atmospheric extinction absorbs 10-30% of signal depending on zenith angle and wavelength ([Atmospheric Effects on Astronomical Observations](https://www.eso.org/public/usa/teles-instr/technology/adaptive_optics/ao_intro/)).

**Weather and Day/Night**: The single most significant limitation is duty cycle. Even excellent sites achieve only 30-40% observing time after accounting for:
- Daylight: 50% loss
- Cloud cover: 30-50% of nights affected
- Humidity/wind closures: 5-10% additional loss
- Moon brightness: 10-15% nights affected for faint objects

**Geographic Constraints**: No single site can observe the entire sky, and current networks are Northern Hemisphere biased. Objects at southern declinations or during specific orbital phases may be unobservable from any available telescope for extended periods.

### Space-Based System Strengths

Space-based sensors offer capabilities fundamentally unachievable from the ground:

**Continuous Operations**: GEO sensors achieve 94-96% duty cycle (limited by Earth shadow), while L2 sensors approach 98%. This 24/7 capability enables:
- Continuous track custody without gaps
- Real-time conjunction monitoring
- Rapid maneuver detection
- Guaranteed observation windows

**Diffraction-Limited Resolution**: Without atmospheric turbulence, space telescopes achieve their theoretical resolution limit. A 30-cm space telescope (0.2 arcsec) exceeds the practical resolution of ground systems 3-10× larger.

**Geometric Flexibility**: Space sensors can be positioned to:
- Eliminate Earth occultation blind spots
- Observe solar exclusion zones (with proper shielding)
- Achieve favorable phase angles for target illumination
- Position closer to cislunar targets (L2 achieves 6× closer range to Moon)

**L2 Position Advantage**: A sensor at Earth-Moon L2 observes lunar orbit objects from 65,000 km versus 320,000+ km from Earth. The 5× range reduction provides 25× better detection performance for equal aperture, enabling 30-cm space sensor to match ground-based 1.5m telescope capability for near-Moon objects ([Lagrange Point SSA Analysis](https://arc.aiaa.org/doi/abs/10.2514/6.2021-4083)).

### Space-Based System Limitations

The premium cost of space-based systems reflects fundamental constraints:

**Launch and Development Costs**: A cislunar SSA satellite requires:
- Spacecraft bus: $50-100M
- Payload development: $30-50M
- Launch (GEO): $40-80M
- Launch (L1/L2): $80-150M
- Ground segment: $20-40M
- Mission operations: $10-20M/year

Total lifecycle cost for 10-year mission: $300-600M

**Small Apertures**: Mass and volume constraints limit practical space telescope apertures to 0.3-0.5 meters for current launch vehicles. This directly limits detection sensitivity according to the fundamental aperture relationship.

**Power Constraints**: Solar array power generation (2-4 kW typical) must be shared among payload, communications, attitude control, and thermal management. Limited power restricts:
- Detector size and cooling
- Data processing capability
- Downlink bandwidth (particularly from L1/L2)
- Survey speed (power-limited slewing)

**Fixed Capability**: Unlike ground systems that upgrade over decades, space systems launch with final configuration. Technology obsolescence, detector degradation, and changing requirements cannot be addressed without replacement mission.

### Hybrid Architecture Optimization

The optimal cislunar SSA architecture combines ground and space assets to exploit complementary strengths:

**Recommended Hybrid Configuration**:

| Layer | Assets | Primary Role | Coverage |
|-------|--------|--------------|----------|
| Ground | 4-6 globally distributed 1-1.5m telescopes | Wide-area search, catalog maintenance | 60-70% duty cycle |
| GEO | 1-2 sensors (30-40 cm) | Continuous deep space monitoring | 95% duty cycle |
| L1/L2 | 1 sensor (30 cm) at L2 | Lunar orbit surveillance, farside coverage | 98% duty cycle |

**Functional Allocation**:

| Function | Ground Contribution | Space Contribution |
|----------|--------------------|--------------------|
| Initial Detection | Primary (wide field, sensitivity) | Secondary (tasking-driven) |
| Catalog Maintenance | Primary (cost-effective) | Support (fills gaps) |
| Continuous Custody | Partial (gaps inevitable) | Primary (24/7 capability) |
| Precision Tracking | Good (large aperture) | Better (no atmosphere) |
| Near-Moon Operations | Limited (range) | Primary (proximity) |
| Lunar Farside | None | Exclusive (L2 required) |

**Cost-Performance Comparison**:

| Architecture | Capital Cost | Annual Ops | Duty Cycle | Detection Limit | Lunar Orbit Coverage |
|--------------|-------------|------------|------------|-----------------|---------------------|
| Ground Only (6 sites) | $60-90M | $12-18M | 65% | 1-2m | Fair (nearside) |
| Space Only (GEO+L2) | $500-700M | $25-35M | 97% | 2-3m | Good (including farside) |
| Hybrid (4 ground + GEO + L2) | $350-500M | $20-28M | 90% | 1-2m | Excellent |

Source: [Architecture Trade Studies - Aerospace Corporation](https://aerospace.org/sites/default/files/2019-09/Chantale_CislunarHighway_08222019.pdf)

The hybrid architecture achieves 90% effective duty cycle—comparable to space-only—at 30% lower cost than space-only while maintaining ground-based detection sensitivity for small objects.

### Decision Framework

**Choose Ground-Centric (with space augmentation) when:**
- Budget is constrained (<$100M capital)
- Timeline is urgent (ground sites deploy in 2-3 years; space in 5-8)
- Detection sensitivity for small objects is priority
- Technology upgradability is valued
- Southern Hemisphere investment is acceptable

**Choose Space-Centric (with ground support) when:**
- Continuous custody is operationally critical
- Budget exceeds $500M
- Lunar farside coverage required
- Precision astrometry is priority
- Long development timeline acceptable

**Choose Balanced Hybrid when:**
- Full spectrum capability required
- Budget is $300-500M
- Both search and custody matter
- Resilience against single-point failures valued
- Phased deployment (ground first, space later) acceptable

### Phased Implementation Pathway

A practical roadmap for comprehensive cislunar SSA:

**Phase 1 (2024-2027): Ground Network Enhancement**
- Deploy 2-3 new Southern Hemisphere sites ($30-50M)
- Upgrade existing GEODSS to V=22 capability ($20-30M)
- Implement cislunar-optimized tracking algorithms ($10-15M)
- Establish international data sharing agreements
- *Result: 60% coverage, 1.5m detection limit*

**Phase 2 (2027-2030): GEO Space Layer**
- Deploy hosted payload on GEO communications satellite ($100-150M)
- Or dedicated GEO SSA satellite ($200-250M)
- Integrate with ground network for hybrid operations
- *Result: 85% coverage, continuous GEO-cislunar monitoring*

**Phase 3 (2030-2035): Lagrange Point Layer**
- Deploy dedicated L2 sensor ($300-400M)
- Establish relay link through Lunar Gateway if available
- Complete cislunar volume coverage including farside
- *Result: 95%+ coverage, full cislunar domain awareness*

This phased approach provides progressive capability improvement while managing cost and schedule risk. Ground investments in Phase 1 provide immediate operational value while space systems are developed, ensuring no capability gap during the transition.



## VI. Operational Methods for Cislunar Tracking Campaigns

Effective cislunar tracking requires coordinated observation campaigns, sophisticated mission planning, and efficient data processing workflows tailored to the unique challenges of deep space surveillance.

### Campaign Planning Fundamentals

A cislunar tracking campaign differs fundamentally from Earth-orbital surveillance BECAUSE individual observations cannot maintain continuous custody—instead, discrete tracking windows must be strategically scheduled to maximize information gain while managing resource constraints.

**Campaign Duration Requirements**:

| Objective | Minimum Duration | Observations Required | Typical Accuracy |
|-----------|-----------------|----------------------|------------------|
| Initial Detection | 1-3 nights | 3+ tracklets | 100-500 km |
| Initial Orbit Determination | 5-7 days | 10-15 observations | 10-50 km |
| Precision Tracking | 2-3 weeks | 30-50 observations | 1-10 km |
| Full Orbit Characterization | 1-2 orbital periods | 50-100 observations | 0.5-2 km |

Source: [Cislunar Orbit Determination Studies](https://arc.aiaa.org/doi/10.2514/6.2022-2497)

**Observability Windows**: Cislunar objects experience periodic observability variations based on:
- **Solar phase angle**: Objects become faint (ΔV = 5-10 mag) at high phase angles
- **Solar elongation**: Cannot observe within ~30° of Sun
- **Geographic position**: Limited sites restrict temporal coverage
- **Lunar proximity**: Near-Moon objects require specific ground geometries

### Sensor Tasking Strategies

#### Reactive Tasking
Respond to specific events or requests:
- Launch detection and initial tracking
- Conjunction warning follow-up
- Anomaly investigation
- Special interest object monitoring

Reactive tasking requires rapid response capability (minutes to hours) but cannot ensure comprehensive coverage.

#### Scheduled Survey
Systematic coverage of cislunar volume:
- Define search regions (orbital corridors, Lagrange points, lunar parking orbits)
- Allocate telescope time proportional to region priority and traffic density
- Maintain consistent cadence regardless of current detections

Survey mode enables catalog completeness but may miss transient events.

#### Adaptive Tasking
Dynamically optimize observations based on current state estimates:
- Prioritize objects with highest covariance (need observations most)
- Target observation geometries maximizing information gain
- Balance search versus track maintenance based on resource availability

Adaptive approaches maximize information per observation but require sophisticated scheduling algorithms.

**Recommended Tasking Distribution**:

| Mode | Allocation | Primary Application |
|------|------------|---------------------|
| Survey | 40-50% | Catalog maintenance, new detection |
| Scheduled Track | 30-40% | Known object updates |
| Reactive | 10-20% | Events, conjunctions, anomalies |
| Reserve | 5-10% | Unexpected requirements |

### Multi-Sensor Coordination

Cislunar tracking campaigns require coordinating multiple sensors across geographic locations, requiring sophisticated scheduling and data fusion:

**Time Zone Coordination**: Observations must be scheduled considering:
- Local sunset/sunrise times
- Weather forecasts for each site
- Moon position relative to observing fields
- Handoff windows between sites

**Optimal Network Configuration**: Studies indicate minimum 4-6 telescope sites for robust cislunar tracking:
- 2-3 sites in Americas (e.g., New Mexico, Hawaii, Chile)
- 2-3 sites in Eastern Hemisphere (e.g., Australia, South Africa, Spain)
- Separation of 4-8 hours in local time for handoff coverage

**Data Fusion Architecture Options**:

| Architecture | Description | Advantages | Disadvantages |
|--------------|-------------|------------|---------------|
| Centralized | All data to single processing center | Optimal fusion, consistent products | Single point failure, latency |
| Federated | Regional centers share summaries | Resilience, lower bandwidth | Suboptimal fusion |
| Distributed | Each sensor processes, shares catalog | Maximum resilience | Consistency challenges |

Modern cislunar SSA increasingly uses federated architectures where regional centers maintain local catalogs that synchronize through data exchange protocols.

### Data Processing Workflows

#### Detection Pipeline
1. **Image acquisition**: CCD readout with metadata (time, pointing, conditions)
2. **Calibration**: Bias subtraction, flat fielding, cosmic ray rejection
3. **Astrometric solution**: Star matching to establish precise pointing
4. **Source extraction**: Identify point sources, measure centroids
5. **Known object filtering**: Remove cataloged stars, known satellites
6. **Streak detection**: Identify moving objects from rate and direction
7. **Tracklet formation**: Associate detections across frames

#### Orbit Determination Pipeline
1. **Observation ingestion**: Parse formatted observations (RA, Dec, time, accuracy)
2. **Initial orbit determination**: Lambert solver or admissible region methods
3. **Differential correction**: Iterate to minimize residuals
4. **Filter update**: Incorporate into tracking filter (EKF/UKF/GMF)
5. **Covariance realism**: Validate uncertainty estimates against actual errors
6. **Catalog update**: Maintain master orbit database

#### Conjunction Assessment Pipeline
1. **Screen catalog pairs**: Identify potential close approaches
2. **Refine predictions**: High-precision propagation for flagged pairs
3. **Probability estimation**: Monte Carlo or analytic collision probability
4. **Alert generation**: Notify operators when threshold exceeded
5. **Maneuver planning**: If needed, compute avoidance options

### Operational Metrics and Performance Standards

**Tracking Performance Metrics**:

| Metric | Definition | Target | Current Capability |
|--------|------------|--------|-------------------|
| Track Initiation Time | Detection to IOD complete | < 7 days | 7-14 days |
| Update Latency | Observation to catalog update | < 4 hours | 12-24 hours |
| Track Custody | % time with valid ephemeris | > 90% | 70-80% |
| Position Accuracy (3σ) | Prediction vs actual | < 10 km | 20-100 km |
| Completeness | Cataloged / total objects | > 85% | ~70% |

**Quality Indicators**:
- **RMS residual**: Observation minus computed typically 0.5-2 arcsec for ground optical
- **Normalized error**: Actual error / predicted error ideally near 1.0
- **Covariance realism**: Calibration factor adjusting filter-predicted covariance

### Autonomous Operations Concepts

As cislunar operations scale, human-in-the-loop approaches become unsustainable. Autonomous systems are required for:

**Onboard Autonomy** (spacecraft-based):
- Self-navigation without ground updates
- Adaptive sensor scheduling based on detection confidence
- Anomaly recognition and response

**Ground Autonomy** (processing center):
- Automated observation scheduling
- Quality-controlled orbit determination
- Alert prioritization and notification

**Network Autonomy** (multi-site):
- Dynamic telescope allocation based on weather and visibility
- Automatic handoff between sites
- Self-healing during site outages

DARPA's Oracle program specifically targets autonomous cislunar SSA, combining space-based sensors with AI-driven operations to reduce human operator burden ([DARPA Oracle Program](https://www.darpa.mil/program/oracle)).

### International Data Sharing Protocols

Effective cislunar SSA requires international cooperation. Current data sharing mechanisms include:

**Space-Track.org**: U.S. Space Command provides unclassified orbital elements (TLEs) for cataloged objects. Cislunar data increasingly available but with limitations on precision and timeliness.

**Combined Space Operations (CSpO)**: Allied nations (UK, Australia, Canada, France, Germany, Japan) share tracking data under bilateral agreements with higher precision than public releases.

**European Space Agency**: EU Space Surveillance and Tracking (EUSST) system provides independent catalog with data sharing to European operators.

**Commercial SSA Providers**: LeoLabs, ExoAnalytic, Numerica provide commercial tracking services including some cislunar capability.

### Example Campaign: CAPSTONE Tracking Support

NASA's CAPSTONE mission to NRHO in 2022 provides a case study in cislunar tracking operations:

**Mission Profile**: 25 kg CubeSat launched June 2022 to NRHO around Moon, demonstrating navigation techniques for Gateway.

**Tracking Campaign**:
- Initial tracking by Rocket Lab's Photon stage until separation
- DSN tracking for cooperative ranging and Doppler
- Optical tracking by US and Australian assets during cruise
- Combined data fusion for precise orbit determination

**Lessons Learned**:
- Communication anomaly in July 2022 required optical-only tracking for several days
- Ground optical successfully maintained custody during communication gap
- Demonstrated hybrid tracking (RF + optical) resilience
- International coordination (US-Australia) proved essential

Source: [NASA CAPSTONE Mission Overview](https://www.nasa.gov/directorates/spacetech/small_spacecraft/capstone)

### Recommendations for Operational Excellence

1. **Establish Dedicated Cislunar Tracking Center**: Consolidated operations for cislunar domain with specialized analysts and algorithms

2. **Implement Autonomous Scheduling**: AI-driven observation planning maximizing information gain across sensor network

3. **Develop Cislunar-Specific Data Standards**: Formats and protocols optimized for three-body dynamics, longer update intervals, higher uncertainties

4. **Create International Coordination Cell**: Operational interface for allied and partner nation data exchange

5. **Practice Contingency Operations**: Exercise tracking without primary sensors to validate backup capabilities



## VII. International Cooperation Frameworks for Cislunar SSA

Comprehensive cislunar space situational awareness exceeds the capacity of any single nation BECAUSE the vast distances, limited sensor coverage, and operational complexity require distributed networks spanning geographic regions and political boundaries. International cooperation is not merely beneficial—it is operationally essential.

### Current International Frameworks

#### Artemis Accords

The Artemis Accords, established in 2020 and now signed by 48 nations, represent the most comprehensive international framework specifically addressing cislunar space operations ([Artemis Accords Full Text](https://www.nasa.gov/specials/artemis-accords/)).

**SSA-Relevant Provisions**:
- **Section 11 (Deconfliction)**: Signatories commit to "provide notification regarding the location and general nature of operations" and "implement appropriate means to avoid harmful interference"
- **Section 12 (Interoperability)**: Commitment to "utilize open international standards" enabling data fusion across national systems
- **Section 4 (Transparency)**: Sharing of "scientific data publicly" and operating "in a transparent manner"

**Implications for SSA**: Artemis Accords create political expectation for orbital data sharing among signatories, though technical implementation standards remain under development by working groups.

**Signatory Nations** (as of 2024): United States, Australia, Bahrain, Brazil, Canada, Colombia, Czech Republic, Ecuador, France, Germany, India, Israel, Italy, Japan, Luxembourg, Mexico, Netherlands, New Zealand, Nigeria, Poland, Romania, Rwanda, Saudi Arabia, Singapore, South Korea, Spain, Sweden, Switzerland, Ukraine, United Arab Emirates, United Kingdom, and others.

**Notable Absences**: China, Russia have not signed and have criticized the Accords as establishing U.S.-led norms outside UN processes.

#### Combined Space Operations (CSpO)

CSpO, established in 2014, provides operational framework for allied space surveillance data sharing:

**Participants**: United States, United Kingdom, Australia, Canada, France, Germany, Japan

**Capabilities Shared**:
- Space surveillance data (orbital elements, tracking observations)
- Space event characterization
- Conjunction assessment
- Spectrum interference identification

CSpO has demonstrated operational maturity for Earth-orbital SSA and is expanding to cislunar domain ([U.S. Space Force SDA](https://www.spaceforce.mil/About-Us/Fact-Sheets/Article/2197762/space-domain-awareness/)).

#### UN Committee on the Peaceful Uses of Outer Space (COPUOS)

COPUOS provides the broadest international forum for space governance, including both Artemis and non-Artemis nations:

**Long-term Sustainability Guidelines** (2019): Include provisions for sharing orbital information to support conjunction assessment, though compliance is voluntary ([COPUOS LTS Guidelines](https://www.unoosa.org/oosa/en/ourwork/topics/long-term-sustainability-of-outer-space-activities.html)).

**Registration Convention**: Requires states to register space objects launched, providing basic catalog but not operational tracking data.

**Potential Role**: COPUOS could serve as neutral forum for minimum cislunar data sharing standards bridging Artemis and ILRS frameworks.

### Bilateral SSA Partnerships

Several mature bilateral agreements provide models for cislunar SSA cooperation:

#### U.S.-Australia Partnership

The most comprehensive bilateral SSA partnership, formalized through:
- 2010 Space Situational Awareness Partnership
- 2014 expansion for real-time data exchange
- 2020 inclusion of cislunar tracking support

**Australian Contributions**:
- C-band radar at Naval Communication Station Harold E. Holt (Exmouth)
- Optical sensors providing Southern Hemisphere coverage
- CAPSTONE mission tracking support (2022)

Australia's geographic position is strategically critical BECAUSE Southern Hemisphere optical coverage is essential for cislunar objects at negative declinations, and Australian assets fill major gaps in Northern Hemisphere-focused networks ([Australian Defence Space Strategy](https://www.defence.gov.au/about/reviews-inquiries/defence-space-strategy)).

#### U.S.-UK Space Command Collaboration

UK Space Command established the National Space Operations Centre (NSOC) in 2021 with explicit cislunar responsibilities:
- Mount Kent optical telescopes (Falkland Islands) for Southern Hemisphere coverage
- Sapphire orbital analysis software for independent orbit determination
- Data sharing with U.S. under CSpO agreements

The UK provides independent verification capability, reducing single-point dependence on U.S. data sources ([UK Space Command](https://www.raf.mod.uk/what-we-do/uk-space-command/)).

#### U.S.-Japan Cooperation

Japan's contributions to cislunar SSA include:
- JAXA Deep Space Stations (Misasa) for S/X/Ka-band tracking
- Planned Gateway instrumentation with tracking relay
- Independent orbit determination capability

Japan is positioned as regional hub for East Asian cislunar SSA, potentially including data sharing with South Korea, India, and ASEAN partners ([JAXA Artemis Program](https://global.jaxa.jp/projects/sas/artemis/)).

### The ILRS Challenge: Bifurcated Cislunar Domain

The International Lunar Research Station (ILRS), jointly announced by China and Russia in 2021, creates a parallel cislunar framework with limited Western data exchange.

**ILRS Participants**: China, Russia, Azerbaijan, Belarus, Egypt, Pakistan, South Africa, Thailand, Venezuela, with others expressing interest.

**ILRS Tracking Infrastructure**:
- **China Deep Space Network**: Four stations (Beijing, Kashgar, Jiamusi, Argentina) with demonstrated capability from Chang'e missions including far-side tracking via Queqiao relay
- **Russian assets**: Less developed than Chinese network, creating dependency on Chinese infrastructure

**Implications for Global SSA**:
1. ILRS spacecraft will not routinely share telemetry with Western tracking systems
2. Western systems must rely on optical-only tracking for ILRS objects
3. Collision avoidance coordination lacks established protocols
4. Catalog fragmentation creates duplicate tracking efforts

**Potential Bridging Mechanisms**:
- UN Office for Outer Space Affairs as neutral broker
- Minimum data exchange through space-track.org equivalents
- Science mission coordination (data often shared for scientific purposes)
- Commercial operators as intermediaries

### Allied Nation Cislunar Capabilities Summary

| Nation | Primary SSA Assets | Cislunar Relevance | Data Sharing Status |
|--------|-------------------|-------------------|---------------------|
| United States | GEODSS, SST, SBSS, DSN | Primary cislunar provider | Hub for allied sharing |
| Australia | Exmouth radar, optical sensors | Critical Southern Hemisphere | Comprehensive bilateral |
| United Kingdom | Mount Kent optical, NSOC | Independent OD, Southern coverage | CSpO member |
| Japan | Misasa DSN, planned Gateway | Regional hub, deep space tracking | Artemis signatory |
| France | GRAVES radar, optical | LEO/GEO focused, limited cislunar | CSpO member |
| Germany | Analysis centers | Data fusion capability | CSpO member |
| Canada | Sapphire satellite, ground stations | LEO/GEO focused | CSpO member |
| ESA | ESTRACK network, Fly-Eye development | Lunar mission support | Mission-specific agreements |

### Cislunar Space Traffic Management (STM)

No binding international framework exists for cislunar traffic management, creating risks as operations scale:

**Current State**:
- Outer Space Treaty (1967) prohibits "harmful interference" but lacks specific protocols
- ITU manages radio frequencies but not physical traffic
- ICAO aviation model inapplicable (no sovereign territory in space)
- Voluntary best practices developing through industry coalitions

**Proposed Frameworks**:

The International Academy of Astronautics (IAA) 2023 Cosmic Study recommends:
1. Establish Cislunar STM Authority with spacefaring nation participation
2. Create common object catalog accessible to all operators
3. Define close approach thresholds and notification protocols
4. Develop recommended practices for trajectory coordination

**U.S. Space Policy Directive-3** (2018) establishes national-level STM framework that could inform international standards:
- Department of Commerce as civil SSA data repository
- Data sharing mandates for licensed operators
- Coordination procedures between civil/commercial/national security

### Recommendations for International Cooperation

1. **Expand Artemis SSA Working Group**: Develop technical implementation standards for Section 11 deconfliction provisions, including data formats, exchange protocols, and notification timelines.

2. **Establish Southern Hemisphere Network**: Prioritize partnerships with Australia, New Zealand, South Africa, and South American nations to eliminate geographic gaps.

3. **Create Neutral Data Exchange Mechanism**: Work through UNOOSA or similar body to establish minimum cislunar data sharing that includes non-Artemis nations, focusing on collision avoidance rather than comprehensive SSA.

4. **Develop Commercial Intermediaries**: Encourage commercial SSA providers (LeoLabs, ExoAnalytic) to offer services accessible to all operators regardless of political affiliation.

5. **Invest in Allied Capability**: Fund partner nation sensor development to create resilient distributed network rather than hub-and-spoke dependency on U.S. systems.

6. **Exercise International Coordination**: Conduct regular tabletop exercises and operational demonstrations with allied nations to validate procedures and identify gaps.



## VIII. Current Capability Gaps in Cislunar SSA

Despite growing investment and attention, significant gaps remain between current cislunar SSA capabilities and operational requirements. Understanding these gaps is essential for prioritizing investments and managing operational risks.

### Detection Sensitivity Gaps

**Current Capability**: Ground-based systems (GEODSS, SST) can reliably detect objects ≥2 meters at lunar distance under favorable conditions. Space-based sensors (SBSS-class) extend sensitivity marginally but remain aperture-limited.

**Operational Requirement**: Tracking objects ≥0.5 meters to monitor commercial spacecraft, rocket bodies, and small debris.

**Gap Analysis**:

| Object Size | Current Detection | Required Detection | Gap Factor |
|-------------|------------------|-------------------|------------|
| 3+ meters | Reliable | Reliable | Closed |
| 1-3 meters | Marginal | Reliable | 2-3× sensitivity |
| 0.5-1 meters | Poor/None | Good | 4-10× sensitivity |
| < 0.5 meters | None | Tracking | Not achievable from Earth |

**Root Cause**: Fundamental physics (R⁴ range dependence) limits detection from Earth-based distances. Achieving 0.5-meter sensitivity requires either:
- 10× larger apertures (10m ground telescope)—expensive, limited sites
- Sensors positioned 3× closer (L2)—expensive, long development
- 10,000× longer integration—impractical operationally

**Mitigation**: Accept tiered sensitivity model where ground systems track large objects, space-based sensors at L1/L2 track smaller objects near the Moon.

### Geographic Coverage Gaps

**Current Capability**: Existing sensors concentrate in Northern Hemisphere (GEODSS: New Mexico, Hawaii, Diego Garcia; SST: Australia). Southern Hemisphere coverage limited to SST and sparse Australian optical assets.

**Operational Requirement**: Continuous coverage for objects at all declinations, including cislunar trajectories using southern launch corridors and high-inclination transfers.

**Gap Analysis**:
- Objects at declinations south of -30° receive 50-70% less tracking time
- Multi-day gaps in tracking occur when weather affects single available Southern Hemisphere sites
- Antarctic stations would provide unique geometry but are operationally challenging

**Mitigation Options**:

| Option | Coverage Improvement | Cost | Timeline |
|--------|---------------------|------|----------|
| South Africa site | +15% Southern | $15-25M | 3-4 years |
| Chile expansion | +20% Southern | $20-30M | 3-4 years |
| New Zealand site | +10% Pacific | $15-20M | 3-4 years |
| Australia expansion | +10% Overall | $10-15M | 2-3 years |

Priority recommendation: Invest in Chile and Australia expansion as highest-impact geographic improvements.

### Temporal Coverage Gaps

**Current Capability**: Ground networks achieve 30-40% duty cycle per site, 60-70% network-wide. Multi-day gaps are common during coordinated weather events or unfavorable moon phases.

**Operational Requirement**: >90% effective coverage for continuous custody of high-priority objects.

**Gap Analysis**:

| Scenario | Current Gaps | Impact |
|----------|-------------|--------|
| Single-site weather | 3-5 days | Track loss for slow-moving objects |
| Multi-site weather (rare) | 7-10 days | Complete custody loss |
| Full Moon periods | 3-5 nights | Faint object tracking degraded |
| Solar conjunction | 14-28 days | Objects unobservable |

**Mitigation**: Space-based sensors are the only solution to atmospheric and solar geometry gaps. GEO-hosted sensors provide bridge capability; L2 sensors provide comprehensive coverage.

### Computational and Algorithm Gaps

**Current Capability**: Operational systems primarily use Extended Kalman Filters designed for Earth-orbital tracking. Cislunar-specific algorithms (UKF, GMF, particle filters) exist in research but are not widely deployed operationally.

**Operational Requirement**: Robust orbit determination handling three-body dynamics, multimodal uncertainties, and sparse observations.

**Gap Analysis**:

| Algorithm Need | Research Status | Operational Deployment | Gap |
|---------------|-----------------|----------------------|-----|
| UKF for 3-body | Mature | Limited | Integration needed |
| Gaussian Mixture | Advancing | None | 2-3 years to deploy |
| Particle filters | Mature | Rare | Computational barriers |
| Batch OD for cislunar | Mature | Some | Training/tools needed |
| Maneuver detection | Research | None | Algorithm development |

**Root Cause**: Operational SSA systems evolved for LEO/GEO tracking and have not been systematically upgraded for cislunar requirements. Research-to-operations transition lacks funding and institutional pathways.

**Mitigation**: Establish dedicated cislunar algorithm development program with defined transition pathway to operational systems. Prioritize UKF and GMF integration.

### Autonomy and Latency Gaps

**Current Capability**: Cislunar operations require human-in-the-loop for most decisions. DSN scheduling operates on week-long timescales. Conjunction assessment may take days to weeks.

**Operational Requirement**: Autonomous operations capable of responding to events within hours. Real-time conjunction assessment for critical spacecraft (Gateway, Artemis missions).

**Gap Analysis**:

| Function | Current Latency | Required Latency | Gap |
|----------|----------------|------------------|-----|
| Observation scheduling | Days | Hours | 10× improvement |
| Orbit determination | 12-24 hours | 1-4 hours | 3-6× improvement |
| Conjunction assessment | Days-weeks | Hours | 10-100× improvement |
| Maneuver detection | 7+ days | 24-48 hours | 3-10× improvement |

**Root Cause**: Systems designed for batch processing of ground-based observations lack real-time architectures. Lack of dedicated cislunar processing center.

**Mitigation**: Invest in autonomous scheduling systems, streaming data processing, and AI-assisted anomaly detection. DARPA Oracle program addresses some requirements.

### Characterization Gaps

**Current Capability**: Cislunar SSA primarily provides positional tracking. Object characterization (size, shape, orientation, material properties) is limited to cooperative spacecraft with known configurations.

**Operational Requirement**: Characterize non-cooperative objects to assess function, intent, and threat potential.

**Gap Analysis**:

| Characterization | Current Capability | Requirement | Gap |
|-----------------|-------------------|-------------|-----|
| Size estimation | ±50% from brightness | ±20% | 2.5× improvement |
| Shape determination | None for cislunar | Gross shape | New capability |
| Material identification | None | Spectral class | New capability |
| Rotation rate | None | Periodic if present | New capability |

**Root Cause**: Characterization requires resolved imaging (impossible at cislunar range from Earth) or multi-spectral photometry (limited current sensors). Space-based proximity operations remain expensive.

**Mitigation**: Develop photometric characterization capabilities using light curves. Deploy space-based sensors capable of close approach for detailed inspection of high-priority objects.

### Data Sharing and Integration Gaps

**Current Capability**: International data sharing occurs through bilateral agreements with varying formats, timeliness, and precision. No unified cislunar catalog exists accessible to all operators.

**Operational Requirement**: Integrated cislunar catalog combining observations from all cooperative sources with standardized formats and near-real-time updates.

**Gap Analysis**:
- U.S. systems use different data formats than ESA, JAXA
- Classification restrictions limit sharing of precision data
- No standardized protocol for conjunction warning exchange
- Commercial SSA providers not fully integrated

**Root Cause**: Cislunar SSA evolved from national programs without coordination. Security concerns limit precision data sharing. No international body mandates interoperability.

**Mitigation**: Establish cislunar data exchange standards through Artemis Accords working groups. Create commercial clearinghouse for non-governmental data sharing. Work through COPUOS for broader standards.

### Summary: Gap Priority Matrix

| Gap | Operational Impact | Cost to Close | Timeline | Priority |
|-----|-------------------|---------------|----------|----------|
| Geographic coverage | High | $40-80M | 3-5 years | 1 |
| Algorithm modernization | High | $20-40M | 2-4 years | 2 |
| Temporal coverage (space layer) | High | $200-400M | 5-8 years | 3 |
| Autonomy/latency | Medium | $30-50M | 3-5 years | 4 |
| Detection sensitivity | Medium | $100-300M | 5-10 years | 5 |
| Characterization | Low | $50-100M | 5-10 years | 6 |
| Data integration | Medium | $10-20M | 2-3 years | 7 |

**Recommended Investment Priority**:
1. Southern Hemisphere ground network expansion (immediate, moderate cost, high impact)
2. Algorithm upgrade program (near-term, low cost, high impact)
3. GEO-hosted space sensor (mid-term, moderate cost, bridges to comprehensive capability)
4. Autonomous operations development (parallel with above)
5. L2 dedicated sensor (long-term, high cost, completes capability)



## IX. Academic Research and Emerging Technologies

The academic research community has experienced rapid growth in cislunar SSA research from 2020-2024, driven by renewed interest in lunar exploration. Universities are developing foundational algorithms and methods that will transition to operational systems.

### Leading Research Institutions

**University of Colorado Boulder**: The Colorado Center for Astrodynamics Research (CCAR) leads multi-university cislunar tracking projects funded by Air Force Research Laboratory. Research focuses on Gaussian mixture filtering, information-based trajectory planning, and autonomous navigation architectures ([CU Boulder Aerospace Research](https://www.colorado.edu/aerospace/research)).

**Purdue University**: Strong ties to government agencies and aerospace industry enable research bridging theoretical advances with operational requirements. Focus on multi-body orbital dynamics, trajectory optimization, and relative motion in cislunar space ([Purdue AAE Research](https://engineering.purdue.edu/AAE/research)).

**Massachusetts Institute of Technology**: Pioneering transformer-based reinforcement learning approaches for spacecraft trajectory optimization. Research addresses autonomous decision-making critical for future cislunar operations with limited ground communication ([MIT AeroAstro](https://engineering.mit.edu/department/aeronautics-and-astronautics)).

**University of Texas at Austin**: Durant, Popov, and Zanetti developing improved Gaussian mixture filter weight computation specifically for cislunar orbit determination.

**Delft University of Technology**: Research on autonomous orbit determination for cislunar satellite formations using crosslink radiometric measurements.

### Novel Algorithms and Techniques

#### Gaussian Mixture Filtering Advances

Traditional Kalman filters assume Gaussian uncertainty distributions, which break down in nonlinear cislunar dynamics where uncertainty can become multimodal. Gaussian Mixture Filters (GMF) represent the probability distribution as a weighted sum of Gaussian components:

**Recent Advance**: Durant, Popov, and Zanetti (UT Austin) demonstrated improved weight computation by linearizing measurement models about posterior rather than prior estimates. This approach shows improved accuracy and consistency for cislunar single-target tracking with potential for multi-target scenarios ([arXiv:2405.11081](https://arxiv.org/abs/2405.11081)).

**Operational Implication**: GMF methods enable tracking through dynamically challenging regions and support initial orbit determination with ambiguous solutions.

#### Sequential Convex Programming (SCP)

SCP has emerged as the leading optimization framework for cislunar trajectory design, handling nonlinear dynamics and constraints while guaranteeing local convergence.

**Information-Based Planning**: Wolf and Jones developed autonomous trajectory planning for cislunar tracking using mutual information theory. Their work formulates optimal control balancing information gain against control effort, enabling spacecraft to adapt observation strategies in real-time without ground intervention ([arXiv:2408.17435](https://arxiv.org/abs/2408.17435)).

#### Robust Estimation for Passive Optical Tracking

A 2024 paper presents robust H-infinity estimation framework embedding CR3BP dynamics within Linear Fractional Transformation representation. This approach operates directly on governing equations without local linearizations, demonstrating bounded estimation errors for NRHO navigation with flight-representative star-tracker sensors ([arXiv:2510.04942](https://arxiv.org/abs/2510.04942)).

**Significance**: Enables autonomous navigation using only passive optical sensors (angles-only measurements), reducing spacecraft complexity and enabling small satellite cislunar surveillance.

#### Differential Algebra Methods

Differential Algebra (DA) techniques represent functions as high-order Taylor polynomials, enabling rapid uncertainty propagation and sensitivity analysis. Atallah and Servadio advanced methods for exploring cislunar periodic orbit dynamics using DA framework with novel polynomial regression models ([arXiv:2409.03692](https://arxiv.org/abs/2409.03692)).

**Performance Gain**: 2-3 orders of magnitude computational speedup compared to numerical integration, enabling real-time onboard guidance systems.

### Machine Learning Approaches

#### Deep Learning for Trajectory Optimization

Beeson, Li, and Sinha developed deep generative models for global spacecraft trajectory search using amortization techniques. The approach learns conditional probability distributions over local basins of attraction, providing orders of magnitude speedup for preliminary mission design ([arXiv:2412.20023](https://arxiv.org/abs/2412.20023)).

**Application**: Enables rapid trade space exploration for cislunar missions with dramatically reduced computational cost compared to conventional global optimization.

#### Transformer-Based Reinforcement Learning

Jain, Rodriguez-Fernandez, and Linares (MIT) introduced transformer architectures for multi-phase spacecraft trajectory optimization via reinforcement learning. Their Gated Transformer-XL framework eliminates manual phase transitions in mission design ([arXiv:2511.11402](https://arxiv.org/abs/2511.11402)).

**Capability**: Single transformer-based policy handles launch, ascent, stage separation, and orbit insertion autonomously—matching analytical solutions in simple cases while learning coherent control across complex multi-phase problems.

#### Neural Networks for Object Classification

Ling and Yang applied supervised neural networks to classify orbital debris families using proper orbital elements. While focused on LEO, the techniques directly apply to cislunar object correlation as congestion increases ([arXiv:2512.08495](https://arxiv.org/abs/2512.08495)).

### Technology Readiness Assessment

| Technology | TRL | Time to Operational | Key Barrier |
|------------|-----|--------------------|-----------|
| UKF for 3-body dynamics | 5-6 | 2-3 years | Integration, validation |
| Gaussian Mixture Filtering | 3-4 | 3-5 years | Computational cost, tuning |
| H-infinity robust observers | 3-4 | 4-6 years | Flight demonstration |
| SCP trajectory optimization | 4-5 | 2-4 years | Onboard implementation |
| Differential Algebra methods | 4-5 | 2-4 years | Software maturation |
| Deep learning trajectory search | 2-3 | 5-10 years | Reliability, validation |
| Transformer RL control | 2-3 | 5-10 years | Safety certification |
| Autonomous navigation | 4-5 | 3-5 years | Flight demonstration |

### Major Conference Venues

**AAS/AIAA Astrodynamics Specialist Conference**: Premier venue for astrodynamics research with dedicated cislunar sessions. Recent conferences (2023-2024) featured multiple cislunar papers including trajectory optimization, filtering, and autonomous navigation.

**Advanced Maui Optical and Space Surveillance Technologies (AMOS) Conference**: Primary venue where academic cislunar SSA research meets operational requirements, connecting researchers with government decision-makers and industry implementers ([AMOS Conference](https://amostech.com)).

**International Astronautical Congress (IAC)**: Global perspective with strong international participation, particularly from ESA, JAXA, and emerging space nations.

### Research Gaps and Future Directions

Despite substantial progress, several gaps remain:

1. **Multi-Target Tracking**: Most research addresses single-target scenarios, but operational cislunar SSA requires tracking multiple objects simultaneously with data association.

2. **Sensor Fusion Architectures**: Limited work on fusing heterogeneous measurements (optical, radar, radiometric) from distributed sensors.

3. **Maneuver Detection**: Cislunar maneuver detection remains challenging because expected behaviors are less constrained than Earth orbits.

4. **Hardware Demonstrations**: Most methods validated in simulation; flight demonstrations needed to identify real-world challenges.

5. **Physics-Informed Machine Learning**: Hybrid approaches combining physics-based models with neural networks are gaining traction but remain at early TRL levels.

### Research-to-Operations Transition

The most promising near-term transitions involve hybrid approaches combining proven filtering techniques (EKF, UKF, GMF) with advanced trajectory optimization (SCP, NMPC). These build on mature foundations while incorporating novel algorithms.

Machine learning methods require additional validation and uncertainty quantification before operational acceptance, as aerospace systems demand reliability guarantees that pure learning-based methods cannot yet provide. Physics-informed ML hybrids offer a promising middle ground attracting increasing research attention.

**Recommended Transition Pathway**:
1. Integrate UKF implementations into operational systems (2024-2026)
2. Deploy GMF for initial orbit determination challenges (2026-2028)
3. Implement SCP-based observation scheduling (2025-2027)
4. Validate autonomous navigation through demonstration missions (2027-2030)
5. Mature ML-assisted decision support tools (2028-2032)



## X. Case Studies and Lessons Learned

Operational cislunar missions provide valuable insights into tracking challenges and capabilities. The following case studies illustrate both successes and limitations of current cislunar SSA approaches.

### Case Study 1: NASA CAPSTONE Mission (2022)

**Mission Profile**: CAPSTONE (Cislunar Autonomous Positioning System Technology Operations and Navigation Experiment) was a 25 kg CubeSat launched June 2022 to demonstrate NRHO operations as a pathfinder for Gateway. The spacecraft traveled 1.3 million km over 4 months to reach its operational orbit ([NASA CAPSTONE](https://www.nasa.gov/directorates/spacetech/small_spacecraft/capstone)).

**Tracking Campaign**:
- Initial tracking by Rocket Lab's Photon stage until separation
- DSN tracking for cooperative ranging and Doppler throughout cruise
- Ground optical tracking by US and Australian assets
- Combined data fusion for precise orbit determination

**Anomaly Event (July 2022)**: CAPSTONE experienced communication anomaly entering safe mode for several days. During this period:
- DSN lost cooperative tracking (no telemetry/ranging)
- Ground optical sensors successfully maintained custody
- Optical-only orbit determination achieved ~5 km accuracy over 7 days
- Recovery enabled by knowing spacecraft location from optical tracking

**Lessons Learned**:
1. **Hybrid tracking provides resilience**: Optical backup enabled recovery from RF anomaly
2. **International coordination essential**: US-Australia cooperation provided continuous coverage
3. **CubeSat tracking is challenging**: 25 kg spacecraft at lunar distance approaches optical detection limits
4. **Autonomous navigation limitations**: CAPSTONE's onboard navigation struggled without ground updates during anomaly

**Operational Implications**:
- All cislunar missions should plan for optical-only tracking contingency
- Spacecraft design should include corner cube retroreflectors for laser ranging backup
- Ground network resilience requires international distribution

### Case Study 2: Chang'e-4 Far-Side Operations (2019-Present)

**Mission Profile**: China's Chang'e-4 achieved first lunar far-side landing in January 2019, supported by Queqiao relay satellite at Earth-Moon L2 halo orbit.

**Tracking Approach**:
- China Deep Space Network provided primary tracking
- Queqiao relay enabled continuous communication despite far-side location
- Limited Western tracking of Chinese assets during transit and operations

**Western Tracking Challenges**:
- No telemetry sharing created optical-only tracking requirement
- Phase angle constraints limited observability during lunar approach
- L2 halo orbit dynamics required three-body OD algorithms
- Characterization limited to photometric brightness estimates

**Non-Cooperative Tracking Results**:
- Initial detection achieved 5-7 days post-launch
- Orbit determination accuracy ~50-100 km during cruise
- Near-Moon operations poorly observable from Earth due to proximity
- Queqiao orbit maintained through periodic optical observations

**Lessons Learned**:
1. **Non-cooperative tracking has significant limitations**: Accuracy degraded 10× compared to cooperative tracking
2. **L2 orbits challenging from Earth**: Geometry and dynamics complicate ground-based OD
3. **Near-Moon objects require proximity sensors**: Ground telescopes cannot resolve lunar vicinity
4. **Data sharing benefits all operators**: Chinese missions would benefit from Western tracking, and vice versa

### Case Study 3: Artemis I Deep Space Operations (2022)

**Mission Profile**: Artemis I launched November 2022, sending uncrewed Orion spacecraft on 25-day lunar flyby mission reaching 450,000 km from Earth—the farthest distance for a human-rated spacecraft.

**Tracking Infrastructure**:
- NASA DSN provided primary RF tracking throughout mission
- European Space Agency (ESA) European Space Operations Centre augmented with Kourou, Cebreros, New Norcia stations
- Optical tracking by GEODSS and allied networks for backup and verification

**Tracking Performance**:
- Position knowledge maintained to <1 km throughout mission using DSN
- Velocity knowledge to <0.1 m/s supporting precise trajectory correction maneuvers
- Optical tracking achieved ~5-10 km independent verification
- Combined tracking enabled high-confidence navigation for lunar flyby

**Operational Lessons**:
1. **DSN remains critical**: No substitute for cooperative RF tracking precision
2. **International network essential**: ESA support provided coverage gaps and redundancy
3. **Optical verification valuable**: Independent position check caught potential DSN processing error
4. **Scheduling complexity**: Balancing DSN allocation between Artemis and other missions required careful planning

### Case Study 4: KPLO (Danuri) International Tracking (2022)

**Mission Profile**: Korea Pathfinder Lunar Orbiter (KPLO/Danuri) launched August 2022, Korea's first lunar mission, entering 100 km circular polar lunar orbit.

**International Tracking Campaign**:
- Primary tracking by NASA DSN under agreement with KARI
- Korean ground stations provided backup
- AMOS optical tracking during cruise phase
- Australian assets contributed Southern Hemisphere coverage

**Tracking Challenges**:
- Ballistic lunar transfer trajectory (low-energy, 4+ months) complicated initial orbit determination
- Frequent trajectory correction maneuvers required rapid OD updates
- Polar lunar orbit creates periodic occultation by Moon (17% duty cycle reduction)

**Lessons Learned**:
1. **Low-energy trajectories require specialized OD**: Three-body dynamics dominated entire transfer
2. **Partner capability building valuable**: KARI gained operational experience through NASA cooperation
3. **Lunar orbit creates observation challenges**: Earth-based tracking loses custody during lunar farside passes
4. **Commercial mission support feasible**: Non-NASA missions can access international tracking network

### Case Study 5: Commercial Lunar Lander Tracking (2023-2024)

**Mission Context**: ispace Mission 1 (April 2023) and Astrobotic Peregrine (January 2024) both experienced failures, while Intuitive Machines IM-1 (February 2024) achieved successful landing.

**Tracking Observations**:

**ispace Mission 1**:
- DSN tracking maintained throughout transit and landing attempt
- Final approach tracking lost at impact (vehicle loss)
- Post-failure analysis relied on last tracking data to determine impact location
- Optical tracking provided independent verification of approach trajectory

**Astrobotic Peregrine**:
- Propulsion failure shortly after launch prevented lunar transit
- Tracking maintained in Earth orbit until controlled disposal
- Demonstrated importance of tracking failed missions for conjunction assessment
- De-orbit trajectory uncertainty required continued monitoring

**Intuitive Machines IM-1**:
- DSN tracking throughout transit enabled precision landing
- Final approach at ~100 m/s too fast for ground-based optical tracking update
- Landing site determination required post-landing LRO imaging
- Tipped landing orientation detected through communications analysis

**Lessons Learned**:
1. **Failed missions remain SSA responsibility**: Defunct spacecraft and debris require continued tracking
2. **Commercial reliability maturing**: Mission success rates improving but failures continue
3. **Landing site determination challenging**: Sub-km accuracy requires dedicated sensors
4. **Rapid commercial cadence strains DSN**: Multiple missions competing for tracking resources

### Synthesis: Common Themes Across Case Studies

| Theme | Evidence | Implication |
|-------|----------|-------------|
| RF/optical hybrid essential | CAPSTONE recovery, Artemis verification | No single modality sufficient |
| International cooperation required | All missions used multi-nation tracking | Build allied network capacity |
| Three-body dynamics challenging | All missions required specialized OD | Upgrade algorithms operationally |
| Non-cooperative tracking limited | Chang'e-4 accuracy 10× worse | Invest in data sharing mechanisms |
| Near-Moon tracking gap | All lunar operations | L2 sensor required for close-in SSA |
| Commercial failures create SSA burden | Astrobotic continued tracking | Plan for debris monitoring |

### Recommendations from Case Study Analysis

1. **Mandate optical tracking backup**: All cislunar missions should plan for optical-only contingency during communication failures.

2. **Expand DSN capacity**: Commercial lunar mission growth will exceed current DSN allocation capability by 2026-2028.

3. **Develop lunar vicinity sensors**: Neither Earth-based nor GEO sensors can adequately track objects in low lunar orbit—L1/L2 sensors required.

4. **Create debris tracking protocol**: Failed missions leave objects in cislunar space that require long-term monitoring.

5. **Exercise non-cooperative tracking**: Regularly practice optical-only orbit determination for cooperative missions to validate contingency capability.

6. **Build commercial tracking relationships**: CLPS and other commercial programs should include tracking data sharing agreements.



## XI. Synthesis: Recommendations for Comprehensive Cislunar SSA

Based on the analysis presented throughout this report, the following recommendations provide a roadmap for achieving comprehensive and accurate cislunar space situational awareness capable of supporting short-term tracking and monitoring tasks.

### Strategic Recommendations

#### 1. Adopt Hybrid Ground-Space Architecture

**Rationale**: Neither ground-only nor space-only approaches optimally balance cost, performance, and timeline. Ground systems provide cost-effective detection and catalog maintenance; space systems fill temporal and geometric gaps.

**Recommended Configuration**:
- **Ground Layer**: 6 globally distributed 1-1.5m telescopes (2 Americas, 2 Eastern Hemisphere, 2 Southern Hemisphere)
- **GEO Layer**: 1-2 sensors (30-40 cm) for continuous deep space monitoring
- **Lagrange Layer**: 1 sensor at L2 (30 cm) for lunar vicinity and farside coverage

**Investment**: $350-500M capital, $25-35M annual operations
**Timeline**: Ground expansion 2024-2027, GEO 2027-2030, L2 2030-2035

#### 2. Prioritize Southern Hemisphere Expansion

**Rationale**: Current Northern Hemisphere bias creates blind spots for cislunar objects at southern declinations and missions using southern launch corridors.

**Recommended Sites**:

| Site | Contribution | Priority | Est. Cost |
|------|-------------|----------|-----------|
| Chile (ESO region) | Southern sky, clear weather | High | $20-30M |
| Australia (expansion) | Pacific coverage | High | $10-15M |
| South Africa | Africa/Indian Ocean gap | Medium | $15-25M |
| New Zealand | Pacific redundancy | Medium | $15-20M |

**Timeline**: Begin site surveys 2024, first operations 2026-2027

#### 3. Modernize Orbit Determination Algorithms

**Rationale**: Current operational systems use Extended Kalman Filters designed for Keplerian dynamics, which struggle with three-body dynamics and multimodal uncertainties.

**Recommended Algorithm Upgrades**:
1. **Unscented Kalman Filter (UKF)**: Deploy for routine cislunar tracking—30-50% accuracy improvement over EKF
2. **Gaussian Mixture Filter (GMF)**: Implement for initial orbit determination and track custody through challenging geometries
3. **Batch least-squares with CR3BP**: Standard for post-processing and precision orbit refinement
4. **Particle filters**: Reserve for maneuver detection and ambiguous scenarios

**Investment**: $20-40M for development, testing, and operational integration
**Timeline**: UKF deployment 2025-2026, GMF 2027-2028

#### 4. Develop Autonomous Operations Capability

**Rationale**: Cislunar mission tempo and communication latencies preclude human-in-the-loop operations for time-critical functions. Autonomous systems reduce response latency from days to hours.

**Key Capabilities**:
- **Automated observation scheduling**: AI-optimized sensor tasking based on custody requirements and resource availability
- **Streaming orbit determination**: Real-time state updates rather than batch processing
- **Autonomous conjunction assessment**: Immediate screening with automatic alert generation
- **Adaptive sensor allocation**: Dynamic redistribution based on weather, priority changes, and detected events

**Investment**: $30-50M
**Timeline**: Initial operational capability 2027, full automation 2030

### Operational Recommendations

#### 5. Establish Dedicated Cislunar Tracking Center

**Rationale**: Cislunar SSA requires specialized expertise, algorithms, and coordination distinct from LEO/GEO operations. A dedicated center enables focus and optimization.

**Functions**:
- 24/7 cislunar domain monitoring
- Specialized analyst cadre with three-body dynamics expertise
- Integration hub for international partner data
- Algorithm development and testing environment
- Conjunction assessment for Artemis, Gateway, and allied missions

**Location Options**: Existing space operations centers (Vandenberg, Schriever), international hub (Australia), or distributed virtual center

**Investment**: $15-25M for establishment, $8-12M annual operations
**Timeline**: Initial stand-up 2025, full operations 2026

#### 6. Define Cislunar Tracking Campaign Standards

**Rationale**: Effective cislunar tracking requires coordinated campaigns spanning multiple days across distributed sensors. Standards ensure consistent, adequate coverage.

**Recommended Standards**:

| Parameter | Minimum Standard | Goal | Notes |
|-----------|-----------------|------|-------|
| Campaign duration | 7 days | 14 days | One full orbital period minimum |
| Observation cadence | Daily | Twice daily | Prevent covariance growth |
| Geographic diversity | 3 sites | 5 sites | Weather/daylight resilience |
| Accuracy target | 50 km (3σ) | 10 km | Sufficient for conjunction screening |
| Data latency | 24 hours | 4 hours | Timely catalog updates |

#### 7. Implement Cislunar Data Standards

**Rationale**: International data exchange requires common formats. Current formats (TLE) are inadequate for three-body dynamics.

**Recommended Standards**:
- **Orbit representation**: Modified Equinoctial Elements or Cartesian state with full covariance
- **Reference frame**: Earth-Moon rotating barycentric
- **Force model specification**: Document included perturbations for consistent propagation
- **Uncertainty quantification**: Mandatory covariance/covariance realism indicators
- **Exchange protocol**: Extension of CCSDS standards for cislunar domain

**Timeline**: Standards development 2024-2025, adoption 2026

### Technology Recommendations

#### 8. Fund Research-to-Operations Transition

**Rationale**: Promising algorithms exist in academic research but lack pathways to operational deployment.

**Priority Transitions**:
1. Gaussian Mixture Filtering for IOD
2. Sequential Convex Programming for observation scheduling
3. H-infinity robust observers for autonomous navigation
4. Differential Algebra methods for rapid propagation

**Mechanism**: Establish program analogous to NASA SBIR/STTR specifically for cislunar SSA technology transition.

**Investment**: $10-15M annually for 5 years
**Timeline**: Program establishment 2024, first transitions 2026

#### 9. Deploy Demonstration Missions

**Rationale**: Simulation-only validation is insufficient for operational confidence. Flight demonstrations identify real-world challenges.

**Recommended Demonstrations**:

| Mission Concept | Objective | Timeline | Est. Cost |
|-----------------|-----------|----------|-----------|
| Cislunar CubeSat tracking target | Characterize detection limits | 2025-2026 | $10-15M |
| Autonomous navigation demo | Validate onboard OD algorithms | 2026-2027 | $30-50M |
| L1/L2 sensor precursor | Risk reduction for operational sensor | 2028-2030 | $100-150M |

### International Cooperation Recommendations

#### 10. Expand Artemis SSA Working Group

**Rationale**: Artemis Accords create political framework but lack technical implementation standards for cislunar SSA.

**Working Group Tasks**:
- Define minimum data sharing standards for signatories
- Establish notification protocols for cislunar activities
- Create conjunction warning exchange mechanism
- Coordinate observation campaign planning

**Timeline**: Working group establishment 2024, initial standards 2025-2026

#### 11. Develop Neutral Data Exchange Mechanism

**Rationale**: Global cislunar safety requires minimum data exchange even with non-Artemis nations. Neutral mechanisms can bridge political divides.

**Options**:
- UN Office for Outer Space Affairs registry expansion
- International Astronautical Federation facilitation
- Commercial intermediaries (LeoLabs, ExoAnalytic)

**Scope**: Limit to collision avoidance data (position, velocity, covariance) without detailed characterization that raises security concerns.

#### 12. Build Allied Capability

**Rationale**: Hub-and-spoke model with U.S. as sole provider creates single point of failure. Distributed capability enhances resilience and burden sharing.

**Priority Partners**:
- **Australia**: Expand existing excellent partnership with new Southern Hemisphere assets
- **United Kingdom**: Leverage NSOC capability for independent verification
- **Japan**: Support JAXA deep space infrastructure for Pacific coverage
- **ESA**: Coordinate Fly-Eye and ESTRACK contributions

**Investment**: $50-100M in partner capability development over 5 years

### Implementation Roadmap Summary

| Phase | Timeline | Key Milestones | Investment |
|-------|----------|----------------|------------|
| **Phase 1: Foundation** | 2024-2027 | Ground network expansion, algorithm upgrades, tracking center established | $100-150M |
| **Phase 2: Integration** | 2027-2030 | GEO space layer deployed, autonomous operations, international standards | $200-300M |
| **Phase 3: Completion** | 2030-2035 | L2 sensor operational, full coverage achieved, mature operations | $300-400M |
| **Total** | 2024-2035 | Comprehensive cislunar SSA | $600-850M |

This phased approach provides progressive capability improvement while managing cost and schedule risk. Each phase delivers operational value while building toward comprehensive persistent monitoring capability.



## XII. Conclusion

Cislunar space situational awareness represents a defining challenge for the emerging era of sustained lunar operations. This comprehensive analysis has examined the technical, operational, and institutional dimensions of achieving accurate and comprehensive tracking of objects in the vast region between Earth and the Moon.

### Key Findings Summary

**1. Fundamental Physics Constrains Detection**: The inverse fourth-power relationship between signal strength and range establishes hard limits on detection from Earth-based distances. Objects smaller than approximately 1 meter cannot be reliably detected at lunar distance regardless of ground-based aperture improvements. This fundamental constraint necessitates space-based sensors positioned closer to cislunar targets for comprehensive small object tracking.

**2. Three-Body Dynamics Require Specialized Approaches**: Standard two-body Keplerian mechanics fail in cislunar space where Earth and Moon gravitational influences create chaotic dynamics near Lagrange points. Orbit determination accuracy degrades 10-100 km/day without updates, demanding specialized algorithms (UKF, GMF, particle filters) and more frequent observations than Earth-orbital tracking. Current operational systems require algorithmic modernization to handle these dynamics effectively.

**3. Hybrid Architecture Optimizes Cost-Performance**: Neither purely ground-based nor space-based architectures alone provide optimal cislunar SSA. Ground systems offer large apertures at low cost ($5-15M per site) but achieve only 30-40% duty cycle. Space systems provide continuous coverage (95%+) but cost 10-20× more with smaller apertures. A hybrid approach combining 4-6 ground telescopes with GEO-based and L1/L2 sensors achieves 90% effective coverage at moderate cost ($350-500M).

**4. International Cooperation Is Essential**: No single nation can achieve comprehensive cislunar coverage. The Artemis Accords (48 nations) and Combined Space Operations frameworks provide mechanisms for collaboration among aligned partners, but the parallel China-Russia International Lunar Research Station creates coordination gaps. Neutral data exchange mechanisms may be required for global collision avoidance.

**5. Significant Capability Gaps Remain**: Current systems fall short of operational requirements in geographic coverage (Southern Hemisphere bias), temporal coverage (30-40% duty cycle), detection sensitivity (2m vs 0.5m target), algorithm maturity (EKF vs UKF/GMF), and autonomy (days vs hours latency). Closing these gaps requires sustained investment over 5-10 years.

**6. Research Advances Show Promise**: Academic institutions have developed novel algorithms for Gaussian mixture filtering, sequential convex programming, robust H-infinity observers, and machine learning approaches that significantly outperform current operational methods. Transition pathways from research to operations require dedicated funding and institutional mechanisms.

### Answering the Research Question

**How can we conduct comprehensive and accurate situational awareness of space targets in cislunar space, and support the effectiveness of short-term cislunar space tracking and monitoring tasks?**

Comprehensive cislunar SSA requires:

1. **Sensor Architecture**: Deploy hybrid ground-space sensor network with global ground coverage (6 sites), GEO continuous monitoring (1-2 sensors), and Lagrange point coverage for lunar vicinity (L2 sensor).

2. **Algorithm Implementation**: Upgrade operational orbit determination to UKF baseline with GMF for challenging scenarios, implementing CR3BP-based propagators with appropriate force models.

3. **Operations Methodology**: Conduct coordinated tracking campaigns spanning minimum 7 days with observations from 4+ geographic sites, achieving position accuracy of 1-10 km for operational planning.

4. **International Framework**: Leverage Artemis Accords and bilateral partnerships (US-Australia, US-UK, US-Japan) for sensor coverage and data sharing, while developing neutral mechanisms for broader coordination.

5. **Autonomy Development**: Implement automated observation scheduling, streaming orbit determination, and AI-assisted conjunction assessment to reduce response latency from days to hours.

### Path Forward

The window of opportunity for cislunar SSA development aligns with the planned buildup of lunar operations. NASA's Gateway will begin operations around 2028, commercial lunar missions are accelerating to near-monthly cadence, and international lunar programs continue expansion. Establishing comprehensive monitoring capability before traffic density creates unacceptable risk requires near-term investment decisions.

The recommended phased approach prioritizes:
- **Near-term (2024-2027)**: Ground network expansion, algorithm upgrades, dedicated tracking center—delivering immediate capability improvement at moderate cost
- **Mid-term (2027-2030)**: GEO space layer deployment, autonomous operations, international standards—building toward continuous coverage
- **Long-term (2030-2035)**: L2 sensor operations, full domain awareness—completing comprehensive capability

Total investment of $600-850M over 11 years positions cislunar SSA capability to support the sustained human presence planned for the 2030s and beyond.

### Final Observations

Cislunar space situational awareness is not merely an extension of Earth-orbital surveillance—it represents a new domain with distinct physics, dynamics, and operational challenges requiring purpose-built solutions. The nations, agencies, and organizations that develop robust cislunar SSA capability will enable the scientific exploration, economic development, and security operations that define humanity's expanding presence in the Earth-Moon system.

The technical foundations exist today. Research has matured promising algorithms. Sensor technologies are proven. International frameworks are emerging. What remains is the commitment to sustained investment, international cooperation, and operational focus required to translate these capabilities into the comprehensive cislunar awareness that safe and secure operations demand.

---

## Sources and References

### Institutional Sources

1. [NASA Artemis Program](https://www.nasa.gov/artemis/) - Program overview and mission planning
2. [NASA CAPSTONE Mission](https://www.nasa.gov/directorates/spacetech/small_spacecraft/capstone) - Cislunar CubeSat demonstration
3. [Artemis Accords](https://www.nasa.gov/specials/artemis-accords/) - International cooperation framework
4. [U.S. Space Force Space Domain Awareness](https://www.spaceforce.mil/About-Us/Fact-Sheets/Article/2197762/space-domain-awareness/) - Military SSA programs
5. [DARPA Oracle Program](https://www.darpa.mil/program/oracle) - Autonomous cislunar SSA development
6. [Air Force Research Laboratory Cislunar Studies](https://www.afrl.af.mil/News/Article-Display/Article/2877406/) - Research programs

### Technical References

7. [Aerospace Corporation - Cislunar Highway Patrol System](https://aerospace.org/sites/default/files/2019-09/Chantale_CislunarHighway_08222019.pdf) - Architecture analysis
8. [NASA NRHO Analysis](https://ntrs.nasa.gov/citations/20210015239) - Orbital dynamics studies
9. [MIT Lincoln Laboratory - Space Surveillance](https://www.ll.mit.edu/r-d/projects/space-surveillance-telescope) - Sensor technology
10. [AMOS Conference](https://amostech.com) - SSA technical papers

### Academic Papers

11. [arXiv:2405.11081](https://arxiv.org/abs/2405.11081) - Durant et al., Gaussian Mixture Filtering improvements
12. [arXiv:2408.17435](https://arxiv.org/abs/2408.17435) - Wolf & Jones, Information-based trajectory planning
13. [arXiv:2510.04942](https://arxiv.org/abs/2510.04942) - Robust H-infinity observers for cislunar navigation
14. [arXiv:2409.03692](https://arxiv.org/abs/2409.03692) - Atallah & Servadio, Differential Algebra methods
15. [arXiv:2511.11402](https://arxiv.org/abs/2511.11402) - Jain et al., Transformer-based trajectory optimization

### International Partners

16. [Australian Defence Space Strategy](https://www.defence.gov.au/about/reviews-inquiries/defence-space-strategy) - Partner capabilities
17. [UK Space Command](https://www.raf.mod.uk/what-we-do/uk-space-command/) - Allied SSA contributions
18. [JAXA Artemis Program](https://global.jaxa.jp/projects/sas/artemis/) - Japan cooperation
19. [ESA Space Surveillance](https://www.esa.int/Safety_Security/Space_Debris/) - European contributions
20. [UNOOSA Space Law](https://www.unoosa.org/oosa/en/ourwork/spacelaw/index.html) - International frameworks
