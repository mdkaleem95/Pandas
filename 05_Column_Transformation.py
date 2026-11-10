# ==========================================================
# 5. COLUMN OPERATIONS
# ==========================================================

# Rename columns
df = df.rename(columns={
    "name": "employee_name",
    "salary": "monthly_salary"
})

# Add new calculated columns
df["annual_salary"] = df["monthly_salary"] * 12

df["annual_bonus"] = df["annual_salary"] * 0.10

df["total_compensation"] = (
    df["annual_salary"] + df["annual_bonus"]
)

# Create conditional column
df["salary_category"] = np.where(
    df["monthly_salary"] >= 100000,
    "High Salary",
    "Standard Salary"
)

# Apply custom transformation
df["employee_name"] = df["employee_name"].apply(
    lambda name: name.upper()
)

print("\n===== TRANSFORMED COLUMNS =====")
print(df)
