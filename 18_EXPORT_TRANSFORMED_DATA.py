# ==========================================================
# 18. EXPORT TRANSFORMED DATA
# ==========================================================

# Export final employee dataset
df.to_csv(
    "employees_transformed.csv",
    index=False
)

# Export department summary
department_summary.to_csv(
    "department_summary.csv",
    index=False
)

# Export results into Excel
with pd.ExcelWriter("employee_analysis.xlsx") as writer:

    df.to_excel(
        writer,
        sheet_name="Employees",
        index=False
    )

    department_summary.to_excel(
        writer,
        sheet_name="Department Summary",
        index=False
    )

    merged_data.to_excel(
        writer,
        sheet_name="Merged Data",
        index=False
    )
