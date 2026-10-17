import pandas as pd
import numpy as np
import sqlite3 as sq

connection = sq.connect("insurance.db")
database = pd.read_sql("SELECT * FROM claims_data", connection)
connection.close()

claims = database[database["CLM_AMT"]>0]['CLM_AMT']

expected_loss = claims.mean()
variance_loss = claims.var()
std_deviation_loss = claims.std()

var_95 = np.percentile(claims, 95)

print(f"Total Insured Policies: {len(database):,}")
print(f"Policies with Claims: {len(claims):,}")
print(f"Expected Loss: ${expected_loss:,.2f}")
print(f"Variance Loss: {variance_loss:,.2f}")
print(f"Standard Deviation Loss: ${std_deviation_loss:,.2f}")
print(f"VaR(95%): ${var_95:,.2f}")