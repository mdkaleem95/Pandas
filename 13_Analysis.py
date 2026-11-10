# ==========================================================
# 13. PIVOT TABLE
# ==========================================================

pivot_result = pd.pivot_table(

    df,

    index="department",

    values="monthly_salary",

    aggfunc=["mean", "sum", "count"]

)

print("\n===== PIVOT TABLE =====")
print(pivot_result)
