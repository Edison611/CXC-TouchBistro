import joblib
import pandas as pd

# Load the trained model
model = joblib.load("touchbistro_model/model.pkl")

# New input data (EXCLUDING the transaction count)
input_data = pd.DataFrame([{
    "concept_BAR": True,  # Replace with actual restaurant concept
    "bill_day_of_week": 4,  # 0=Monday, ..., 6=Sunday
    "date": "2025-01-01",  # Actual date, future concept
    "bill_hour": 22  # 10 PM
}])


# Ensure all missing columns are present
missing_cols = [col for col in model.feature_names_in_ if col not in input_data.columns]
for col in missing_cols:
    input_data[col] = 0  # Fill missing columns with 0

# Reorder columns to match training data
input_data = input_data[model.feature_names_in_]
print(input_data)

# Predict
predicted_transactions = model.predict(input_data)
print(f"Predicted Transactions: {predicted_transactions[0]}")
