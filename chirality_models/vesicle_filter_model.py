# chirality_models/vesicle_filter_model.py

import numpy as np
import matplotlib.pyplot as plt

def simulate_vesicle_filtering(cycles=100, absorption_bias=0.03):
    """Simulate enantioselective filtering by vesicle membranes."""
    population = {'L': 500, 'D': 500}
    logs = []

    for _ in range(cycles):
        population['L'] *= (1 + absorption_bias)
        population['D'] *= (1 - absorption_bias)
        total = population['L'] + population['D']
        logs.append((population['L'] / total, population['D'] / total))

    return np.array(logs)

if __name__ == "__main__":
    data = simulate_vesicle_filtering()
    plt.plot(data[:, 0], label='L-Protected')
    plt.plot(data[:, 1], label='D-Exposed')
    plt.title("Vesicle Filtering of Chiral Molecules")
    plt.xlabel("Cycles")
    plt.ylabel("Relative Concentration")
    plt.legend()
    plt.grid(True)
    plt.show()

