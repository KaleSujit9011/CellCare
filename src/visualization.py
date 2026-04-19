import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_stress_features(df):
    plt.figure(figsize=(12,8))
    features = ['C1','C2','C3', 'C4']
    for i,feature in enumerate(features):
        plt.subplot(2,2,i+1)
        plt.plot(df['cycle_number'], df[feature])
        plt.title(feature)
        plt.xlabel('Cycle Number')
        plt.ylabel('Values')

    plt.suptitle('Stress features Over Cycle')
    plt.tight_layout()
    plt.savefig('../outputs/plots/stress_features_curves.png')
    plt.show()

def plot_degradation(df):
    plt.figure()
    plt.plot(df['cycle_number'], df['capacity'])
    plt.xlabel('Cycle Number')
    plt.ylabel('Capacity(Ah)')
    plt.title('Battery Degradation Curve')
    plt.axhline(y=1.4, color='r', linestyle='--', label='End of Life (1.4Ah)')
    plt.legend()
    plt.savefig('../outputs/plots/degradation_curve.png')
    plt.show()


def plot_rul(df):
    plt.figure()
    plt.plot(df['cycle_number'],df['RUL'], label='Remaining Useful Life')
    plt.xlabel('cycle_number')
    plt.ylabel('RUL')
    plt.title('Battery RUL')
    plt.legend()
    plt.savefig('../outputs/plots/rul_curve.png')
    plt.show()

def plot_stress_distribution(df):
    counts = df['stress_level'].value_counts()
    plt.figure()
    for level, value in counts.items():
        plt.bar(level, value, label=level)  # each bar gets its own label
    plt.xlabel('Stress Level')
    plt.ylabel('Number of cycles')
    plt.title('Stress Level Distribution')
    plt.legend()
    plt.savefig('../outputs/plots/stress_distribution_curve.png')
    plt.show()


def plot_actual_vs_predicted(y_test, y_pred, model_name):
    plt.figure()
    plt.scatter(y_test, y_pred, alpha=0.7)
    plt.plot([y_test.min(), y_test.max()],
             [y_test.min(), y_test.max()],
             'r--', label='Perfect Prediction')
    plt.xlabel('Actual Capacity')
    plt.ylabel('Predicted Capacity')
    plt.title(f'Actual vs Predicted - {model_name}')
    plt.legend()
    plt.savefig(f'../outputs/plots/actual_vs_predicted_{model_name}.png')

def plot_feature_importance(model, feature_names, model_name):
    plt.figure(figsize=(8, 5))
    importance = model.feature_importances_
    sorted_idx = np.argsort(importance)
    plt.barh(
        np.array(feature_names)[sorted_idx],
        importance[sorted_idx]
    )
    plt.title(f'Feature Importance - {model_name}')
    plt.xlabel('Importance Score')
    plt.savefig(f'../outputs/plots/feature_importance_{model_name}.png')


def plot_correlation_heatmap(df):
    plt.figure(figsize=(10, 8))
    cols = ['C1', 'C2', 'C3', 'C4', 'min_voltage', 'capacity', 'RUL']
    correlation = df[cols].corr()

    sns.heatmap(
        correlation,
        annot=True,  # shows numbers inside boxes
        fmt='.2f',  # 2 decimal places
        cmap='coolwarm',  # blue=negative, red=positive correlation
        center=0
    )
    plt.title('Feature Correlation Heatmap')
    plt.tight_layout()
    plt.savefig('../outputs/plots/correlation_heatmap.png')


def plot_model_comparison(rf_mae, rf_r2, xgb_mae, xgb_r2):
    plt.figure(figsize=(10, 5))

    models = ['Random Forest', 'XGBoost']
    maes = [rf_mae, xgb_mae]
    r2s = [rf_r2, xgb_r2]

    # MAE comparison
    plt.subplot(1, 2, 1)
    plt.bar(models, maes, color=['blue', 'orange'])
    plt.title('MAE Comparison (lower is better)-prediction error')
    plt.ylabel('MAE')

    # R2 comparison
    plt.subplot(1, 2, 2)
    plt.bar(models, r2s, color=['blue', 'orange'])
    plt.title('R2 Score Comparison (higher is better)- accuracy')
    plt.ylabel('R2 Score')

    plt.suptitle('Model Comparison')
    plt.tight_layout()
    plt.savefig('../outputs/plots/model_comparison.png')


def plot_safe_vs_dangerous(df):
    plt.figure(figsize=(10, 5))
    safe = df[df['capacity'] >= 1.6]
    warning = df[(df['capacity'] >= 1.4) & (df['capacity'] < 1.6)]
    dangerous = df[df['capacity'] < 1.4]

    plt.scatter(safe['cycle_number'], safe['capacity'],
                color='green', label='Safe', alpha=0.7)
    plt.scatter(warning['cycle_number'], warning['capacity'],
                color='orange', label='Warning', alpha=0.7)
    plt.scatter(dangerous['cycle_number'], dangerous['capacity'],
                color='red', label='Dangerous', alpha=0.7)

    plt.axhline(y=1.6, color='orange', linestyle='--')
    plt.axhline(y=1.4, color='red', linestyle='--')
    plt.xlabel('Cycle Number')
    plt.ylabel('Capacity (Ah)')
    plt.title('Safe vs Warning vs Dangerous Cycles')
    plt.legend()
    plt.savefig('../outputs/plots/safe_vs_dangerous.png')

if __name__ == "__main__":
    df = pd.read_csv('../data/processed/battery_features.csv')
    print(df.head())
    print(df.info())
    plot_degradation(df)
    plot_rul(df)
    plot_stress_features(df)
    plot_stress_distribution(df)
    plot_correlation_heatmap(df)
    plot_safe_vs_dangerous(df)