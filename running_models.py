import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from IPython.display import display
from sklearn.model_selection import train_test_split

from both_models import RF_model, LR_model
from create_dictionary import feature_mapping
from revealing_features import df

# --- 1) Original dataset ---
print("### ORIGINAL DATASET ###")
X = df.drop(columns=["target", "y"])
y = df["y"]

# identify columns
numeric_cols = X.select_dtypes(include=["Int64", "int64", "float64"]).columns.tolist()
binary_cols = [c for c in numeric_cols if set(X[c].dropna().unique()) <= {0, 1}]
numeric_cols = [c for c in numeric_cols if c not in binary_cols]
categorical_cols = X.select_dtypes(include=["object", "category"]).columns.tolist()

# split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# ─── Cell 1: Run RF & LR, display their metrics, and build comparison_df ───


# 1) Run Random Forest
feat_imp_rf, rf_pipe, X_test_rf, y_test_rf, metrics_rf = RF_model(
    X_train, X_test, y_train, y_test,
    numeric_cols, binary_cols, categorical_cols,
    feature_mapping
)
print("### Random Forest Metrics ###")
display(metrics_rf)

# 2) Run Logistic Regression
feat_imp_lr, lr_pipe, X_test_lr, y_test_lr, metrics_lr = LR_model(
    X_train, X_test, y_train, y_test,
    numeric_cols, binary_cols, categorical_cols,
    feature_mapping
)
print("### Logistic Regression Metrics ###")
display(metrics_lr)

# 3) Extract Test‐set row and build comparison_df
rf_scores = metrics_rf.loc["Test"]
lr_scores = metrics_lr.loc["Test"]

comparison_df = pd.DataFrame({
    "Random Forest": rf_scores,
    "Logistic Regression": lr_scores
}).T.round(4)

print("=== Model Comparison (Test Set) ===")
display(comparison_df)

# consistent palette for the two models
palette = sns.color_palette("Set2", n_colors=2)

ax = comparison_df.T.plot(
    kind="bar",
    figsize=(10, 6),
    title="Model Comparison (Test Set Metrics)",
    color=palette
)
plt.ylabel("Score")
plt.xticks(rotation=45)
plt.grid(axis="y")
plt.legend(title="Model")
plt.tight_layout()
plt.show()

clean_descs = [desc.split("&")[0].strip() for desc in feat_imp_rf.keys()]
imps = list(feat_imp_rf.values())

plt.figure(figsize=(8, 10))
y_pos = range(len(imps))
plt.barh(y_pos, imps)
plt.yticks(y_pos, clean_descs)
plt.xlabel("Feature Importance")
plt.title("Top 20 Feature Importances (cleaned)")
plt.gca().invert_yaxis()  # highest importance on top
plt.tight_layout()
plt.show()
