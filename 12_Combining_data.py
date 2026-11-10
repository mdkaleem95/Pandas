# ==========================================================
# 12. CONCATENATION
# ==========================================================

new_employees = pd.DataFrame({

    "employee_id": [110, 111],
    "employee_name": ["Imran", "Zoya"],
    "department": ["DevOps", "HR"],
    "monthly_salary": [88000, 72000],
    "age": [29, 26],
    "joining_date": pd.to_datetime(
        ["2025-01-10", "2025-02-15"]
    )

})

combined_data = pd.concat(
    [df, new_employees],
    ignore_index=True
)

print("\n===== CONCATENATED DATA =====")
print(combined_data)
