import matplotlib.pyplot as plt

from remove_nulls import df

rare_condition_cols = ["CystFib_2122", "blood_2122", "palsy_2122", "genetic_2122", "DownSynd_2122"]

# 1) How common each condition feature across the whole database (with a positive value)
prevalence = {col: (df[col].isin([2, 3])).sum() for col in rare_condition_cols}
plt.figure(figsize=(8, 4))
plt.bar(prevalence.keys(), prevalence.values())
plt.ylabel('Number of Children')
plt.title('Prevalence of Selected Rare Conditions')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2) How much records we'll drop out of the grand total.
total = len(df)
mask_removed = df[rare_condition_cols].isin([2, 3]).any(axis=1)
removed = mask_removed.sum()
kept = total - removed

plt.figure(figsize=(6, 6))
plt.pie([kept, removed], labels=['Kept', 'Removed'], autopct='%1.1f%%', startangle=90)
plt.title('Dataset Split: Kept vs. Removed Records')
plt.tight_layout()
plt.show()

rare_condition_cols = [col for col in rare_condition_cols if col != "genetic_2122"]
rare_condition_cols = [col for col in rare_condition_cols if col in df.columns]
rare_condition_check = df[rare_condition_cols].fillna(1)
print(f"Rare disease columns found in the dataset: {rare_condition_cols}")

for col in rare_condition_cols:
    print(f"{col}: {df[col].dropna().unique()}")

# Here will filter the rows (inputs) of the subjects that has rare condition/disease

rows_before = df.shape[0]
df = df[~rare_condition_check.isin([2, 3]).any(axis=1)]
rows_after = df.shape[0]
print(f"Dropped {rows_before - rows_after} rows with rare genetic/severe conditions.")
print("New dataset shape: ", df.shape)

df = df.drop(columns=rare_condition_cols)
print(f"Dropped {len(rare_condition_cols)} rare condition columns (now all has a value of 1).")
print("New dataset shape:", df.shape)
