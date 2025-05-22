# ADHD Classifier 🧠

This project aims to develop a machine learning-based classifier to help identify children likely to be diagnosed with Attention Deficit Hyperactivity Disorder (ADHD), using data from the National Survey of Children’s Health (NSCH).

## 📊 Dataset

The dataset is derived from the [NSCH](https://www.cdc.gov/nchs/slaits/nsch.htm), containing demographic and health-related survey responses from parents of over 100,000 children in the U.S. It includes features such as:
- Child age, sex, race
- Medical conditions and behavioral history
- Family background and environment

## ⚙️ Preprocessing Steps

1. **Null filtering**: Removed features with >80% nulls, and entries with >80% null values.
2. **Low variance**: Dropped columns with very low variability across samples.
3. **Redundancy**: Removed manually known redundant or irrelevant features.
4. **Feature engineering**: Created new statistical groupings and behavior-based flags.
5. **Target preparation**: Created a binary classification label based on ADHD diagnosis.

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- Install required packages:
  ```bash
  pip install pandas numpy matplotlib
