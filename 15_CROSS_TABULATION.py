# ==========================================================
# 15. CROSS TABULATION
# ==========================================================

cross_tab = pd.crosstab(
    df["department"],
    df["salary_category"]
)

print("\n===== CROSS TABULATION =====")
print(cross_tab)
