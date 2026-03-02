import joblib
import pandas as pd

def predict_pol(input_features):
    model = joblib.load("src/models/pol_model.pkl")
    
    # Convert input into DataFrame with proper feature names
    feature_names = ["band_1", "band_2", "band_3", "band_4"]
    input_df = pd.DataFrame([input_features], columns=feature_names)
    
    prediction = model.predict(input_df)
    return prediction[0]

if __name__ == "__main__":
    sample_input = [0.62, 0.71, 0.79, 0.76]
    result = predict_pol(sample_input)
    print(f"Predicted Pol%: {result:.2f}")