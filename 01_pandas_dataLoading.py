pip install pandas numpy openpyxl

# ==========================================================
# PROJECT: PANDAS DATA TRANSFORMATION
# Description: Employee Data Cleaning and Transformation
# ==========================================================

import pandas as pd
import numpy as np

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 150)


# ==========================================================
# 1. CREATE SAMPLE DATASETS
# ==========================================================

employees = pd.DataFrame({

    "employee_id": [101, 102, 103, 104, 105, 106, 106, 107, 108, 109],
    "name": ["Kaleem", "Ali", "Ahmed", "Sara", "John",
             "David", "David", "Maria", "Robert", "Fatima"],
    "department": ["Data Engineering", "DevOps", "HR",
                   "Data Engineering", "Finance", "DevOps",
                   "DevOps", "HR", "Finance", "Data Engineering"],
    "salary": [110000, 90000, 75000, np.nan, 85000,
               95000, 95000, 70000, np.nan, 120000],
    "age": [31, 28, 35, 29, np.nan, 32, 32, 27, 40, 30],
    "joining_date": ["2022-01-15", "2023-03-10", "2021-06-20",
                     "2022-08-12", "2020-05-18", "2023-01-25",
                     "2023-01-25", "2024-02-01", "2021-09-15",
                     "2022-11-05"],
    "email": ["kaleem@gmail.com", "ali@gmail.com", "ahmed@gmail.com",
              "sara@gmail.com", "john@gmail.com", "david@gmail.com",
              "david@gmail.com", "maria@gmail.com", "robert@gmail.com",
              "fatima@gmail.com"]

})

departments = pd.DataFrame({

    "department": ["Data Engineering", "DevOps", "HR", "Finance"],
    "manager": ["Manager A", "Manager B", "Manager C", "Manager D"],
    "location": ["Hyderabad", "Bangalore", "Mumbai", "Pune"]

})
