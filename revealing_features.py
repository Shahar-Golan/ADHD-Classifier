from statistical_features import df_reduced

df = df_reduced

# Rename the column
df = df.rename(columns={'ADHD_2122': 'target'})

# Move the 'target' column to the end
target_column = df.pop('target')
df['target'] = target_column

# 1. How many rows are about to be dropped?
mask = df['target'].isna()
print(f"Rows with null target: {mask.sum()}\n")

# 2. For each of the three columns, show value‐counts in that subset
for col in ['ADHDind_2122', "ADHDMed_2122"]:
    print(f"== Distribution of {col} among rows with null target ==")
    print(df.loc[mask, col].value_counts(dropna=False))
    print()

Revealing_Features = [
    "K2Q31A",  # ADD/ADHD
    "K2Q31B",  # ADD/ADHD currently
    "ADHDind_2122",  # Does this child currently have ADD/ADHD
    "K2Q31D",  # ADD/ADHD - medication currently
    "K2Q31C", "ADHDSevInd_2122",  # Would you describe child's current AD(H)D mild, moderate or severe.
    "ADHDMed_2122",  # is currently taking medication for ADD/ADHD
    "ADDTREAT", "ADHDBehTreat_2122",  # past 12 month behavioral treatment for AD(H)D.
    "MedEmotion_2122"  # Medication for ADD/ADHD, autism/ASD
]

df = df.drop(columns=Revealing_Features, errors='ignore')

to_remove = ['VideoCOVID_2122', 'PrevCOVID_2122', 'Childcare0to5COVID_2122', 'Childcare6to11COVID_2122',
             # COVID-19 related questions
             'ADHDSev_2122',  # found out while running random forest
             'MEDB10ScrQ5_2122',
             'qualnum4_2122',
             'SC_K2Q10',
             'mhealth_2122'
             ]

df = df.drop(columns=to_remove, errors='ignore')
