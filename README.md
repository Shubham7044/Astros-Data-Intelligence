🚀 Astros Data Intelligence Platform

End-to-End Data Science & Machine Learning Pipeline

📌 Overview

The Astros Data Intelligence Platform is a production-style, end-to-end data science project that demonstrates how raw, real-world data can be transformed into actionable insights using structured preprocessing, machine learning, and explainable AI techniques.

This project is designed to reflect industry-level data science workflows, focusing on automation, reproducibility, and interpretability rather than just model accuracy.

🎯 Problem Statement

Customer churn is a major business challenge where organizations lose customers due to pricing, service quality, or contract factors.

Objective:

Predict whether a customer is likely to churn

Identify the key factors driving churn

Generate interpretable insights that support data-driven decisions

📂 Dataset

Dataset: Telco Customer Churn Dataset
🔗 Telco Customer Churn (IBM sample dataset)
👉 https://www.kaggle.com/datasets/blastchar/telco-customer-churn

Type: Real-world structured dataset

Target Variable: Churn (Binary Classification)

Dataset Characteristics

Combination of numerical and categorical features

Customer demographics, service usage, and billing information

Cleaned and validated through automated data quality checks

Identifier columns such as customerID are removed to prevent data leakage.

🏗️ Project Structure
Astros-Data-Intelligence/
│
├── data/
│   └── raw/                     # Dataset location (not committed)
│
├── src/
│   ├── data_quality.py          # Data validation & outlier detection
│   ├── data_cleaning.py         # Missing value handling & cleanup
│   ├── feature_engineering.py   # Encoding & scaling
│   ├── model_training.py        # Train-test split
│   ├── model_comparison.py      # ML model benchmarking
│   ├── explainability.py        # Feature importance analysis
│   └── utils.py                 # Report utilities
│
├── reports/
│   ├── data_quality_report.md   # Data quality summary
│   └── insights_summary.md      # Model & business insights
│
├── outputs/
│   └── plots/
│       └── feature_importance.png
│
├── run_pipeline.py              # One-command pipeline execution
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md

🔍 Key Features
✅ Automated Data Quality Checks

Missing value percentage per feature

Outlier detection using IQR method

Auto-generated data quality report

✅ Data Cleaning & Feature Engineering

Missing value handling

Categorical feature encoding

Feature scaling (excluding target variable)

Leakage-safe preprocessing

✅ Machine Learning Models

The following models are trained and compared:

Logistic Regression

Random Forest Classifier

XGBoost Classifier

Model performance is evaluated using accuracy.

📊 Model Performance (Sample Run)
Logistic Regression : 0.7986
Random Forest       : 0.7822
XGBoost             : 0.7815


Insight:
Logistic Regression performs strongly, indicating meaningful linear patterns in churn behavior, while tree-based models help capture non-linear relationships and provide explainability.

🔎 Explainable AI (XAI)

To ensure transparency and trust, the project includes feature importance analysis using Random Forest.

Key Drivers of Churn

Customer tenure

Monthly and total charges

Contract type

Support and security services

The feature importance visualization is automatically generated and saved at:

outputs/plots/feature_importance.png

📝 Automated Reports

After each pipeline run, the following reports are generated:

Data Quality Report
reports/data_quality_report.md

Model Performance & Business Insights
reports/insights_summary.md

These reports are suitable for technical review and business interpretation.

▶️ How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/Shubham7044/Astros-Data-Intelligence.git
cd Astros-Data-Intelligence

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Add Dataset

Place the dataset file at:

data/raw/astros_data.csv

5️⃣ Run the Pipeline
python run_pipeline.py

✅ Output After Execution

Console logs showing each pipeline stage

Auto-generated data quality and insight reports

Feature importance plot saved to disk

Fully automated, end-to-end execution

🧠 Key Learnings

Importance of validating data quality before modeling

Preventing data leakage in ML pipelines

Comparing multiple ML models for informed decisions

Using explainability to make ML models business-friendly

Designing reproducible and production-ready pipelines

🚀 Future Enhancements

Hyperparameter tuning (GridSearch / RandomSearch)

Additional evaluation metrics (ROC-AUC, F1-Score)

REST API deployment using FastAPI

Interactive dashboard using Streamlit or Power BI

Cloud-based data pipelines and orchestration

👤 Author

Shubham Swarnakar
B.Tech – Computer Science (AIML)
Aspiring Data Scientist | Data Engineer | Machine Learning Engineer

📜 License

This project is licensed under the MIT License.
See the LICENSE
 file for details.

⭐ This project demonstrates real-world data science practices, focusing on automation, explainability, and business-driven insights rather than just model accuracy.
