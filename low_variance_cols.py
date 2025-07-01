import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from missing_values import df_reduced



freqs = [
    df_reduced[col].value_counts(normalize=True, dropna=False).values[0]
    for col in df_reduced.columns
]

bins = np.arange(0.90, 1.01, 0.01)

fig, ax = plt.subplots(figsize=(8, 6))
counts, edges, patches = ax.hist(freqs, bins=bins, edgecolor='k')

for count, edge, patch in zip(counts, edges, patches):
    x = edge + patch.get_width() / 2
    y = count
    if count > 0:
        ax.text(x, y + 0.25, f"{int(count)}", ha='center', va='bottom', fontsize=9)

ax.set_xticks(bins)
ax.set_xlim(0.90, 1.00)
ax.set_xlabel("Top-value Frequency")
ax.set_ylabel("Number of Features")
ax.set_title("Distribution of Feature Dominance (Quasi-Constant Check)")
fig.tight_layout()
plt.show()

constant_threshold = 0.99
quasi_constant_cols = []

for col in df_reduced.columns:
    top_freq = df_reduced[col].value_counts(normalize=True, dropna=False).values[0]
    if top_freq >= constant_threshold:
        quasi_constant_cols.append(col)

print(f"Number of constant/quasi-constant features to drop: {len(quasi_constant_cols)}")

df_reduced = df_reduced.drop(columns=quasi_constant_cols)

print("Successfully Dropped constant/quasi-constant features.")
print("New shape of dataset:", df_reduced.shape)
