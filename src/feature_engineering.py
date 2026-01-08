from sklearn.preprocessing import LabelEncoder, StandardScaler

def engineer_features(df, target_col):
    df = df.copy()

    # Encode categorical columns
    le = LabelEncoder()
    for col in df.select_dtypes(include="object").columns:
        if col != target_col:
            df[col] = le.fit_transform(df[col])

    # Encode target separately (KEEP AS 0/1)
    if df[target_col].dtype == "object":
        df[target_col] = df[target_col].map({"No": 0, "Yes": 1})

    # Scale ONLY feature columns
    feature_cols = df.drop(columns=[target_col]).columns
    scaler = StandardScaler()
    df[feature_cols] = scaler.fit_transform(df[feature_cols])

    return df
