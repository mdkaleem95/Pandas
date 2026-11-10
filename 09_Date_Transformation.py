# ==========================================================
# 9. DATE TRANSFORMATIONS
# ==========================================================

# Extract date components
df["joining_year"] = df["joining_date"].dt.year

df["joining_month"] = df["joining_date"].dt.month

df["joining_day"] = df["joining_date"].dt.day

# Calculate employee tenure
today = pd.Timestamp.today().normalize()

df["experience_days"] = (
    today - df["joining_date"]
).dt.days

print("\n===== DATE TRANSFORMATIONS =====")
print(df[[
    "employee_name",
    "joining_date",
    "joining_year",
    "joining_month",
    "experience_days"
]])
