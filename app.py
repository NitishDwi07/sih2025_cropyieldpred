from fastapi import FastAPI
import joblib
import pandas as pd
import json

app = FastAPI()

# ------------------------
# Load models dynamically
# ------------------------
def load_model_and_features(crop):
    model = joblib.load(f"{crop}_best_model.pkl")
    features = joblib.load(f"{crop}_features.pkl")
    return model, features

# ------------------------
# Recommendations helper
# ------------------------
def post_ml_recommendations(soil_moisture, rainfall_percent, humidity_percent):
    recommendations = []
    if soil_moisture < 20:
        recommendations.append(f"Soil moisture {soil_moisture}% → Increase irrigation.")
    if rainfall_percent < 75:
        recommendations.append(f"Rainfall {rainfall_percent}% of avg → Supplemental irrigation.")
    if humidity_percent > 85:
        recommendations.append(f"High humidity {humidity_percent}% → Possible fungal outbreak, preventively spray fungicide.")
    if not recommendations:
        recommendations.append("No immediate action required.")
    return recommendations

# ------------------------
# API endpoint
# ------------------------
@app.post("/predict/{crop}")
async def predict_crop(crop: str, input_json: dict):
    try:
        model, features = load_model_and_features(crop)

        # Convert to DataFrame
        input_df = pd.DataFrame([input_json])

        # One-hot encode categorical columns
        input_encoded = pd.get_dummies(input_df, columns=['season', 'state'], drop_first=True)

        # Align with training features
        for col in features:
            if col not in input_encoded.columns:
                input_encoded[col] = 0
        input_encoded = input_encoded[features]

        # Predict
        prediction = model.predict(input_encoded)[0]

        # Recommendations
        soil_moisture = input_json.get("soil_moisture", 25)
        rainfall_percent = input_json.get("rainfall_percent", 100)
        humidity_percent = input_json.get("avg_humidity_percent", 70)
        recommendations = post_ml_recommendations(soil_moisture, rainfall_percent, humidity_percent)

        return {
            "crop": crop,
            "predicted_yield": round(float(prediction), 2),
            "recommendations": recommendations
        }

    except Exception as e:
        return {"error": str(e)}