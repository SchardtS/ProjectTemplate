# ExampleData Metadata

## General Information
- Experiment Title: Simulation of 100 individual separated cells over time
- Experiment Date: 17.10.2023
- Researcher: Dr. Simon Schardt
- Contact information: simon.schardt@uni-wuerzburg.de

## Simulation Details
- Source code: Not public
- Simulation setting: Cell growth and division with adhesion and repulsion

### Model Parameters
- `T = 234.73532973888538`               (Time)
- `nofSteps = 5000`                      (Number of timesteps)
- `r_max = 1`                            (Maximum radius)
- `k = 0.083`                            (Cell growth rate)
- `F0 = 0.01`                            (Force scaling)
- `alpha = 3`                            (Cell stiffness)
- `sigma = 0.7`                          (Cell distance optimality factor)

### Initial Cell Distribution
- `nofClusters = 100`                                     (Number of initial cell clusters)
- `pos = np.random.uniform(-60, 60, [nofClusters, 2])`    (Uniformly distributed cell positions) (IF REALLY NEEDED INCLUDE SEED HERE!!!)
- `r = np.random.normal(0.8, 0.01, nofClusters)`          (Randomly distributed cell radii) (IF REALLY NEEDED INCLUDE SEED HERE!!!)

## Additional Notes
- Related Publication: https://opus.bibliothek.uni-wuerzburg.de/opus4-wuerzburg/frontdoor/deliver/index/docId/30194/file/schardt_simon_organoid_modeling.pdf
- 
