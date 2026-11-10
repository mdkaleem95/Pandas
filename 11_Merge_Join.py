# ==========================================================
# 11. MERGE AND JOIN
# ==========================================================

# Merge employee and department datasets
merged_data = pd.merge(

    df,
    departments,
    on="department",
    how="left"

)

print("\n===== MERGED DATA =====")
print(merged_data)

# Demonstrate inner join
inner_join = pd.merge(
    df,
    departments,
    on="department",
    how="inner"
)

print("\n===== INNER JOIN =====")
print(inner_join)
