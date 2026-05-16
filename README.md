# Genetic Algorithm vs Particle Swarm Optimization

A comparative study of Genetic Algorithms (GA) and Particle Swarm Optimization (PSO) on CEC2005 benchmark functions.

We implement GA and PSO from scratch and evaluate their performance on a suite of unimodal, multimodal, separable, and non-separable optimization problems. The goal is to understand how different evolutionary strategies behave across varying fitness landscapes.

---

### Algorithms

#### Genetic Algorithm (GA)

- Tournament selection
- One-point crossover
- Gaussian mutation
- Generational evolution

#### Particle Swarm Optimization (PSO)

- Informant-based topology (random dynamic neighbourhoods)
- Velocity updates influenced by:
  - Personal best
  - Informant best
  - Swarm/global best behaviour
- Boundary handling for constrained search space

---

### Benchmark Functions

Experiments were conducted on selected **CEC2005 test functions**:

- **F1 (Sphere)** – unimodal, separable  
- **F2 (Elliptic)** – unimodal, non-separable  
- **F9 (Rastrigin)** – multimodal, separable  
- **F11 (Weierstrass)** – multimodal, non-separable  

---

### Experimental Setup

- Dimensions: ≥10
- Runs per configuration: 10+
- Metric: mean best fitness across runs
- Equal evaluation budget ensured for fair comparison

#### Key Findings

- PSO performed strongly on multimodal and non-separable functions
- GA performed competitively on simpler unimodal landscapes
- Hyperparameters had a significant impact on convergence:
  - Higher crossover rates improved GA performance
  - Moderate swarm sizes (~50) improved PSO stability
- Both methods require careful tuning to avoid premature convergence


| Function | Best Method | Observation |
|----------|------------|-------------|
| F1 | GA ≈ PSO | Fast convergence on simple landscape |
| F2 | PSO | Better handling of non-separability |
| F9 | PSO | Strong performance in multimodal space |
| F11 | PSO | More robust under rugged landscapes |
