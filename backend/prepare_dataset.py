"""
prepare_dataset.py
--------------------
Ye script raw_dataset (phishing_site_urls.csv) ko padhta hai,
clean karta hai, aur ek balanced dataset banata hai training ke liye.

Input  : phishing_site_urls.csv   (columns: URL, Label with values good/bad)
Output : clean_dataset.csv         (columns: url, label with values 0/1)
"""

import pandas as pd

# ---------- Step 1: Raw CSV padhna ----------
print("Step 1: Raw dataset padh rahe hain...")
df = pd.read_csv("phishing_site_urls.csv")

print(f"Total rows loaded: {len(df)}")
print("Columns found:", list(df.columns))

# ---------- Step 2: Missing values hatana ----------
print("\nStep 2: Missing/empty rows hata rahe hain...")
df = df.dropna(subset=["URL", "Label"])
print(f"Rows after removing missing values: {len(df)}")

# ---------- Step 3: Duplicate URLs hatana ----------
print("\nStep 3: Duplicate URLs hata rahe hain...")
df = df.drop_duplicates(subset=["URL"])
print(f"Rows after removing duplicates: {len(df)}")

# ---------- Step 4: Label ko 0/1 me convert karna ----------
print("\nStep 4: Labels ko convert kar rahe hain (good=0, bad=1)...")
df["label"] = df["Label"].str.strip().str.lower().map({"good": 0, "bad": 1})

# Agar koi row map nahi hui (unexpected label value), use hata do
before = len(df)
df = df.dropna(subset=["label"])
after = len(df)
print(f"Rows dropped due to unexpected label values: {before - after}")

df["label"] = df["label"].astype(int)

# ---------- Step 5: Column rename (URL -> url) ----------
df = df.rename(columns={"URL": "url"})
df = df[["url", "label"]]

# ---------- Step 6: Balanced sample banana ----------
print("\nStep 6: Balanced sample bana rahe hain...")

safe_df = df[df["label"] == 0]
phishing_df = df[df["label"] == 1]

print(f"Total safe URLs available: {len(safe_df)}")
print(f"Total phishing URLs available: {len(phishing_df)}")

SAMPLE_SIZE_PER_CLASS = 5000  # aap chahe to badha/ghata sakte ho

sample_size = min(SAMPLE_SIZE_PER_CLASS, len(safe_df), len(phishing_df))
print(f"Har class se {sample_size} rows liye jayenge (balanced).")

safe_sample = safe_df.sample(n=sample_size, random_state=42)
phishing_sample = phishing_df.sample(n=sample_size, random_state=42)

final_df = pd.concat([safe_sample, phishing_sample])

# Shuffle karna zaroori hai taaki sare safe URLs upar aur phishing niche na ho
final_df = final_df.sample(frac=1, random_state=42).reset_index(drop=True)

# ---------- Step 7: Final CSV save karna ----------
final_df.to_csv("clean_dataset.csv", index=False)

print("\n✅ Done! 'clean_dataset.csv' ban gaya hai.")
print(f"Final dataset size: {len(final_df)} rows")
print(final_df["label"].value_counts())
