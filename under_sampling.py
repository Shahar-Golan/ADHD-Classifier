import pandas as pd
from PIL._imaging import display
from sklearn.utils import resample
from create_dictionary import feature_mapping
from revealing_features import df
from both_models import RF_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

pos = df[df.y == 1]
neg = df[df.y == 0]
df_min, df_maj = (pos, neg) if len(pos) < len(neg) else (neg, pos)
maj_down = resample(df_maj, replace=False,
                    n_samples=len(df_min), random_state=42)
df_bal = pd.concat([df_min, maj_down]).sample(frac=1, random_state=42)
X_bal = df_bal.drop(columns=['target', 'y'])
y_bal = df_bal['y']

print("\n### UNDERSAMPLED DATASET ###")
X = X_bal.copy()
y = y_bal.copy()

numeric_cols = X.select_dtypes(include=["Int64", "int64", "float64"]).columns.tolist()
binary_cols = [c for c in numeric_cols if set(X[c].dropna().unique()) <= {0, 1}]
numeric_cols = [c for c in numeric_cols if c not in binary_cols]
categorical_cols = X.select_dtypes(include=["object", "category"]).columns.tolist()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

feat_imp_bal, model_bal, X_test_final_bal, y_test_final_bal, metric_df_bal = RF_model(
    X_train, X_test, y_train, y_test,
    numeric_cols, binary_cols, categorical_cols,
    feature_mapping
)

display(metric_df_bal)

clean_descs = [desc.split("&")[0].strip() for desc in feat_imp_bal.keys()]
imps = list(feat_imp_bal.values())

plt.figure(figsize=(8, 10))
y_pos = range(len(imps))
plt.barh(y_pos, imps)
plt.yticks(y_pos, clean_descs)
plt.xlabel("Feature Importance")
plt.title("Top 20 Feature Importances (cleaned)")
plt.gca().invert_yaxis()  # highest importance on top
plt.tight_layout()
plt.show()
