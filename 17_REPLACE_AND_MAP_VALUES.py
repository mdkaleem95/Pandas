# ==========================================================
# 17. REPLACE AND MAP VALUES
# ==========================================================

df["department_code"] = df["department"].map({

    "Data Engineering": "DE",
    "DevOps": "DO",
    "HR": "HR",
    "Finance": "FIN"

})

df["salary_category"] = df["salary_category"].replace({

    "High Salary": "Premium",
    "Standard Salary": "Regular"

})

print("\n===== MAPPED AND REPLACED VALUES =====")
print(df[[
    "employee_name",
    "department",
    "department_code",
    "salary_category"
]])
