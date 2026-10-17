import pandas as pd
import numpy as np
import sqlite3 as sq

connection = sq.connect("insurance.db")
claims_data = pd.read_sql("SELECT * FROM claims_data", connection)

summary_query = """
SELECT 
    CAR_TYPE AS "Car Type", 
    COUNT(*) AS "Total Policies",
    ROUND(AVG(CLM_AMT), 2) AS "Avg Claim Amount",
    ROUND(SUM(CLM_AMT), 2) AS "Total Liability"
FROM claims_data
GROUP BY CAR_TYPE
ORDER BY "Avg Claim Amount" DESC;
"""
summary_df = pd.read_sql(summary_query, connection)
connection.close()

claims = claims_data[claims_data['CLM_AMT'] > 0]['CLM_AMT']
metrics = {
    "Actuarial Metric": [
        "Total Insured Policies",
        "Policies with Claims",
        "Expected Loss",
        "Loss Variance",
        "Loss Standard Deviation",
        "VaR (95% Confidence Level)"
    ],
    "Value": [
        len(claims_data),
        len(claims),
        claims.mean(),
        claims.var(),
        claims.std(),
        np.percentile(claims, 95)
    ]
}
metrics_df = pd.DataFrame(metrics)

output = "insurance_risk_report.xlsx"
with pd.ExcelWriter(output, engine='openpyxl') as writer:
    summary_df.to_excel(writer, sheet_name="Summary", index=False)
    metrics_df.to_excel(writer, sheet_name="Metrics", index=False)

