from sklearn.model_selection import train_test_split

def validate_target(y):
    unique = y.unique()
    if not set(unique).issubset({0, 1}):
        raise ValueError("Target column is not binary classification")

def split_data(df, target):
    X = df.drop(target, axis=1)
    y = df[target]

    return train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
