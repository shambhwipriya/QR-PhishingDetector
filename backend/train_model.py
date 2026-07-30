"""
train_model.py
-----------------
Ye script training_data.csv padhta hai, data ko train/test me split karta hai,
Random Forest model train karta hai, evaluate karta hai (accuracy, precision,
recall, f1-score, confusion matrix), aur trained model ko
phishing_model.pkl naam se save karta hai.
"""

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
)

# ---------- Step 1: Data padhna ----------
print("Step 1: training_data.csv padh rahe hain...")
df = pd.read_csv("training_data.csv")
print(f"Total rows: {len(df)}")
print("Columns:", list(df.columns))

# ---------- Step 2: Features (X) aur Label (y) alag karna ----------
X = df.drop(columns=["label"])
y = df["label"]

print("\nFeature columns used for training:", list(X.columns))

# ---------- Step 3: Train / Test split ----------
print("\nStep 2: Data ko 80% train aur 20% test me split kar rahe hain...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"Training rows: {len(X_train)}")
print(f"Testing rows: {len(X_test)}")

# ---------- Step 4: Random Forest Model Train Karna ----------
print("\nStep 3: Random Forest model train kar rahe hain...")
model = RandomForestClassifier(
    n_estimators=200,      # 200 decision trees
    max_depth=10,          # overfitting rokne ke liye depth limit
    random_state=42,
    n_jobs=-1              # sare CPU cores use karo, fast training
)
model.fit(X_train, y_train)
print("✅ Model training complete!")

# ---------- Step 5: Test data pe prediction ----------
print("\nStep 4: Test data pe evaluate kar rahe hain...")
y_pred = model.predict(X_test)

# ---------- Step 6: Metrics Calculate Karna ----------
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print("\n===================================")
print("        MODEL EVALUATION RESULTS")
print("===================================")
print(f"Accuracy  : {accuracy:.4f}  ({accuracy*100:.2f}%)")
print(f"Precision : {precision:.4f}  ({precision*100:.2f}%)")
print(f"Recall    : {recall:.4f}  ({recall*100:.2f}%)")
print(f"F1-Score  : {f1:.4f}  ({f1*100:.2f}%)")
print("\nConfusion Matrix:")
print("                 Predicted Safe   Predicted Phishing")
print(f"Actual Safe        {cm[0][0]:<15}  {cm[0][1]}")
print(f"Actual Phishing    {cm[1][0]:<15}  {cm[1][1]}")

print("\nDetailed Classification Report:")
print(classification_report(y_test, y_pred, target_names=["Safe", "Phishing"]))

# ---------- Step 7: Feature Importance Dikhana ----------
print("\nFeature Importance (model ke liye kaunsa feature kitna important tha):")
importances = pd.Series(model.feature_importances_, index=X.columns)
importances = importances.sort_values(ascending=False)
print(importances)

# ---------- Step 8: Model Save Karna ----------
joblib.dump(model, "phishing_model.pkl")
print("\n✅ Model saved as 'phishing_model.pkl'")
print("Ab ye file Flask backend (app.py) me use hogi.")
