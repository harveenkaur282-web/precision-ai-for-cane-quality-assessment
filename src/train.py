import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from utils.data_generator import generate_spectral_data
from utils.preprocessing import split_data

def train_model():
    data = generate_spectral_data()
    X_train, X_test, y_train, y_test = split_data(data)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)

    print(f"Model trained successfully.")
    print(f"Mean Absolute Error: {mae:.2f}")

    joblib.dump(model, "src/models/pol_model.pkl")
    print("Model saved to src/models/pol_model.pkl")

if __name__ == "__main__":
    train_model()