# ==========================================================
# 14. MELT - WIDE TO LONG FORMAT
# ==========================================================

melt_data = df[[
    "employee_name",
    "monthly_salary",
    "annual_salary"
]]

long_format = pd.melt(

    melt_data,

    id_vars=["employee_name"],

    value_vars=["monthly_salary", "annual_salary"],

    var_name="salary_type",

    value_name="salary_amount"

)

print("\n===== MELTED DATA =====")
print(long_format)
