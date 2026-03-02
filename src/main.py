import numpy as np
from predict import predict_pol

def simulate_real_time_prediction():
    simulated_input = np.random.normal([0.6, 0.7, 0.8, 0.75], 0.02)
    pol = predict_pol(simulated_input)
    print(f"Real-time Predicted Pol%: {pol:.2f}")

if __name__ == "__main__":
    simulate_real_time_prediction()