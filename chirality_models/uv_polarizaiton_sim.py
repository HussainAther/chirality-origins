# chirality_models/uv_polarization_sim.py

import numpy as np
import matplotlib.pyplot as plt

def simulate_uv_exposure(time_steps=100, light_bias=0.02):
    """Simulate enantiomeric excess due to circularly polarized UV light."""
    racemic_mixture = {'L': 0.5, 'D': 0.5}
    history = []

    for _ in range(time_steps):
        racemic_mixture['L'] *= (1 + light_bias)
        racemic_mixture['D'] *= (1 - light_bias)
        total = racemic_mixture['L'] + racemic_mixture['D']
        racemic_mixture['L'] /= total
        racemic_mixture['D'] /= total
        history.append((racemic_mixture['L'], racemic_mixture['D']))

    return np.array(history)

if __name__ == "__main__":
    data = simulate_uv_exposure()
    plt.plot(data[:, 0], label='L-Amino Acids')
    plt.plot(data[:, 1], label='D-Amino Acids')
    plt.title("Chiral Bias Under Circularly Polarized UV")
    plt.xlabel("Time Steps")
    plt.ylabel("Fraction")
    plt.legend()
    plt.grid(True)
    plt.show()

