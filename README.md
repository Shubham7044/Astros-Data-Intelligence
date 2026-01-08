🚀 Astros Data Intelligence Platform

Overview
The Astros Data Intelligence Platform is a production-grade data science project that demonstrates how real-world data can be validated, processed, modeled, and interpreted to generate actionable business insights.
The focus of this project is not only predictive performance, but also data quality, reproducibility, and explainability, which are critical in real organizational environments.

Business Objective

Customer churn significantly impacts business revenue and long-term growth.

This project aims to:

Predict customer churn using machine learning

Identify the key drivers influencing churn behavior

Provide explainable insights to support data-driven decision-making

Dataset

Name: Telco Customer Churn Dataset

Source: Kaggle (IBM Sample Dataset)

Type: Real-world structured data

Target Variable: Churn (Binary classification)

🔗 Dataset Link:
https://www.kaggle.com/datasets/blastchar/telco-customer-churn

Identifier columns such as customer IDs are intentionally excluded to prevent data leakage.

Key Capabilities

Automated data quality validation (missing values & outliers)

Robust data cleaning and feature engineering

Multiple machine learning model comparison

Explainable AI using feature importance analysis

Automated insight and reporting generation

Fully reproducible and modular pipeline design

Machine Learning Models

The platform benchmarks multiple algorithms to ensure informed model selection:

Logistic Regression

Random Forest Classifier

XGBoost Classifier

Model evaluation is performed using accuracy to compare baseline and ensemble performance.

Model Performance (Sample Results)
Logistic Regression : 0.7986
Random Forest       : 0.7822
XGBoost             : 0.7815


Interpretation:
Strong Logistic Regression performance suggests meaningful linear patterns in churn behavior, while tree-based models capture non-linear relationships and enable explainability.

Explainability & Insights

To ensure transparency and trust, the project includes feature importance analysis.

Key churn drivers identified:

Customer tenure

Monthly and total charges

Contract type

Support and security services

This allows stakeholders to understand why predictions are made, not just what is predicted.

Reporting & Outputs

The pipeline automatically generates:

A Data Quality Report summarizing validation checks

A Model & Business Insights Report highlighting performance and drivers

A saved feature importance visualization for explainability

These artifacts are suitable for both technical review and business discussions.

Key Learnings

Importance of data validation before modeling

Preventing data leakage in ML pipelines

Comparing multiple models for reliable conclusions

Using explainable ML to bridge technical and business understanding

Designing reproducible, production-ready data systems

Future Scope

Hyperparameter tuning and advanced metrics (ROC-AUC, F1)

API deployment using FastAPI

Interactive dashboards (Streamlit / Power BI)

Cloud-based data pipelines and orchestration

Author

Shubham Swarnakar
B.Tech – Computer Science (AIML)
Aspiring Data Scientist | Data Engineer | Machine Learning Engineer

License

This project is licensed under the MIT License.
See the LICENSE
 file for details.

⭐ This repository represents real-world data science practices with emphasis on quality, explainability, and business relevance rather than just model accuracy.
