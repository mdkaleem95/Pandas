# ==========================================================
# 7. SELECTING ROWS AND COLUMNS
# ==========================================================

# Select specific columns
selected_columns = df[
    ["employee_name", "department", "monthly_salary"]
]

# Select rows using loc
loc_data = df.loc[0:3, ["employee_name", "monthly_salary"]]

# Select rows using iloc
iloc_data = df.iloc[0:5, 0:4]

print("\n===== SELECTED COLUMNS =====")
print(selected_columns)

print("\n===== LOC SELECTION =====")
print(loc_data)

print("\n===== ILOC SELECTION =====")
print(iloc_data)
