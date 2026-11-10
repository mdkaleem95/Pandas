# ==========================================================
# 3. DATA CLEANING
# ==========================================================

# Remove duplicate employee records
df = df.drop_duplicates()

# Handle missing salary values
df["salary"] = df["salary"].fillna(df["salary"].median())

# Handle missing age values
df["age"] = df["age"].fillna(df["age"].median())

# Remove leading/trailing spaces and standardize text
df["name"] = df["name"].str.strip().str.title()

df["department"] = (
    df["department"].str.strip().str.title()
)

# Standardize email addresses
df["email"] = df["email"].str.strip().str.lower()

print("\n===== CLEANED DATA =====")
print(df)

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DUPLICATE COUNT =====")
print(df.duplicated().sum())
