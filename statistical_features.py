import pandas as pd
import matplotlib.pyplot as plt
from remove_manually import df_reduced


# National Performance Measure, National Outcome Measure and Standardized Measure
npm_and_nom_drop = [
    "npmExBrstfed6mto2y_2122", "npmDevScrnng_2122", "npmPrevDent1to17_2122", "npmPhysAct6to11_2122",
    "npmFoodSit0to11_2122", "npmPrevMed12to17_2122", "npmMentHTx12to17_2122", "npmMentor12to17_2122",
    "npmPerDrNs_2122","npmPerDrNsCSHCN_2122", "npmUsualSck_2122", "npmUsualSckCSHCN_2122", "npmFamCent_2122",
    "npmFamCentCSHCN_2122", "npmNoRefPrb2_2122", "npmNoRefPrb2CSHCN_2122", "npmCareCoorR_2122",
    "npmCareCoorRCSHCN_2122", "npmMedHome_2122", "npmMedHomeCSHCN_2122", "npmTransition_2122",
    "npmTransitionCSHCN_2122","npmBully12to17_2122","npmBully12to17CSHCN_2122", "npmBullied12to17_2122",
    "npmBullied12to17CSHCN_2122","nomCavities_2122", "nomChHlthSt_2122", "nomObesity6to17_2122",
    "nomBehavior6to11_2122", "nomAnxietyDep12to17_2122", "nomSystCareCSHCN_2122",
    "nomFlrish6mto5_2122", "nomFlrish6to17_2122", "nomFlrish6to17CSHCN_2122", "smSmoking_2122", "smAdeqIns_2122",
    "smForgoneHC_2122", "smPhysAct12to17_2122"
]

# Here we'll drop all the measures calculated on the entire data,
# National Performance Measure, National Outcome Measure and Standardized Mesaure:
to_drop_npm = [col for col in npm_and_nom_drop if col in df_reduced.columns]
df_reduced.drop(columns=to_drop_npm, errors='ignore', inplace=True)

print("All measurment features were successfully dropped!")
print("New shape of our dataset: ", df_reduced.shape)

df_reduced = df_reduced.drop(columns=['STRATUM', 'FORMTYPE', 'fwc_2122'])
