import pandas as pd
import matplotlib.pyplot as plt
from grouping_features import df_reduced

df = df_reduced

adhd_col = 'ADHDind_2122' # column that indicates an ADHD diagnosis

adhd_positive = df[df[adhd_col] == 3] # that means adhd = true
adhd_negative = df[df[adhd_col] == 2] # that means adhd = false
adhd_diagnoised = df[df[adhd_col].isin([2, 3])] # all positivly diagnosed past & present
adhd_undiagnoised = df[df[adhd_col] == 1] # those who does not have the condition

print("Number of diagnosed ADHD cases, those who has the condition: ", adhd_positive.shape[0])
print("Number of previously diagnosed ADHD cases, that got negative response ", adhd_negative.shape[0])
print("Number of all diagnosed ADHD cases, previously & currently: ", adhd_diagnoised.shape[0])
print("Number of non-diagnosed or unknown ADHD cases: ", adhd_undiagnoised.shape[0])


labels = [
    "Positive ADHD (3)",
    "Negative ADHD (2)",
    "Undiagnosed/Unknown (1)"
]
counts = [
    adhd_positive.shape[0],
    adhd_negative.shape[0],
    adhd_undiagnoised.shape[0]
]

colors = ['red', 'red', 'blue']  # Color map for bars

# Plot
plt.figure(figsize=(8, 5))
bars = plt.bar(labels, counts, color=colors, edgecolor='k')

# Add value labels on top
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height, f"{height:,}",
             ha='center', va='bottom')

plt.ylabel("Number of Individuals")
plt.title("ADHD Diagnosis Distribution")
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()

# Features that revealing the target column,
# potential to remove before modeling.

IMPORTANT_LABELS = [
    "K2Q31A",  # ADD/ADHD
    "K2Q31B",  # ADD/ADHD currently
    "ADHDind_2122",  # Does this child currently have ADD/ADHD
    "K2Q31D",  # ADD/ADHD - medication currently
    "K2Q31A", "K2Q31B", "K2Q31C", "ADHDSevInd_2122",
    # Would you describe child's current AD(H)D mild, moderate or severe.
    "K2Q31A", "K2Q31B", "K2Q31D", "ADHDMed_2122",  # is currently taking medication for ADD/ADHD
    "K2Q31A", "K2Q31B", "ADDTREAT", "ADHDBehTreat_2122",  # past 12 month behavioral treatment for AD(H)D.
    "MedEmotion_2122",  # Medication for ADD/ADHD, autism/ASD
]
