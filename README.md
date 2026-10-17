# Actuarial Risk and Claims Data Analyzer

## Overview
This project provides an end-to-end data pipeline and risk modeling framework for automotive insurance claims. It covers data cleaning, relational database integration via SQLite, actuarial risk metric calculations, and automated report generation in Excel format.

The primary objective is to evaluate portfolio-level financial exposure by estimating severity metrics and downside tail risk using Value at Risk (VaR).

## Architecture & Data Flow
1. Data Ingestion & Cleaning (`data_cleaning.py`)
   - Handles missing categorical values via imputation.
   - Applies numerical median imputation for key policy features.
   - Cleans financial fields by stripping currency symbols and casting to appropriate data types.

2. Database Pipeline (`database_pipeline.py`)
   - Stores cleaned policy data into an SQLite relational database (`insurance.db`).
   - Executes structured SQL queries to aggregate policy counts and total liabilities by car type.

3. Actuarial Risk Modeling (`model.py`)
   - Filters active claim instances (`CLM_AMT > 0`).
   - Calculates key statistical metrics:
     - Expected Loss (Average Severity)
     - Loss Variance
     - Loss Standard Deviation
     - Value at Risk (VaR) at 95% confidence level using non-parametric percentile estimation.

4. Executive Reporting (`report.py`)
   - Queries summary metrics and vehicle category breakdowns from SQLite.
   - Generates a multi-tab Excel report (`insurance_risk_report.xlsx`) using Pandas and OpenPyXL with adjusted column widths.

## Key Metrics Summary
Based on the default dataset analysis:
- Total Insured Policies: 10,302
- Policies with Claims: 2,746
- Expected Loss: \$5,669.73
- Loss Standard Deviation: \$7,759.06
- Value at Risk (VaR 95%): \$16,801.75

## Technology Stack
- Python 3.x
- Pandas & NumPy (Data Processing and Numerical Calculations)
- SQLite3 (Relational Database Storage)
- OpenPyXL (Excel Report Generation)

## Project Structure
├── data_cleaning.py       # Raw data preprocessing and sanitization
├── database_pipeline.py   # SQLite table creation and data insertion
├── model.py               # Actuarial risk modeling script
├── report.py              # Automated Excel report generation script
├── car_insurance_claim.csv # Raw dataset
├── .gitignore             # Ignored files for version control
└── README.md              # Project documentation

## How to Run
1. Install required dependencies:
   pip install pandas numpy openpyxl

2. Run the pipeline step-by-step:
   python data_cleaning.py
   python database_pipeline.py
   python model.py
   python report.py
