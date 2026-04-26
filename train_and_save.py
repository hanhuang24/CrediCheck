import pickle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix,
    roc_curve,
    roc_auc_score
)

# =========================
# 1. Compare tuned models
# =========================
final_compare = pd.DataFrame({
    'Model': ['Logistic Regression', 'Decision Tree', 'Random Forest'],
    'Best_CV_Score': [
        grid_log.best_score_,
        grid_dt.best_score_,
        grid_rf.best_score_
    ]
}).sort_values(by='Best_CV_Score', ascending=False)

print("Tuned Model Comparison:")
print(final_compare)

# =========================
# 2. Select best model
# =========================
best_model_name = final_compare.iloc[0]['Model']
print("\nBest Model Selected:", best_model_name)

if best_model_name == 'Logistic Regression':
    final_model = best_log_model
    X_test_final = X_test_scaled
    scaler_to_save = scaler
elif best_model_name == 'Decision Tree':
    final_model = best_dt_model
    X_test_final = X_test
    scaler_to_save = None
else:
    final_model = best_rf_model
    X_test_final = X_test
    scaler_to_save = None

# =========================
# 3. Final evaluation
# =========================
y_pred_final = final_model.predict(X_test_final)
y_prob_final = final_model.predict_proba(X_test_final)[:, 1]

acc = accuracy_score(y_test, y_pred_final)
pre = precision_score(y_test, y_pred_final)
rec = recall_score(y_test, y_pred_final)
f1 = f1_score(y_test, y_pred_final)
auc = roc_auc_score(y_test, y_prob_final)

print(f"\nFinal Model: {best_model_name}")
print("-" * 40)
print("Accuracy :", round(acc, 4))
print("Precision:", round(pre, 4))
print("Recall   :", round(rec, 4))
print("F1-score :", round(f1, 4))
print("AUC      :", round(auc, 4))

print("\nClassification Report:")
print(classification_report(y_test, y_pred_final))

# =========================
# 4. Confusion Matrix
# =========================
cm = confusion_matrix(y_test, y_pred_final)
plt.figure(figsize=(5, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title(f'Confusion Matrix - Final Model ({best_model_name})')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.tight_layout()
plt.show()

# =========================
# 5. ROC Curve
# =========================
fpr, tpr, _ = roc_curve(y_test, y_prob_final)
plt.figure(figsize=(6, 4))
plt.plot(fpr, tpr, label=f'{best_model_name} (AUC = {auc:.3f})')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title(f'ROC Curve - Final Model ({best_model_name})')
plt.legend()
plt.tight_layout()
plt.show()

# =========================
# 6. Feature Importance
# =========================
if best_model_name in ['Decision Tree', 'Random Forest']:
    importances = final_model.feature_importances_
    feature_importance_df = pd.DataFrame({
        'Feature': X_train.columns,
        'Importance': importances
    }).sort_values(by='Importance', ascending=False)

    plt.figure(figsize=(8, 5))
    sns.barplot(
        data=feature_importance_df.head(10),
        x='Importance',
        y='Feature',
        palette='Blues_r'
    )
    plt.title(f'Top 10 Feature Importances - {best_model_name}')
    plt.xlabel('Importance')
    plt.ylabel('Feature')
    plt.tight_layout()
    plt.show()

# =========================
# 7. Save deployment package
# =========================
deployment_package = {
    "model_name": best_model_name,
    "model": final_model,
    "feature_columns": X_train.columns.tolist(),
    "scaler": scaler_to_save,
    "metrics": {
        "accuracy": round(acc, 4),
        "precision": round(pre, 4),
        "recall": round(rec, 4),
        "f1_score": round(f1, 4),
        "auc": round(auc, 4)
    }
}

with open("deployment_package.pkl", "wb") as f:
    pickle.dump(deployment_package, f)

print("\nSaved deployment_package.pkl successfully")