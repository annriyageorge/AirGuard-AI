import pandas as pd

# Load dataset
df = pd.read_csv("Air_quality_data.csv")

print("Original shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Pollutant columns needed for AirGuard AI
pollutants = [
    "PM2.5",
    "PM10",
    "NO2",
    "SO2",
    "CO",
    "O3"
]

# Convert pollutant columns to numeric
for col in pollutants:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Convert AQI to numeric
df["AQI"] = pd.to_numeric(df["AQI"], errors="coerce")

# Remove rows where AQI is missing
df = df.dropna(subset=["AQI"])

# Fill missing pollutant values with median
for col in pollutants:
    df[col] = df[col].fillna(df[col].median())

# Remove impossible negative values
for col in pollutants:
    df = df[df[col] >= 0]

# Save cleaned dataset
df.to_csv("air_quality_cleaned.csv", index=False)

print("\nCleaned shape:", df.shape)

print("\nRemaining missing values:")
print(df[pollutants + ["AQI", "AQI_Bucket"]].isnull().sum())

print("\nAQI categories:")
print(df["AQI_Bucket"].value_counts())

print("\nSaved as: air_quality_cleaned.csv")