#RUL = Remaining Useful Life
#eol_cycle = End of life  cycles

import pandas as pd

battery = pd.read_csv('../data/processed/battery_features.csv')
eol_cycle = battery[battery['capacity'] <= 1.4]['cycle_number'].min()
print(eol_cycle)

battery['RUL'] = eol_cycle - battery['cycle_number']
battery['RUL'] = battery['RUL'].clip(lower=0)

print(battery[['cycle_number', 'capacity', 'RUL']].head(10))
print(battery[['cycle_number', 'capacity', 'RUL']].tail(10))
print(battery['C1'].describe())
battery['stress_level'] = pd.cut(
    battery['C1'].abs(),
    bins=[0.000021 , 0.000027, 0.000035 ,0.000044],  # your boundary values
    labels=['low', 'medium', 'high']  # 'low', 'medium', 'high'
)
print(battery['stress_level'].value_counts())
print(battery['stress_level'].isna().sum())

print(battery[battery['stress_level'].isna()]['C1'].abs())

battery.to_csv('../data/processed/battery_features.csv', index=False)
print(battery[['cycle_number', 'capacity', 'RUL', 'stress_level']].head())

