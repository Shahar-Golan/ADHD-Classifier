# ADHD Classifier 🧠

A reproducible machine-learning pipeline for predicting children at risk of Attention-Deficit/Hyperactivity Disorder (ADHD) using the publicly available National Survey of Children’s Health (NSCH) dataset.

---

## 1  Overview

Early identification of ADHD can improve access to timely interventions.  
This project trains several baseline models (Logistic Regression, Random Forest) and an optimized Random Forest classifier that:

* Ingests raw NSCH survey files (≈ 100 k respondents)  
* Performs automated cleaning, encoding, and feature-engineering  
* Evaluates models with cross-validated metrics and class-imbalance handling  
* Outputs an interpretable report of feature importances and performance scores

The code is modular, so you can swap models or preprocessing steps with minimal changes.

---

## 2  Dataset

| Source | National Survey of Children’s Health (NSCH) |
|--------|---------------------------------------------|
| Years  | 2021 – 2022 (combined PUF files)            |
| Size   | ~ 102 k children, 400 + variables           |
| Access | 🔑 **Required** (free, but registration)    |

1. Request the Public Use File (PUF) via the Child and Adolescent Health Measurement Initiative:  
   <https://www.childhealthdata.org/help/dataset>
2. In the short form indicate: **“Academic research on ADHD classification”** as your purpose.  
3. After approval, download the CSV + codebook zip and place it in the project folder.

## 3  Installation

```bash
# Clone your fork
git clone https://github.com/Shahar-Golan/ADHD-Classifier.git
cd ADHD-Classifier

# Create environment (Python ≥ 3.8 recommended)
python -m venv .venv
source \.venv\Scripts\activate

# Install core dependencies
pip install -r requirements.txt


