import pandas as pd
import matplotlib.pyplot as plt
from handle_rare_disease import df

missing_summary = pd.DataFrame({
    'missing_count': df.isnull().sum(),
    'missing_percent': df.isnull().mean() * 100
})
missing_summary = missing_summary.sort_values(by='missing_percent', ascending=False)
print(missing_summary.head(20))

pct = missing_summary['missing_percent']

plt.figure(figsize=(8, 4))
plt.hist(pct, bins=20, edgecolor='k')
plt.axvline(80, color='r', linestyle='--', label='80% cutoff')
plt.axvline(50, color='orange', linestyle='--', label='50% cutoff')
plt.xlabel('% Missing')
plt.ylabel('Number of features')
plt.title('Distribution of feature missingness')
plt.legend()
plt.tight_layout()
plt.show()

high_missing_cols = missing_summary[missing_summary['missing_percent'] > 80].index.tolist()
print(f"\nNumber of features with >80% missing that we're about to drop: {len(high_missing_cols)}")

df_reduced = df.drop(columns=high_missing_cols)

print("\nSuccessfully dropped features with over 80% missing values.")
print("New shape of dataset: ", df_reduced.shape)

missing_summary.to_csv("missing_summary_before_dropping.csv", index=True)
