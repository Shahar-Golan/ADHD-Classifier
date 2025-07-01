# ─── Cell: Venn Diagram of Top-10 Feature CODES ───
import matplotlib.pyplot as plt
from IPython.core.display_functions import display
from matplotlib_venn import venn2
import numpy as np
from running_models import numeric_cols, binary_cols, feat_imp_lr, feat_imp_rf, rf_pipe, categorical_cols, lr_pipe

# --- 1) Get raw feature lists & importances from each pipeline ---

# Random Forest
rf = rf_pipe.named_steps["rf"]
prep_rf = rf_pipe.named_steps["prep"]
cat_feats_rf = prep_rf.transformers_[2][1] \
    .named_steps["onehot"] \
    .get_feature_names_out(categorical_cols).tolist()
all_feats_rf = numeric_cols + binary_cols + cat_feats_rf
importances_rf = rf.feature_importances_
# sort and take top 10
idxs_rf = np.argsort(importances_rf)[::-1][:10]
rf_top10_codes = set(all_feats_rf[i] for i in idxs_rf)

# Logistic Regression
lr = lr_pipe.named_steps["lr"]
prep_lr = lr_pipe.named_steps["prep"]
cat_feats_lr = prep_lr.transformers_[2][1] \
    .named_steps["onehot"] \
    .get_feature_names_out(categorical_cols).tolist()
all_feats_lr = numeric_cols + binary_cols + cat_feats_lr
coefs_lr = lr.coef_[0]
# sort by absolute coefficient and take top 10
idxs_lr = np.argsort(np.abs(coefs_lr))[::-1][:10]
lr_top10_codes = set(all_feats_lr[i] for i in idxs_lr)

# --- 2) Compute intersection ---
shared_codes = rf_top10_codes & lr_top10_codes
shared_label = "\n".join(sorted(shared_codes))

# --- 3) Plot the Venn diagram of feature CODES ---
plt.figure(figsize=(8, 6))
venn = venn2(
    subsets=(rf_top10_codes, lr_top10_codes),
    set_labels=("Random Forest", "Logistic Regression")
)
venn.get_label_by_id("11").set_text(shared_label)

plt.title("Top 10 Feature Code Overlap Between Models")
plt.tight_layout()
plt.show()

top_rf = pd.DataFrame({
    "feature": list(feat_imp_rf.keys()),
    "RF Importance": list(feat_imp_rf.values())
}).head(10)

top_lr = pd.DataFrame({
    "feature": list(feat_imp_lr.keys()),
    "LR |Coef|": np.abs(list(feat_imp_lr.values()))
}).head(10)

top_rf["Source"] = "Random Forest"
top_lr["Source"] = "Logistic Regression"

combined_top = pd.concat([
    top_rf[["feature", "Source"]],
    top_lr[["feature", "Source"]]
], axis=0)

combined_summary = (
    combined_top
    .groupby("feature")
    .count()
    .rename(columns={"Source": "Count"})
    .reset_index()
)
combined_summary["Models"] = combined_summary["Count"].map({1: "Unique", 2: "Shared"})

merged = pd.merge(top_rf, top_lr, on="feature", how="outer")
merged = pd.merge(merged, combined_summary[["feature", "Models"]], on="feature", how="left")

merged["RF Importance"] = merged["RF Importance"].fillna(0)
merged["LR |Coef|"] = merged["LR |Coef|"].fillna(0)
merged["Sort Score"] = merged["RF Importance"] + merged["LR |Coef|"]

merged = merged.sort_values(
    by=["Models", "Sort Score"],
    ascending=[False, False]
).reset_index(drop=True)

pd.set_option("display.max_rows", None)
display(merged)
