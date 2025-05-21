import pandas as pd
import matplotlib.pyplot as plt
from main import df

# different missing values across the dataset
missing_values = [95, 99, 90, 96, 995, 998, 999, 9990, 9995, 9999]

# now we'll count the number of instances of each distinct missing value
counts = { mv: df.isin([mv]).sum().sum() for mv in missing_values }


# We'll sort the results
temp = pd.Series(counts)
temp = temp[temp>0].sort_index()
temp.index = temp.index.astype(str)


fig, ax = plt.subplots(figsize=(8,4))
temp.plot(kind='barh', edgecolor='k', legend=False, ax=ax)

x_offset = max(temp.values) * 0.01
for rect in ax.patches:
    width = rect.get_width()
    y = rect.get_y() + rect.get_height() / 2
    # add commas
    ax.text(width + x_offset, y, f"{int(width):,}", va='center')


ax.set_xlabel("Count")
ax.set_ylabel("Missing-Value codes")
plt.title("Counts of different missing-value codes before recoding")
plt.tight_layout()
plt.show()

total = temp.sum()
df.replace(missing_values, np.nan, inplace=True)
print(f"Total missing values that were successfully replaced with NaN: {int(total):,}")