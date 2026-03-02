import numpy as np
import pandas as pd

def generate_spectral_data(samples=500):
    np.random.seed(42)
    
    # Simulated spectral bands (like NIR wavelengths)
    band_1 = np.random.normal(0.6, 0.05, samples)
    band_2 = np.random.normal(0.7, 0.04, samples)
    band_3 = np.random.normal(0.8, 0.03, samples)
    band_4 = np.random.normal(0.75, 0.02, samples)

    # Simulated relationship to Pol%
    pol_percentage = (
        20 * band_1 +
        15 * band_2 +
        10 * band_3 +
        12 * band_4 +
        np.random.normal(0, 0.5, samples)
    )

    data = pd.DataFrame({
        "band_1": band_1,
        "band_2": band_2,
        "band_3": band_3,
        "band_4": band_4,
        "pol_percentage": pol_percentage
    })

    return data