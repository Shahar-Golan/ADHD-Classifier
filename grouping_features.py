import pandas as pd
import matplotlib.pyplot as plt
from statistical_features import df_reduced


# 1) Compute unique non-null counts per column
unique_counts = df_reduced.nunique(dropna=True)

# 2) Total features
total_feats = df_reduced.shape[1]

# 3) Classify by number of unique values
binary_feats      = unique_counts[unique_counts == 2].index.tolist()
categorical_feats = unique_counts[unique_counts == 3].index.tolist()
numerical_feats   = unique_counts[unique_counts > 3].index.tolist()

# 4) Print summary
print(f"Total features: {total_feats}")
print(f"Binary features (2 values, NaN excluded): {len(binary_feats)}")
print(f"Categorical features (3 values, NaN excluded): {len(categorical_feats)}")
print(f"Numerical features (>3 values, NaN excluded): {len(numerical_feats)}")

# 5) (Optional) List them (only first 10)
print("\nBinary feature list (top 10):")
for f in binary_feats[:10]:
    print(" •", f)

print("\nCategorical feature list (top 10):")
for f in categorical_feats[:10]:
    print(" •", f)

print("\nNumerical feature list (top 10):")
for f in numerical_feats[:10]:
    print(" •", f)


types = [len(binary_feats), len(categorical_feats), len(numerical_feats)]
plt.figure(figsize=(4,3))
plt.bar(["Binary","Cat (3)","Numeric"], types, color=['C0','C1','C2'])
plt.ylabel("Number of Features")
plt.title("Feature Type Breakdown")
plt.tight_layout()
plt.show()

unique_counts2 = unique_counts.drop(index=['HHID'], errors='ignore')
cardinality_counts = unique_counts2.value_counts().sort_index()

unique_counts2_sorted = unique_counts2.sort_values(ascending=False)
unique_counts2_sorted.head(10)

# We'll recreate the same graph, but this time will focues on 0-20 number of features

plt.figure(figsize=(10,5))
bars = plt.bar(cardinality_counts.index, cardinality_counts.values, width=0.5)
for bar in bars:
    cnt = int(bar.get_height())
    if bar.get_x() <= 20:
        plt.text(bar.get_x() + bar.get_width()/2, cnt + 0.5, str(cnt), ha='center', va='bottom', fontsize=9)
plt.xlim(0, 20)
plt.xticks(range(0,21,1))
plt.xlabel('Number of different values per Feature')
plt.ylabel('Number of Features')
plt.title('Feature Cardinality (0-20 values)')
plt.tight_layout()
plt.show()
