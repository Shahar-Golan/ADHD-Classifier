from revealing_features import df
import re

# Cell B: Convert Int-like floats & drop IDs
float_cols = df.select_dtypes("float64").columns.tolist()
int_like = [c for c in float_cols
            if (df[c].dropna() % 1 == 0).all()]

# cast to nullable Int64
df[int_like] = df[int_like].astype("Int64")

# drop structural IDs
to_drop = [c for c in ["HHID", "FIPSST", "STRATUM", "FORMTYPE"] if c in df]
df = df.drop(columns=to_drop)

df = df.dropna(subset=['target']).copy()

df["y"] = df["target"].replace({1: 0, 2: 1, 3: 1})
df.head()

feature_mapping = {}
pattern = re.compile(r'^\s*"([^"]+)"\s*:\s*"(.+?)"\s*,?\s*$')

with open("FeatureMapping.json", "r", encoding="utf-8") as f:
    for line in f:
        m = pattern.match(line)
        if m:
            key, val = m.groups()
            feature_mapping[key] = val

print(f"Loaded {len(feature_mapping)} entries from FeatureMapping.json")

low_var_cols = [col for col in df.columns if df[col].nunique() <= 1]
print("Constant / single-value columns:", low_var_cols)

df = df.drop(columns=low_var_cols)
