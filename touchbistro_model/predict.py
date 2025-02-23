import joblib
import pandas as pd

# Load the trained model
model = joblib.load("touchbistro_model/model.pkl")

# New input data (EXCLUDING the transaction count)
new_data = pd.DataFrame([{
    "concept": "BAR",  # Replace with actual restaurant concept
    "day_of_week": 1,  # 1=Monday, ..., 7=Sunday
    "date": "2024-12-25",  # Actual date
    "hour": 4  # 6 PM
}])

# Convert date
new_data["bill_date"] = pd.to_datetime(new_data["date"])
new_data["year"] = new_data["bill_date"].dt.year
new_data["month"] = new_data["bill_date"].dt.month
new_data["day"] = new_data["bill_date"].dt.day
new_data["week_of_year"] = new_data["bill_date"].dt.isocalendar().week
new_data["is_weekend"] = new_data["day_of_week"].apply(lambda x: 1 if x in [6, 7] else 0)

# Drop date column
new_data.drop(columns=["date", "bill_date"], inplace=True)

# Ensure all missing columns are present
missing_cols = [col for col in model.feature_names_in_ if col not in new_data.columns]
for col in missing_cols:
    new_data[col] = 0  # Fill missing columns with 0

# Reorder columns to match training data
new_data = new_data[model.feature_names_in_]

# Convert types to float
new_data = new_data.astype("float32")

# Predict
predicted_transactions = model.predict(new_data)
print(f"Predicted Transactions: {predicted_transactions[0]}")
