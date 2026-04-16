import pandas as pd
df = pd.read_csv("sample_dataset.csv")

# STEP 1: FIX COLUMN NAMES FIRST
df.columns = df.columns.str.lower().str.strip()

print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# STEP 2: CLEANING

df = df.drop_duplicates()

# Handle missing values
df['sales'] = df['sales'].fillna(df['sales'].mean())
df['city'] = df['city'].fillna("Unknown")
df['age'] = df['age'].fillna(df['age'].mean())
df['gender'] = df['gender'].fillna("Unknown")
df['profit'] = df['profit'].fillna(df['profit'].mean())
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

# STEP 3: FEATURE ENGINEERING

df['profit_ratio'] = df['profit'] / df['sales']
df['age_group'] = pd.cut(
    df['age'],
    bins=[18, 25, 35, 50, 65],
    labels=["Young", "Adult", "Mid-age", "Senior"]
)

# STEP 4: SAVE CLEAN DATA

df.to_csv("cleaned_dataset.csv", index=False)

print("\n Cleaning Completed Successfully!")