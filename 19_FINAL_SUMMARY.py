# ==========================================================
# 19. FINAL SUMMARY
# ==========================================================

print("\n===== FINAL DATA SUMMARY =====")

print("Total Employees:", len(df))

print(
    "Total Monthly Salary:",
    df["monthly_salary"].sum()
)

print(
    "Average Monthly Salary:",
    round(df["monthly_salary"].mean(), 2)
)

print(
    "Total Departments:",
    df["department"].nunique()
)

print("\nAll Pandas transformations completed successfully!")

print("\nGenerated Files:")
print("1. employees_transformed.csv")
print("2. department_summary.csv")
print("3. employee_analysis.xlsx")
