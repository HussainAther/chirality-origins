# chirality_models/autocatalysis_model.py

import numpy as np
import matplotlib.pyplot as plt

def autocatalytic_chirality_sim(steps=100, feedback_strength=0.05):
    """Simulate autocatalytic amplification of chirality."""
    L, D = 1.0, 1.0
    trace = []

    for _ in range(steps):
        rate_L = L * (1 + feedback_strength * L)
        rate_D = D * (1 + feedback_strength * D)
        L, D = rate_L, rate_D
        total = L + D
        L /= total
        D /= total
        trace.append((L, D))

    return np.array(trace)

if __name__ == "__main__":
    result = autocatalytic_chirality_sim()
    plt.plot(result[:, 0], label='L-Amino Acids')
    plt.plot(result[:, 1], label='D-Amino Acids')
    plt.title("Autocatalytic Chiral Amplification")
    plt.xlabel("Time Steps")
    plt.ylabel("Relative Concentration")
    plt.legend()
    plt.grid(True)
    plt.show()

