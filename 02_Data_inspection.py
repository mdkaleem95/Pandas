# ==========================================================
# 2. LOAD AND INSPECT DATA
# ==========================================================

# Save sample input data
employees.to_csv("employees_raw.csv", index=False)

# Read CSV file
df = pd.read_csv("employees_raw.csv")

print("\n===== ORIGINAL DATA =====")
print(df)

print("\n===== DATASET INFORMATION =====")
print(df.info())

print("\n===== STATISTICAL SUMMARY =====")
print(df.describe())

print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())

print("\n===== DATASET SHAPE =====")
print(df.shape)
