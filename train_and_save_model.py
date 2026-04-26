import os
import pickle
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.ensemble import RandomForestClassifier

# =========================================
# 1. Load dataset
# =========================================
file_path = "loan_approval_dataset.csv"

if not os.path.exists(file_path):
    raise FileNotFoundError(f"Dataset not found: {file_path}")

df = pd.read_csv(file_path)
df.columns = df.columns.str.strip()

print("Dataset loaded successfully.")
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())

# =========================================
# 2. Find target column
# =========================================
possible_targets = ["loan_status", "Loan_Status", "status", "loan_approved"]

target_col = None
for col in possible_targets:
    if col in df.columns:
        target_col = col
        break

if target_col is None:
    raise ValueError("Target column not found in dataset.")

print("Target column:", target_col)

# =========================================
# 3. Clean target column
# =========================================
df[target_col] = df[target_col].astype(str).str.strip().str.lower()

# 常见映射：approved / rejected
target_mapping = {
    "approved": 1,
    "rejected": 0,
    "yes": 1,
    "no": 0,
    "1": 1,
    "0": 0
}

df[target_col] = df[target_col].map(target_mapping)

if df[target_col].isnull().sum() > 0:
    raise ValueError("Target column contains unmapped values. Please inspect the original target labels.")

# =========================================
# 4. Split features and target
# =========================================
X = df.drop(columns=[target_col]).copy()
y = df[target_col].copy()

# 删除无用ID列（如果有）
possible_id_cols = ["loan_id", "Loan_ID", "id", "ID"]
for col in possible_id_cols:
    if col in X.columns:
        X = X.drop(columns=[col])

# =========================================
# 5. Encode categorical features
# =========================================
categorical_cols = X.select_dtypes(include=["object"]).columns.tolist()

print("Categorical columns:", categorical_cols)

X = pd.get_dummies(X, columns=categorical_cols, drop_first=False)

feature_columns = X.columns.tolist()

print("Feature columns count:", len(feature_columns))

# =========================================
# 6. Train-test split
# =========================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# =========================================
# 7. Scaling
# =========================================
# 对 RandomForest 来说可以不缩放，这里保留 None
scaler = None

# 如果你后面改成 LogisticRegression，可启用下面两行
# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)

# =========================================
# 8. Train model
# =========================================
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=None,
    random_state=42
)

model.fit(X_train, y_train)

print("Model training completed.")

# =========================================
# 9. Evaluate model
# =========================================
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, zero_division=0)
recall = recall_score(y_test, y_pred, zero_division=0)
f1 = f1_score(y_test, y_pred, zero_division=0)

try:
    y_prob = model.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, y_prob)
except Exception:
    auc = None

metrics = {
    "accuracy": round(accuracy, 4),
    "precision": round(precision, 4),
    "recall": round(recall, 4),
    "f1_score": round(f1, 4),
    "auc": round(auc, 4) if auc is not None else "N/A"
}

print("Metrics:", metrics)

# =========================================
# 10. Save deployment package
# =========================================
deployment_package = {
    "model_name": "Random Forest",
    "model": model,
    "feature_columns": feature_columns,
    "scaler": scaler,
    "metrics": metrics
}

with open("deployment_package.pkl", "wb") as f:
    pickle.dump(deployment_package, f)

print("deployment_package.pkl saved successfully.")

# =========================================
# 11. Verify saved file
# =========================================
with open("deployment_package.pkl", "rb") as f:
    check_package = pickle.load(f)

print("Saved keys:", list(check_package.keys()))
print("Saved model name:", check_package.get("model_name"))
print("Model exists:", check_package.get("model") is not None)
print("Feature columns exists:", check_package.get("feature_columns") is not None)
print("Feature columns sample:", check_package.get("feature_columns")[:10])
print("Metrics:", check_package.get("metrics"))
