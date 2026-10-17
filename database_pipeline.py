import pandas as pd
import load as ld
import sqlite3 as sq

connection = sq.connect("insurance.db")

ld.data.to_sql("claims_data", connection, if_exists="replace", index=False)

query = """
SELECT 
    CAR_TYPE, 
    COUNT(*) AS Total_Policies,
    ROUND(AVG(CLM_AMT), 2) AS Avg_Claim_Amount,
    ROUND(AVG(INCOME), 2) AS Avg_Income,
    ROUND(SUM(CLM_AMT), 2) AS Total_Claim_Liability
FROM claims_data
GROUP BY CAR_TYPE
ORDER BY Avg_Claim_Amount DESC;
"""

results = pd.read_sql(query, connection)
print(results)
connection.close()