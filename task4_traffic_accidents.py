import pandas as pd
import glob

# Load the accident dataset
file_path = glob.glob("dataset/*.csv")[0]
df = pd.read_csv(file_path)

# Dataset shape
print("Dataset Shape:", df.shape)

# First 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Column names
print("\nColumn Names:")
print(df.columns.tolist())
# ----------------------------------------
# Accident Pattern Analysis
# ----------------------------------------

# Convert Start_Time to datetime
df["Start_Time"] = pd.to_datetime(df["Start_Time"], errors="coerce")

# Extract time-related information
df["Hour"] = df["Start_Time"].dt.hour
df["Day"] = df["Start_Time"].dt.day_name()

# Accident count by weather condition
print("\nTop Weather Conditions:")
print(df["Weather_Condition"].value_counts().head(10))

# Accident count by time of day
print("\nAccidents by Hour:")
print(df["Hour"].value_counts().sort_index())

# Accident count by severity
print("\nAccidents by Severity:")
print(df["Severity"].value_counts().sort_index())

# Accident count by Sunrise/Sunset
print("\nAccidents by Sunrise/Sunset:")
print(df["Sunrise_Sunset"].value_counts())

# Accident count by traffic signal
print("\nAccidents at Traffic Signals:")
print(df["Traffic_Signal"].value_counts())
import matplotlib.pyplot as plt

# Create outputs folder if it doesn't exist
import os
os.makedirs("outputs", exist_ok=True)

# 1. Accidents by Hour
plt.figure(figsize=(10, 6))
df["Hour"].value_counts().sort_index().plot(kind="bar")
plt.title("Accidents by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Number of Accidents")
plt.tight_layout()
plt.savefig("outputs/accidents_by_hour.png", dpi=300)
plt.show()


# 2. Accidents by Weather Condition
plt.figure(figsize=(10, 6))
df["Weather_Condition"].value_counts().head(10).sort_values().plot(kind="barh")
plt.title("Top 10 Weather Conditions During Accidents")
plt.xlabel("Number of Accidents")
plt.ylabel("Weather Condition")
plt.tight_layout()
plt.savefig("outputs/accidents_by_weather.png", dpi=300)
plt.show()


# 3. Accidents by Severity
plt.figure(figsize=(8, 5))
df["Severity"].value_counts().sort_index().plot(kind="bar")
plt.title("Accidents by Severity")
plt.xlabel("Severity")
plt.ylabel("Number of Accidents")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("outputs/accidents_by_severity.png", dpi=300)
plt.show()


# 4. Day vs Night
plt.figure(figsize=(7, 5))
df["Sunrise_Sunset"].value_counts().plot(kind="bar")
plt.title("Accidents: Day vs Night")
plt.xlabel("Time of Day")
plt.ylabel("Number of Accidents")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("outputs/accidents_day_night.png", dpi=300)
plt.show()


# 5. Traffic Signal
plt.figure(figsize=(7, 5))
df["Traffic_Signal"].value_counts().plot(kind="bar")
plt.title("Accidents at Traffic Signals")
plt.xlabel("Traffic Signal")
plt.ylabel("Number of Accidents")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("outputs/accidents_traffic_signal.png", dpi=300)
plt.show()
# ----------------------------------------
# Accident Hotspot Analysis
# ----------------------------------------

# Top 10 states with the most accidents
print("\nTop 10 States by Accident Count:")
print(df["State"].value_counts().head(10))


# Top 10 cities with the most accidents
print("\nTop 10 Cities by Accident Count:")
print(df["City"].value_counts().head(10))


# Visualize top 10 states
plt.figure(figsize=(10, 6))
df["State"].value_counts().head(10).sort_values().plot(kind="barh")
plt.title("Top 10 States by Number of Accidents")
plt.xlabel("Number of Accidents")
plt.ylabel("State")
plt.tight_layout()
plt.savefig("outputs/top_10_accident_states.png", dpi=300)
plt.show()


# Visualize top 10 cities
plt.figure(figsize=(10, 6))
df["City"].value_counts().head(10).sort_values().plot(kind="barh")
plt.title("Top 10 Cities by Number of Accidents")
plt.xlabel("Number of Accidents")
plt.ylabel("City")
plt.tight_layout()
plt.savefig("outputs/top_10_accident_cities.png", dpi=300)
plt.show()
# ----------------------------------------
# Final Summary
# ----------------------------------------

print("\n" + "=" * 50)
print("TRAFFIC ACCIDENT ANALYSIS SUMMARY")
print("=" * 50)

print("\nTotal Accidents:", len(df))

print("\nMost Common Weather Condition:")
print(df["Weather_Condition"].value_counts().idxmax())

print("\nMost Common Accident Severity:")
print(df["Severity"].value_counts().idxmax())

print("\nPeak Accident Hour:")
print(df["Hour"].value_counts().idxmax())

print("\nMost Common Accident State:")
print(df["State"].value_counts().idxmax())

print("\nMost Common Accident City:")
print(df["City"].value_counts().idxmax())

print("\nDay vs Night:")
print(df["Sunrise_Sunset"].value_counts())

print("\nAnalysis completed successfully!")