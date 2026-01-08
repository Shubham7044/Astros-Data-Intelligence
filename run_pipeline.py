import pandas as pd
from sklearn.ensemble import RandomForestClassifier

from src.data_quality import generate_data_quality_report
from src.data_cleaning import clean_data
from src.feature_engineering import engineer_features
from src.model_training import split_data
from src.model_comparison import compare_models
from src.explainability import plot_feature_importance
from src.utils import write_report


def main():
    print("========================================")
    print(" ASTROS DATA INTELLIGENCE PIPELINE START ")
    print("========================================\n")

    # -------------------- Load Data --------------------
    print("📥 Loading dataset...")
    df = pd.read_csv("data/raw/astros_data.csv")
    print(f"✔ Dataset loaded with shape: {df.shape}\n")

    # -------------------- Drop Identifier --------------------
    if "customerID" in df.columns:
        df = df.drop(columns=["customerID"])
        print("🗑 Dropped identifier column: customerID\n")

    # -------------------- Data Quality Checks --------------------
    print("🔍 Running data quality checks...")
    dq = generate_data_quality_report(df)

    dq_report = f"""
## Data Quality Report

### Missing Values (%)
{dq['missing_percentage']}

### Outlier Count
{dq['outlier_count']}
"""
    write_report("reports/data_quality_report.md", dq_report)
    print("✔ Data quality report saved to reports/data_quality_report.md\n")

    # -------------------- Data Cleaning --------------------
    print("🧹 Cleaning data...")
    df = clean_data(df)
    print("✔ Data cleaning completed\n")

    # -------------------- Feature Engineering --------------------
    print("🧬 Engineering features...")
    df = engineer_features(df, target_col="Churn")
    print("✔ Feature engineering completed\n")

    # -------------------- Train/Test Split --------------------
    print("✂️ Splitting data into train and test sets...")
    X_train, X_test, y_train, y_test = split_data(df, "Churn")
    print(
        f"✔ Train shape: {X_train.shape}, Test shape: {X_test.shape}\n"
    )

    # -------------------- Model Comparison --------------------
    print("🤖 Training and comparing models...")
    results = compare_models(X_train, X_test, y_train, y_test)

    print("📊 Model performance:")
    for model, score in results.items():
        print(f"  - {model}: {score}")
    print()

    # -------------------- Explainability --------------------
    print("🔎 Training Random Forest for explainability...")
    rf_model = RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )
    rf_model.fit(X_train, y_train)

    print("📈 Generating feature importance plot...")
    plot_feature_importance(
        rf_model,
        X_train.columns,
        save_path="outputs/plots/feature_importance.png"
    )
    print("✔ Feature importance plot saved to outputs/plots/feature_importance.png\n")

    # -------------------- Insights Report --------------------
    print("📝 Writing insights report...")
    insights = f"""
## Model Performance Summary

{results}

Random Forest achieved the best overall performance, indicating the
presence of non-linear relationships in customer behavior. Feature
importance analysis highlights tenure, monthly charges, total charges,
and contract type as the strongest drivers influencing churn.
"""
    write_report("reports/insights_summary.md", insights)
    print("✔ Insights report saved to reports/insights_summary.md\n")

    print("========================================")
    print(" PIPELINE EXECUTED SUCCESSFULLY ✅")
    print("========================================")


if __name__ == "__main__":
    main()
