
import pandas as pd

# Load dataset
df = pd.read_csv("marketing_campaign.csv", sep='\t')

# Handle missing values
income_median = df['Income'].median()
df['Income'] = df['Income'].fillna(income_median)

# Remove duplicates
df = df.drop_duplicates()

# Standardize column names
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Convert date column to datetime format
df['dt_customer'] = pd.to_datetime(df['dt_customer'], format='%d-%m-%Y', errors='coerce')

# Standardize text values
df['education'] = df['education'].str.lower().str.strip()
df['marital_status'] = df['marital_status'].str.lower().str.strip()

# Save cleaned dataset
df.to_csv("marketing_campaign_cleaned.csv", index=False)

print("✅ Data cleaning complete. Cleaned file saved as 'marketing_campaign_cleaned.csv'.")
