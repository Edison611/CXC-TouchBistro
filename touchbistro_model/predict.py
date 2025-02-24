import joblib
import pandas as pd

# Load the trained model
model = joblib.load("touchbistro_model/model.pkl")

# New input data (EXCLUDING the transaction count)
input_data = pd.DataFrame([{
    "concept_BAR": True,  # Replace with actual restaurant concept
    "bill_day_of_week": 5,  # 0=Monday, ..., 6=Sunday
    "date": "2025",  # Actual date
    "bill_hour": 20  # 10 PM
}])

# # Convert date
# new_data["bill_date"] = pd.to_datetime(new_data["date"])
# new_data["month"] = new_data["bill_date"].dt.month
# new_data["day"] = new_data["bill_date"].dt.day
# Drop date column
# new_data.drop(columns=["date", "bill_date"], inplace=True)

# Ensure all missing columns are present
missing_cols = [col for col in model.feature_names_in_ if col not in input_data.columns]
for col in missing_cols:
    input_data[col] = 0  # Fill missing columns with 0

# Reorder columns to match training data
input_data = input_data[model.feature_names_in_]

print(input_data)

# Predict
predicted_transactions = model.predict(input_data)
print(predicted_transactions)
print(f"Predicted Transactions: {predicted_transactions[0]}")
