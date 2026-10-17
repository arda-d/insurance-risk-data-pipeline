import pandas as pd
import numpy as np

data = pd.read_csv("car_insurance_claim.csv")

financial_cols = ["INCOME", "HOME_VAL", "BLUEBOOK", "OLDCLAIM", "CLM_AMT"]
for column in financial_cols:
    if column in data.columns:
        cleaned_series = (data[column]
                          .astype(str)
                          .str.replace('$', '', regex=False)
                          .str.replace(',', '', regex=False)
                          .str.strip()
                          )
        cleaned_series = cleaned_series.replace(['nan', 'None', '', 'null', 'NaN'], np.nan)
        data[column] = pd.to_numeric(cleaned_series, errors='coerce')

numeric_cols = ["AGE", "YOJ", "INCOME", "HOME_VAL", "CAR_AGE", "BLUEBOOK", "OLDCLAIM", "CLM_AMT"]
for column in numeric_cols:
    if column in data.columns:
        median_val = data[column].median()
        data[column] = data[column].fillna(median_val)

data["OCCUPATION"] = data["OCCUPATION"].fillna("Unknown")