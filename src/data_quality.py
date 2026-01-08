import numpy as np

def generate_data_quality_report(df):
    report = {}

    report["missing_percentage"] = (
        df.isnull().sum() / len(df) * 100
    ).round(2).to_dict()

    numeric_cols = df.select_dtypes(include=np.number)
    outliers = {}

    for col in numeric_cols:
        Q1 = numeric_cols[col].quantile(0.25)
        Q3 = numeric_cols[col].quantile(0.75)
        IQR = Q3 - Q1
        outliers[col] = int(
            ((numeric_cols[col] < Q1 - 1.5 * IQR) |
             (numeric_cols[col] > Q3 + 1.5 * IQR)).sum()
        )

    report["outlier_count"] = outliers
    return report
