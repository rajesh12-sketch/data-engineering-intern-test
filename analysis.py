import pandas as pd

print("Starting Data Engineer Test Script...")

# -----------------------------
# 1. Load CSV Files
# -----------------------------
lead_logs = pd.read_csv("lead_log.csv")
paid_transactions = pd.read_csv("paid_transactions.csv")
referral_rewards = pd.read_csv("referral_rewards.csv")
user_logs = pd.read_csv("user_logs.csv")
user_referral_logs = pd.read_csv("user_referral_logs.csv")
user_referral_statuses = pd.read_csv("user_referral_statuses.csv")
user_referrals = pd.read_csv("user_referrals.csv")

print("All datasets loaded successfully")

# -----------------------------
# 2. Data Profiling
# -----------------------------
print("\nNull values in user_referrals:")
print(user_referrals.isnull().sum())

print("\nDistinct values in user_referrals:")
print(user_referrals.nunique())

# -----------------------------
# 3. Join Tables
# -----------------------------

# Join referral statuses
data = user_referrals.merge(
    user_referral_statuses,
    left_on="user_referral_status_id",
    right_on="id",
    how="left"
)

# Join referral rewards
data = data.merge(
    referral_rewards,
    left_on="referral_reward_id",
    right_on="id",
    how="left"
)

# Join transactions
data = data.merge(
    paid_transactions,
    on="transaction_id",
    how="left"
)

# Join user info (referrer)
data = data.merge(
    user_logs,
    left_on="referrer_id",
    right_on="user_id",
    how="left"
)

print("All tables joined successfully")

# -----------------------------
# 4. Data Cleaning
# -----------------------------

# Convert reward_value to numeric (fix error)
data["reward_value"] = pd.to_numeric(data["reward_value"], errors="coerce")

# Fill missing values
data["reward_value"] = data["reward_value"].fillna(0)

# -----------------------------
# 5. Create Referral Source Category
# -----------------------------

def referral_source_category(row):
    if row["referral_source"] == "User Sign Up":
        return "Online"
    elif row["referral_source"] == "Draft Transaction":
        return "Offline"
    elif row["referral_source"] == "Lead":
        return "Lead"
    else:
        return "Unknown"

data["referral_source_category"] = data.apply(referral_source_category, axis=1)

# -----------------------------
# 6. Business Logic Validation
# -----------------------------

data["is_business_logic_valid"] = (
    (data["reward_value"] > 0) &
    (data["transaction_status"] == "PAID") &
    (data["transaction_type"] == "NEW")
)

# -----------------------------
# 7. Select Final Report Columns
# -----------------------------

final_report = data[[
    "referral_id",
    "referral_source",
    "referral_source_category",
    "referral_at",
    "referrer_id",
    "referee_id",
    "referee_name",
    "referee_phone",
    "transaction_id",
    "transaction_status",
    "transaction_type",
    "reward_value",
    "is_business_logic_valid"
]]

# -----------------------------
# 8. Export Final CSV
# -----------------------------

final_report.to_csv("final_report.csv", index=False)

print("\nFinal report created successfully!")
print("Total rows in report:", len(final_report))
print("File saved as final_report.csv")
print("Rows in final report:", len(final_report))