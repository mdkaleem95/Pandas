# ==========================================================
# 10. GROUP BY AND AGGREGATIONS
# ==========================================================

department_summary = df.groupby("department").agg(

    total_employees=("employee_id", "count"),

    average_salary=("monthly_salary", "mean"),

    maximum_salary=("monthly_salary", "max"),

    minimum_salary=("monthly_salary", "min"),

    total_salary=("monthly_salary", "sum")

).reset_index()

print("\n===== DEPARTMENT SUMMARY =====")
print(department_summary)
