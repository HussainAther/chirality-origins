# __main__.py

import argparse
from chirality_models import uv_polarization_sim, vesicle_filter_model, autocatalysis_model
import pandas as pd
import os

def save_to_csv(data, filename):
    df = pd.DataFrame(data, columns=["L", "D"])
    os.makedirs("output", exist_ok=True)
    df.to_csv(f"output/{filename}", index=False)
    print(f"Saved results to output/{filename}")

def main():
    parser = argparse.ArgumentParser(description="Run chirality simulations.")
    parser.add_argument("--model", type=str, choices=["uv", "vesicle", "autocatalysis"], required=True, help="Model to run.")
    parser.add_argument("--steps", type=int, default=100, help="Number of steps/cycles to simulate.")
    parser.add_argument("--bias", type=float, default=0.02, help="Bias or strength parameter.")
    args = parser.parse_args()

    if args.model == "uv":
        data = uv_polarization_sim.simulate_uv_exposure(time_steps=args.steps, light_bias=args.bias)
        save_to_csv(data, "uv_polarization.csv")

    elif args.model == "vesicle":
        data = vesicle_filter_model.simulate_vesicle_filtering(cycles=args.steps, absorption_bias=args.bias)
        save_to_csv(data, "vesicle_filter.csv")

    elif args.model == "autocatalysis":
        data = autocatalysis_model.autocatalytic_chirality_sim(steps=args.steps, feedback_strength=args.bias)
        save_to_csv(data, "autocatalysis.csv")

if __name__ == "__main__":
    main()

