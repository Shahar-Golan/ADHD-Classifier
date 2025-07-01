import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, FunctionTransformer, StandardScaler, MaxAbsScaler


# ─── Updated Cell 1: evaluate_model returns a metrics DataFrame ───
def RF_model(X_train, X_test, y_train, y_test,
             numeric_cols, binary_cols, categorical_cols,
             feature_mapping):
    # split validation
    X_val, X_test_final, y_val, y_test_final = train_test_split(
        X_test, y_test, test_size=0.5, stratify=y_test, random_state=42
    )

    # pipeline setup (unchanged)
    numeric_transformer = Pipeline([("imputer", SimpleImputer(strategy="median"))])
    binary_transformer = Pipeline([("imputer", SimpleImputer(strategy="most_frequent"))])
    categorical_transformer = Pipeline([
        ("imputer", SimpleImputer(strategy="constant", fill_value="Missing")),
        ("to_str", FunctionTransformer(lambda df: df.astype(str), validate=False)),
        ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
    ])
    preprocessor = ColumnTransformer([
        ("num", numeric_transformer, numeric_cols),
        ("bin", binary_transformer, binary_cols),
        ("cat", categorical_transformer, categorical_cols),
    ])
    model = Pipeline([
        ("prep", preprocessor),
        ("rf", RandomForestClassifier(
            n_estimators=200, max_depth=10,
            class_weight="balanced", random_state=42)),
    ])

    # fit
    model.fit(X_train, y_train)

    # compute metrics
    results = []
    for name, X_ev, y_ev in [
        ("Train", X_train, y_train),
        ("Validation", X_val, y_val),
        ("Test", X_test_final, y_test_final)
    ]:
        y_pred = model.predict(X_ev)
        acc = model.score(X_ev, y_ev)
        cr = classification_report(y_ev, y_pred, target_names=["No ADHD", "ADHD"], output_dict=True)
        # flatten metrics
        results.append({
            "Set": name,
            "Accuracy": acc,
            "No ADHD Precision": cr["No ADHD"]["precision"],
            "No ADHD Recall": cr["No ADHD"]["recall"],
            "ADHD Precision": cr["ADHD"]["precision"],
            "ADHD Recall": cr["ADHD"]["recall"]
        })

    metrics_df = pd.DataFrame(results).set_index("Set")

    # feature importances (unchanged)
    rf = model.named_steps["rf"]
    prep_step = model.named_steps["prep"]
    num_feats = numeric_cols
    bin_feats = binary_cols
    cat_feats = prep_step.transformers_[2][1] \
        .named_steps["onehot"] \
        .get_feature_names_out(categorical_cols).tolist()
    importances = rf.feature_importances_
    indices = np.argsort(importances)[::-1]
    feat_importance_dict = {
        feature_mapping.get((num_feats + bin_feats + cat_feats)[i]):
            importances[i]
        for i in indices[:20]
    }

    return feat_importance_dict, model, X_test_final, y_test_final, metrics_df


def LR_model(X_train, X_test, y_train, y_test,
             numeric_cols, binary_cols, categorical_cols,
             feature_mapping):
    # split validation/test
    X_val, X_test_final, y_val, y_test_final = train_test_split(
        X_test, y_test, test_size=0.5, stratify=y_test, random_state=42
    )

    # transformers
    numeric_transformer = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ])
    binary_transformer = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("scaler", StandardScaler()),
    ])
    categorical_transformer = Pipeline([
        ("imputer", SimpleImputer(strategy="constant", fill_value="Missing")),
        ("to_str", FunctionTransformer(lambda df: df.astype(str), validate=False)),
        ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
        ("scaler", MaxAbsScaler()),
    ])

    preprocessor = ColumnTransformer([
        ("num", numeric_transformer, numeric_cols),
        ("bin", binary_transformer, binary_cols),
        ("cat", categorical_transformer, categorical_cols),
    ])

    # full pipeline
    model = Pipeline([
        ("prep", preprocessor),
        ("lr", LogisticRegression(
            penalty="l2",
            solver="lbfgs",
            C=0.2,
            max_iter=5000,
            class_weight="balanced",
            random_state=42,
            n_jobs=-1
        ))
    ])

    # fit
    model.fit(X_train, y_train)

    # compute metrics for train/val/test
    records = []
    for name, X_e, y_e in [
        ("Train", X_train, y_train),
        ("Validation", X_val, y_val),
        ("Test", X_test_final, y_test_final)
    ]:
        y_pred = model.predict(X_e)
        acc = model.score(X_e, y_e)
        cr = classification_report(
            y_e, y_pred,
            target_names=["No ADHD", "ADHD"],
            output_dict=True
        )
        records.append({
            "Set": name,
            "Accuracy": acc,
            "No ADHD Precision": cr["No ADHD"]["precision"],
            "No ADHD Recall": cr["No ADHD"]["recall"],
            "ADHD Precision": cr["ADHD"]["precision"],
            "ADHD Recall": cr["ADHD"]["recall"],
        })
    metrics_df = pd.DataFrame(records).set_index("Set")

    # extract top-20 coefficients by absolute value
    lr = model.named_steps["lr"]
    prep_step = model.named_steps["prep"]

    # get one-hot feature names
    cat_feats = prep_step.transformers_[2][1] \
        .named_steps["onehot"] \
        .get_feature_names_out(categorical_cols).tolist()
    all_feats = numeric_cols + binary_cols + cat_feats

    coefs = lr.coef_[0]
    idxs = np.argsort(np.abs(coefs))[::-1][:20]

    feat_importance_dict = {
        feature_mapping.get(all_feats[i], all_feats[i]): coefs[i]
        for i in idxs
    }

    return feat_importance_dict, model, X_test_final, y_test_final, metrics_df
