from fastapi import FastAPI
import pandas as pd
from ucimlrepo import fetch_ucirepo

app = FastAPI()

# Fetch dataset
bank_marketing = fetch_ucirepo(id=222)
X = bank_marketing.data.features
y = bank_marketing.data.targets

# Combine features and targets into one DataFrame
df = pd.concat([X, y], axis=1)

@app.get("/")
def home():
    return {"message": "Welcome to the Bank Marketing Dataset API"}

@app.get("/data")
def get_data():
    try:
        print("📢 Debug: /data endpoint accessed")
        print(f"✅ Data shape: {df.shape}")  # Check if data exists

        # Convert NaN and Infinite values to None (JSON-compliant)
        cleaned_df = df.replace([float("inf"), float("-inf")], None)
        cleaned_df = cleaned_df.fillna(value="Unknown")  # ✅ Replace NaN with "Unknown"




        return cleaned_df.to_dict(orient="records")
    except Exception as e:
        print(f"❌ ERROR in /data: {str(e)}")
        return {"error": str(e)}

    try:
        print("📢 Debug: /data endpoint accessed")
        print(f"✅ Data shape: {df.shape}")  # Check if data exists

        # Replace NaN and Infinite values
        cleaned_df = df.replace([float("inf"), float("-inf")], None)  # Convert infinite values to None
        cleaned_df = cleaned_df.fillna(None)  # Convert NaN to None

        return cleaned_df.to_dict(orient="records")
    except Exception as e:
        print(f"❌ ERROR in /data: {str(e)}")
        return {"error": str(e)}

@app.get("/metadata")
def get_metadata():
    return bank_marketing.metadata

@app.get("/variables")
def get_variables():
    return bank_marketing.variables
