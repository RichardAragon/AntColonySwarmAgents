import numpy as np
import random

# Define the Queen with Improved Stagnation Response
class QueenAgent:
    def __init__(self):
        self.memory = []  # Stores past decisions and their outcomes
        self.strategy_changes = 0  # Track how often swarm strategies are adjusted
        self.history = []  # Tracks rolling accuracy for stagnation detection

    def decide_adjustments(self, swarm_results, stagnation_count):
        """Determine adjustments based on swarm performance and past experiences."""
        avg_accuracy = sum([r[2] for r in swarm_results]) / len(swarm_results)
        self.history.append(avg_accuracy)

        # Ensure rolling memory does not exceed 3 rounds
        if len(self.history) > 3:
            self.history.pop(0)

        # Detect if accuracy has not improved for 2 consecutive rounds
        if len(self.history) >= 2 and len(set(self.history[-2:])) == 1:
            stagnation_count = 2  # Force stagnation detection

        adjustments = []

        if stagnation_count >= 2:  # If stagnation persists, force changes
            self.strategy_changes += 1
            for worker in swarm:
                # 30% chance of full mutation (worker is entirely reset)
                if random.random() < 0.3:
                    worker.update_strategy(random.choice(["random", "pattern", "majority", "hybrid"]))
                else:
                    worker.update_strategy(self.fuse_strategies())

                worker.update_learning_rate()
                adjustments.append(worker.id)
            
            return f"Queen detected stagnation and forced {len(adjustments)} workers to evolve."

        return "Queen maintains current strategy. No significant stagnation detected."
    
    def fuse_strategies(self):
        """Creates a new strategy by fusing two existing ones."""
        base_strategies = ["random", "pattern", "majority", "hybrid"]
        return f"{random.choice(base_strategies)}-{random.choice(base_strategies)}"


# Define the Worker Agents
class WorkerAgent:
    def __init__(self, id, strategy, learning_rate):
        self.id = id
        self.strategy = strategy
        self.learning_rate = learning_rate
        self.accuracy = random.uniform(0.4, 0.6)
        self.fib_step = 1
        self.fitness = 0

    def perform_task(self, data):
        """Simulated classification task."""
        if self.strategy == "random":
            return random.choice([0, 1])
        elif self.strategy == "pattern":
            return 1 if sum(data) % 2 == 0 else 0
        elif self.strategy == "majority":
            return 1 if sum(data) > len(data) / 2 else 0
        elif "hybrid" in self.strategy:
            return 1 if (sum(data) % 3 == 0 and sum(data) > 5) else 0
        elif "-" in self.strategy:  # Handle fused strategies
            strat1, strat2 = self.strategy.split("-")
            return 1 if (self.perform_task_strategy(strat1, data) + self.perform_task_strategy(strat2, data)) % 2 == 0 else 0

    def perform_task_strategy(self, strat, data):
        """Helper function for fused strategies."""
        if strat == "random":
            return random.choice([0, 1])
        elif strat == "pattern":
            return 1 if sum(data) % 2 == 0 else 0
        elif strat == "majority":
            return 1 if sum(data) > len(data) / 2 else 0
        else:
            return 0

    def update_strategy(self, new_strategy):
        """Updates worker's strategy."""
        self.strategy = new_strategy
    
    def update_learning_rate(self):
        """Fibonacci-inspired adaptive learning rate increase."""
        fib_sequence = [0, 1]
        for _ in range(self.fib_step):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        self.learning_rate += fib_sequence[-1] * 0.001
        self.fib_step += 1


# Initialize Queen and Swarm
queen = QueenAgent()
num_workers = 10
swarm = [WorkerAgent(i, random.choice(["random", "pattern", "majority", "hybrid"]), random.uniform(0.01, 0.1)) for i in range(num_workers)]

# Define Task Data (Binary Classification)
num_samples = 100
dataset = [np.random.randint(0, 2, size=10).tolist() for _ in range(num_samples)]
true_labels = [random.choice([0, 1]) for _ in range(num_samples)]

# Multi-Round Learning with More Aggressive Stagnation Response
num_rounds = 5
stagnation_count = 0
last_avg_accuracy = 0

for round_num in range(num_rounds):
    results = []
    for worker in swarm:
        worker_results = [worker.perform_task(sample) for sample in dataset]
        accuracy = sum([1 if worker_results[i] == true_labels[i] else 0 for i in range(num_samples)]) / num_samples
        worker.accuracy = accuracy
        worker.fitness += accuracy
        results.append((worker.id, worker.strategy, accuracy))

    # Detect stagnation with rolling history
    avg_accuracy = sum([r[2] for r in results]) / len(results)
    if avg_accuracy <= last_avg_accuracy:
        stagnation_count += 1
    else:
        stagnation_count = 0  # Reset stagnation counter if improvement occurs

    last_avg_accuracy = avg_accuracy

    # Queen makes adaptive decisions based on memory
    queen_response = queen.decide_adjustments(results, stagnation_count)

    # Store round results
    print(f"\nRound {round_num + 1}:")
    print("\n".join([f"Worker {r[0]} used {r[1]} strategy, accuracy: {r[2]:.2f}" for r in results]))
    print(f"{queen_response}\n")

# Final swarm status after all rounds
final_swarm_results = [(worker.id, worker.strategy, worker.accuracy) for worker in swarm]

# Output Final Evolution Results
import pandas as pd
df = pd.DataFrame(final_swarm_results, columns=["Worker ID", "Final Strategy", "Final Accuracy"])
