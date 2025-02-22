# Ant Colony Swarm Agents

## Overview
**Ant Colony Swarm Agents** is an advanced swarm intelligence framework developed by **Moonshot Laboratories** under the **MIT License**. This project implements an AI-based swarm system where a **Queen Agent** governs **Worker Agents**, optimizing their performance through multi-round learning, stagnation detection, and strategy evolution.

The Queen dynamically adjusts strategies based on stagnation detection, enabling aggressive forced evolution, strategy fusion, and worker mutations. The framework integrates **Fibonacci-based learning rates** to enhance adaptive learning.

## Features
- **Queen-Controlled Swarm Optimization**: The Queen Agent governs Worker Agents, detects stagnation, and forces strategic adjustments.
- **Aggressive Stagnation Detection**: The system actively detects performance stagnation and triggers worker strategy modifications.
- **Forced Strategy Fusion**: The Queen can fuse multiple strategies to create hybrid solutions.
- **Worker Mutations**: Workers have a chance to mutate their strategies for better performance.
- **Fibonacci-Based Learning Rates**: Learning rates adapt dynamically following a Fibonacci-inspired progression.
- **Multi-Round Evolution**: The system iteratively refines strategies over multiple training rounds.
- **Binary Classification Task**: Workers perform a simulated classification task to evaluate performance.

## Installation
### Requirements
This project runs on **Python 3.8+** and requires the following dependencies:
```sh
pip install numpy pandas
```

## Usage
To run the swarm simulation, execute the following command:
```sh
python ant_colony_swarm.py
```

### Example Output
The system runs over multiple rounds, displaying worker performance and Queen decisions:
```
Round 1:
Worker 0 used majority strategy, accuracy: 0.52
Worker 1 used random strategy, accuracy: 0.47
...
Queen detected stagnation and forced 6 workers to evolve.
...
```
At the end of all rounds, a **final summary** of worker evolution and performance is generated.

## Code Structure
- **`QueenAgent`**: Governs the swarm, detects stagnation, and enforces strategy changes.
- **`WorkerAgent`**: Executes tasks using different strategies and updates its learning rate based on Fibonacci progression.
- **`Swarm Simulation`**: Runs multiple learning rounds where workers attempt to optimize their accuracy.

## Future Enhancements
- **Adaptive Exploration Strategies**: Implement reinforcement learning for workers to dynamically explore strategies.
- **Parallelized Execution**: Enable multi-threading for large-scale simulations.
- **Extended Problem Domains**: Expand beyond binary classification tasks.

## License
This project is licensed under the **MIT License**. Feel free to modify and use it as needed.

## Acknowledgments
Developed by **Moonshot Laboratories** as part of research into **swarm intelligence and AI-driven optimization.**
