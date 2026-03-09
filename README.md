# Data Engineering Internship Assessment – Referral Data Analysis

## Project Overview

This project is a **Data Engineering take-home assessment** that analyzes referral program data and validates referral rewards using predefined business logic.

The goal is to process multiple datasets, combine them, and generate a final report identifying whether each referral transaction meets the required business conditions.

The project uses **Python and Pandas** to perform data loading, cleaning, transformation, and validation.

---

## Dataset Files

The following datasets are used in this project:

* lead_log.csv
* paid_transactions.csv
* referral_rewards.csv
* user_logs.csv
* user_referral_logs.csv
* user_referral_statuses.csv
* user_referrals.csv

These datasets represent different parts of a referral system such as users, transactions, referral statuses, and rewards.

---

## Technologies Used

* Python
* Pandas
* CSV Data Processing
* Docker
* GitHub

---

## Project Workflow

1. Load all datasets using Python Pandas.
2. Perform data profiling to check missing values and unique values.
3. Join multiple datasets to create a unified referral dataset.
4. Clean and transform the data.
5. Apply business logic to determine valid referral rewards.
6. Generate the final report.

---

## Business Logic Validation

A referral is considered valid if:

* Reward value is greater than 0
* Transaction status is **PAID**
* Transaction type is **NEW**

The result is stored in the column:

is_business_logic_valid

---

## How to Run the Project

1. Install Python
2. Install Pandas

pip install pandas

3. Run the analysis script

python analysis.py

---

## Output

The script generates the following file:

final_report.csv

This file contains the processed dataset along with the business logic validation results.

---

## Author

Rajesh
Data Engineering Internship Assessment Submission
