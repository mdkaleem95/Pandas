# ==========================================================
# 16. RANKING AND BINNING
# ==========================================================

df["salary_rank"] = df["monthly_salary"].rank(
    ascending=False,
    method="dense"
)

df["age_group"] = pd.cut(

    df["age"],

    bins=[0, 25, 35, 45, 100],

    labels=["Below 25", "26-35", "36-45", "Above 45"]

)

print("\n===== RANKING AND AGE GROUPS =====")
print(df[[
    "employee_name",
    "monthly_salary",
    "salary_rank",
    "age_group"
]])
