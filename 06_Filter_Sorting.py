# ==========================================================
# 6. FILTERING AND SORTING
# ==========================================================

# Filter employees with salary above 90000
high_salary = df[df["monthly_salary"] > 90000]

# Multiple conditions
data_engineers = df[
    (df["department"] == "Data Engineering") &
    (df["monthly_salary"] >= 90000)
]

# Filter using isin()
selected_departments = df[
    df["department"].isin(["DevOps", "Finance"])
]

# Filter using query()
young_employees = df.query("age < 35")

# Sort by salary in descending order
sorted_employees = df.sort_values(
    by="monthly_salary",
    ascending=False
)

print("\n===== HIGH SALARY EMPLOYEES =====")
print(high_salary)

print("\n===== DATA ENGINEERS =====")
print(data_engineers)

print("\n===== SORTED EMPLOYEES =====")
print(sorted_employees)
