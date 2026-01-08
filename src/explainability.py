import matplotlib.pyplot as plt
import pandas as pd
import os

def plot_feature_importance(model, feature_names, save_path=None):
    importance = model.feature_importances_

    df = pd.DataFrame({
        "Feature": feature_names,
        "Importance": importance
    }).sort_values(by="Importance", ascending=False)

    plt.figure(figsize=(10, 6))
    plt.barh(df["Feature"], df["Importance"])
    plt.gca().invert_yaxis()
    plt.title("Feature Importance (Random Forest)")
    plt.tight_layout()

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path)

    # 🔥 IMPORTANT: close figure instead of blocking show
    plt.close()
