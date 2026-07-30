"""
generate_features.py
----------------------
Ye script clean_dataset.csv (url, label) padhta hai,
har URL ke liye feature.py se features extract karta hai,
aur final training-ready CSV banata hai: training_data.csv
"""

import pandas as pd
from feature import extract_features

print("Step 1: clean_dataset.csv padh rahe hain...")
df = pd.read_csv("clean_dataset.csv")
print(f"Total URLs: {len(df)}")

print("\nStep 2: Har URL se features extract kar rahe hain...")
print("(Isme thoda time lag sakta hai, please wait...)")

feature_rows = []
errors = 0

for i, row in df.iterrows():
    url = str(row["url"])
    label = row["label"]

    try:
        features = extract_features(url)
        features["label"] = label
        feature_rows.append(features)
    except Exception as e:
        errors += 1
        continue

    # Progress dikhane ke liye har 1000 URLs pe update
    if (i + 1) % 1000 == 0:
        print(f"  Processed {i + 1} / {len(df)} URLs...")

print(f"\nTotal errors during feature extraction: {errors}")

# ---------- Final DataFrame banana ----------
features_df = pd.DataFrame(feature_rows)

print("\nStep 3: training_data.csv save kar rahe hain...")
features_df.to_csv("training_data.csv", index=False)

print("\n✅ Done! 'training_data.csv' ban gaya hai.")
print(f"Final shape: {features_df.shape[0]} rows, {features_df.shape[1]} columns")
print("\nColumns:", list(features_df.columns))
print("\nSample rows:")
print(features_df.head())
