Crop Yield ML Module

This module predicts crop yield and provides actionable recommendations for irrigation and crop management based on user input and real-time weather data. It currently supports Rice, Maize, Potato, Sugarcane, and Wheat.

User Inputs Required: 
- Crop
- Season
- State
- Area
- Production
- Fertilizer
- Pesticide
- Soil nutrients (N, P, K)
- Soil pH
- City
- Soil moisture (%)
- Rainfall (% relative to historical average)

Outputs: 
- Predicted yield (tons/hectare) 
- Post-ML recommendations for irrigation or fungicide application.

Files for Integration:
- ML models: <crop>_best_model.pkl
- Feature files: <crop>_features.pkl
- Crop mapping: crop_models_mapping.json

Notes:
- Uses OpenWeatherMap API for real-time weather (API key stored in .env).
- Only the above files are required for integration; .env and any checkpoint/temporary files should not be entertained.

-----------------------------------------------------
USAGE INSTRUCTIONS:

1. Install dependencies:
   pip install -r requirements.txt

2. Prepare input data:
   Create a JSON file (e.g., input.json) with the following format:
   {
     "crop": "Rice",
     "season": "Kharif",
     "state": "Assam",
     "area": 1000,
     "production": 800,
     "fertilizer": 500,
     "pesticide": 50,
     "N": 40,
     "P": 20,
     "K": 30,
     "soil_pH": 6.5,
     "city": "Guwahati",
     "soil_moisture": 25,
     "rainfall": 80
   }

3. Run prediction:
   python scripts/run_prediction.py --input input.json

4. Output:
   - Predicted crop yield in tons/hectare
   - Recommendations for irrigation and crop management
   (Displayed in terminal or can be returned as JSON if integrated with a backend)

5. Testing models (optional):
   python scripts/testpickelfile.py
   (verifies that all models and feature files load correctly)
