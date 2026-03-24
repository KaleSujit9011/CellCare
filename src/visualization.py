import pandas as pd
import matplotlib.pyplot as plt

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
    # plt.show()
    plt.savefig('../outputs/plots/stress_features_curves.png')

def plot_degradation(df):
    plt.figure()
    plt.plot(df['cycle_number'], df['capacity'])
    plt.xlabel('Cycle Number')
    plt.ylabel('Capacity(Ah)')
    plt.title('Battery Degradation Curve')
    plt.axhline(y=1.4, color='r', linestyle='--', label='End of Life (1.4Ah)')
    # plt.show()
    plt.legend()
    plt.savefig('../outputs/plots/degradation_curve.png')


def plot_rul(df):
    plt.figure()
    plt.plot(df['cycle_number'],df['RUL'], label='Remaining Useful Life')
    plt.xlabel('cycle_number')
    plt.ylabel('RUL')
    plt.title('Battery RUL')
    # plt.show()
    plt.legend()
    plt.savefig('../outputs/plots/rul_curve.png')

def plot_stress_distribution(df):
    counts = df['stress_level'].value_counts()
    plt.bar(counts.index , counts.values)
    plt.figure()
    plt.xlabel('Stress Level')
    plt.ylabel('Number of cycles')
    plt.title(' Stress Level Distribution ')
    # plt.show()
    plt.savefig('../outputs/plots/stress_distribution_curve.png')

if __name__ == "__main__":
    # from data_loader import load_mat, extract_discharge_cycles
    # mat = load_mat("data/raw/B0005.mat")
    # df = extract_discharge_cycles(mat)
    df = pd.read_csv('../data/processed/battery_features.csv')
    print(df.head())
    print(df.info())
    plot_degradation(df)
    plot_rul(df)
    plot_stress_features(df)
    plot_stress_distribution(df)