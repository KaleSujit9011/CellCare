
import pandas as pd
import os

battery = pd.read_csv('../processed/battery_features.csv')
# print(battery.head())
base_dir = os.path.dirname(__file__)  # folder of creating_file.py

# # Sample 1 — Safe battery (early cycles)
safe = battery.iloc[0:1][['C1', 'C2', 'C3', 'C4', 'min_voltage', 'capacity']]
file_path = os.path.join(base_dir, "safe_battery.csv")
safe.to_csv(file_path, index=False)

# # Sample 2 — Warning battery (mid cycles)
warning = battery.iloc[80:81][['C1', 'C2', 'C3', 'C4', 'min_voltage', 'capacity']]
file_path = os.path.join(base_dir, "warning_battery.csv")
warning.to_csv(file_path, index=False)

# # Sample 3 — Dangerous battery (late cycles)
dangerous = battery.iloc[160:161][['C1', 'C2', 'C3', 'C4', 'min_voltage', 'capacity']]
file_path = os.path.join(base_dir, "dangerous_battery.csv")
dangerous.to_csv(file_path, index=False)

print("Demo CSV files created!")