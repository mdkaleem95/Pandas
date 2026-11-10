# ==========================================================
# 4. DATA TYPE CONVERSION
# ==========================================================

df["employee_id"] = df["employee_id"].astype(int)

df["salary"] = pd.to_numeric(df["salary"])

df["age"] = df["age"].astype(int)

df["joining_date"] = pd.to_datetime(df["joining_date"])

print("\n===== UPDATED DATA TYPES =====")
print(df.dtypes)
