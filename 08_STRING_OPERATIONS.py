# ==========================================================
# 8. STRING OPERATIONS
# ==========================================================

df["email_domain"] = df["email"].str.split("@").str[1]

df["department_short"] = df["department"].str.replace(
    "Data Engineering", "DE"
)

df["name_length"] = df["employee_name"].str.len()

print("\n===== STRING TRANSFORMATIONS =====")
print(df[[
    "employee_name",
    "email",
    "email_domain",
    "department_short",
    "name_length"
]])
